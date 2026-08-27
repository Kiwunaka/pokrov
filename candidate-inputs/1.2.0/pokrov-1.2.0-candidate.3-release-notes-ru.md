# POKROV 1.2.0 — direct beta candidate 3

Это точный кандидат прямого beta-релиза Android и Windows. Он не является
широким stable-релизом, не опубликован в Microsoft Store или Google Play и не
разрешает продвижение без отдельного go/no-go по оставшимся ручным воротам.

## Что изменилось после candidate 2

Из production-конфигурации выключена ошибочная bridge-реклама `ru_spb` для
маршрута type 3. Сам Санкт-Петербург не удалён: обычный прямой endpoint и
варианты type 1/type 2 сохранены. Защита от self-hop по-прежнему не позволяет
узлу использовать самого себя как bridge-hop.

Клиент теперь сбрасывает сохранённый непрямой вариант в `direct`, если backend
перестал его рекламировать, очищает устаревшее staged/active состояние и при
необходимости переподключается. Список вариантов прокручивается, поэтому все
доступные режимы можно увидеть на небольшом экране.

Сборщик Windows исправлен для строгого PowerShell-режима и принимает явно
замороженный Core root. Candidate 3 собран из итоговых merge-коммитов и exact
POKROV Core authority без подмены runtime-байтов.

## Android

Все APK и AAB заново собраны и подписаны production-сертификатом POKROV. Для
обычной прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `f41c76ebf7bf69f6681d7df87e7722dcdccdec383ef950156b69829caee71c51`;
- размер: `295051181` байт.

Точный universal APK candidate 3 установлен обновлением в LDPlayer поверх
предыдущей версии с сохранением данных и тем же production signer. Запуск,
экран правил и сохранение переключателей `AI-сервисы` и `Игры` после
принудительного перезапуска прошли. Аккаунт в эмуляторе просрочен, поэтому
каталог локаций скрыт, а TUN/DNS/egress на exact APK не проверены.

Отдельная ограниченная проверка backend на физическом Beeline origin после
исправления конфигурации подтвердила прямой SPB и type 1, а также прямой
Frankfurt и SPB type 2. Она выполнена не exact-байтами candidate 3 и не заменяет
device/OEM и полный RU-origin gate.

## Windows

Windows-установщик не имеет Authenticode-подписи. Microsoft Defender
SmartScreen может показать предупреждение о неизвестном издателе. Запускайте
его только из официального канала POKROV после сверки SHA-256.

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `9962e3e80947dae374619ed388fc08b7322bffda38202a42e5812597c7818021`;
- размер: `28898240` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Исключение не разрешает trusted, signed, Store или broad-stable заявления.
Exact candidate 3 clean-host install/service/IPC/restart/uninstall gate остаётся
обязательным до дальнейшего продвижения.

## Лабораторные режимы и DNS

`awg2_lab` и `awg31_lab` остаются default-off. Для AWG 3.1 ещё нет доказанного
отдельного принадлежащего POKROV endpoint, поэтому публичное включение
запрещено. Hysteria2 не входит в 1.2.0.

AI и Games/Xbox — настраиваемые доменные маршруты внутри активного VPN. Это не
DNS-only обход и не обещание доступа к ChatGPT, Gemini или Xbox без туннеля.

Публичный signed manifest связывает точные SHA-256, размеры, исходные коммиты,
SBOM и provenance. Продвижение обязано использовать те же байты без пересборки.
Актуальные ограничения перечислены в
`pokrov-1.2.0-candidate.3-known-issues-ru.md`.
