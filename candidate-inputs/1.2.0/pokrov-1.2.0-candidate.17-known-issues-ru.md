# POKROV 1.2.0 candidate 17 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact byte-identical direct
  beta 1.2.0.
- Exact Windows installer ещё должен пройти изолированную Windows 10/11 VM:
  install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и
  uninstall.
- Android candidate 17 использует те же production-signed build `4049` bytes,
  но новая source tuple требует отдельного exact-candidate runtime record на
  физическом устройстве и LDPlayer. OEM/Doze, modem path, WARP, per-app,
  Private DNS, IPv6/leak и endurance остаются ручными проверками.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  DE listeners AWG2/AWG3.1 готовы на сервере, но новый candidate 17 client
  runtime ещё не получил отдельный release PASS. Собственной криптографии нет.
- xHTTP reserve и Hysteria2 требуют отдельного interop, network и rollback
  evidence после 1.2.0.
- Smart DNS выключен по умолчанию. Live `dns.pokrov.space`, TLS/SNI, bounded
  ChatGPT/Gemini/Xbox policy и rollback доказаны на текущем runtime, но новый
  candidate 17 client binding, полная leak/load matrix и authenticated app
  sessions остаются открыты.
- Оба немецких delivery endpoint работают на текущем Brain runtime через одну
  серверную ноду и один user mapping. Это не переносит автоматически proof на
  новый Android/Windows candidate и не гарантирует доступность каждого адреса
  у каждого мобильного оператора.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Только реально
  выполненные hosted jobs могут считаться `PASS`.
- Candidate 17 переиспользует шесть byte-identical build `4049` артефактов.
  Новый SBOM, provenance, strict handoff и подпись обязательны; runtime credit
  candidate 16 автоматически не переносится.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются exact Android/Windows gates, RU-origin, payment-provider
  E2E, Operator OIDC/RBAC, legal/commercial approval, rollback и итоговый Gate F.
