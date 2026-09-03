# POKROV 1.2.0 candidate 32 — известные ограничения

- Windows EXE не подписан Authenticode. Для direct beta ожидаются SmartScreen
  и `Unknown publisher`; owner exception не является trusted/Store proof.
- Exact candidate 32 ещё не установлен на физический ARM64-телефон и не прошёл
  Wi-Fi/Билайн, permission, default/fallback, AWG 3.1, AWG2, WARP, Smart DNS,
  Private DNS, IPv4/IPv6/leak, Doze/OEM, handover и endurance matrix.
- Exact candidate 32 ещё не прошёл изолированную Windows VM matrix: install и
  upgrade, managed VLESS/AWG/WARP/Smart DNS, TUN/DNS/egress, reboot/recovery,
  connected uninstall, sleep/crash и Windows 10.
- Platform `d0dd37c1003198ba08cffc49a040a77e21621a86` не развёрнут в production.
  Current-origin, Brain-origin и RU-origin доказательства для candidate 32
  отсутствуют; старые результаты не переносятся автоматически.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, Store object, runtime sync или stable pointer.
- Действует `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Platform
  и client jobs, завершившиеся с нулём шагов из-за GitHub Billing, остаются
  `BLOCKED_BY_ACCESS_GITHUB_BILLING`, а не `PASS`.
- Подпись release-index подтверждает неизменность manifest input, но не
  превращает manual, external или отсутствующие проверки в `PASS` и не
  разрешает promotion.
- До итогового решения остаются exact device/runtime matrices, STOP-SHIP и
  no-open-P0 aggregate, rollback/kill drill, provider E2E, Operator OIDC/RBAC/
  action-intent, legal/commercial approval, performance/release health и
  финальный Gate F.
