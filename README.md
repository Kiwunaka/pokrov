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

Candidate 9 was generated and signed from exact release-index commit
`26c151093a2b53da5a59befc2532d5c9d68bc311`. Its manifest SHA-256 is
`aebfd0f4481dd6edacf61654ca6ba9ae02de38433f0bffcdbdafec7ddd9bc8b7`,
its detached signature SHA-256 is
`0ead7eec1e884a6710cca65621da0113c963c7eaa528dc1665111b911e32c2e9`,
and its public receipt SHA-256 is
`6ad892067d6dbc81c93718168617059ab63510160461f88f08523a4e02a98125`.
Main-only signer run `33290668318` signed and independently revalidated all six
exact `1.2.0+4046` artifacts using key `pokrov-release-2026-01`. Candidate 9
binds platform `84687875916bbb35c0e28e0c2a8c7ea276753f31`, unchanged client
`3459438f02bd774e722b1b858e7f7f16d57a9f5c`, and unchanged Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. The client artifacts are
byte-identical to candidate 8; regenerated full-product SBOM, provenance, and
strict-v2 handoff bind them to the platform-only RU-origin probe HMAC
permission-contract correction. The offline verifier passes all six artifacts
and all eight Windows runtime files. Release-index source-contract and signer
Actions both completed with real `PASS`. Candidate 9 remains an Actions
artifact only with `promotion_authorized=false`: no tag, GitHub Release,
public assets, store submission, stable pointer or promotion was created.

Candidate 10 was generated and signed from exact release-index commit
`fc00b26d402b167260e495eb33397115bef1c317`. Its manifest SHA-256 is
`0711546b0da4b811fba42e1ad543797494e4104bd95251c9e8e8011ac04dff83`,
its detached signature SHA-256 is
`6f96f8932e388f221cf7d5e10dc1680fbcbb62f87efe00410439eb9f62e42799`,
and its public receipt SHA-256 is
`094a42f3c0d9be3957b3065344e5bfce4880c2899833fed3b4d211d8d453a89c`.
Main-only signer run `33292070137` signed and independently revalidated all six
exact `1.2.0+4046` artifacts using key `pokrov-release-2026-01`. Candidate 10
binds platform `209b8f40c36d95f2bbc67caa52a41ecb09f46720`, unchanged client
`3459438f02bd774e722b1b858e7f7f16d57a9f5c`, and unchanged Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. The client artifacts are
byte-identical to candidate 9; regenerated full-product SBOM, provenance, and
strict-v2 handoff bind them to the platform-only RU-origin connected-family and
manifest-driven HTTPS threshold correction. Public source-contract and signer
Actions both completed all real steps with `PASS`. Candidate 10 remains an
Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer or promotion was
created.

