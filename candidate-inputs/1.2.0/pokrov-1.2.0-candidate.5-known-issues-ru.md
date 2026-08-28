# POKROV 1.2.0 candidate 5 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  unknown-publisher предупреждения; исключение действует только для direct
  beta 1.2.0.
- Exact candidate 5 Windows EXE ещё не прошёл чистый Windows 10/11 gate:
  install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и
  uninstall остаются обязательными.
- APK/AAB подписаны production-сертификатом, но именно эти candidate 5 bytes
  ещё не прошли физическую Beeline/OEM, update, Doze, Private DNS, IPv6,
  handoff, endurance и signer-recovery матрицу.
- LDPlayer ранее подтвердил UI и безопасный cleanup на build `4046`, но новый
  точный x86_64 APK candidate 5 ещё должен быть установлен и привязан к
  отдельному device evidence.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Локальные lifecycle/packet-boundary проверки не заменяют отдельный owned
  endpoint, server handshake, TUN, DNS, egress, leak и rollback proof.
- Живая managed-profile policy пока не выдаёт AWG-варианты. Это ожидаемая
  серверная policy boundary, а не доказанный отказ клиента.
- `DNS напрямую · лаборатория` выводит напрямую только выбранный DoH-резолвер.
  Он не меняет внешний IP и не гарантирует доступ к ChatGPT, Gemini, Xbox или
  другим сервисам. Их traffic groups остаются внутри активного VPN.
- Каталог показывал семь локаций в LDPlayer, но доступность Санкт-Петербурга у
  разных операторов не заявляется. Возможны endpoint-блокировка, фильтрация
  оператора или недоступность конкретного серверного варианта.
- Android AAB не загружен в Google Play; store submission для 1.2.0 не
  запрошен. Linux и Apple не входят в публичную матрицу 1.2.0.
- Владелец отказался от платного GitHub-плана и branch protection. Используется
  `OWNER_SOLO_EXCEPTION`; независимый review и защищённая ветка не заявляются.
- До продвижения остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval, exact-candidate device gates и
  rollback drill. RU-origin требуется только для отдельного RU-ready заявления.
- Перевод остальных репозиториев в public — отдельная операция после полной
  проверки истории и текущего дерева на секреты; candidate 5 сам по себе её не
  выполняет.
