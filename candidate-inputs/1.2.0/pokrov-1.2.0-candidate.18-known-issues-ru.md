# POKROV 1.2.0 candidate 18 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact direct beta 1.2.0.
- Точный Windows setup прошёл isolated Windows 11 clean-app-state install,
  `11/11` file identity, SCM service, authenticated IPC, restart, uninstall и
  migration с публичной 1.1.6. Live TUN, connected DNS/egress, sleep,
  reboot/crash, connected uninstall и интерактивный SmartScreen остаются
  ручными проверками; clean-app-state VM не заявляется как clean OS.
- Candidate 17 отклонён и не должен публиковаться: в его Windows setup нет трёх
  VC runtime DLL, а setup мог вернуть ложный успех после failure службы.
- Exact x86_64 APK прошёл LDPlayer install/launch/byte-identity и не дал crash,
  но LDPlayer находится за host Hiddify/TUN. Его сетевой результат не является
  доказательством AWG/DNS/egress для candidate 18.
- Физический ARM64-телефон должен проверить точный candidate 18 APK отдельно
  на Wi-Fi и Билайне: default/fallback, AWG 3.1, AWG2, WARP, Smart DNS,
  Private DNS, IPv4/IPv6/leak, Doze/OEM и endurance.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Собственной криптографии нет. xHTTP reserve и Hysteria2 требуют отдельного
  interop, network и rollback evidence после 1.2.0.
- Smart DNS выключен по умолчанию. Live `dns.pokrov.space`, TLS/SNI и bounded
  ChatGPT/Gemini/Xbox policy доказаны на текущем runtime, но exact candidate 18
  physical binding, полная leak/load matrix и authenticated app sessions
  остаются открыты.
- Оба немецких delivery endpoint описывают одну физическую серверную ноду и
  один user mapping. Доступность каждого адреса у каждого мобильного оператора
  не гарантируется.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Только реально
  выполненные hosted jobs могут считаться `PASS`.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся unsigned/freeze input.
- До go/no-go остаются exact physical Android gates, RU-origin,
  payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval,
  rollback и итоговый Gate F.