Candidate 11 was generated and signed from exact release-index commit
`8c314a10893bb6260f59f171ecab296103c0e0c1`. Its manifest SHA-256 is
`22ea88cb7679510d51af6b35a7d31e65ec654fb17806ddf9ebd71c7da350a29f`,
its detached signature SHA-256 is
`c1a4c3cea72db5dc2089fb3259970a1665bc2dd49bc0a24093e728cf8c1e912c`,
and its public receipt SHA-256 is
`f78e61b05ce0579f5a978b404ab3fe4992df31e3562f46d5788ee1e9aec015aa`.
Main-only signer run `33306436427` signed and independently revalidated all six
freshly rebuilt exact `1.2.0+4047` artifacts using key
`pokrov-release-2026-01`. Candidate 11 binds platform
`01cf5de682c01bffbead7703db901450ca7fb1fb`, client
`348de306fc1f2243d022157b54fa7f09ffd2840b`, and Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`. The Core change removes raw
legacy settings/error logging while retaining the existing ABI and AWG lab
lifecycle. Offline supply-chain validation passed all six artifacts and all
eight Windows runtime files; the public source-contract and signer Actions
also completed real steps with `PASS`. Candidate 11 remains a 14-day Actions
artifact only with `promotion_authorized=false`: no tag, GitHub Release,
public assets, store submission, stable pointer or promotion was created.

Candidate 12 was generated and signed from exact release-index commit
`13cb67dfb56393e26ea75744c9379e19d96df5de`. Its manifest SHA-256 is
`22ba8bb11b198ade9c2a254eaf49d46324aea6ca0b952498d994e03fcd41ab98`,
its detached signature SHA-256 is
`c2ad2655ef7e6996a26bbfb12a990f6e8f77518749491d149603542e37131b32`,
and its public receipt SHA-256 is
`1144f7ac86c52ea36778d4879c8e7059307e1bcb5a01fcdd0d00e32ecb837444`.
Main-only signer run `33313761896` signed and independently revalidated all six
freshly rebuilt exact `1.2.0+4048` artifacts using key
`pokrov-release-2026-01`. Candidate 12 binds platform
`9e873eb496f13edc098e27f1a233f227d0bf48dc`, client
`5b1aa02b79212f7b55e76e5086a41a84efb36195`, and Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 11 after
the AWG lab Smart Connect exclusion failure and corrects stale Windows manifest
claims before freeze. Offline supply-chain validation passed all six artifacts
and all eight Windows runtime files; the public source-contract and signer
Actions completed real steps with `PASS`. Candidate 12 remains a 14-day Actions
artifact only with `promotion_authorized=false`: no tag, GitHub Release,
public assets, store submission, stable pointer or promotion was created.

Candidate 13 was generated and signed from exact release-index commit
`440f3be1a5f3ae5c6c78c62036858884e5bc3c94`. Its manifest SHA-256 is
`b8a10cf8fbc1683cc9a1540edf74f29fd417f422bc3d2be97f4deae85075190c`,
its detached signature SHA-256 is
`ede7844c2b2a94b0d89b7aa72b75c5ff3eec5e5662ec907c0b181ff08d5c0e4d`,
and its public receipt SHA-256 is
`fc3b1319812df374c27e34c9698af8bcf9a67b66ada95bb4e1be1906d82bb295`.
Main-only signer run `33318660441` signed and independently revalidated all six
freshly rebuilt exact `1.2.0+4049` artifacts using key
`pokrov-release-2026-01`. Candidate 13 binds platform
`7d983c0ab52e9c01f94da8916a6bca6a0039be8d`, client
`ce2581dd16d276d20eace7a56f0337c4b9319168`, and Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 12 after
the Android Core event-fence restart failure. The exact production-signed
x86_64 APK then passed the bounded LDPlayer AWG 3.1 → AWG2 → default warm
lifecycle in one process with green tunnel, DNS and VPN-egress readback; the
sanitized local runtime summary SHA-256 is
`22dbd83bb0267ecd55bfa8b15284d149f5465270edf11bd1f0f9122e21ddb195`.
Physical Android and exact Windows clean-host gates remain manual. Offline
supply-chain validation passed all six artifacts and all eight Windows runtime
files; the final public source-contract and signer Actions completed real steps
with `PASS`. Candidate 13 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer or promotion was created.

Candidate 14 was generated and signed from exact release-index commit
`ef084ae2f8550b7aa488fc1a7de492e706812821`. Its manifest SHA-256 is
`e847bb33c9d7004cb74f0baf311b1b7bf7cd9ab20d72bfe88d3a6c9c8656bc07`,
its detached signature SHA-256 is
`86a76642ecfde2855914be03240c17f2757921a6467bae2ef7a65971eb0ed10f`,
and its public receipt SHA-256 is
`7b616beadbb0aa225d6b2efc2388ec3799df02692835ae1fe6165cea2828c2a1`.
Main-only signer run `33359918180` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:bd060147872d1b0b2810099d87d51f7f05bdf4c24dc55df50a4c162831562110`.
Candidate 14 binds platform
`6f694d003934731045b5d02dccff1d61fecc1380`, client
`75ba7e721cfee486f7189edd51de97aba2746722`, and Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 13 after
the platform dependency-lock refresh. The six client artifacts are
byte-identical to candidate 13; regenerated CycloneDX SBOM, SLSA provenance
and strict-v2 handoff bind them to the successor source tuple. Offline
supply-chain validation passed all six artifacts and all eight Windows runtime
files; the public source-contract and signer Actions completed real steps with
`PASS`. Candidate 14 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer or promotion was created.

