# POKROV 1.2.0 — direct beta candidate 16

Это точный закрытый кандидат Android и Windows после исправления готовности
managed profile. Он привязан к platform
`719e23dc49407beb9ae30d98d17d4b73d18ae37c`, client
`75ba7e721cfee486f7189edd51de97aba2746722` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 16 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что изменилось после candidate 15

Candidate 15 сохранён как неизменяемое evidence. В successor platform сохранён
ограниченный по времени panel sync, а для уже выданного managed profile добавлен
строгий fallback по подтверждённым данным provisioning. Пока live sync не
завершён, API сверяет `UserNode` и активный `AccessKey` с текущим пользовательским
пулом и допускает только реально подтверждённые и сейчас доступные ноды.

При наличии такого пересечения профиль получает `readiness_source=confirmed_mapping`.
При отсутствии подтверждённой доступной ноды остаётся честный `pending_sync`.
`sync_ok` не подменяется успешным значением, а manifest и Smart Connect
ограничиваются тем же подтверждённым набором.

Исправление прошло focused platform suite (`154 passed`, `8 subtests passed`),
client UI/API tests (`16 passed`) и docs contract (`28 passed`). Exact platform
deploy на Brain подтверждён source probe `197/197`, публичный API после перезапуска
`portal-api` ответил HTTP 200.

Client и Core не менялись. Шесть build `4049` артефактов переиспользованы только
после проверки имени, размера и SHA-256. Для candidate 16 заново сформированы
CycloneDX SBOM, SLSA/in-toto provenance и strict-v2 handoff с новой точной
source tuple.

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

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `5cddb0d264a05db59c099af8a26f26dd3094746632222e1527e9c0a129801e42`;
- размер: `126265693` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production fingerprint. Google Play submission не выполнялся.

После exact deploy x86_64 APK с теми же byte-identical build `4049` bytes прошёл
проверку default-профиля в LDPlayer `emulator-5554`: приложение перешло в
`Подключено`, а экран деталей подтвердил туннель, DNS и выход через POKROV.
После проверки соединение штатно выключено. Физический телефон не использовался.

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

Выбор AWG 3.1 и AWG2 в клиенте ранее подтверждён, но runtime health transport в
LDPlayer ещё не дал релизного PASS. Оба lab-профиля остаются выключенными по
умолчанию. xHTTP и Hysteria2 остаются post-1.2.0 reserve/lab lanes.

## Точная поставка

Strict-v2 handoff и offline validator подтвердили `6/6` артефактов и `8/8`
Windows runtime-файлов. SBOM SHA-256:
`47785d3b6a4745141cb3ad93cbf8c99e4d6e16d419531d31dc3c44bfa143cb7a`.
Provenance SHA-256:
`844fcda1ee6c6ba3aed76ccc57a08daa39e779d65945b5e74f5b14308de2864c`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
