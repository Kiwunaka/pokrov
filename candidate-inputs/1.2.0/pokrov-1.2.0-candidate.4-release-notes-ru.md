# POKROV 1.2.0 — direct beta candidate 4

Это точный кандидат прямого beta-релиза Android и Windows. Он не является
широким stable-релизом, не опубликован в Microsoft Store или Google Play и не
разрешает продвижение без отдельного go/no-go по оставшимся воротам.

## Что изменилось после candidate 3

Добавлен закрытый `awg31_lab`, выключенный по умолчанию. Локальный тест POKROV
Core поднимает настоящий userspace-device `amneziawg-go/v3`, применяет IPC
конфигурацию, отправляет внутренний UDP-пакет и видит внешний зашифрованный
пакет без утечки исходного payload. По 25 жизненных циклов AWG 2 и AWG 3.1
прошли на неизменённом production runtime Core. Это не доказывает handshake,
TUN, DNS или egress с отдельным живым AWG-сервером.

В настройки защищённого DNS добавлен закрытый режим `DNS напрямую ·
лаборатория`. Он отправляет только выбранный зашифрованный DoH-резолвер через
managed direct outbound. AI-сервисы, Games/Xbox и остальной трафик остаются
внутри VPN. Режим `Автоматически` сохраняет DNS из серверного профиля и скрывает
лабораторный переключатель.

Exact APK build 32 установлен в LDPlayer. Выбор Google DNS, переключение между
VPN и direct DNS, сохранение настройки после перезапуска и возврат к безопасному
автоматическому режиму прошли. Тестовый доступ в эмуляторе просрочен, поэтому
живой туннель, DNS-запросы и egress этим прогоном не доказаны.

## Android

Четыре direct APK и один store-handoff AAB заново собраны и подписаны
production-сертификатом POKROV. Для обычной прямой установки предназначен
universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `cf506349d3f6d76d01bd3b153cbb1a5f9bd176a78cd9f1ee3a27632ce781dbec`;
- размер: `295067561` байт;
- версия: `1.2.0`, build `32`, min SDK `24`, target SDK `36`.

Store-handoff AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `14f874732c59bd137a73b7536642bcad0677e8025f102df85acbeccb86a3ab33`;
- размер: `126178306` байт.

AAB включён в точный набор поставки, но его загрузка в Google Play для 1.2.0
не запрошена.

## Windows

Windows-установщик не имеет Authenticode-подписи. Microsoft Defender
SmartScreen может показать предупреждение о неизвестном издателе. Запускайте
его только из официального канала POKROV после сверки SHA-256.

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `8b0b5385eb357c6f6f9636cc960bc201e1008d7a96a1a567b3b970e42986a37d`;
- размер: `28900769` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Исключение не разрешает trusted, signed, Store или broad-stable заявления.
Exact candidate 4 ещё должен пройти clean-host install, SCM service,
authenticated IPC, TUN, DNS, egress, recovery и uninstall.

## Точная поставка

Кандидат связывает platform
`01ce413ad55758345fe1e4ab5c4a44ce3b03b6c2`, client
`7dd9fe3d8aef09756f7b2bba898fa0b4cb496993`, Core
`344b317a7a09eca7943a93866b193553538bd8f6` и исходный release-index
`32f560dd34191a0117f1f60714f35aa1216a2d4a`.

SBOM, SLSA provenance, Android signer evidence и Windows owner exception
привязаны ко всем шести артефактам. Продвижение обязано использовать те же
байты без пересборки. Актуальные ограничения перечислены в
`pokrov-1.2.0-candidate.4-known-issues-ru.md`.
