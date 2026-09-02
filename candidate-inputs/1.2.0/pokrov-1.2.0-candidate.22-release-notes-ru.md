# POKROV 1.2.0 — direct beta candidate 22

Это точный закрытый кандидат Android и Windows `1.2.0+4051`. Он заменяет
candidate 21 и привязан к platform `d16087d5da509e17163bdd7293bec5711aa7eedc`, client `0aad6bbb3a8baf9bd9e2436ed9e57f7c6fbbafed` и Core
artifact source `cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 22 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 21

Windows-служба теперь изолирует отклонённые или оборванные IPC-подключения:
клиент, закрывший pipe до hello, не завершает основной accept-loop службы.
На изолированной Windows 11 VM точный setup обновил установленный build 4050 до
4051. Обычный non-elevated пользователь подтвердил идентичность `11/11`
runtime-файлов, LocalSystem/Auto service, первый оборванный pre-hello pipe,
следующее подключение к тому же процессу службы и запуск UI без повышения прав.

Тот же VM-срез связывает исходную сеть, default connect с TUN и отличающимися
egress/route/DNS, восстановление подключения после перезапуска службы и точный
возврат исходных egress/route/DNS после disconnect. Эти проверки относятся
только к точным байтам candidate 22 и указанной Windows 11 VM.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `f6dd81ec42c5eabf9c56ce1c11663518a14e904735cb1b045a352137eb1720f7`;
- размер: `295370157` байт;
- версия: `1.2.0`, build `4051`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `77bfcaa298d7b9ef4ccf36f179daa715eb619aade8247299dc65075a9b9a6bf4`, `101366674` байт;
- `pokrov-android-armeabi-v7a.apk` — `3f3505f9535a306cf30855bb5e6f3a67826139c3c2298fc1f96e5d701e26036c`, `90778784` байт;
- `pokrov-android-x86_64.apk` — `31962adcc276eb517c1807b7c2ceb8be28d8d4c86755f69924d3ded8a9cfc181`, `109951985` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `fe075bb328133a0da762248ae5364c101853fc72200644d6d21597aad0c875bf`;
- размер: `126263361` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

Все APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Точные candidate 22 APK всё ещё требуют отдельного LDPlayer install/launch и
физического ARM64 runtime на Wi-Fi и Билайне: default/fallback, AWG 3.1, AWG2,
Smart DNS, WARP, IPv4/IPv6/leak, Doze/OEM и endurance.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `effc6a8ed7ccfa943986aca93f4d1d846d66c8d42730ea0b77854b48f77bf409`;
- размер: `29137688` байт;
- версия: `1.2.0+4051`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest связывает `11/11` обязательных файлов. Owner exception сохраняет
обязательное предупреждение SmartScreen/`Unknown publisher` и не разрешает
trusted, Store или broad-stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.

Для точного source tuple прошли AWG control-plane `72/72` и client
materialization `2/2`; это source-only evidence, а не live Android/Windows
interop. Smart DNS routing `18/18`, UI `2/2` и Windows endpoint contract прошли
в своих ограниченных срезах. In-app выбор, физический DoH/leak/load и реальные
авторизованные ChatGPT/Gemini/Xbox sessions остаются открыты. xHTTP и Hysteria2
не переводятся в обязательную линию 1.2.0.

## Точная поставка

Strict-v2 handoff и offline validator связывают `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256: `be462e77e4d5ea03b85dfc1bdcd3b9681c1d3023414c8781c56c9e7f3d53f19e`. Provenance SHA-256:
`13bf87993cdcd7dc7cb80791ccbc15ef6b886d390d1ef563c5cd3718229b5ee7`. Release-handoff SHA-256: `6fd9cb567e286b322133c5ec60e830e196acaf363a502fb5413d77ecdb58e566`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt. Даже после подписи кандидат не создаёт
тег, GitHub Release, публичные assets, store submission или stable pointer.
