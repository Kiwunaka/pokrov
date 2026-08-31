# POKROV 1.2.0 candidate 15 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для direct beta 1.2.0.
- Exact Windows installer ещё не прошёл чистую Windows 10/11 матрицу: install,
  SCM service, authenticated IPC, TUN, DNS, egress, recovery и uninstall.
- Exact candidate 15 ещё не установлен на физический Android. Предыдущее
  LDPlayer evidence относится к тем же APK bytes, но не переносится как новый
  candidate-specific `PASS`. OEM/Doze, физический modem path, WARP runtime,
  per-app, Private DNS, IPv6/leak и endurance остаются `MANUAL_OWNER_TEST`.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 3.1 использует upstream-совместимый transport; собственной криптографии
  нет. xHTTP reserve и Hysteria2 требуют отдельного interop, network и rollback
  evidence после 1.2.0.
- Managed-profile platform path теперь ограничен общим deadline и не запускает
  legacy panel read для device-bound lab profiles. Exact candidate readback в
  LDPlayer ещё должен подтвердить default, AWG 3.1, AWG2 и cleanup.
- Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT, Gemini
  и Xbox есть, но authoritative `dns.pokrov.space`, TLS, authenticated policy,
  allowlist и leak/fail-closed readback ещё не подтверждены.
- Current-origin, Brain-origin и RU-origin для exact candidate 15 ещё не
  обновлены. Предыдущие отчёты не переносятся; доступность Санкт-Петербурга на
  мобильных операторах не заявляется и не блокирует AWG/DNS-релизную работу.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Нулевые private
  hosted jobs не считаются `PASS`.
- Candidate 15 переиспользует шесть byte-identical build `4049` артефактов
  после platform-only managed-profile correction. Новый SBOM, provenance,
  strict handoff и подпись обязательны; candidate 14 promotion credit
  автоматически не переносится.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются физический Android/Windows gates, current/Brain/RU
  refresh, payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval
  и rollback drill.
