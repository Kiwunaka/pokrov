"""Deterministically prepare and sign one candidate release-index manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

import validate_release_index as validator


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_COMMIT = "0" * 40
SHA256 = re.compile(r"^[0-9a-f]{64}$")
COMMIT = re.compile(r"^[0-9a-f]{40}$")
CANDIDATE_ID = re.compile(r"^pokrov-1\.2\.0-[a-z0-9][a-z0-9._-]{7,95}$")
MAX_TEMPLATE_BYTES = 256 * 1024


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _canonical_json(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise validator.ValidationError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _parse_template(template_bytes: bytes) -> dict[str, Any]:
    if not template_bytes or len(template_bytes) > MAX_TEMPLATE_BYTES:
        raise validator.ValidationError("manifest template size is invalid")
    try:
        value = json.loads(
            template_bytes.decode("utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise validator.ValidationError("manifest template must be unique-key UTF-8 JSON") from exc
    if not isinstance(value, dict):
        raise validator.ValidationError("manifest template must contain a JSON object")
    return value


def _prepare_manifest(
    template_bytes: bytes,
    *,
    expected_template_sha256: str,
    expected_candidate_id: str,
    release_index_commit: str,
) -> tuple[dict[str, Any], bytes, str]:
    template_sha256 = _sha256_bytes(template_bytes)
    if not SHA256.fullmatch(expected_template_sha256):
        raise validator.ValidationError("expected template SHA-256 is invalid")
    if template_sha256 != expected_template_sha256:
        raise validator.ValidationError("manifest template SHA-256 mismatch")
    if not COMMIT.fullmatch(release_index_commit):
        raise validator.ValidationError("release-index commit is invalid")
    if not CANDIDATE_ID.fullmatch(expected_candidate_id):
        raise validator.ValidationError("expected candidate id is invalid")

    manifest = _parse_template(template_bytes)
    if manifest.get("candidate_id") != expected_candidate_id:
        raise validator.ValidationError("candidate id does not match the reviewed dispatch input")
    if manifest.get("candidate_created") is not True:
        raise validator.ValidationError("candidate template must explicitly create a candidate")
    if manifest.get("promotion_authorized") is not False:
        raise validator.ValidationError("candidate signing cannot authorize promotion")
    product = manifest.get("product")
    if not isinstance(product, dict) or (
        product.get("channel") != "candidate" or product.get("state") != "CANDIDATE"
    ):
        raise validator.ValidationError("signing workflow accepts only a candidate manifest")
    promotion = manifest.get("promotion")
    if not isinstance(promotion, dict) or promotion.get("rollback_target") != "1.1.6":
        raise validator.ValidationError("candidate must retain the reviewed 1.1.6 rollback target")
    sources = manifest.get("sources")
    release_index_source = sources.get("release_index") if isinstance(sources, dict) else None
    if not isinstance(release_index_source, dict) or (
        release_index_source.get("repository") != "Kiwunaka/pokrov"
        or release_index_source.get("commit") != PLACEHOLDER_COMMIT
    ):
        raise validator.ValidationError(
            "template must bind Kiwunaka/pokrov through the zero-commit placeholder"
        )
    release_index_source["commit"] = release_index_commit
    manifest_bytes = _canonical_json(manifest)
    return manifest, manifest_bytes, template_sha256


def _load_private_key(private_key_pem: bytes) -> Ed25519PrivateKey:
    try:
        private_key = serialization.load_pem_private_key(private_key_pem, password=None)
    except (TypeError, ValueError) as exc:
        raise validator.ValidationError("release signing secret is not an unencrypted PEM key") from exc
    if not isinstance(private_key, Ed25519PrivateKey):
        raise validator.ValidationError("release signing secret is not an Ed25519 private key")
    return private_key


def prepare_signed_manifest(
    root: Path,
    *,
    template_bytes: bytes,
    expected_template_sha256: str,
    expected_candidate_id: str,
    release_index_commit: str,
    private_key_pem: bytes,
    active_keys: list[dict[str, Any]],
    output_dir: Path,
) -> dict[str, Any]:
    root = root.resolve()
    output_dir = output_dir.resolve()
    try:
        output_dir.relative_to(root)
    except ValueError:
        pass
    else:
        raise validator.ValidationError("signed candidate output must stay outside the source checkout")
    if output_dir.exists():
        raise validator.ValidationError("signed candidate output directory already exists")
    output_dir.parent.mkdir(parents=True, exist_ok=True)

    manifest, manifest_bytes, template_sha256 = _prepare_manifest(
        template_bytes,
        expected_template_sha256=expected_template_sha256,
        expected_candidate_id=expected_candidate_id,
        release_index_commit=release_index_commit,
    )
    private_key = _load_private_key(private_key_pem)
    signature_bytes = private_key.sign(manifest_bytes)

    with tempfile.TemporaryDirectory(
        prefix=".pokrov-release-signing-", dir=output_dir.parent
    ) as temporary:
        payload_dir = Path(temporary) / "payload"
        payload_dir.mkdir()
        manifest_path = payload_dir / "release-index.json"
        signature_path = payload_dir / "release-index.json.sig"
        receipt_path = payload_dir / "signing-receipt.json"
        manifest_path.write_bytes(manifest_bytes)
        signature_path.write_bytes(signature_bytes)
        ready = validator.validate_ready(
            root,
            manifest_path,
            signature_path,
            active_keys,
        )
        receipt = {
            "schema": "pokrov.release-index.signing-receipt/v1",
            "candidate_id": manifest["candidate_id"],
            "release_index_commit": release_index_commit,
            "template_sha256": template_sha256,
            "manifest_sha256": ready["manifest_sha256"],
            "signature_sha256": ready["signature_sha256"],
            "signing_key_id": ready["signing_key_id"],
            "artifact_count": ready["artifact_count"],
            "promotion_authorized": False,
            "output_kind": "ACTIONS_ARTIFACT_ONLY",
        }
        receipt_path.write_bytes(_canonical_json(receipt))
        payload_dir.replace(output_dir)
    return receipt


def _git(root: Path, *arguments: str, text: bool = True) -> subprocess.CompletedProcess[Any]:
    return subprocess.run(
        ["git", *arguments],
        cwd=root,
        check=True,
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
    )


def _require_clean_checkout(root: Path) -> None:
    status = _git(root, "status", "--porcelain=v1", "--untracked-files=no").stdout
    if status.strip():
        raise validator.ValidationError("release-index checkout has tracked modifications")


def _read_tracked_template(root: Path, template_argument: Path) -> bytes:
    unresolved = root / template_argument
    if unresolved.is_symlink():
        raise validator.ValidationError("manifest template cannot be a symlink")
    candidate = unresolved.resolve()
    try:
        relative = candidate.relative_to(root)
    except ValueError as exc:
        raise validator.ValidationError("manifest template must stay inside the checkout") from exc
    if (
        len(relative.parts) != 3
        or relative.parts[:2] != ("candidate-inputs", "1.2.0")
        or relative.suffix != ".json"
    ):
        raise validator.ValidationError(
            "manifest template must be candidate-inputs/1.2.0/<name>.json"
        )
    if not candidate.is_file():
        raise validator.ValidationError("manifest template must be a regular tracked file")
    relative_git = relative.as_posix()
    tracked_bytes = _git(root, "show", f"HEAD:{relative_git}", text=False).stdout
    working_bytes = candidate.read_bytes()
    if tracked_bytes != working_bytes:
        raise validator.ValidationError("manifest template bytes do not match HEAD")
    return working_bytes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--template-sha256", required=True)
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--release-index-commit", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    key_material = bytearray(
        os.environ.pop("POKROV_RELEASE_SIGNING_KEY_PEM", "").encode("utf-8")
    )
    try:
        if not key_material:
            raise validator.ValidationError(
                "POKROV_RELEASE_SIGNING_KEY_PEM is required"
            )
        _require_clean_checkout(root)
        head = validator._git_head(root)
        if args.release_index_commit.lower() != head:
            raise validator.ValidationError(
                "requested release-index commit does not match checkout HEAD"
            )
        source, active_keys = validator.validate_source(root)
        if source["status"] != "CONTRACT_READY_PRE_CANDIDATE":
            raise validator.ValidationError("source contract is not ready for candidate signing")
        template_bytes = _read_tracked_template(root, args.template)
        receipt = prepare_signed_manifest(
            root,
            template_bytes=template_bytes,
            expected_template_sha256=args.template_sha256.lower(),
            expected_candidate_id=args.candidate_id,
            release_index_commit=head,
            private_key_pem=bytes(key_material),
            active_keys=active_keys,
            output_dir=args.output_dir,
        )
        print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"RELEASE_INDEX_SIGNING_FAILED: {exc}", file=sys.stderr)
        return 1
    finally:
        for index in range(len(key_material)):
            key_material[index] = 0


if __name__ == "__main__":
    raise SystemExit(main())
