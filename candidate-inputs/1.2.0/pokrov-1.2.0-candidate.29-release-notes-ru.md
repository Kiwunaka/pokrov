# POKROV 1.2.0 — direct beta candidate 29

Это новый приватный кандидат `1.2.0+4053`, полностью собранный через CLI из
текущих `platform/master`, `client/main` и закреплённого Core. Он привязан к
platform `efb05e0899ad51afd4453ae2fb75f8cafe96db7e`, client
`7e3e771fe36333a75244cbfd828c60beb84c7ff1` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 29 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Главное изменение

Windows-инсталлятор сохраняет владельца уже существующей установки при
обновлении и проверяет точный SID. Чистая установка по-прежнему работает
fail-closed. Исправление закрывает воспроизводимый дефект первого обновления
candidate 27; precursor candidate 28 уже прошёл установку, TUN/DNS и reboot.
Candidate 29 пересобирает все шесть клиентских файлов из текущих исходников.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `365d9b329a80148df5be22e7e00c0d9632e85cd18b981af3869a73cacff656e5`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4053`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `bd65a3f3072d642b532198ae1e703039c903f8e152edcec8c7f7616f2fc83779`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `6c9a7933e948e49429e7a272e4f021106f673fa2bbb8fe78354b3f1a3fb99918`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `143c58176193dcb84e543ba4559e61bfc2ec7bb43681c7124d83292499da570d`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `f28719706dcbdb5ac0a5fd3d4d325cd7c90d68a674aafe2a7a483ae92b248aa1`;
- размер: `126263353` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

Все APK production-signed, release/non-debuggable. AAB подписан тем же
self-managed production upload-key; целостность JAR-подписи и fingerprint
проверены. Google Play submission не выполнялся.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `60487a7bb17da33dbca842a146f6eb24dddd089e532c241670c9c0fd79610451`;
- размер: `29154403` байт;
- версия: `1.2.0+4053`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest `8d535ff682b7beac7a23c52d63cd37698a1d6d8edbf19c48a2121ac9f398f9a3`
связывает `11/11` обязательных файлов. Owner exception сохраняет обязательное
предупреждение SmartScreen/`Unknown publisher` и не разрешает trusted, Store
или broad-stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.
Hysteria2 и xHTTP не переводятся в обязательную линию 1.2.0 без отдельного
interop, network и rollback evidence.

## Точная поставка

Strict-v2 handoff и offline validator связали `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM содержит `352` компонента и имеет SHA-256
`07a4e19ebdb1631c46ae324935b1bf629996d62b1597bbcd44c71606eeb42e44`.
Provenance SHA-256:
`2993b8a16d2d21f41c63f59c037e0c3fb452c3e23bf8baeb2affb7e5a14c7c77`.
Release-handoff SHA-256:
`f05791698e835da61680698cd2284bdd46dd2bbb76c4add69384c00b43fe9ab8`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt. Даже после подписи кандидат не создаёт
тег, GitHub Release, публичные assets, store submission или stable pointer.
