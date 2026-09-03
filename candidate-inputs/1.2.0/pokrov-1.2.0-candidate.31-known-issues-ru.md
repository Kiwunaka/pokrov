# POKROV 1.2.0 candidate 31 — известные ограничения

- Windows EXE не подписан Authenticode. Для direct beta ожидаются SmartScreen
  и `Unknown publisher`; действует owner exception, но trusted/Store claim
  запрещён.
- Candidate 31 использует точные байты проверенной CLI-сборки. Новые SBOM,
  provenance и handoff привязаны к candidate 31; supply validator прошёл.
- Исправления platform до `84837ce68a028f0c81580a5f1beefddba584de6d`
  ещё не развёрнуты в production. Fresh-trial и managed runtime retest до
  отдельного разрешённого deploy остаются `NOT_RUN`.
- В текущем CLI-сеансе ADB не видел телефон или LDPlayer. Exact APK ещё не
  проверен на физическом ARM64-телефоне по Wi-Fi и Билайну.
- Обязательные mobile-проверки: default/fallback, AWG 3.1, AWG2, WARP,
  Smart DNS, Private DNS, IPv4/IPv6/leak, Doze/OEM, handover и endurance.
- Побайтно идентичный Windows setup имеет сохранённые headless-результаты для
  `11/11` runtime-файлов, службы, direct TUN/DNS и reboot. Реальные managed
  VLESS/AWG/WARP/Smart DNS ещё требуют точного повторного теста после deploy.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или production promotion.
- Действует `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Hosted
  jobs, не выполнившие ни одного шага из-за GitHub Billing, не считаются PASS.
- Подпись release-index подтверждает неизменность input, но сама по себе не
  разрешает promotion.
- До go/no-go остаются physical Android, managed Windows transports,
  current/brain/RU origins, provider E2E, Operator OIDC/RBAC,
  legal/commercial approval, rollback rehearsal и итоговый Gate F.
