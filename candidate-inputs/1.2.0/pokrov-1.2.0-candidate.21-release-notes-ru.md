# POKROV 1.2.0 — direct beta candidate 21

Это точный закрытый кандидат Android и Windows `1.2.0+4050`. Он заменяет
отклонённый candidate 20 и привязан к platform
`e2608130e85d9a0f8fa4b920f46cf3d7679332c3`, client
`1e164586d741484b5ae8fb2ee267ef5dd813cadb` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 21 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 20

Candidate 20 сохранён как неизменяемое evidence и отклонён. После принудительной
остановки Windows-службы SCM запускал новый процесс, но recovery journal
оставался на стадии `committed`; сеть уже была восстановлена, однако служба не
закрывала транзакцию и обычный UI получал runtime-unavailable.

Candidate 21 добавляет детерминированное возобновление recovery при старте
службы. Изолированная Windows 11 VM была оставлена в точном проблемном состоянии
candidate 20, после чего setup candidate 21 выполнил upgrade. Новый процесс
службы восстановил чистую стадию journal, удалил pending/network state и сохранил
`11/11` обязательных runtime-файлов. Затем обычный non-elevated UI подтвердил
default Germany connect, один TUN, изменение маршрута и DNS, authenticated DE
egress и точный возврат исходных egress/route/DNS после disconnect.

Это доказательство включает upgrade/startup recovery и default connect/disconnect
на точном candidate 21. Свежая принудительная остановка уже установленной службы
candidate 21 не выполнялась: запрос UAC был отменён до изменения состояния.
Windows 10, sleep/resume, connected reboot/uninstall, AWG 3.1/AWG2 на Windows и
интерактивный SmartScreen остаются отдельными проверками.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `396e8aca2b3b77d727c66ce1287430bdbb550619cd36618c8be1daed07351578`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4050`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `d5dd9905bafdc30809a1199dde5961129680a03513b60a6e46f323a6a583693c`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `f39eaa0dabe4a6cd87113506e5ffc954623f6e82d3f684252639c035d898d2f5`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `fc6da2ca396d3e81c4bff1dc3bf7f40700fbf5fdc7bf0d76742e5d80984751e5`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `fdd8e1df6a0e52ae1f48234f9c049c071d3fb2a946498c125a3d8c43f188cfcd`;
- размер: `126263297` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

Все APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Candidate 21 APK ещё не получил точный LDPlayer install/launch PASS и физический
ARM64 runtime PASS. Wi-Fi и Билайн, default/fallback, AWG 3.1, AWG2, Smart DNS,
WARP, IPv4/IPv6/leak, Doze/OEM и endurance должны быть проверены на этих точных
APK-байтах.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `87f90be11a927c271c84e8042f17e052ee1070a1ac4923fa3949d6e19c00dff3`;
- размер: `29143633` байт;
- версия: `1.2.0+4050`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest связывает `11/11` обязательных файлов. Owner exception сохраняет
обязательное предупреждение SmartScreen/`Unknown publisher` и не разрешает
trusted, Store или stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.

Для точного source tuple прошли AWG control-plane `72/72` и client
materialization `2/2`; это source-only evidence, а не live Android/Windows
interop. Smart DNS routing `18/18`, UI `2/2` и Windows endpoint contract прошли
в своих ограниченных срезах. In-app выбор, физический DoH/leak/load и реальные
ChatGPT/Gemini/Xbox sessions остаются открыты. xHTTP и Hysteria2 не переводятся
в обязательную линию 1.2.0.

## Точная поставка

Strict-v2 handoff и offline validator связывают `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`c01234bf303b516764da9046fa08208b31126255355e68ca25b1f54180082738`.
Provenance SHA-256:
`b6e63ae0708f23932de4e07039b3c99c8be892a779df6135450ea6717f1ad4ad`.
Release-handoff SHA-256:
`07e0009c8d773402e25f2ab8cb823bafab738026439b8c60f5d509629b7955e9`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt в 14-дневном Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
