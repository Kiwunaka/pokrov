# POKROV 1.2.0 — direct beta candidate 17

Это точный закрытый кандидат Android и Windows после восстановления немецкой
ноды с двумя провайдерскими адресами. Он привязан к platform
`d6898e63c5c9ab7dd267b9d5150b54196f99d967`, client
`977c6edd21d4746d5b1b8770d031734df46ad108` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 17 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что изменилось после candidate 16

Candidate 16 сохранён как неизменяемое evidence. Platform теперь описывает одну
физическую DE-ноду с одним inbound, capacity/health record и user mapping, но с
двумя delivery endpoints: `Германия 1` и `Германия 2`. Sing-box/Hiddify, Happ,
Clash, raw VLESS и Xray compatibility получают оба адреса без создания
фиктивной второй серверной ноды и без двойного provisioning.

Текущий Brain runtime прошёл source readback `197/197`. Оба DE DNS-имени трижды
доступны по TCP/443; authenticated VLESS/Reality egress через каждый адрес дал
HTTP 204. Live subscription rendering прошёл `4/4` формата при ровно одном DE
user mapping. AWG2 и AWG 3.1 listeners на сервере active/enabled; новый
exact-candidate клиентский lab runtime проверяется отдельно.

Client добавляет только точный manual hosted replay трёх полных SHA, Linux
journald proof и release-документацию. Android/Windows artifact inputs и Core
не менялись. Шесть build `4049` артефактов переиспользованы только после
проверки имени, размера и SHA-256. Для candidate 17 заново сформированы
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

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `0afaf6e1d73a7e72762d945557f48793646a9bdbf12bb8ca2e843d4b94df276c`;
- размер: `28932793` байт;
- версия: `1.2.0+4049`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

EXE byte-identical candidate 16, поэтому сохраняется ранее принятый exact-byte
SmartScreen/`Unknown publisher` exception. Runtime manifest совпадает для всех
`8/8` обязательных файлов. Изолированная Windows VM с TUN, DNS, egress,
recovery и uninstall остаётся отдельной exact-candidate проверкой.

## Протокольная линия

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Собственной
криптографии и отдельного бренда AWG нет.

Оба lab-профиля выключены по умолчанию. Серверная готовность DE подтверждена,
но Android/Windows runtime candidate 17 должен быть повторён. xHTTP и Hysteria2
остаются post-1.2.0 reserve/lab lanes.

## Точная поставка

Strict-v2 handoff и offline validator подтвердили `6/6` артефактов и `8/8`
Windows runtime-файлов. SBOM SHA-256:
`40fd7be694814b8cba0908ef83936ce882ed09524b0c195adf7be277aece9176`.
Provenance SHA-256:
`4552f16cd150d87cd299b0202c22bbdd3533bba6f7146ade8a8bda20b6d4a7ba`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
