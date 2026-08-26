# POKROV 1.2.0 candidate 2 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  unknown-publisher предупреждения; исключение действует только для direct
  beta 1.2.0.
- Exact candidate.2 Windows EXE ещё не прошёл чистый hosted Windows gate:
  install, SCM service, authenticated IPC, restart и uninstall обязаны пройти
  до следующего уровня готовности.
- Новые exact candidate.2 APK/AAB production-signed, но повторная физическая
  Beeline/OEM, update, Doze, Private DNS, IPv6 и signer-recovery матрица не
  выполнена.
- Прямой Санкт-Петербург на физическом Beeline origin остаётся недоступен.
  Два bridge-варианта на том же origin прошли TUN, DNS и egress; это не доказывает
  прямой endpoint и не разрешает общий RU-ready claim.
- AWG 3.1 Lab выключен по умолчанию: отдельный owned endpoint отсутствует.
  Hysteria2 не входит в 1.2.0.
- AI и Games/Xbox работают как ограниченные маршруты внутри активного VPN, а
  не как DNS-only доступ. Транзакции ChatGPT, Gemini и Xbox не доказаны.
- Android AAB не загружен в Store. Linux и Apple не входят в публичную матрицу
  1.2.0.
- До продвижения остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval и rollback drill. RU-origin
  требуется только для отдельного RU-ready заявления.
