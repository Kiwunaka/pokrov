# POKROV 1.2.0 candidate 4 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  unknown-publisher предупреждения; исключение действует только для direct
  beta 1.2.0.
- Exact candidate 4 Windows EXE ещё не прошёл чистый Windows 10/11 gate:
  install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и
  uninstall остаются обязательными.
- Exact build 32 universal APK прошёл установку, запуск и сохранение настроек
  DNS в LDPlayer. Из-за просроченного тестового доступа каталог, живой TUN,
  DNS-запросы и egress не проверены.
- APK/AAB production-signed, но физическая Beeline/OEM, update, Doze, Private
  DNS, IPv6, handoff, endurance и signer-recovery матрица не выполнена.
- `awg2_lab` и `awg31_lab` выключены по умолчанию. Userspace-device lifecycle
  прошёл локально, но отдельный owned AWG endpoint, server handshake, TUN, DNS
  и egress не доказаны. Hysteria2 не входит в 1.2.0.
- `DNS напрямую · лаборатория` выводит напрямую только выбранный DoH-резолвер.
  Он не меняет внешний IP и не гарантирует доступ к заблокированным сервисам.
  AI-сервисы и Games/Xbox остаются маршрутами внутри активного VPN.
- Доступность Санкт-Петербурга у разных операторов не заявляется и не является
  отдельным блокером этого кандидата. Возможны endpoint-блокировка, фильтрация
  оператора или недоступность конкретного серверного варианта.
- Android AAB не загружен в Google Play; store submission для 1.2.0 не
  запрошен. Linux и Apple не входят в публичную матрицу 1.2.0.
- Hosted platform/client проверки останавливаются до первого шага из-за
  GitHub billing/spending limit. Это `BLOCKED_BY_ACCESS`, а не PASS и не ошибка
  кода.
- До продвижения остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval и rollback drill. RU-origin
  требуется только для отдельного RU-ready заявления.
