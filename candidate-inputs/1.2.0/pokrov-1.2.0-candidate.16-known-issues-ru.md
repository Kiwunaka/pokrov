# POKROV 1.2.0 candidate 16 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для direct beta 1.2.0.
- Exact Windows installer ещё не прошёл чистую Windows 10/11 матрицу: install,
  SCM service, authenticated IPC, TUN, DNS, egress, recovery и uninstall.
- Физический Android для candidate 16 не проверен. LDPlayer evidence относится
  к exact byte-identical x86_64 APK и новой platform tuple; OEM/Doze, физический
  modem path, WARP runtime, per-app, Private DNS, IPv6/leak и endurance остаются
  `MANUAL_OWNER_TEST`.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Выбор AWG 3.1/AWG2 в клиенте подтверждён, но transport health в LDPlayer ещё
  не получил релизный PASS. Собственной криптографии нет.
- xHTTP reserve и Hysteria2 требуют отдельного interop, network и rollback
  evidence после 1.2.0.
- Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT, Gemini
  и Xbox есть, но authoritative `dns.pokrov.space`, TLS, authenticated policy,
  allowlist и leak/fail-closed readback ещё не закрыты полным evidence.
- Current-origin и RU-origin для exact candidate 16 ещё не обновлены. Brain
  source deploy подтверждён `197/197`, а default LDPlayer path после него прошёл;
  доступность отдельных городских нод на мобильных операторах не заявляется.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Нулевые private
  hosted jobs не считаются `PASS`.
- Candidate 16 переиспользует шесть byte-identical build `4049` артефактов после
  platform-only managed-profile correction. Новый SBOM, provenance, strict
  handoff и подпись обязательны; promotion credit candidate 15 автоматически
  не переносится.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются физический Android/Windows gates, current/RU refresh,
  payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval и rollback
  drill.
