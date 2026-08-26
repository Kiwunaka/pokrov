# POKROV 1.2.0 candidate 1 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  unknown-publisher предупреждения; исключение действует только для direct
  beta 1.2.0.
- Exact Android `versionCode 4030` пока не прошёл физический Beeline/OEM,
  обновление, Doze, Private DNS, IPv6 и signer-recovery матрицу.
- Exact Windows EXE пока не прошёл чистую Windows 10/11 матрицу установки,
  TUN, DNS, egress, crash/reboot recovery, rollback и uninstall cleanup.
- LDPlayer подтвердил прямой Санкт-Петербург. Режимы type 2 и type 3 на
  эмуляторе отказали fail-closed; результат диагностический и не заменяет
  physical/mobile-origin проверку.
- AWG 3.1 Lab выключен по умолчанию: отдельный owned endpoint отсутствует.
  Hysteria2 не входит в 1.2.0.
- AI и Games/Xbox работают как ограниченные маршруты внутри активного VPN, а
  не как DNS-only доступ. Транзакции ChatGPT, Gemini и Xbox не доказаны.
- Android AAB не загружен в Store. Linux и Apple не входят в публичную матрицу
  1.2.0.
- До продвижения остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval и rollback drill. RU-origin
  требуется только для отдельного RU-ready заявления.