Candidate 15 was generated and signed from exact release-index commit
`a86491695ce3e6809818c7604f94a68fda9ad759`. Its manifest SHA-256 is
`d168bafc4d5cb4178196546ea5aa4d85c2a063f1fa14509a25a6ec7a8d162529`,
its detached signature SHA-256 is
`b5c0f4c51bb61a3e15b24ef4e8a0337fe0bfd8cd4fb7f2fff30628a9272ce295`,
and its public receipt SHA-256 is
`72451a7ab48b317774bf8e070344f3ed4999628563e97703d6b7ac900f60350d`.
Main-only signer run `33385577377` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:b29cf15ecdf64555f5c4942ee4bdd9c70da53a598c444c7ff749ce205ba2868e`.
Candidate 15 binds platform
`48669df4cfc466af6957ebfff7daf9eb5fb3cd66`, unchanged client
`75ba7e721cfee486f7189edd51de97aba2746722`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 14
after the platform managed-profile bounded-read correction. The six client
artifacts are byte-identical to candidate 14; regenerated CycloneDX SBOM,
SLSA provenance and strict-v2 handoff bind them to the successor source tuple.
Offline supply-chain validation passed all six artifacts and all eight Windows
runtime files; the public source-contract and signer Actions completed all real
steps with `PASS`. Candidate 15 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer or promotion was created.

Candidate 16 was generated and signed from exact release-index commit
`54cfa03502ffafa5e4fb230a2cbdb0c0572c429f`. Its manifest SHA-256 is
`ae1906e68df755b1e0ce6a77d6ede8256f923e72fe11da57f1cae89a82c4ffe6`,
its detached signature SHA-256 is
`f5df63578d56db84a48eac1c68f1192e81462e8b407b1b6ff877c2b415507a9a`,
and its public receipt SHA-256 is
`1231ab6988746ca0e9725296826de2a9696a9a78600aa5e7f0b0c1b8c5782de4`.
Main-only signer run `33402507136` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:aba50268ad4acffc3fcc360d11dcd026590c3fae1635729a0378588d95c52b8d`.
Candidate 16 binds platform
`719e23dc49407beb9ae30d98d17d4b73d18ae37c`, unchanged client
`75ba7e721cfee486f7189edd51de97aba2746722`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 15
after the confirmed-node managed-profile readiness correction. The six client
artifacts are byte-identical to candidate 15; regenerated CycloneDX SBOM,
SLSA provenance and strict-v2 handoff bind them to the successor source tuple.
Offline supply-chain validation passed all six artifacts and all eight Windows
runtime files; the public source-contract and signer Actions completed all real
steps with `PASS`. Candidate 16 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer or promotion was created.

