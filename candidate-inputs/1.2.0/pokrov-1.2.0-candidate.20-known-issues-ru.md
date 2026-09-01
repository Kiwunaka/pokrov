# POKROV 1.2.0 candidate 20 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact direct beta 1.2.0.
- Точный Windows setup прошёл isolated Windows 11 machine install, `11/11`
  file identity, обычный UI, SCM `LocalSystem` service, четыре service-owned
  rule-set, default connect, TUN, DNS, authenticated egress, rollback, clean
  uninstall и migration с публичной 1.1.6. Windows 10, AWG 3.1/AWG2 на
  Windows, sleep/reboot/crash, connected uninstall и интерактивный SmartScreen
  остаются отдельными проверками.
- Windows VM сохранила авторизованное пользовательское состояние приложения
  между удалением candidate 19 и установкой candidate 20. Предыдущая машинная
  установка, служба и owner registry были полностью удалены; это не заявляется
  как новый пользовательский профиль.
- Candidate 19 отклонён и не должен публиковаться: абсолютные AppData-пути к
  локальным `.srs` не переносились в service-owned рабочий каталог, поэтому
  Core завершал подключение с `CORE-005`. Candidate 20 передаёт ограниченный
  bundle через authenticated IPC и материализует rule-set службой.
- Candidate 20 APK ещё не прошёл LDPlayer install/launch/byte-identity и
  физический ARM64 runtime. LDPlayer находится за host Hiddify/TUN, поэтому его
  сетевой результат не будет доказательством AWG/DNS/egress.
- Физический ARM64-телефон должен проверить точный candidate 20 APK отдельно
  на Wi-Fi и Билайне: default/fallback, AWG 3.1, AWG2, WARP, Smart DNS,
  Private DNS, IPv4/IPv6/leak, Doze/OEM и endurance.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Собственной криптографии нет. xHTTP reserve и Hysteria2 требуют отдельного
  interop, network и rollback evidence после 1.2.0.
- Smart DNS выключен по умолчанию. Live `dns.pokrov.space`, TLS/SNI и bounded
  ChatGPT/Gemini/Xbox policy доказаны на текущем runtime, но exact candidate 20
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
