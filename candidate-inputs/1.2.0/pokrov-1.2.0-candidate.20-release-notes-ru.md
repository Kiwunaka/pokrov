# POKROV 1.2.0 — direct beta candidate 20

Это точный закрытый кандидат Android и Windows после исправления передачи
локальных бинарных rule-set из обычного Windows UI в службу `LocalSystem`. Он
привязан к platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`8ab9815ab98f111140c0c8ce4e289555652d56e8` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 20 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 19

Candidate 19 сохранён как неизменяемое evidence и отклонён. Клиент записывал в
managed profile абсолютные AppData-пути к локальным `.srs`, а служба переносила
в защищённый каталог только JSON. Core получал недоступный путь и завершал
подключение с `CORE-005`.

Candidate 20 собран заново из уже влитого client `main`. Обычный UI передаёт
ограниченный bundle через существующий authenticated IPC. Служба строго
проверяет имена, число и общий размер rule-set, материализует байты в защищённый
A/B slot рядом с service-owned profile и только после этого атомарно применяет
JSON. Собственная криптография не добавлялась; ACL pipe и проверка вызывающего
процесса не ослаблены.

Изолированная Windows 11 VM подтвердила точный setup SHA-256
`330b87cb074a04f43cb7004e4c03cdd0c692b54397acbc223f25dd6e0be8587f`:
машинную установку, `11/11` файлов, службу `LocalSystem`, обычный UI, четыре
service-owned rule-set, default Germany connect, TUN, DNS `172.19.0.2`,
authenticated egress через Германию, disconnect с возвратом исходных маршрутов
и DNS, clean uninstall и migration с публичной 1.1.6. Отчёт не содержит raw
профиль, адреса подключения или открытый egress IP.

Этот PASS относится к точному Windows 11 default-path кандидату. Windows 10,
AWG 3.1/AWG2 на Windows, sleep/reboot/crash, connected uninstall и
интерактивный SmartScreen остаются отдельными проверками.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `927270b36ceedc34caa6feaf22c548094fda759d4ed211bdc7b017330f3f48a8`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4049`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `8dfca42e13eb4d64c9d627f377d8a201ad2a74fa0ca64c11e45c914d9a89056c`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `7d41ed5b4856443033203ce4c889377926fb16d1ccc84f47bd39121269e63b6d`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `d8ae790d93a956e31c40778b769f7af69e6658d1e10f346d68096e7e764264b1`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `96af83cf988d26dab876f6e09a3862b6a6d568b29931dc5f2f76fbc914eee115`;
- размер: `126263352` байта;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Candidate 20 APK ещё не получил физический runtime PASS. LDPlayer за host
Hiddify/TUN пригоден только для install/launch/process/crash smoke, но не для
release-сетевого доказательства. Wi-Fi и Билайн, default/fallback, AWG 3.1,
AWG2, Smart DNS, WARP, IPv4/IPv6/leak и endurance должны быть проверены на
физическом ARM64-телефоне с этими точными APK-байтами.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `330b87cb074a04f43cb7004e4c03cdd0c692b54397acbc223f25dd6e0be8587f`;
- размер: `29140987` байт;
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
candidate 20 client runtime на физическом Wi-Fi/Билайне ещё не получил PASS.
xHTTP и Hysteria2 остаются post-1.2.0 reserve/lab lanes.

## Точная поставка

Strict-v2 handoff и offline validator связывают `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`afd0abf6da411027892953b6c5724748061a132b2e5de6656952f04edac34959`.
Provenance SHA-256:
`f6b4bb3c32c5fbc6906e65cef5c72ba82fc309964454413160be25a037e10bd2`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