Candidate 17 was generated and signed from exact release-index commit
`2df538cb4e6e64f291a93ae4cdcebc85ce93fb17`. Its manifest SHA-256 is
`bea4774f48646c672e1ca96b2e48ef9f559b3ec800e7bd7bc6f1a8ee793fdb1e`,
its detached signature SHA-256 is
`e58419f3c4d252db5d2a3cce8cbcc88e5868c201cef8e2df55bcf39991885717`,
and its public receipt SHA-256 is
`bec4c0ccb45b363ca4d2f1baaa872bb7f7fae069b5d8f5ad80270da8556b0ba1`.
Main-only signer run `33463318296` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:08cd43c54b3d82a92ba64725590da4925464ac1327930d4b759a18c36de97f18`.
Candidate 17 binds platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`977c6edd21d4746d5b1b8770d031734df46ad108`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 16
after the dual-delivery-endpoint DE topology correction and exact-ref hosted
replay support landed. The six client artifacts are byte-identical to candidate
16; regenerated CycloneDX SBOM, SLSA provenance and strict-v2 handoff bind them
to the successor source tuple. Offline supply-chain validation passed all six
artifacts and all eight Windows runtime files; the public source-contract and
signer Actions completed all real steps with `PASS`. Candidate 17 remains a
14-day Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer or promotion was
created.

Candidate 18 was generated and signed from exact release-index commit
`5dc25bdde2ce146c65c37c08bf96afebe722f759`. Its manifest SHA-256 is
`d686238265e19b7a63759b735e18a49d8910f1885098dc923c5f1c51130f9a56`,
its detached signature SHA-256 is
`a5584da629e4562b2ec6d79824f5d121e691f8b7e3ce0a83475f6a00464b6324`,
and its public receipt SHA-256 is
`42a4c7381dc8dab6cdb226476f0ab316222bd96f16994d75e10f22f0436fe83d`.
Main-only signer run `33475398520` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:b997c61e2f6adbc958a34bed1f3b068f4ae7add8070beb5ed0a4e511d7b5fcc8`.
Candidate 18 binds platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`820ca1016bdfef0f44a1d217e3804adb9b365ca5`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 17
after the Windows setup added the three required Microsoft VC143 app-local
runtime DLLs, fail-closed service installation, and guarded migration from the
public per-user 1.1.6 install. Offline supply-chain validation passed all six
artifacts and all 11 Windows runtime files. Exact Windows 11 clean-app-state
install/service/IPC/restart/uninstall and public-1.1.6 migration evidence passed;
physical Android Wi-Fi and Beeline network gates remain manual. Candidate 18
remains a 14-day Actions artifact only with `promotion_authorized=false`: no
tag, GitHub Release, public assets, store submission, stable pointer or
promotion was created.

Candidate 19 was generated and signed from exact release-index commit
`43fc20fd25342f314554a89ef75e1122f00aee01`. Its manifest SHA-256 is
`bb78970700d8dc51b6b31caabb76a9b4ca6c94da2f8eef82f1c99ab61b5e6a87`,
its detached signature SHA-256 is
`1d39b7bb7b20481bd165348abc1321ccd9ef4131021505c4054a8c22f6c24e38`,
and its public receipt SHA-256 is
`12b2de4a89eb2fa48e359bc740b39c924941a725d97009387b6343a047094f84`.
Main-only signer run `33489470612` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:f57e5949b25570b2179d75c5bc2ef14049bcdb6aebdf85f307d591a110f037ea`.
Candidate 19 binds platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`10f5516648fd40d6c94eb7a7ca0d05be161d393c`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It rejects and supersedes
candidate 18 after exact ordinary-user testing exposed that the UI tried to
read the `LocalSystem` service process token and then closed the authenticated
pipe. Candidate 19 binds the server PID to the protected SCM service record
without weakening pipe ACLs or server-side caller authorization. Offline
supply-chain validation passed all six artifacts and all 11 Windows runtime
files. Exact Windows 11 clean-app-state installation, non-elevated UI/service
IPC, clean uninstall, and public-1.1.6 migration pass; connected Windows and
physical Android Wi-Fi/Beeline gates remain open. Candidate 19 remains a
14-day Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer, or promotion was
created.

Candidate 20 was generated and signed from exact release-index commit
`61ad0b0e0780775b8f95f1a567e94d75d198a483`. Its manifest SHA-256 is
`046d331274da76ba524f824debb17c4abc080657456c41099246589cc3c1770a`,
its detached signature SHA-256 is
`f5e81d310fa18b464421afe4c0da010e3b9c112c9affba64e7d1631b4f6890ea`,
and its public receipt SHA-256 is
`47429c2cb3b77520257bb63e7a41652d3744e0a4f710589bf4c20eec289b9479`.
Main-only signer run `33509003189` signed and independently revalidated all six
exact `1.2.0+4049` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:8c38f1e92eb3996e4c7b7a01f088e073e8003e79f90ed49ebad1e1ecb2d39fdc`.
An earlier dispatch `33508836174` failed closed on a template SHA-256 mismatch
and created no signed artifact.

