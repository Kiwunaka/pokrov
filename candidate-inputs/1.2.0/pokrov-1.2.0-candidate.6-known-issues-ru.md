# POKROV 1.2.0 candidate 6 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и
  `Unknown publisher`; исключение действует только для direct beta 1.2.0.
- На текущем рабочем ПК недоступны Windows Sandbox, Hyper-V, VMware и
  VirtualBox. Поэтому exact candidate 6 ещё не прошёл обязательный чистый
  Windows 10/11 gate: install, SCM service, authenticated IPC, TUN, DNS,
  egress, recovery и uninstall.
- На физическом Beeline-устройстве установлен POKROV `1.2.0+4046`, но телефон
  в момент фиксации кандидата был закрыт keyguard. Оставшаяся точная матрица
  WARP, per-app, Private DNS, IPv6, OEM/Doze и leak должна быть выполнена после
  ручной разблокировки владельцем.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  AWG 2/3.1 имеют положительный pre-candidate runtime proof, но остаются
  закрытыми лабораторными вариантами и требуют retained evidence на exact
  candidate 6 bytes.
- Внешний Smart DNS выключен по умолчанию. Source-contract для
  OpenAI/ChatGPT, Gemini и Xbox доказан, но живой управляемый resolver не
  развёрнут: у существующих узлов нет свободного подтверждённого public
  TCP/443 endpoint, новая платная инфраструктура не разрешена. Доступ к этим
  сервисам без VPN пока не заявляется.
- WARP на LDPlayer не дал отдельного egress из-за сетевого origin самого
  эмулятора. Это environment-blocked проверка, а не доказанный дефект
  candidate 6. Физическая проверка WARP остаётся обязательной.
- Доступность Санкт-Петербурга на мобильных операторах не заявляется; эта
  локация не блокирует AWG/DNS-релизную работу и требует отдельной диагностики
  endpoint/операторской фильтрации.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Для
  candidate 6 действует `OWNER_SOLO_EXCEPTION`; независимый review не
  заявляется.
- До go/no-go остаются current-origin и Brain-origin, payment-provider E2E,
  Operator OIDC/RBAC, legal/commercial approval, exact-candidate device gates
  и rollback drill. RU-origin требуется только для отдельного RU-ready
  заявления.
- Перевод репозиториев в public не входит в candidate 6 и не нужен для его
  закрытой проверки.
