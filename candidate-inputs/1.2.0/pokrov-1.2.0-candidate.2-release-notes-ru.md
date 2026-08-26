# POKROV 1.2.0 — direct beta candidate 2

Это точный кандидат прямого beta-релиза Android и Windows. Он не является
широким stable-релизом, не опубликован в Microsoft Store или Google Play и не
разрешает продвижение без отдельного go/no-go по оставшимся ручным воротам.

## Что изменилось после candidate 1

Candidate 1 был отклонён чистым Windows-host: установщик вернул код 0, но из-за
неверного quoting в `sc.exe create` не создал запись `POKROVService`. Candidate
2 заменяет непроверяемые команды Inno Setup на fail-closed регистрацию службы:
каждый шаг SCM проверяет exit code, а частично созданная новая служба удаляется
перед аварийным завершением установки.

Backend также блокирует использование Санкт-Петербурга или другого RU-узла как
его собственного bridge-hop. Это исключает самозацикленный маршрут, но не
маскирует отдельную недоступность прямого SPB endpoint у конкретного оператора.

## Android

Все APK и AAB заново собраны из exact client `main` и подписаны production-
сертификатом POKROV. Для обычной прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `799d96e150ac2a658f66c3495347aff9bf3a314969906c2e9a6f0e7315232e2b`;
- размер: `295018413` байт.

Физическая Beeline-проверка backend после защиты от self-hop подтвердила TUN,
DNS и egress для двух bridge-вариантов Санкт-Петербурга. Прямой SPB endpoint на
том же мобильном origin остался недоступен. Новые candidate.2 APK пока не
прошли повторную exact-byte device/OEM матрицу, поэтому это отдельный gate.

## Windows

Windows-установщик не имеет Authenticode-подписи. Microsoft Defender
SmartScreen может показать предупреждение о неизвестном издателе. Запускайте
его только из официального канала POKROV после сверки SHA-256.

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `4226daa49975cb25dae5bec8cbcd26299648ee89f5dbff613f62d807be0ac412`;
- размер: `28893114` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Исключение не разрешает trusted, signed, Store или broad-stable заявления.
Exact candidate.2 clean-host install/service/IPC/restart/uninstall gate остаётся
обязательным до дальнейшего продвижения.

## Лабораторные режимы и DNS

`awg2_lab` и `awg31_lab` остаются default-off. Для AWG 3.1 ещё нет доказанного
отдельного принадлежащего POKROV endpoint, поэтому публичное включение
запрещено. AI и Games/Xbox — ограниченные маршруты внутри активного VPN, а не
DNS-only обход и не обещание доступа без VPN.

Публичный signed manifest связывает точные SHA-256, размеры, исходные коммиты,
SBOM и provenance. Продвижение обязано использовать те же байты без пересборки.
Актуальные ограничения перечислены в
`pokrov-1.2.0-candidate.2-known-issues-ru.md`.
