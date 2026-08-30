# POKROV 1.2.0 — direct beta candidate 11

Это новый точный закрытый кандидат Android и Windows, собранный из platform
`01cf5de682c01bffbead7703db901450ca7fb1fb`, client
`348de306fc1f2243d022157b54fa7f09ffd2840b` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`. Candidate 11 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go.

## Что изменилось после candidate 10

Candidate 11 не переиспользует старые APK, AAB или EXE. Все шесть клиентских
артефактов пересобраны для `1.2.0+4047` и привязаны к новому Core. Из legacy
Core-обвязки удалено логирование полного JSON настроек, таблицы настроек и
неограниченного текста ошибок: WARP-ключи, токены и сырой runtime config не
должны попадать в процессный лог. ABI-возврат локальной ошибки сохранён.

Core CI для точного source commit прошёл тесты, vet, race, staticcheck,
govulncheck, fuzz, SBOM и двукратную воспроизводимость Android AAR и Windows
DLL. Клиент закрепляет именно эти байты; полный локальный Flutter/Gradle набор
также прошёл до сборки кандидата. AWG 2 и mobile-safe AWG 3.1 остаются частью
закрытой lab-линии, выключенной по умолчанию. Собственной криптографии и бренда
«POKROV AWG» нет.

Старые device/network результаты candidate 10 не переносятся на новые байты.
Candidate 11 ещё не устанавливался на физический телефон: устройство временно
забрано владельцем. Это остаётся `MANUAL_OWNER_TEST`, а не `PASS`.

## Android

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `706c546e4d1f1d5a5f476a10f21bd178aff412ffbc163b4a3d0557b4c9655e1a`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4047`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `1a579bfaa11359fcab9c13cf80368877b88651d84d4039b0d0656c0b536cd048`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `b1f85958a21bc9864f68b6879dc0110e3e8b881443d6caa59773a5a11e89d387`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `60863b1fa36ea8b2a90d20fd0446a8784c694045aa935f7c8e9885df46bc978a`, `109951989` байт.

Store AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `689887846af8774b0b08d91f5238735781d77c0ca308f0b860d1533d1422e56a`;
- размер: `126265513` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

APK прошли `apksigner` и manifest-проверку; AAB прошёл `jarsigner`, проверку
production-сертификата и merged manifest. Загрузка в Google Play не
выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `46d1407902695de323962175b9fe36af6b9e97e8ef05a67e9f77068112e7595a`;
- размер: `28931270` байт;
- версия: `1.2.0+4047`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Runtime manifest совпал для всех `8/8` обязательных файлов. Exact bundled Core
DLL выдержал 100 proxy-only start/stop циклов без изменения системных маршрутов.
Это не доказывает TUN, DNS capture, leak protection, install/service/recovery и
uninstall на чистой Windows 10/11 VM. Установщик нужно брать только из
официального канала POKROV и сверять по SHA-256; SmartScreen и `Unknown
publisher` ожидаемы.

## Точная поставка

Strict-v2 handoff и fail-closed offline validator подтвердили `6/6`
артефактов и `8/8` Windows runtime-файлов. CycloneDX SBOM содержит `349`
компонентов и `350` dependency-записей; SLSA provenance содержит шесть exact
subjects. Core AAR и DLL имеют SHA-256
`2a9677d9e24ed7ef66d4e98f90e7033eb5450c9a2755f0fe6b8bba58036c6a69` и
`f284fa8841f1a45271874a7a05ed6093fb0e3efbdd03e00001edd046be708204`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен сформировать отдельный Ed25519 receipt и Actions artifact. Даже после
подписи кандидат не создаёт тег, GitHub Release, публичные assets, store
submission или stable pointer.
