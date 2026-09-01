# POKROV 1.2.0 — direct beta candidate 18

Это точный закрытый кандидат Android и Windows после исправления Windows-
установщика candidate 17. Он привязан к platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`820ca1016bdfef0f44a1d217e3804adb9b365ca5` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 18 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 17

Candidate 17 сохранён как неизменяемое evidence и отклонён: его Windows setup
не включал `msvcp140.dll`, `vcruntime140.dll` и `vcruntime140_1.dll`. На чистой
Windows служба не могла стартовать, а старый installer ошибочно возвращал код
`0`.

Candidate 18 собран заново из уже влитого client `main`. Windows package теперь
включает Microsoft-signed x64 VC143 app-local runtime, проверяет его signer и
фиксирует все три DLL в manifest/SBOM. Регистрация службы стала транзакционной:
ошибка запуска возвращает ненулевой setup exit и удаляет частичную установку.
Добавлена guarded migration публичной per-user версии 1.1.6 в machine-wide
службу: старый install удаляется только после успешного запуска новой службы.

Изолированная Windows 11 VM подтвердила точный setup SHA-256
`21dca69a4cffe9648bf9788c1279606896c798b32617dd88fa0d9c1e9c1bf2d3`:
установку, `11/11` файлов, службу `LocalSystem`, authenticated IPC,
stop/restart, clean uninstall и отсутствие изменения idle DNS/routes. Второй
сценарий подтвердил migration с публичной 1.1.6 и финальную очистку. Live TUN,
connected DNS/egress, sleep/reboot/crash и интерактивный SmartScreen остаются
отдельными ручными проверками.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `428fa89f12a3079a90123711161d7b66f7c1c5e545c5db9248be0443a639e91d`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4049`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `4983209204ba4a1090483ffb3c6f6741261d80215ff1a2703e951093c5166297`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `9f6e67e3e8a4bad81f4c80c32653cc5b4849b73cd26f82a29a19096e453d5a22`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `ed0917660ab00e3258308b1cb53c9106b5d292bc8f1a0f24c13a169f32c2b9f0`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `188ec02eda345a1a821e91d2908c73a8b4a385fcf640de3f38719cbdeeafebd1`;
- размер: `126265673` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Exact x86_64 APK установлен в LDPlayer с проверкой байтов установленного
`base.apk`, версии и отсутствия crash. Сетевой результат LDPlayer не считается
release proof: host Windows использует собственный Hiddify/TUN. Wi-Fi и Билайн,
AWG 3.1/AWG2, Smart DNS, WARP, IPv6/leak и endurance должны быть повторены на
физическом ARM64-телефоне с этими точными APK-байтами.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `21dca69a4cffe9648bf9788c1279606896c798b32617dd88fa0d9c1e9c1bf2d3`;
- размер: `29127743` байта;
- версия: `1.2.0+4049`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

В manifest находятся `11/11` обязательных файлов. App-local runtime имеет
отдельные SHA-256 и Microsoft signer proof на build-host. Owner exception
сохраняет обязательное предупреждение SmartScreen/`Unknown publisher` и не
разрешает trusted/store/stable claim.

## Протокольная линия

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Собственной
криптографии и отдельного бренда AWG нет.

Оба lab-профиля выключены по умолчанию. Серверные listeners сохранены, но
candidate 18 client runtime на физическом Wi-Fi/Билайне ещё не получил PASS.
xHTTP и Hysteria2 остаются post-1.2.0 reserve/lab lanes.

## Точная поставка

Strict-v2 handoff и offline validator связывают `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`60499706a642cfe38ef696f41d2a6955373b112943ed5a982f4b6eb0b2f57f55`.
Provenance SHA-256:
`9417e86a3da9675dc39df0895a74e4d8bf2d50bf48f931c3efe5c431b498c8f1`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
