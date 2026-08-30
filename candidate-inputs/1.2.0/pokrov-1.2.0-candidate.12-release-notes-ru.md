# POKROV 1.2.0 — direct beta candidate 12

Это новый точный закрытый кандидат Android и Windows, собранный из platform
`9e873eb496f13edc098e27f1a233f227d0bf48dc`, client
`5b1aa02b79212f7b55e76e5086a41a84efb36195` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`. Candidate 12 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go.

## Что изменилось после candidate 11

Candidate 11 отклонён для замены: повторный AWG 3.1 lab-прогон остановился до
выдачи профиля, потому что обычные Smart Connect exclusions ошибочно
применялись к явно выбранной lab-локации. В candidate 12 `awg2_lab`,
`awg31_lab` и `hy2_lab` очищают Smart Connect-контекст и идут через отдельный
явный lab-путь. Полный bootstrap-набор `86/86`, Flutter analyze и
cross-repository contracts прошли локально.

Windows packaging metadata больше не переносит retained candidate 8 evidence
как доказательство текущего кандидата. Исторический current-host результат
прямо помечен как относящийся только к старым байтам. Все шесть клиентских
артефактов заново собраны из exact client source `5b1aa02…6195`; reuse старых
APK, AAB или EXE не заявляется.

VLESS/Reality остаётся основным стабильным маршрутом. AWG 3.1 — второй
приоритетный transport в закрытой lab-линии, AWG2 — скрытая совместимость.
xHTTP рассматривается как резервный transport VLESS, а Hysteria2 — как
последующий bounded lab fallback; они не объявляются готовыми или включёнными
в этом кандидате. Собственной криптографии и бренда «POKROV AWG» нет.

## Android

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `d3ee5cd24207426607aa550293d3534b47df3a0e7319137ead72a98136c2e5a3`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4048`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `0345607856166416837c00842048ee9f41286ec64691768159593a05e050646e`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `7f11de91628918536ec114540bb66d69f24d099355eb3d0a6b25679a920bfc12`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `e7f74fb22e981c1765642e9197c785b7242827db26b2a623f42ab122dadddd3c`, `109951989` байт.

Store AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `87f37243c20bc5f934976898964c3633def4eb410606af190930d938c690e4c8`;
- размер: `126265684` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK прошли `apksigner`, package/version/ABI и release/non-debuggable проверки.
AAB прошёл JAR signature integrity и точный production fingerprint; сертификат
self-managed и не имеет публичной PKI-цепочки. Загрузка в Google Play не
выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `ebbe06f5196fc6bc25b5eaa960d6c8afd834b9d09e3ae3a6c42e3cd07289c99c`;
- размер: `28931263` байт;
- версия: `1.2.0+4048`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Runtime manifest совпал для всех `8/8` обязательных файлов. Свежая сборка
прошла после полного локального Windows/Flutter/Gradle gate предыдущего exact
runtime-среза и после focused contract-проверок metadata-исправления. Это не
доказывает TUN, DNS capture, leak protection, install/service/recovery и
uninstall на чистой Windows 10/11 VM. SmartScreen и `Unknown publisher`
ожидаемы.

## Точная поставка

Strict-v2 handoff и fail-closed offline validator подтвердили `6/6`
артефактов и `8/8` Windows runtime-файлов. CycloneDX 1.5 SBOM содержит `349`
компонентов; SLSA/in-toto provenance содержит шесть exact subjects. Core AAR и
DLL имеют SHA-256
`2a9677d9e24ed7ef66d4e98f90e7033eb5450c9a2755f0fe6b8bba58036c6a69` и
`f284fa8841f1a45271874a7a05ed6093fb0e3efbdd03e00001edd046be708204`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
