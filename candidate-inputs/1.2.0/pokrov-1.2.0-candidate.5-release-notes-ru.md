# POKROV 1.2.0 — direct beta candidate 5

Это точный кандидат прямого beta-релиза Android и Windows, собранный из уже
слитых веток platform `master`, client `main` и Core `main`. Он не является
широким stable-релизом, не опубликован в Microsoft Store или Google Play и не
разрешает продвижение без отдельного go/no-go по оставшимся воротам.

## Что изменилось после candidate 4

Клиент переведён на package version `1.2.0+4046`, а точные source bindings
слиты в основные ветки. Набор пересобран заново: четыре direct APK, один AAB и
Windows x64 installer. Новый strict-v2 handoff связывает все шесть файлов с
одним source tuple, CycloneDX SBOM и SLSA provenance.

Закрытые `awg2_lab` и `awg31_lab` остаются выключенными по умолчанию. Core
содержит также ограниченный default-off Hysteria2 outbound; импорт сырых HY2
URI выключен. Это лабораторные capability lanes, а не новый пользовательский
список протоколов. Живая managed-profile policy пока не выдаёт AWG-варианты,
поэтому отдельные server handshake, TUN, DNS, egress и leak-прогоны для этих
методов ещё не доказаны.

Режим `DNS напрямую · лаборатория` выводит напрямую только выбранный
зашифрованный DoH-резолвер. AI-сервисы, Games/Xbox и остальной трафик остаются
маршрутами внутри VPN. Режим не обещает обход блокировок сам по себе и не
меняет внешний IP.

## Android

Четыре direct APK и один store-handoff AAB подписаны production-сертификатом
POKROV. Для обычной прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `2825a832a43404d7f16b42fbaf6f5e1f443505cca6a9ac8bf4e93e5ae46cbebb`;
- размер: `295299185` байт;
- версия: `1.2.0`, build `4046`, min SDK `24`.

Store-handoff AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `d4c00669ef5c551f6fb849cc34078b452a6fa43ba79b9f10f5c698fb007fd2d8`;
- размер: `126256131` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

AAB включён в точный набор поставки, но его загрузка в Google Play для 1.2.0
не запрошена.

## Windows

Windows-установщик не имеет Authenticode-подписи. Microsoft Defender
SmartScreen может показать предупреждение о неизвестном издателе. Запускайте
его только из официального канала POKROV после сверки SHA-256.

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `81c2a86ec3234162e85399ac348e36fcea413ee87e33b71b260533bdc1e6277f`;
- размер: `28913774` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Исключение не разрешает trusted, signed, Store или broad-stable заявления.
Exact candidate 5 ещё должен пройти clean-host install, SCM service,
authenticated IPC, TUN, DNS, egress, recovery и uninstall.

## Точная поставка

Кандидат связывает platform
`6ea08e9222dff67c93ffa0bb9585a57c5ffe220c`, client
`6b596cefbc043c2da30b31007789cea7e30fc336`, Core product source
`e8eb7721fc6eaac6813d3a888ac90d0da1f541a1` и release-index commit, который
будет вписан signer workflow при подготовке подписанного manifest.

SBOM содержит точные файлы, Flutter/Dart runtime dependencies, Core и его Go
module inventory. SLSA provenance фиксирует build parameters, материалы,
подписи Android и owner exception Windows. Продвижение обязано использовать
те же байты без пересборки. Актуальные ограничения перечислены в
`pokrov-1.2.0-candidate.5-known-issues-ru.md`.
