# POKROV 1.2.0 candidate 11 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для direct beta 1.2.0.
- Exact Windows installer candidate 11 ещё не прошёл чистую Windows 10/11
  матрицу: install, SCM service, authenticated IPC, TUN, DNS, egress, recovery
  и uninstall. Локальный 100-cycle тест доказывает только proxy-only Core ABI.
- Candidate 11 ещё не установлен на физический Android: телефон временно
  забран владельцем. Старые успешные проверки candidate 10 не являются
  доказательством новых APK. OEM/Doze, WARP runtime, per-app, Private DNS,
  IPv6/leak и endurance остаются `MANUAL_OWNER_TEST`.
- Exact candidate 11 ещё не прошёл новый LDPlayer network/lab прогон. Старые
  AWG 2/AWG 3.1 и Smart DNS результаты сохраняются как история, но не
  повышаются до `PASS` для новых байтов.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 3.1 использует upstream-совместимый transport с MTU `1280`, header
  protection и randomized trailers; собственной криптографии нет. Hysteria2
  не включается без доверенного TLS и отдельного exact interop.
- Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT, Gemini
  и Xbox есть, но новый внешний resolver/access path должен пройти DNSSEC/TLS,
  authenticated policy, allowlist и leak/fail-closed readback. Обычная смена
  DNS сама по себе не обещается как обход блокировок.
- Current-origin, Brain-origin и RU-origin для exact candidate 11 ещё не
  обновлены. Предыдущие отчёты не переносятся; доступность Санкт-Петербурга на
  мобильных операторах не заявляется и не блокирует AWG/DNS-релизную работу.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Нулевые private
  hosted jobs не считаются `PASS`, при этом Core exact CI прошёл реальными
  шагами, а клиентский полный набор прошёл локально.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются exact device/Windows gates, current/Brain/RU refresh,
  payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval и
  rollback drill.
