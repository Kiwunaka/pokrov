"""Fail-closed source and signed-manifest validator for the public index."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = Path("release-index.contract.json")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
OWNER_UNSIGNED_WINDOWS_STATUS = "SKIPPED_BY_OWNER"
OWNER_UNSIGNED_WINDOWS_EXCEPTION = "OWNER_ACCEPTED_UNSIGNED_WINDOWS_BETA_1_2_0"
CANDIDATE_1_2_ARTIFACT_IDS = {
    "android-arm64-v8a",
    "android-armeabi-v7a",
    "android-market",
    "android-universal",
    "android-x86-64",
    "windows-x64-setup",
}


class ValidationError(ValueError):
    pass


def _read_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValidationError(f"{path} must contain a JSON object")
    return value


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require(condition: bool, field: str, errors: list[str]) -> None:
    if not condition:
        errors.append(field)


def _active_keys(keyring: dict[str, Any], errors: list[str]) -> list[dict[str, Any]]:
    _require(
        keyring.get("schema") == "pokrov.release-index.keyring/v1",
        "keyring.schema",
        errors,
    )
    keys = keyring.get("keys", [])
    _require(isinstance(keys, list), "keyring.keys", errors)
    active: list[dict[str, Any]] = []
    if not isinstance(keys, list):
        return active
    for key in keys:
        if not isinstance(key, dict) or key.get("state") != "active":
            continue
        encoded = key.get("public_key_base64")
        try:
            decoded = base64.b64decode(encoded, validate=True)
        except (TypeError, ValueError):
            decoded = b""
        valid = (
            isinstance(key.get("id"), str)
            and re.fullmatch(r"[a-z0-9][a-z0-9._-]{2,63}", key["id"])
            and len(decoded) == 32
        )
        _require(bool(valid), "keyring.active_key", errors)
        if valid:
            active.append({**key, "public_key": decoded})
    return active


def validate_source(root: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    contract_path = root / CONTRACT_PATH
    if not contract_path.is_file():
        raise ValidationError("release-index.contract.json is missing")
    contract = _read_object(contract_path)
    errors: list[str] = []
    _require(
        contract.get("schema") == "pokrov.release-index.contract/v1",
        "schema",
        errors,
    )
    _require(contract.get("repository") == "Kiwunaka/pokrov", "repository", errors)
    _require(contract.get("promotion_branch") == "main", "promotion_branch", errors)
    _require(
        contract.get("candidate_manifest_path") == "releases/1.2.0/release-index.json",
        "candidate_manifest_path",
        errors,
    )
    target = contract.get("development_target", {})
    if not isinstance(target, dict):
        target = {}
    _require(target.get("product_version") == "1.2.0", "target.version", errors)
    _require(target.get("state") == "PRE_CANDIDATE_LOCAL", "target.state", errors)
    _require(target.get("candidate_created") is False, "target.candidate", errors)
    _require(target.get("promotion_authorized") is False, "target.promotion", errors)

    signature = contract.get("signature_policy", {})
    if not isinstance(signature, dict):
        signature = {}
    _require(signature.get("algorithm") == "ed25519", "signature.algorithm", errors)
    _require(signature.get("threshold") == 1, "signature.threshold", errors)
    _require(
        signature.get("detached_signature_suffix") == ".sig",
        "signature.suffix",
        errors,
    )
    _require(
        signature.get("signed_payload") == "exact_manifest_bytes",
        "signature.payload",
        errors,
    )

    same_byte = contract.get("same_byte_policy", {})
    if not isinstance(same_byte, dict):
        same_byte = {}
    for field in (
        "require_artifact_sha256",
        "require_github_asset_digest_match",
        "require_manifest_signature",
        "stable_pointer_atomic",
    ):
        _require(same_byte.get(field) is True, f"same_byte.{field}", errors)
    _require(
        same_byte.get("rebuild_on_promotion") is False,
        "same_byte.rebuild_on_promotion",
        errors,
    )

    candidate_exception = contract.get("candidate_exception_policy", {})
    _require(
        candidate_exception
        == {
            "id": OWNER_UNSIGNED_WINDOWS_EXCEPTION,
            "product_version": "1.2.0",
            "platform": "windows",
            "artifact_id": "windows-x64-setup",
            "artifact_name": "pokrov-windows-setup-x64.exe",
            "artifact_kind": "exe",
            "architectures": ["x86_64"],
            "signing_status": OWNER_UNSIGNED_WINDOWS_STATUS,
            "distribution": "direct_download_only",
            "maximum_artifacts": 1,
            "candidate_only": True,
            "promotion_authorized": False,
            "warning": (
                "Microsoft Defender SmartScreen and unknown-publisher warning expected"
            ),
        },
        "candidate_exception_policy",
        errors,
    )

    schema = contract.get("manifest_schema", {})
    if not isinstance(schema, dict):
        schema = {}
    schema_path = root / str(schema.get("path") or "")
    declared_schema_hash = str(schema.get("sha256") or "").lower()
    _require(
        schema.get("path") == "schemas/release-index-manifest-v2.schema.json",
        "manifest_schema.path",
        errors,
    )
    _require(
        SHA256.fullmatch(declared_schema_hash) is not None,
        "manifest_schema.sha256",
        errors,
    )
    _require(schema_path.is_file(), "manifest_schema.file", errors)
    if schema_path.is_file():
        _require(
            _sha256(schema_path) == declared_schema_hash,
            "manifest_schema.bytes",
            errors,
        )
        schema_object = _read_object(schema_path)
        _require(
            schema_object.get("$schema")
            == "https://json-schema.org/draft/2020-12/schema",
            "manifest_schema.draft",
            errors,
        )

    keyring_path = root / str(contract.get("trusted_keyring_path") or "")
    _require(
        contract.get("trusted_keyring_path") == "trusted/release-signing-keys.json",
        "trusted_keyring_path",
        errors,
    )
    _require(keyring_path.is_file(), "keyring.file", errors)
    keyring = _read_object(keyring_path) if keyring_path.is_file() else {}
    active_keys = _active_keys(keyring, errors)

    retained = contract.get("retained_public_release", {})
    if not isinstance(retained, dict):
        retained = {}
    _require(retained.get("version") == "1.1.6", "retained.version", errors)
    _require(retained.get("tag") == "v1.1.6", "retained.tag", errors)
    _require(
        retained.get("trust_state") == "LEGACY_CHECKSUM_ONLY_NOT_CANDIDATE_ELIGIBLE",
        "retained.trust_state",
        errors,
    )
    _require(retained.get("manifest_signature") is False, "retained.signature", errors)
    if errors:
        raise ValidationError("invalid source contract: " + ", ".join(errors))

    candidate_templates = _validate_candidate_templates(root)
    status = (
        "CONTRACT_READY_PRE_CANDIDATE" if active_keys else "BLOCKED_OWNER_SIGNING_KEY"
    )
    return (
        {
            "status": status,
            "contract_sha256": _sha256(contract_path),
            "manifest_schema_sha256": _sha256(schema_path),
            "active_signing_keys": len(active_keys),
            "candidate_templates": len(candidate_templates),
            "candidate_template_ids": [
                template["candidate_id"] for template in candidate_templates
            ],
            "candidate_created": False,
            "promotion_authorized": False,
        },
        active_keys,
    )


def _git_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.stdout.strip().lower()


def _verify_signature(
    manifest_bytes: bytes, signature_bytes: bytes, active_keys: list[dict[str, Any]]
) -> str:
    try:
        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PublicKey,
        )
    except ImportError as exc:
        raise ValidationError(
            "ready validation requires pinned requirements-release.txt"
        ) from exc
    for key in active_keys:
        try:
            Ed25519PublicKey.from_public_bytes(key["public_key"]).verify(
                signature_bytes, manifest_bytes
            )
        except InvalidSignature:
            continue
        return str(key["id"])
    raise ValidationError("detached Ed25519 signature is not trusted")


def _validate_artifact_signing_policy(manifest: dict[str, Any]) -> int:
    artifacts = manifest.get("artifacts", [])
    product = manifest.get("product", {})
    owner_exceptions: list[dict[str, Any]] = []
    for artifact in artifacts:
        signing = artifact.get("signing", {})
        status = signing.get("status")
        if status == "TRUSTED":
            continue
        if status != OWNER_UNSIGNED_WINDOWS_STATUS:
            raise ValidationError(
                f"unsupported signing status for {artifact.get('id', 'unknown')}"
            )
        owner_exceptions.append(artifact)

    if not owner_exceptions:
        return 0
    if len(owner_exceptions) != 1:
        raise ValidationError("exactly one owner-approved unsigned artifact is allowed")
    artifact = owner_exceptions[0]
    signing = artifact["signing"]
    exact_exception = (
        manifest.get("promotion_authorized") is False
        and product.get("version") == "1.2.0"
        and product.get("channel") == "candidate"
        and product.get("state") == "CANDIDATE"
        and artifact.get("id") == "windows-x64-setup"
        and artifact.get("platform") == "windows"
        and artifact.get("kind") == "exe"
        and artifact.get("name") == "pokrov-windows-setup-x64.exe"
        and artifact.get("architectures") == ["x86_64"]
        and signing.get("exception_code") == OWNER_UNSIGNED_WINDOWS_EXCEPTION
        and signing.get("distribution") == "direct_download_only"
    )
    if not exact_exception:
        raise ValidationError("owner-approved unsigned Windows exception is out of scope")
    return 1


def _validate_candidate_templates(root: Path) -> list[dict[str, Any]]:
    template_root = root / "candidate-inputs" / "1.2.0"
    if not template_root.exists():
        return []
    if not template_root.is_dir():
        raise ValidationError("candidate-inputs/1.2.0 must be a directory")
    schema = _read_object(root / "schemas/release-index-manifest-v2.schema.json")
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:
        raise ValidationError(
            "candidate template validation requires pinned requirements-release.txt"
        ) from exc
    validator = Draft202012Validator(schema)
    summaries: list[dict[str, Any]] = []
    for template_path in sorted(template_root.glob("*.json")):
        manifest = _read_object(template_path)
        errors = sorted(
            validator.iter_errors(manifest), key=lambda item: list(item.path)
        )
        if errors:
            first = errors[0]
            location = ".".join(str(part) for part in first.path) or "root"
            raise ValidationError(
                f"candidate template schema violation at {location}: {first.message}"
            )
        candidate_id = str(manifest["candidate_id"])
        if template_path.name != f"{candidate_id}.json":
            raise ValidationError("candidate template filename must match candidate id")
        release_index_source = manifest["sources"]["release_index"]
        if release_index_source != {
            "repository": "Kiwunaka/pokrov",
            "commit": "0" * 40,
        }:
            raise ValidationError("candidate template release-index placeholder is invalid")
        expected_repositories = {
            "platform": "Kiwunaka/portal",
            "client": "Kiwunaka/POKROV-app",
            "core": "Kiwunaka/pokrov-core",
        }
        for source_id, repository in expected_repositories.items():
            if manifest["sources"][source_id]["repository"] != repository:
                raise ValidationError(
                    f"candidate template repository is invalid for {source_id}"
                )
        artifacts = manifest["artifacts"]
        ids = [artifact["id"] for artifact in artifacts]
        names = [artifact["name"] for artifact in artifacts]
        if set(ids) != CANDIDATE_1_2_ARTIFACT_IDS or len(ids) != len(
            CANDIDATE_1_2_ARTIFACT_IDS
        ):
            raise ValidationError("candidate template artifact set is incomplete")
        if len(names) != len(set(names)):
            raise ValidationError("candidate template artifact names must be unique")
        for artifact in artifacts:
            if artifact["github_asset_digest"] != f"sha256:{artifact['sha256']}":
                raise ValidationError(
                    f"candidate template asset digest mismatch for {artifact['id']}"
                )
        owner_exception_count = _validate_artifact_signing_policy(manifest)
        public_documents = {
            "release_notes": (
                template_root / f"{candidate_id}-release-notes-ru.md",
                "POKROV-1.2.0-RELEASE-NOTES-RU.md",
            ),
            "known_issues": (
                template_root / f"{candidate_id}-known-issues-ru.md",
                "POKROV-1.2.0-KNOWN-ISSUES-RU.md",
            ),
        }
        for document_id, (document_path, asset_name) in public_documents.items():
            if not document_path.is_file():
                raise ValidationError(f"candidate {document_id} file is missing")
            document = manifest[document_id]
            if document["sha256"] != _sha256(document_path):
                raise ValidationError(f"candidate {document_id} SHA-256 mismatch")
            if not document["url"].endswith(f"/{asset_name}"):
                raise ValidationError(f"candidate {document_id} URL is not canonical")
        summaries.append(
            {
                "candidate_id": candidate_id,
                "template_sha256": _sha256(template_path),
                "artifact_count": len(artifacts),
                "owner_unsigned_windows_exception_count": owner_exception_count,
            }
        )
    return summaries


def validate_ready(
    root: Path,
    manifest_path: Path,
    signature_path: Path,
    active_keys: list[dict[str, Any]],
) -> dict[str, Any]:
    if not active_keys:
        raise ValidationError("owner must provision an active trusted Ed25519 key")
    if not manifest_path.is_file() or not signature_path.is_file():
        raise ValidationError("candidate manifest and detached signature are required")
    manifest_bytes = manifest_path.read_bytes()
    signature_bytes = signature_path.read_bytes()
    if len(signature_bytes) != 64:
        raise ValidationError("detached Ed25519 signature must be exactly 64 bytes")
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    schema = _read_object(root / "schemas/release-index-manifest-v2.schema.json")
    try:
        from jsonschema import Draft202012Validator
    except ImportError as exc:
        raise ValidationError(
            "ready validation requires pinned requirements-release.txt"
        ) from exc
    errors = sorted(
        Draft202012Validator(schema).iter_errors(manifest),
        key=lambda item: list(item.path),
    )
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.path) or "root"
        raise ValidationError(
            f"manifest schema violation at {location}: {first.message}"
        )
    artifacts = manifest["artifacts"]
    ids = [artifact["id"] for artifact in artifacts]
    names = [artifact["name"] for artifact in artifacts]
    if len(ids) != len(set(ids)) or len(names) != len(set(names)):
        raise ValidationError("artifact ids and names must be unique")
    for artifact in artifacts:
        if artifact["github_asset_digest"] != f"sha256:{artifact['sha256']}":
            raise ValidationError(f"GitHub asset digest mismatch for {artifact['id']}")
    owner_exception_count = _validate_artifact_signing_policy(manifest)
    if manifest["sources"]["release_index"]["commit"] != _git_head(root):
        raise ValidationError("manifest does not bind the exact release-index revision")
    key_id = _verify_signature(manifest_bytes, signature_bytes, active_keys)
    return {
        "status": "READY_SIGNED_MANIFEST",
        "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "signature_sha256": hashlib.sha256(signature_bytes).hexdigest(),
        "signing_key_id": key_id,
        "artifact_count": len(artifacts),
        "owner_unsigned_windows_exception_count": owner_exception_count,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--require-ready", action="store_true")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--signature", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    try:
        source, active_keys = validate_source(root)
        output: dict[str, Any] = {"source": source}
        if args.require_ready:
            contract = _read_object(root / CONTRACT_PATH)
            manifest = (
                args.manifest.resolve()
                if args.manifest
                else root / contract["candidate_manifest_path"]
            )
            signature = (
                args.signature.resolve()
                if args.signature
                else manifest.with_name(manifest.name + ".sig")
            )
            output["candidate"] = validate_ready(root, manifest, signature, active_keys)
        print(json.dumps(output, sort_keys=True))
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"RELEASE_INDEX_INVALID: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
