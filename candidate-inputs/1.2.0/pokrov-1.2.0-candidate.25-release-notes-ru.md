# POKROV 1.2.0 — direct beta candidate 25

Это закрытый successor-кандидат `1.2.0+4053`, который добавляет только
platform webapp development-lock correction. Он привязан к platform
`883cd1038a087fbf9f570cffcbfdfd5f5197ffd4`, неизменившемуся client
`54259b0f84e16c58e2d1f5f04b369af4fd0834b2` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 25 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Изменение после candidate 24

Webapp lock обновляет `@humanfs/node 0.16.7 -> 0.16.8`, совместимый
`@humanfs/core 0.19.1 -> 0.19.2` и требуемый `@humanfs/types 0.15.0`.
`package.json` и application source не менялись. Fresh audits webapp,
adminapp и marketing возвращают ноль findings; полный local-quality gate
проходит `15/15`, client widgets `413/413`, cabinet `69/69`, static
performance `9/9`. Точные post-merge Contract и Guardrails для нового
platform SHA проходят.

Поскольку Android, Windows, client и Core source не менялись, candidate 25
явно переиспользует все шесть candidate 24 client artifacts побайтно. Это не
rebuild и не relabel старого platform source: новый SBOM, provenance и
strict-v2 handoff привязаны к candidate 25 и новому platform SHA.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `71e15a2ca70d6143ca4beab9587e3d7abaea42077ac317566c3f5c36ff8cf52b`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4053`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `4e8cac9e8619c25ccb42a923a19f4ad04d52b7f3c4a08945f0c1c5cd0cdf9be9`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `592781d254d79c7821b339bc2eb701f66501c2294a8bda24935db6f0a603dc5e`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `7bcdc01edb25b37f2297ea2adadace4b12f0135b93ef000e5464d22132f49d7a`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `bd892e56dffe0e38d8890e384c6169e12ae73eb88eb8cdcca7d0602fe203c086`;
- размер: `126263352` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

Все APK production-signed, release/non-debuggable. AAB сохраняет точный
production upload-key fingerprint. Google Play submission не выполнялся.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `ffc9b07c59f75372b48c5c1e94551d6d9af710ac0287cd1352142b0964707fb3`;
- размер: `29139238` байт;
- версия: `1.2.0+4053`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest `344b842cd0222aa642115c00f42810bf922492394435271d43d9837169f187c0`
связывает `11/11` обязательных файлов. Owner exception сохраняет обязательное
предупреждение SmartScreen/`Unknown publisher` и не разрешает trusted, Store
или broad-stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.
Hysteria2 и xHTTP не переводятся в обязательную линию 1.2.0 без отдельного
interop, network и rollback evidence.

## Точная поставка

Strict-v2 handoff и offline validator связали `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`f6d8ec5b7ab999bd8d7ca648aed4ff640543fef11c8176781922e82482779d70`.
Provenance SHA-256:
`4f106a2ed15b37457816460d42db5706f79c377bf7671bb9ba58bd93cf414f0d`.
Release-handoff SHA-256:
`b65b9e7ec16b85c55235f4f5b9481507e13dccd07f0ba2c0a74202d661702908`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt. Даже после подписи кандидат не создаёт
тег, GitHub Release, публичные assets, store submission или stable pointer.
