# POKROV 1.2.0 candidate 3 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  unknown-publisher предупреждения; исключение действует только для direct
  beta 1.2.0.
- Exact candidate 3 Windows EXE ещё не прошёл чистый hosted Windows gate:
  install, SCM service, authenticated IPC, restart и uninstall обязаны пройти
  до следующего уровня готовности.
- Exact candidate 3 universal APK прошёл обновление, запуск и сохранение
  AI/Games-настроек в LDPlayer. Из-за просроченного тестового доступа каталог,
  TUN, DNS и egress на этой APK не проверены.
- Новые exact candidate 3 APK/AAB production-signed, но повторная физическая
  Beeline/OEM, update, Doze, Private DNS, IPv6 и signer-recovery матрица не
  выполнена. Предыдущий ограниченный Beeline smoke подтверждает исправленный
  backend, но не exact candidate 3 и не общий RU-ready claim.
- Ошибочная type 3 bridge-реклама `ru_spb` выключена. Прямой SPB и варианты
  type 1/type 2 сохранены; отдельное широкое доказательство доступности у
  разных операторов отсутствует.
- AWG 3.1 Lab и AWG 2 Lab выключены по умолчанию: отдельный owned endpoint для
  публичного включения не доказан. Hysteria2 не входит в 1.2.0.
- AI и Games/Xbox работают как ограниченные маршруты внутри активного VPN, а
  не как DNS-only доступ. Транзакции ChatGPT, Gemini и Xbox не доказаны.
- Android AAB не загружен в Store. Linux и Apple не входят в публичную матрицу
  1.2.0.
- До продвижения остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval и rollback drill. RU-origin
  требуется только для отдельного RU-ready заявления.
