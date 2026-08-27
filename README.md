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

The owner-approved 1.2.0 Windows direct-beta exception is narrower than a
trusted release claim. One candidate manifest may mark only
`pokrov-windows-setup-x64.exe` as `SKIPPED_BY_OWNER`, direct-download-only, with
the exact SmartScreen/unknown-publisher warning. Android remains production
signed. A stable manifest or any authorized promotion rejects the unsigned
exception; trusted, Store and broad-stable Windows claims still require a
valid Authenticode signer.

The retained 1.1.6 line predates this contract. It has GitHub SHA-256 digests
and `SHA256SUMS.txt`, but no detached manifest signature or signed source/SBOM
binding. It is `LEGACY_CHECKSUM_ONLY_NOT_CANDIDATE_ELIGIBLE` and must not be
used as proof for a new candidate.

## 1.2.0 state

`release-index.contract.json` defines the mutable development-target policy and
`schemas/release-index-manifest-v2.schema.json` defines the exact public
manifest. The trusted keyring contains the reviewed public half of
`pokrov-release-2026-01`; the private half is excluded from Git and retained in
the owner-controlled `POKROV_RELEASE_SIGNING_KEY_PEM` Actions secret.

Candidate 2 was generated and signed from exact release-index commit
`4c6d46c10083e68dc5d2032c13f51c4e80a17049`. Its manifest SHA-256 is
`1697a1bce4f72314aa1f60cd74a1711f9b8f7d70091c5757e98fbdc09b4ce5e0` and
its detached signature SHA-256 is
`ebf259f1a9d3c9d561e3f39123c12804a178da5f15efcb293aeab47d45308a82`.
The exact unsigned Windows artifact later passed the bounded private clean-host
gate; the sanitized follow-up record is retained under
`candidate-evidence/1.2.0/`. Candidate 2 remains private,
`promotion_authorized=false`, and is neither the public `v1.2.0` release nor a
stable/latest pointer. The development target stays `PRE_CANDIDATE_LOCAL`
independently of this immutable candidate snapshot.

Candidate 3 was generated and signed from exact release-index commit
`6a1afa95fe52da2d559ba7b1da88715cd0344bb2`. Its manifest SHA-256 is
`a2752b6a3b95faacf13a68edb708c560966a0f5eb8727e109d7f1603fdc81090` and
its detached signature SHA-256 is
`926f0b4667a58ba9cc5ace5c4e6c3c8129d1ec3d4d449b3f0831a8c527cd7121`.
The exact APK passed upgrade/start/settings-persistence checks in LDPlayer,
while the expired emulator entitlement blocked catalog and tunnel proof. The
exact unsigned Windows artifact passed the bounded private clean-host gate in
run `33033294889`; sanitized evidence is retained under
`candidate-evidence/1.2.0/`. Candidate 3 remains private,
`promotion_authorized=false`, and is neither the public `v1.2.0` release nor a
stable/latest pointer.

Run the source check with:

```text
python -B scripts/validate_release_index.py
```

Use `--require-ready` only in a candidate workflow. It fails closed while the
trusted keyring is empty or any required candidate input is absent.

## Candidate signing control

`Prepare signed candidate manifest` is a manual, `main`-only Actions workflow.
It does not create a GitHub Release, upload public release assets, update a
stable pointer, authorize promotion, or write back to the repository.

The reviewed input must first be committed under
`candidate-inputs/1.2.0/<name>.json`. It is a complete v2 candidate manifest
template with `sources.release_index.commit` set to forty zeroes,
`promotion_authorized=false`, candidate channel/state, and rollback target
`1.1.6`. The operator dispatches the workflow with the exact tracked path,
template SHA-256, and candidate id. The signer then:

1. requires a clean checkout and byte equality with `HEAD`;
2. binds `sources.release_index.commit` to the dispatched `main` SHA;
3. emits deterministic canonical UTF-8 JSON;
4. signs the exact bytes using `POKROV_RELEASE_SIGNING_KEY_PEM` from Actions;
5. verifies the signature against the public keyring and v2 schema; and
6. uploads the manifest, raw 64-byte signature, and public receipt as a
   14-day Actions artifact only.

The private key is accepted only through the process environment, never as a
CLI argument or repository file. Tracked candidate templates bind an exact
Android/Windows artifact set, source tuple, SBOM, provenance, release notes and
known issues. Candidate 1 retains the rejected Windows SCM behavior as history;
candidate 2 binds the fail-closed replacement and freshly rebuilt artifact set.
Candidate 3 binds the later SPB/client correction and source-freeze build fixes.
Tracking a reviewed input does not create, sign or publish a candidate. The
manual workflow must still bind the zero-commit placeholder to exact `main`,
sign the canonical bytes and retain the artifact receipt before candidate
creation is proved. Candidate inputs, release notes, and known-issues files are
immutable once their hashes have been signed. Later runtime results are added
under `candidate-evidence/`; they do not rewrite the signed snapshot or
authorize promotion.
