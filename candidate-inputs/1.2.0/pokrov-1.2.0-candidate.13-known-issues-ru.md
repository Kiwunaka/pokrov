# POKROV 1.2.0 candidate 13 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для direct beta 1.2.0.
- Exact Windows installer candidate 13 ещё не прошёл чистую Windows 10/11
  матрицу: install, SCM service, authenticated IPC, TUN, DNS, egress, recovery
  и uninstall. Старое current-host evidence относится к другим байтам.
- Exact candidate 13 не установлен на физический Android. LDPlayer x86_64
  доказал AWG 3.1 → AWG2 → default/Auto в одном процессе, но OEM/Doze,
  физический modem path, WARP runtime, per-app, Private DNS, IPv6/leak и
  endurance остаются `MANUAL_OWNER_TEST`.
- Во время двух VPN teardown на LDPlayer ADB-клиент кратко терял exact serial.
  Немедленный readback восстановился с тем же PID, disconnected UI и без
  активного VPN service/interface. Это не отменяет зелёный runtime-результат,
  но остаётся отдельным наблюдением эмуляторной среды.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 3.1 использует upstream-совместимый transport; собственной криптографии
  нет. xHTTP reserve и Hysteria2 не считаются готовыми до отдельного exact
  interop, network и rollback evidence после 1.2.0.
- Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT, Gemini
  и Xbox есть, но внешний resolver/access path должен пройти authoritative DNS,
  TLS, authenticated policy, allowlist и leak/fail-closed readback. Обычная
  смена DNS сама по себе не обещается как обход блокировок.
- Current-origin, Brain-origin и RU-origin для exact candidate 13 ещё не
  обновлены. Предыдущие отчёты не переносятся; доступность Санкт-Петербурга на
  мобильных операторах не заявляется и не блокирует AWG/DNS-релизную работу.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Нулевые private
  hosted jobs не считаются `PASS`.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются физический Android/Windows gates, current/Brain/RU
  refresh, payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval
  и rollback drill.
