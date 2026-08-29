# POKROV 1.2.0 candidate 7 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  `Unknown publisher`; исключение действует только для direct beta 1.2.0.
- Exact candidate 7 ещё не прошёл обязательный чистый Windows 10/11 gate:
  install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и
  uninstall. На текущем рабочем ПК подходящая изолированная Windows-среда не
  подтверждена.
- Физический Android-телефон снова доступен, однако WARP, per-app, Private DNS,
  IPv6, OEM/Doze и leak-матрица ещё не зафиксированы как evidence exact
  candidate 7. LDPlayer остаётся отдельной emulator-проверкой.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 2/3.1 имеют положительный pre-candidate runtime proof, но остаются
  закрытыми лабораторными вариантами и требуют retained evidence на exact
  candidate 7 bytes.
- Внешний Smart DNS выключен по умолчанию. Source-contract для OpenAI/ChatGPT,
  Gemini и Xbox доказан, но живой управляемый resolver не развёрнут. Доступ к
  этим сервисам без VPN пока не заявляется.
- Доступность Санкт-Петербурга на мобильных операторах не заявляется; эта
  локация не блокирует AWG/DNS-релизную работу и требует отдельной диагностики
  endpoint либо операторской фильтрации.
- Локальная Raspberry Pi 4 с прямым RU-доступом доступна только через терминал
  и ещё не использована для exact candidate 7. До сохранённого RU-origin
  evidence заявление RU-ready запрещено.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Hosted Actions
  могут завершаться до запуска job из-за billing/runner-ограничения, поэтому
  такие запуски не считаются `PASS`.
- До go/no-go остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval, exact-candidate device gates
  и rollback drill. RU-origin нужен только для отдельного RU-ready заявления.
- Перевод репозиториев в public не входит в candidate 7 и не нужен для его
  закрытой проверки.
