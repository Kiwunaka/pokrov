from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/validate_release_index.py"
SPEC = importlib.util.spec_from_file_location("validate_release_index", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


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


if __name__ == "__main__":
    unittest.main()