Candidate 20 binds platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`8ab9815ab98f111140c0c8ce4e289555652d56e8`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It rejects and supersedes
candidate 19 after exact connected Windows testing exposed unresolved absolute
AppData paths for local binary rule sets. Candidate 20 transfers a bounded
bundle over the existing authenticated IPC channel and materializes four rule
sets in the service-owned protected A/B profile slot. Offline supply-chain
validation passed all six artifacts and all 11 Windows runtime files. Exact
Windows 11 machine install, ordinary UI, default connect, TUN, DNS,
authenticated egress, disconnect rollback, clean uninstall, and public-1.1.6
migration pass. Physical Android Wi-Fi/Beeline, Windows 10, Windows recovery,
and non-default protocol gates remain open. Candidate 20 remains a 14-day
Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer, or promotion was
created.

Candidate 21 was generated and signed from exact release-index commit
`cae911e506d95eb72c1364b847992e30cbf9baf9`. Its manifest SHA-256 is
`ce0b8586d4d9b5b625bbcd2c93b03fd783f89b4958a7fd79e58ef65b52c3dc6`,
its detached signature SHA-256 is
`ef474e6e1e147093b8b15c3cdc29bd35b5779249854a63ef7d6535d2588c7a58`,
and its signer receipt SHA-256 is
`aaa027cc5d71fd567c6f3c0b8a9e3b0e965a67760fd02d1769eb3d54062926f8`.
Main-only signer run `33586752995` signed and independently revalidated all six
exact `1.2.0+4050` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:9bd2ac5e7e69722c143ec1a50fc7e24564396f6fec647f21a6a2a84188823568`.

Candidate 21 binds platform
`e2608130e85d9a0f8fa4b920f46cf3d7679332c3`, client
`1e164586d741484b5ae8fb2ee267ef5dd813cadb`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It rejects and supersedes
candidate 20 after a forced Windows service termination left the durable
recovery journal at `committed` after SCM restart. Candidate 21 resumes that
recovery deterministically on service startup. Offline supply-chain validation
passed all six artifacts and all 11 Windows runtime files. Exact Windows 11
upgrade from the retained committed state, startup recovery, ordinary UI,
default connect, TUN, route/DNS change, authenticated DE egress and exact
disconnect restoration pass. A fresh in-place forced termination of the
already installed candidate 21 service is `NOT_RUN` because UAC was cancelled
before service termination. Physical Android Wi-Fi/Beeline, Windows 10,
non-default protocol, broader leak/lifecycle, payment, operator, legal and final
Gate F checks remain open. Candidate 21 remains a 14-day Actions artifact only
with `promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer, or promotion was created.

Candidate 22 was generated and signed from exact release-index commit
`d45b5035e135130cbdec3968e712201e5bc78230`. Its manifest SHA-256 is
`81c56e9fcf7478c50d5881538d26fd72459f05a04d9cce403ec99d8ecdcc7d59`,
its detached signature SHA-256 is
`b230a4423064f5b45813fec6eb88a956b820cb6603ad2986b641f2bdd4a8a387`,
and its signer receipt SHA-256 is
`6512351934514fd63347ddd7f40e83c5ab56148a8e5e1eb899ac22ed12812124`.
Main-only signer run `33656388958` signed and independently revalidated all six
exact `1.2.0+4051` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:c41c82689af24facab3e4f753c5eed7c72ab2ea358ac66df4aff905dae2db6ed`.

Candidate 22 binds platform
`d16087d5da509e17163bdd7293bec5711aa7eedc`, client
`0aad6bbb3a8baf9bd9e2436ed9e57f7c6fbbafed`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 21
after isolating rejected or interrupted Windows pipe sessions from the service
accept loop. Offline supply-chain validation passed all six artifacts and all
11 Windows runtime files. Exact Windows 11 upgrade from build 4050 to 4051,
ordinary-user UI, rejected pre-hello continuity, default Germany TUN/route/DNS
and authenticated DE egress pass. A fresh forced service termination changed
the process id, completed startup rollback to a clean journal, then the
ordinary UI restaged the profile, reconnected and restored the exact RU
route/DNS baseline after disconnect. Physical Android Wi-Fi/Beeline, Windows
10, remaining protocol/lifecycle, provider, Operator, legal and final Gate F
checks remain open. Candidate 22 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer, or promotion was created.

Candidate 23 was generated and signed from exact release-index commit
`95f9f03ae80eb291d7138df1b3996054f9a05336`. Its manifest SHA-256 is
`5073c201541be70be124ab305203f830fd3c531725ad4f6632115e2e738301a1`,
its detached signature SHA-256 is
`92027334651409cdf5e8efe7f53e0992bff54bffb2381ae382263e00b6d78863`,
and its signer receipt SHA-256 is
`d11e24ac84846231a52f42a2dc0f64576d3b7a04a8e005794210457c35828ba6`.
Main-only signer run `33690078543` signed and independently revalidated all six
exact `1.2.0+4052` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:2ca86de6dfcd006a067f90dbae068d365ae18aa3df081c989a5eecd7b48bc3c8`.

