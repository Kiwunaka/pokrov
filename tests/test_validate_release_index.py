from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/validate_release_index.py"
SPEC = importlib.util.spec_from_file_location("validate_release_index", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

SIGN_MODULE_PATH = ROOT / "scripts/sign_release_index.py"
SIGN_SPEC = importlib.util.spec_from_file_location(
    "sign_release_index", SIGN_MODULE_PATH
)
assert SIGN_SPEC is not None and SIGN_SPEC.loader is not None
SIGN_MODULE = importlib.util.module_from_spec(SIGN_SPEC)
sys.modules[SIGN_SPEC.name] = SIGN_MODULE
SIGN_SPEC.loader.exec_module(SIGN_MODULE)


class ReleaseIndexSourceTest(unittest.TestCase):
    def test_current_source_is_valid_with_owner_key(self) -> None:
        summary, active_keys = MODULE.validate_source(ROOT)

        self.assertEqual(summary["status"], "CONTRACT_READY_PRE_CANDIDATE")
        self.assertEqual(summary["active_signing_keys"], 1)
        self.assertEqual(active_keys[0]["id"], "pokrov-release-2026-01")
        self.assertEqual(len(active_keys[0]["public_key"]), 32)
        self.assertFalse(summary["candidate_created"])
        self.assertFalse(summary["promotion_authorized"])

    def test_signature_verifier_accepts_only_exact_bytes(self) -> None:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PrivateKey,
        )

        private_key = Ed25519PrivateKey.generate()
        public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        payload = b'{"candidate":"synthetic-test-only"}\n'
        signature = private_key.sign(payload)
        active_keys = [
            {
                "id": "synthetic-test-key",
                "public_key": public_key,
            }
        ]

        self.assertEqual(
            MODULE._verify_signature(payload, signature, active_keys),
            "synthetic-test-key",
        )
        with self.assertRaisesRegex(MODULE.ValidationError, "signature is not trusted"):
            MODULE._verify_signature(payload + b" ", signature, active_keys)

    def _candidate_template(self) -> dict[str, object]:
        artifact_signing = {
            "status": "TRUSTED",
            "identity": "synthetic-test-identity",
            "fingerprint": "sha256:" + "1" * 64,
            "lineage_sha256": "2" * 64,
        }
        return {
            "schema": "pokrov.release-index.manifest/v2",
            "candidate_id": "pokrov-1.2.0-synthetic-test",
            "candidate_created": True,
            "promotion_authorized": False,
            "product": {
                "version": "1.2.0",
                "build": 30,
                "package_version": "1.2.0+30",
                "channel": "candidate",
                "state": "CANDIDATE",
            },
            "sources": {
                "platform": {"repository": "Kiwunaka/platform", "commit": "3" * 40},
                "client": {"repository": "Kiwunaka/POKROV-app", "commit": "4" * 40},
                "core": {"repository": "Kiwunaka/POKROV-core", "commit": "5" * 40},
                "release_index": {
                    "repository": "Kiwunaka/pokrov",
                    "commit": SIGN_MODULE.PLACEHOLDER_COMMIT,
                },
            },
            "contracts": {
                "release_handoff_sha256": "6" * 64,
                "product_facts_sha256": "7" * 64,
                "error_catalog_sha256": "8" * 64,
                "observability_schema_sha256": "9" * 64,
            },
            "compatibility": {
                "core_version": "1.1.0",
                "desktop_abi": 2,
                "event_abi": 1,
                "android_min_sdk": 23,
                "windows_min_version": "10 1809",
            },
            "artifacts": [
                {
                    "id": "android-universal",
                    "platform": "android",
                    "kind": "apk",
                    "name": "pokrov-android-universal.apk",
                    "size": 101,
                    "sha256": "a" * 64,
                    "github_asset_digest": "sha256:" + "a" * 64,
                    "url": "https://github.com/Kiwunaka/pokrov/releases/download/v1.2.0-candidate/android.apk",
                    "architectures": ["universal"],
                    "signing": artifact_signing,
                    "sbom_sha256": ["b" * 64],
                    "provenance_sha256": "c" * 64,
                },
                {
                    "id": "windows-x64",
                    "platform": "windows",
                    "kind": "exe",
                    "name": "pokrov-windows-x64-setup.exe",
                    "size": 202,
                    "sha256": "d" * 64,
                    "github_asset_digest": "sha256:" + "d" * 64,
                    "url": "https://github.com/Kiwunaka/pokrov/releases/download/v1.2.0-candidate/windows.exe",
                    "architectures": ["x86_64"],
                    "signing": artifact_signing,
                    "sbom_sha256": ["e" * 64],
                    "provenance_sha256": "f" * 64,
                },
            ],
            "release_notes": {
                "url": "https://pokrov.space/releases/1.2.0/notes",
                "sha256": "1" * 64,
            },
            "known_issues": {
                "url": "https://pokrov.space/releases/1.2.0/issues",
                "sha256": "2" * 64,
            },
            "promotion": {
                "rebuild": False,
                "same_byte_required": True,
                "stable_pointer_atomic": True,
                "rollback_target": "1.1.6",
            },
        }

    def test_candidate_signer_is_deterministic_and_exact_byte_bound(self) -> None:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.ed25519 import (
            Ed25519PrivateKey,
        )

        private_key = Ed25519PrivateKey.generate()
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        public_key = private_key.public_key().public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw,
        )
        template_bytes = (
            json.dumps(self._candidate_template(), ensure_ascii=False, indent=2) + "\n"
        ).encode("utf-8")
        template_sha256 = hashlib.sha256(template_bytes).hexdigest()
        active_keys = [{"id": "synthetic-test-key", "public_key": public_key}]
        head = MODULE._git_head(ROOT)

        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first"
            second = Path(temporary) / "second"
            first_receipt = SIGN_MODULE.prepare_signed_manifest(
                ROOT,
                template_bytes=template_bytes,
                expected_template_sha256=template_sha256,
                expected_candidate_id="pokrov-1.2.0-synthetic-test",
                release_index_commit=head,
                private_key_pem=private_pem,
                active_keys=active_keys,
                output_dir=first,
            )
            second_receipt = SIGN_MODULE.prepare_signed_manifest(
                ROOT,
                template_bytes=template_bytes,
                expected_template_sha256=template_sha256,
                expected_candidate_id="pokrov-1.2.0-synthetic-test",
                release_index_commit=head,
                private_key_pem=private_pem,
                active_keys=active_keys,
                output_dir=second,
            )
            self.assertEqual(first_receipt, second_receipt)
            for name in (
                "release-index.json",
                "release-index.json.sig",
                "signing-receipt.json",
            ):
                self.assertEqual((first / name).read_bytes(), (second / name).read_bytes())
            manifest = json.loads((first / "release-index.json").read_text("utf-8"))
            self.assertEqual(manifest["sources"]["release_index"]["commit"], head)
            self.assertFalse(first_receipt["promotion_authorized"])
            self.assertEqual(first_receipt["output_kind"], "ACTIONS_ARTIFACT_ONLY")

        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(MODULE.ValidationError, "template SHA-256 mismatch"):
                SIGN_MODULE.prepare_signed_manifest(
                    ROOT,
                    template_bytes=template_bytes + b" ",
                    expected_template_sha256=template_sha256,
                    expected_candidate_id="pokrov-1.2.0-synthetic-test",
                    release_index_commit=head,
                    private_key_pem=private_pem,
                    active_keys=active_keys,
                    output_dir=Path(temporary) / "rejected",
                )

        other_private_key = Ed25519PrivateKey.generate()
        other_private_pem = other_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with tempfile.TemporaryDirectory() as temporary:
            rejected_output = Path(temporary) / "untrusted-key"
            with self.assertRaisesRegex(MODULE.ValidationError, "signature is not trusted"):
                SIGN_MODULE.prepare_signed_manifest(
                    ROOT,
                    template_bytes=template_bytes,
                    expected_template_sha256=template_sha256,
                    expected_candidate_id="pokrov-1.2.0-synthetic-test",
                    release_index_commit=head,
                    private_key_pem=other_private_pem,
                    active_keys=active_keys,
                    output_dir=rejected_output,
                )
            self.assertFalse(rejected_output.exists())

    def test_signing_workflow_is_artifact_only_and_secretless_at_rest(self) -> None:
        workflow = (ROOT / ".github/workflows/prepare-signed-candidate.yml").read_text(
            encoding="utf-8"
        )
        signer = SIGN_MODULE_PATH.read_text(encoding="utf-8")
        for marker in (
            "workflow_dispatch:",
            "github.ref == 'refs/heads/main'",
            "permissions:\n  contents: read",
            "secrets.POKROV_RELEASE_SIGNING_KEY_PEM",
            "scripts/sign_release_index.py",
            "scripts/validate_release_index.py",
            "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02",
            "retention-days: 14",
            "persist-credentials: false",
        ):
            self.assertIn(marker, workflow)
        self.assertEqual(workflow.count("secrets.POKROV_RELEASE_SIGNING_KEY_PEM"), 1)
        self.assertNotIn("contents: write", workflow)
        self.assertNotIn("gh release", workflow)
        self.assertIn('os.environ.pop("POKROV_RELEASE_SIGNING_KEY_PEM", "")', signer)
        self.assertNotIn("--private-key", signer)


if __name__ == "__main__":
    unittest.main()
