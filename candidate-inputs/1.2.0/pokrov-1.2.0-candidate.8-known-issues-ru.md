# POKROV 1.2.0 candidate 8 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  `Unknown publisher`; исключение действует только для direct beta 1.2.0.
- Exact candidate 8 ещё не прошёл обязательный чистый Windows 10/11 gate:
  install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и
  uninstall.
- Exact ARM64 candidate 8 прошёл на физическом Android обычный профиль без
  WARP, AWG 2, mobile-safe AWG 3.1, DNS, authenticated egress, Core interop и
  финальный restore. WARP runtime, per-app, Private DNS, IPv6/leak, OEM/Doze и
  endurance-матрица остаются ручными воротами.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 3.1 использует upstream-совместимый transport с MTU `1280`, header
  protection и randomized trailers; собственной криптографии и заявления
  «POKROV AWG» нет.
- Внешний Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT,
  Gemini и Xbox доказан, но живой управляемый resolver/access path не развёрнут.
  Прямой Pi RU-baseline показывает ChatGPT HTTP `403` при рабочем DNS/TLS,
  поэтому обычная смена DNS сама по себе не обещается как обход.
- Raspberry Pi 4 подтверждает только терминальный direct-RU baseline. Он не
  запускал candidate client или Smart DNS runtime и не превращает Gate F
  RU-origin в `PASS`.
- Доступность Санкт-Петербурга на мобильных операторах не заявляется; она не
  блокирует AWG/DNS-релизную работу и требует отдельной диагностики endpoint
  либо операторской фильтрации.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Hosted jobs сейчас
  завершаются до старта из-за Billing & plans и не считаются `PASS`.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются exact Windows, current/Brain refresh, payment-provider
  E2E, Operator OIDC/RBAC, legal/commercial approval, Android remaining matrix
  и rollback drill.
