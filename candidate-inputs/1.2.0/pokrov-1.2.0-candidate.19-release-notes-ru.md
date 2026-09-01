# POKROV 1.2.0 — direct beta candidate 19

Это точный закрытый кандидат Android и Windows после исправления IPC между
обычным Windows UI и службой `LocalSystem`, выявленного на candidate 18. Он
привязан к platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`10f5516648fd40d6c94eb7a7ca0d05be161d393c` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 19 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 18

Candidate 18 сохранён как неизменяемое evidence и отклонён: установленный UI,
запущенный обычным пользователем, пытался прочитать token процесса службы
`LocalSystem`. Windows ожидаемо возвращала access denied; клиент отвергал
правильную службу, закрывал pipe, а служба завершалась с кодом `5`.

Candidate 19 собран заново из уже влитого client `main`. Windows package теперь
проверяет server PID через защищённую SCM-запись `POKROVService`: состояние,
точный PID, тип own-process, путь соседнего `pokrov_service.exe` и аккаунт
`LocalSystem`. ACL pipe и авторизация вызывающего процесса на стороне службы
не ослаблены. Исправления candidate 18 — app-local Microsoft VC143 runtime,
транзакционный installer и guarded migration публичной per-user версии 1.1.6
— сохранены.

Изолированная Windows 11 VM подтвердила точный setup SHA-256
`0782152d3a992b1b6320043b9b8ccedb2944b76dcbf939bf7a6ebdad9759f8ff`:
установку, `11/11` файлов, запуск UI обычным пользователем, сохранение службы
`Running` с exit code `0` и защищённую authenticated IPC-сессию. Отдельно
подтверждены clean uninstall и migration с публичной 1.1.6 с финальной
очисткой. Live TUN, connected DNS/egress, stop/restart, sleep/reboot/crash,
connected uninstall, idle DNS/routes и интерактивный SmartScreen остаются
отдельными проверками для этих точных байтов.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `0d6e70f9a7177eff702f56f7c99f318277aefad193de2621eee658f27bdd71ca`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4049`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `0d6aa17ef8bf5f6e279f15211816bc1d703a16285773f75cb034393346159310`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `e0b58a200b2f74a090e34276607174936e577767239005ef58cfdd6b52f69dd4`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `a0afffdc62800c525ebea96904550a2fd24a91cb4de565652618bddca378fee4`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `01982515d342348d7bdf8f86e07f195c9eae0d9922b07f88e0ffd605a9bfd2d7`;
- размер: `126265618` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Candidate 19 APK ещё не запускался в LDPlayer или на физическом телефоне.
LDPlayer host Windows использует собственный Hiddify/TUN, поэтому его будущая
проверка ограничена install/launch/ABI/crash и byte-identity; сетевой результат
не будет release proof. Wi-Fi и Билайн, AWG 3.1/AWG2, Smart DNS, WARP,
IPv4/IPv6/leak и endurance должны быть проверены на физическом ARM64-телефоне
с этими точными APK-байтами.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `0782152d3a992b1b6320043b9b8ccedb2944b76dcbf939bf7a6ebdad9759f8ff`;
- размер: `29129601` байта;
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
candidate 19 client runtime на физическом Wi-Fi/Билайне ещё не получил PASS.
xHTTP и Hysteria2 остаются post-1.2.0 reserve/lab lanes.

## Точная поставка

Strict-v2 handoff и offline validator связывают `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`d494b4f96ce122cfc67cd34005039da8d52e5202afae49fea2d6e423301e7818`.
Provenance SHA-256:
`99956e5118a7d66a9a8ff805dbc0967380bc3ba65ebc8b9a9f05f722c20851ad`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