Candidate 23 binds platform
`5ba4dba3db0f900466d2f36d84d981a0a9c9fe68`, client
`df9ed85bb0e7fd7bf1e1c43d033825212c2f6354`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 22
with corrected Windows connected-uninstall process, tunnel, service, and file
cleanup ordering. Offline supply-chain validation passed all six artifacts and
all 11 Windows runtime files; bounded artifact and installed-payload scans found
no definite secret material, and native Windows CTest passed `7/7`. Exact
Windows 11 fresh install, `11/11` installed-file identity, running service, and
idle zero-tunnel state pass. The exact connected-uninstall replay, physical
Android Wi-Fi/Beeline, Windows 10, remaining protocol/lifecycle, provider,
Operator, legal, and final Gate F checks remain open. Candidate 23 remains a
14-day Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer, or promotion was
created.

Candidate 24 was generated and signed from exact release-index commit
`a2fb1067adc4f2881299b45929a0d46736f74fff`. Its manifest SHA-256 is
`bdd51f2c428298e3178fd94d9befaf79aa442445a384f52882995ffd5d9ddeed`,
its detached signature SHA-256 is
`ef47e339cafe23bd994844e70fe8263902a0d62f03312a35b10536913e7ac0bc`,
and its signer receipt SHA-256 is
`1ff20e15adda261dff182c1166a276270a05721f3770f5cc4df1d77b61153343`.
Main-only signer run `33698144521` signed and independently revalidated all six
exact `1.2.0+4053` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:09d407e22916f347c4e466ef098966c8f21a5aeb1cadd5c30e9741938f5e6656`.

Candidate 24 binds platform
`06b932b48ffcb92c8ec024b8892aaa9c36359673`, client
`54259b0f84e16c58e2d1f5f04b369af4fd0834b2`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 23
after the confirmed Windows named-pipe startup contention failure. The client
adds bounded connection retries and a 32-client contention regression test.
Full client, Android, Linux, Windows and Gradle tests passed; Debug native
Windows CTest passed `8/8`. Offline supply-chain validation passed all six
artifacts and all 11 Windows runtime files, and bounded scans found no definite
secret material. Exact candidate 24 Windows VM install, physical Android
Wi-Fi/Beeline, Windows 10, remaining protocol/lifecycle, provider, Operator,
legal, and final Gate F checks remain open. Candidate 24 remains a 14-day
Actions artifact only with `promotion_authorized=false`: no tag, GitHub
Release, public assets, store submission, stable pointer, or promotion was
created.

Candidate 25 was generated and signed from exact release-index commit
`18d9cb4c5541481c5e60713376904f962ec19a7c`. Its manifest SHA-256 is
`7161bae715d590fac0623561d147e4d9ee069da14a5e3645001cc4c39aa329b6`,
its detached signature SHA-256 is
`f83cf5acbfa8aa55a45a73f03a2f4e829661215a788f68e8b7b36764b1ff3d14`,
and its signer receipt SHA-256 is
`2c18b318fb538eeec69a9226f4eacf5a19066b0c1d479d26a7b6a13325cdd2cf`.
Main-only signer run `33709201344` signed and independently revalidated all six
exact `1.2.0+4053` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:7dc9beb122c0315017835cad6877513754b9acc5bd0120d369dd16f2602e61bb`.

