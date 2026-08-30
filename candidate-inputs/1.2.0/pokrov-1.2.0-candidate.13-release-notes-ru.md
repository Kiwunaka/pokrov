# POKROV 1.2.0 — direct beta candidate 13

Это новый точный закрытый кандидат Android и Windows, собранный из platform
`7d983c0ab52e9c01f94da8916a6bca6a0039be8d`, client
`ce2581dd16d276d20eace7a56f0337c4b9319168` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`. Candidate 13 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go.

## Что изменилось после candidate 12

Candidate 12 отклонён для замены после точного LDPlayer-прогона. Первый
AWG 3.1 connect был успешным, но следующий обычный AWG2 connect в том же
процессе получил последовательность событий нового Core run, начинающуюся
заново. Process-wide fence ошибочно сравнил её с sequence предыдущего run и
оставил UI в переходном состоянии.

Candidate 13 сбрасывает sequence fence при смене `runId`, даже если локальная
generation нового Android `VpnService` снова начинается с того же значения.
Регрессия покрыта JVM-тестом: новый run принимает перезапущенную
последовательность, а запоздавший callback предыдущего run отклоняется.
Полный exact client gate прошёл локально, включая Flutter, Android direct/store,
Windows и Gradle (`162` tasks).

## Exact LDPlayer runtime

Production-signed x86_64 APK установлен с сохранением данных; SHA-256
установленного `base.apk` совпал с candidate artifact. На LDPlayer Android 9
последовательность AWG 3.1 → clean disconnect → AWG2 → clean disconnect →
default/Auto прошла в одном процессе без `force-stop` и без смены PID.

- AWG 3.1: control-plane selection, точный runtime-profile и зелёные tunnel,
  DNS и VPN-egress;
- AWG2: те же проверки после обычного destroy/recreate `VpnService`;
- default/Auto: обычный VLESS profile с `33` VLESS outbound, зелёные tunnel,
  DNS и VPN-egress;
- финал: клиент отключён, выбран default, lab cohort/allowlist удалены,
  VPN service и tunnel-интерфейс отсутствуют.

Два коротких ADB reconnect произошли именно во время teardown VPN на эмуляторе.
Немедленный readback восстановился с тем же PID и требуемым disconnected state;
это сохранено как наблюдение среды, а не скрыто как идеальный прогон. Сводный
локальный receipt имеет SHA-256
`22dbd83bb0267ecd55bfa8b15284d149f5465270edf11bd1f0f9122e21ddb195`.
Физический Android этим тестом не доказан.

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

APK прошли `apksigner`, package/version/ABI и release/non-debuggable проверки.
AAB прошёл JAR signature integrity и точный production fingerprint; сертификат
self-managed и не имеет публичной PKI-цепочки. Загрузка в Google Play не
выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `0afaf6e1d73a7e72762d945557f48793646a9bdbf12bb8ca2e843d4b94df276c`;
- размер: `28932793` байт;
- версия: `1.2.0+4049`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Runtime manifest совпал для всех `8/8` обязательных файлов. SmartScreen и
`Unknown publisher` ожидаемы. Чистая Windows 10/11 VM, TUN, DNS capture,
recovery и uninstall для этих exact bytes остаются ручными проверками.

## Протокольная линия

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Собственной
криптографии и бренда «POKROV AWG» нет.

xHTTP после 1.2.0 рассматривается как резервный VLESS transport для
TLS/CDN-сред, а Hysteria2 — только как bounded lab fallback при измеримом
выигрыше на проблемных UDP-сетях. Они не включены в candidate 13 и не нужны
для объявления базовой работоспособности 1.2.0.

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
