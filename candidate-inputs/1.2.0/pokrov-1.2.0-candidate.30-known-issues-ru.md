# POKROV 1.2.0 candidate 30 — известные ограничения

- Windows EXE не подписан Authenticode. Для direct beta ожидаются SmartScreen
  и `Unknown publisher`; owner exception не разрешает trusted/Store claim.
- Все шесть файлов собраны через CLI из client
  `7e3e771fe36333a75244cbfd828c60beb84c7ff1`, Core
  `cd8f0f4169d570d693992a959d81d17c2c44884d` и platform
  `7c4133343871ed52257a850e829e906608412753`.
- Exact Windows setup прошёл headless upgrade в Windows 11 VM: `11/11`
  runtime-файлов, служба, direct TUN/DNS lifecycle и connected guest reboot.
  Это синтетический direct-профиль без реквизитов managed-ноды; он не доказывает
  VLESS/AWG/WARP/Smart DNS через реальные серверы.
- Исправление first-run provisioning уже в platform `master`, но ещё не
  развёрнуто в production. Новый live trial до отдельного разрешённого deploy
  остаётся `NOT_RUN`.
- Candidate 29 показал отдельный `FAIL_CORE_EGRESS_PROBE` для AWG 3.1 и AWG2
  на Windows. Candidate 30 не наследует PASS и требует нового managed runtime
  retest после deploy backend-исправления.
- APK/AAB подписаны production-сертификатом и прошли package integrity, но
  exact APK ещё не проверен на физическом ARM64-телефоне по Wi-Fi и Билайну.
- Обязательные mobile-проверки: default/fallback, AWG 3.1, AWG2, WARP,
  Smart DNS, Private DNS, IPv4/IPv6/leak, Doze/OEM, handover и endurance.
- Свежая локальная компиляция точного Core дала DLL на 1024 байта больше
  закреплённого воспроизводимого артефакта и была отвергнута. В candidate 30
  вошёл только ранее доказанный byte-identical Core SHA-256
  `f284fa8841f1a45271874a7a05ed6093fb0e3efbdd03e00001edd046be708204`.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или production promotion.
- Действует `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Hosted
  jobs, не выполнившие ни одного шага из-за GitHub Billing, не считаются PASS.
- Offline supply-chain прошёл, но main-only Ed25519 signer ещё не подписал
  tracked candidate input. Подпись сама по себе также не разрешает promotion.
- До go/no-go остаются physical Android, managed Windows transports,
  current/brain/RU origins, provider E2E, Operator OIDC/RBAC,
  legal/commercial approval, rollback rehearsal и итоговый Gate F.
