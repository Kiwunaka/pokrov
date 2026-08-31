# POKROV 1.2.0 — direct beta candidate 14

Это новый точный закрытый кандидат Android и Windows после обновления
platform-зависимостей. Он привязан к platform
`6f694d003934731045b5d02dccff1d61fecc1380`, client
`75ba7e721cfee486f7189edd51de97aba2746722` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 14 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что изменилось после candidate 13

Candidate 13 сохранён как неизменяемое evidence, но не может продвигаться с
прежними platform lock-файлами. В successor обновлены прямые Python pins:

- `aiohttp 3.14.3`;
- `cryptography 50.0.1`;
- `paramiko 5.0.0`;
- `requests 2.34.2`;
- `pytest 9.1.1`;
- `python-dotenv 1.2.3`.

Production и test hash-locks установлены в новом изолированном Python 3.12
окружении. `pip check`, dependency contract и два свежих lock-аудита прошли;
известных проблем в точных lock-файлах не найдено. Полный platform test slice,
выполненный до freeze на том же дереве, содержит `3622 passed`, `10 skipped`,
`274 subtests passed` и ноль нерешённых ошибок.

Client commit после candidate 13 меняет только документацию. Core source и
runtime-байты не менялись. Поэтому шесть build `4049` артефактов переиспользованы
только после проверки имени, размера и SHA-256. Для candidate 14 заново
сформированы CycloneDX SBOM, SLSA/in-toto provenance и strict-v2 handoff с
новой точной source tuple.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `960712643013ce8f2383ae3068d562c9971cc69184477f650972d0153a1409d4`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4049`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `9bcdbe00fe8f8ed029894a65d531614f4fb912dda27e5fb1bb088c5b7516cc74`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `6308dcdec7ca5f360b1a3726690fca3e80da330906c3d2fe3457e26f44bbd68e`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `73c43e21dfc984c474941e14800c551f9545fe423b8f11458f6d41b8cb9af5ff`, `109951989` байт.

Store AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `5cddb0d264a05db59c099af8a26f26dd3094746632222e1527e9c0a129801e42`;
- размер: `126265693` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK остаются production-signed, release/non-debuggable. AAB сохраняет JAR
signature integrity и точный production fingerprint. Google Play submission
не выполнялся.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `0afaf6e1d73a7e72762d945557f48793646a9bdbf12bb8ca2e843d4b94df276c`;
- размер: `28932793` байт;
- версия: `1.2.0+4049`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Runtime manifest совпадает для всех `8/8` обязательных файлов. SmartScreen и
`Unknown publisher` ожидаемы. Чистая Windows 10/11 VM, TUN, DNS, recovery и
uninstall для этих exact bytes остаются ручными проверками.

## Протокольная линия

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Собственной
криптографии и отдельного бренда AWG нет.

Candidate 13 уже доказал exact x86_64 bytes на LDPlayer в последовательности
AWG 3.1 → AWG2 → default/Auto. Candidate 14 сохраняет те же APK bytes, но новый
candidate-specific runtime credit появится только после отдельного readback,
его нельзя переносить автоматически.

xHTTP и Hysteria2 остаются post-1.2.0 reserve/lab lanes и не являются условием
базовой работоспособности 1.2.0.

## Точная поставка

Strict-v2 handoff и offline validator подтвердили `6/6` артефактов и `8/8`
Windows runtime-файлов. CycloneDX 1.5 SBOM содержит `349` компонентов;
SLSA/in-toto provenance содержит шесть exact subjects. Core AAR и DLL имеют
SHA-256 `2a9677d9e24ed7ef66d4e98f90e7033eb5450c9a2755f0fe6b8bba58036c6a69`
и `f284fa8841f1a45271874a7a05ed6093fb0e3efbdd03e00001edd046be708204`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
