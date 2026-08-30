# POKROV 1.2.0 — direct beta candidate 9

Это точный закрытый кандидат прямого beta-релиза Android и Windows. Он
привязан к platform `84687875916bbb35c0e28e0c2a8c7ea276753f31`, client
`3459438f02bd774e722b1b858e7f7f16d57a9f5c` и Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. Candidate 9 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go по оставшимся воротам.

## Что изменилось после candidate 8

Android, Windows и Core не пересобирались: candidate 9 повторно связывает те же
шесть уже проверенных binary bytes с новым platform revision. Изменение касается
только внутренней RU-origin пробы: root-owned `0640` HMAC credential теперь
может читать ровно назначенная service group, при этом world bits, group
write/execute, не-root owner и чужая группа по-прежнему закрываются. Это не
меняет пользовательский VPN transport, AWG-криптографию или клиентские APK/EXE.

Неизменный точный ARM64 APK ранее проверен на физическом Android через мобильную сеть Билайн.
Обычный профиль без WARP прошёл, а уведомление сменилось с «Защита
подключается» на «Защита включена» только после egress validation. Закрытые
`awg2_lab` и `awg31_lab` отдельно подтвердили туннель, DNS, выход через VPN и
Core/server interop. После проверки устройство возвращено в обычный профиль:
VPN остановлен, WARP выключен, lab allowlist и выдача AWG-материалов сняты.

## Android

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `cd0f6edea8f362a0b3e1b4db5896bc862157b5ce84549284480f55737875a183`;
- размер: `295370385` байт;
- версия: `1.2.0`, build `4046`, min SDK `24`.

ARM64 APK физического прогона:

- файл: `pokrov-android-arm64-v8a.apk`;
- SHA-256: `9278c09fd8fa5768d3260cf796b4230db5acb0a092187aae00c441d717cfc572`;
- размер: `101366934` байт.

Store-handoff AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `719f76d9cd9033e871c4422842a85f015c2428446301b097cb53b9250e1b40e2`;
- размер: `126269104` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

AAB входит в точный набор поставки, но загрузка в Google Play не выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `26ec26d8989d61415f07cbf9707f336ebba0b947fa4ba0ee93d3078fa3984668`;
- размер: `28929376` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Локальный release build прошёл полный Flutter/Android unit matrix, Windows
analyze, сборку и Inno Setup. Runtime manifest подтверждает все `8/8`
обязательных файлов. Установщик нужно запускать только из официального канала
POKROV после сверки SHA-256. Исключение не разрешает заявления `trusted`,
`signed`, Store или broad stable; чистый Windows 10/11 host gate остаётся
ручным.

## Точная поставка

Strict-v2 handoff связывает шесть файлов с одним source tuple. Offline
fail-closed validator подтвердил `6/6` артефактов и `8/8` Windows runtime
файлов; CycloneDX SBOM содержит `349` компонентов, SLSA provenance — шесть
точных subjects. Продвижение обязано использовать те же байты без пересборки.

На момент freeze GitHub-hosted jobs не стартуют из-за состояния Billing &
plans владельца. Владелец отказался от покупок, поэтому нулевой hosted run не
считается `PASS`. Подпись release-index должна подтверждаться отдельным
main-only signer receipt; tracked input сам по себе кандидата не подписывает и
ничего публично не выпускает.
