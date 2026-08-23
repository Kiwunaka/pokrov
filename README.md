# POKROV release index

Public release-only repository for POKROV Android and Windows downloads. Source
development remains in the private POKROV-app repository.

## Trust boundary

GitHub Releases stores immutable public assets. A release is candidate-eligible
only when its exact files are described by the v2 manifest schema, every asset
size and SHA-256 matches both the manifest and GitHub asset digest, and the
exact manifest bytes have a detached Ed25519 signature from an active key in
the repository keyring. Promotion must reuse the same bytes; rebuilding during
promotion is forbidden.

The retained 1.1.6 line predates this contract. It has GitHub SHA-256 digests
and `SHA256SUMS.txt`, but no detached manifest signature or signed source/SBOM
binding. It is `LEGACY_CHECKSUM_ONLY_NOT_CANDIDATE_ELIGIBLE` and must not be
used as proof for a new candidate.

## 1.2.0 state

`release-index.contract.json` defines the pre-candidate source policy and
`schemas/release-index-manifest-v2.schema.json` defines the future exact public
manifest. The trusted keyring is intentionally empty until the owner provisions
and reviews the public half of the release signing key. Therefore 1.2.0 remains
`PRE_CANDIDATE_LOCAL`; candidate creation, signing, publication and promotion
are not authorized by this repository state.

Run the source check with:

```text
python -B scripts/validate_release_index.py
```

Use `--require-ready` only in a candidate workflow. It fails closed while the
trusted keyring is empty or any required candidate input is absent.
