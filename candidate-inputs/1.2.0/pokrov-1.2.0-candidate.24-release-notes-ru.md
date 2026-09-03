# POKROV 1.2.0 — direct beta candidate 24

Это точный закрытый кандидат Android и Windows `1.2.0+4053`. Он заменяет
candidate 23 и привязан к platform
`06b932b48ffcb92c8ec024b8892aaa9c36359673`, client
`54259b0f84e16c58e2d1f5f04b369af4fd0834b2` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 24 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 23

Windows CLI и UI используют ограниченные повторы подключения к локальному
каналу службы. Это устраняет подтверждённую гонку candidate 23: при одновременном
старте множества клиентов служба оставалась запущенной, но подключения могли
получить временный отказ. Тест на 32 параллельных клиента добавлен в исходники и
прошёл вместе с полным клиентским набором тестов.

Точный Windows runtime пересобран из неизменившегося Core и воспроизводит
ожидаемый SHA-256 DLL. Debug native CTest прошёл `8/8`; Release-тест нового
pipe-клиента прошёл. Старый service integration harness в Release не считается
исполненным, потому что его test-mode компилируется только в Debug.

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

Все APK production-signed, release/non-debuggable. AAB проверен штатным
инструментом подписи и имеет ожидаемый production upload-key fingerprint.
Google Play submission не выполнялся.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `ffc9b07c59f75372b48c5c1e94551d6d9af710ac0287cd1352142b0964707fb3`;
- размер: `29139238` байт;
- версия: `1.2.0+4053`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest `344b842cd0222aa642115c00f42810bf922492394435271d43d9837169f187c0`
связывает `11/11` обязательных файлов. Owner exception сохраняет обязательное
предупреждение SmartScreen/`Unknown publisher` и не разрешает trusted, Store или
broad-stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.

AWG control-plane, client materialization и Smart DNS имеют source-level
доказательства, но они не заменяют live interop точного APK candidate 24.
xHTTP и Hysteria2 не переводятся в обязательную линию 1.2.0.

## Точная поставка

Strict-v2 handoff и offline validator связали `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`3fbfb3e5e1d33b942cac82714955d27ff46fcad1608d0bfaa694dd6c91893f3d`.
Provenance SHA-256:
`7b89514a782f092e406e7d5c2fab166bbbe62997101fcde12f75ae3f0326adf4`.
Release-handoff SHA-256:
`87c688ffdd2f71363aa8cf4ca7bf99147d6109cc21d9d5887bc4f025f2fd2b63`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt. Даже после подписи кандидат не создаёт
тег, GitHub Release, публичные assets, store submission или stable pointer.
