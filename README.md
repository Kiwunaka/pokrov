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

Candidate 4 was generated and signed from exact release-index commit
`6d2a7df2870dae4b0540f3a9e19ba044489bdb43`. Its manifest SHA-256 is
`482a507fe1816c56a000ebae5232fabf9c863a61992430db2fa287099393765e` and
its detached signature SHA-256 is
`2995c68ec60d501a8c8726c6677fa93259eff52ef78047d81ab8a7d56e20f7d0`.
Main-only signer run `33073596552` signed and revalidated all six exact build
`1.2.0+32` artifact identities. The candidate binds the AWG 3.1 default-off lab,
direct-DoH lab, five production-signed Android artifacts, the owner-approved
unsigned Windows installer, SBOM, provenance, release notes and known issues.
It remains an Actions artifact only with `promotion_authorized=false`: no tag,
GitHub Release, public assets, stable pointer or promotion was created.

Candidate 5 was generated and signed from exact release-index commit
`1d1b7eec05f311aad3044249982ed6fa0f3ace0d`. Its manifest SHA-256 is
`1f8d6ba056f66dc3f8ea76df16e42f5481fc17b111ea759f191eb4ad4af3c263`
and its detached signature SHA-256 is
`56ed2afe249491546d4e21f1c66490daa6ee376af9b94b53b7a7ea680cf3e874`.
Main-only signer run `33190309331` signed and revalidated all six exact build
`1.2.0+4046` artifact identities using key `pokrov-release-2026-01`; the public
receipt SHA-256 is
`d39ad982b14c55e9e395753f73a9c3d6570ac912e3d8a967a15aac5a0d05060b`.
The candidate binds promoted platform/client source, the exact Core product
source, production-signed Android APK/AAB files, the owner-approved unsigned
Windows installer, strict-v2 handoff, SBOM, provenance, release notes and known
issues. It remains an Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, stable
pointer or promotion was created.

Candidate 6 was generated and signed from exact release-index commit
`8d09ae5e8ec0c8347bcd4e2659944bdf7c9c9db3`. Its manifest SHA-256 is
`8aac2458f8c43c0ef2955719dcede44f495d60acf681bc804bd6bf9828ee9054`,
its detached signature SHA-256 is
`2307906a920fb9b4dcd4c0025bf7628972668905d13897c553ddf27a81592dfa`,
and its public receipt SHA-256 is
`85dd34504d876086aa8bfe3533ad4db964e4f0a9106f9085657dc08c2c7afcaa`.
Main-only signer run `33239993242` signed and independently revalidated six
exact build `1.2.0+4046` artifacts using key `pokrov-release-2026-01`.
Candidate 6 binds the resolver-corrected Core, the current Smart-DNS source
contract, production-signed Android APK/AAB files, the owner-approved unsigned
Windows installer, strict-v2 handoff, SBOM, provenance, release notes and known
issues. It remains an Actions artifact only with `promotion_authorized=false`:
no tag, GitHub Release, public assets, store submission, stable pointer or
promotion was created.

Candidate 7 was generated and signed from exact release-index commit
`f6917c8264015aee72fe51126943b08191e85b07`. Its manifest SHA-256 is
`fb1d7049deaf3047456377e675c45a2177c76c51f8792703886ca2bcca5490ce`,
its detached signature SHA-256 is
`2b20ed7881c36f72b0777aa8c2a571e192895df15eb598165d5e93ae68418abf`,
and its public receipt SHA-256 is
`ff93d33bf0ef4b0e1b036ee1be5b83f769791295d0e1cfcde0a1f854b2799b04`.
Main-only signer run `33256988566` signed and independently revalidated all
six exact build `1.2.0+4046` artifacts using key
`pokrov-release-2026-01`. Candidate 7 binds platform
`af259f377ec7a3cd757f0f43762154dd25e09f94`, client
`b2497af7704d0aa6901541e175ce154b0eab05d7`, Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`, and the exact same six build
`1.2.0+4046` artifact bytes. Its corrected full-product SBOM and provenance
pass the offline fail-closed supply-chain verifier, including the exact Core
AAR/DLL and all eight Windows runtime files. It remains an Actions artifact
only with `promotion_authorized=false`: no tag, GitHub Release, public assets,
store submission, stable pointer or promotion was created.

Candidate 8 was generated and signed from exact release-index commit
`b242e0a3060b04f9b71641a0524bf251a75ce2a8`. Its manifest SHA-256 is
`f0006cec90c84e401e9920d9098102c7f50ab5ace5242e0d7683c3df709a6fbc`,
its detached signature SHA-256 is
`5fcae0675ea45e79baf495859fd170661f5d6dd3a8535275acd4d62680d324f6`,
and its public receipt SHA-256 is
`4109bb3417b32a780604300055f5308acf7dc810e7ea9c547075e1da41cc21fc`.
Main-only signer run `33267152760` signed and independently revalidated all
six rebuilt `1.2.0+4046` artifacts using key `pokrov-release-2026-01`.
Candidate 8 binds platform `241a83b4dca00799b39696a4ae0c3c97e087ec39`,
client `3459438f02bd774e722b1b858e7f7f16d57a9f5c`, and unchanged Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. Its Android notification truth
correction and owned AWG mobile-safe metadata/MTU correction are represented by
fresh Android and Windows bytes; the offline verifier passes all six artifacts
and all eight Windows runtime files. Public release-index Actions completed all
real source-contract and signer steps. Separate private platform/client hosted
jobs remain blocked by their account billing state and are not relabelled as
passes. Candidate 8 remains an Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer or promotion was created.

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
Candidate 4 adds the default-off AWG 3.1 and direct-DoH labs. Candidate 5 moves
the replacement line to build `4046` and retains the later rejected runtime
history. Candidate 6 binds the resolver correction and current Smart-DNS
source contract to a new six-file artifact set. Candidate 7 corrects the
full-product supply-chain evidence and binds the same six bytes to the final
platform verifier merge. Candidate 8 rebuilds the six-file set for the Android
notification-truth and owned AWG mobile-safe corrections and binds it to the
new exact source tuple. None of these candidates authorizes promotion.
Tracking a reviewed input does not create, sign or publish a candidate. The
manual workflow must still bind the zero-commit placeholder to exact `main`,
sign the canonical bytes and retain the artifact receipt before candidate
creation is proved. Candidate inputs, release notes, and known-issues files are
immutable once their hashes have been signed. Later runtime results are added
under `candidate-evidence/`; they do not rewrite the signed snapshot or
authorize promotion.