Candidate 25 binds platform
`883cd1038a087fbf9f570cffcbfdfd5f5197ffd4`, unchanged client
`54259b0f84e16c58e2d1f5f04b369af4fd0834b2`, and unchanged Core artifact
source `cd8f0f4169d570d693992a959d81d17c2c44884d`. It replaces candidate 24
after the platform-only webapp development-lock correction. All six client
artifacts are byte-identical to candidate 24; candidate-specific SBOM,
provenance and strict-v2 handoff bind those bytes to the new platform source.
Fresh webapp, adminapp and marketing audits reported zero findings, the full
platform local-quality gate passed, and exact post-merge Contract and
Guardrails jobs passed. Offline supply-chain validation passed all six
artifacts and all 11 Windows runtime files. Exact candidate 25 Windows VM
install, physical Android Wi-Fi/Beeline, Windows 10, remaining
protocol/lifecycle, provider, Operator, legal, and final Gate F checks remain
open. Candidate 25 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer, or promotion was created.

Candidate 29 was generated and signed from exact release-index commit
`71e2c71fbc1aab0b76ca634e283eaa362e605b97`. Its manifest SHA-256 is
`231e3d5264ba18e68c5aac9b6faa1bca3864c011fbff3771960e84a9edc1e9df`,
its detached signature SHA-256 is
`215f8234376d23806ad89e0d8f7d2aa0f6ad2fcc3dfeeec593e6a6f71db27bfc`,
and its signer receipt SHA-256 is
`097b0c3fbeb63c2e0a2557e9fc614363ef9883c233b6b99dc8c8fb3067524fcf`.
Main-only signer run `33741376651` signed and independently revalidated all six
exact `1.2.0+4053` artifact identities using key
`pokrov-release-2026-01`; the retained Actions artifact digest is
`sha256:e5683b5c7ea9472a8fc8e3689d58cf1d80f64b3effe0ddce5039a19017d1250c`.

Candidate 29 binds platform
`efb05e0899ad51afd4453ae2fb75f8cafe96db7e`, client
`7e3e771fe36333a75244cbfd828c60beb84c7ff1`, and Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`. It supersedes candidate 25
after the Windows installer owner-reuse correction. All six artifacts were
rebuilt through the headless CLI path. The full client release gate, native
Windows Release and Debug tests, Android production signing, AAB integrity,
static archive scan and offline supply validation passed. The exact Windows
setup then passed candidate-28-to-29 upgrade, `11/11` installed-file identity,
ordinary-user UI launch, LocalSystem service, direct TUN/DNS connect and clean
disconnect, and connected guest reboot recovery in the isolated Windows VM.
Physical Android Wi-Fi/Beeline, managed-node protocol matrices, Windows 10,
sleep/resume, provider, Operator, legal and final Gate F checks remain open.
Candidate 29 remains a 14-day Actions artifact only with
`promotion_authorized=false`: no tag, GitHub Release, public assets, store
submission, stable pointer, or promotion was created.

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
new exact source tuple. Candidate 9 retains those exact six bytes while binding
the platform-only RU-origin HMAC permission-contract correction through a new
SBOM, provenance, and strict-v2 handoff. Candidate 10 again retains the exact
six bytes while binding the corrected redacted connected-family and
manifest-driven HTTPS threshold behavior for the RU-origin probe plane. None
of these candidates authorizes promotion. Candidate 11 is retained as the
rejected pre-lab replacement attempt; candidate 12 carries the Smart Connect
lab isolation fix, build `4048`, fresh exact bytes, and current-safe Windows
packaging claims without promoting xHTTP or Hysteria2 from lab status.
Candidate 13 carries the Android Core event-fence restart fix, build `4049`,
fresh exact bytes and the bounded same-process LDPlayer AWG 3.1 → AWG2 →
default proof. It still does not promote xHTTP or Hysteria2 from lab status.
Tracking a reviewed input does not create, sign or publish a candidate. The
manual workflow must still bind the zero-commit placeholder to exact `main`,
sign the canonical bytes and retain the artifact receipt before candidate
creation is proved. Candidate inputs, release notes, and known-issues files are
immutable once their hashes have been signed. Later runtime results are added
under `candidate-evidence/`; they do not rewrite the signed snapshot or
authorize promotion.
