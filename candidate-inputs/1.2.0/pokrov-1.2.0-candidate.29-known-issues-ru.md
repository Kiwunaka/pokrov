# POKROV 1.2.0 candidate 29 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact direct beta 1.2.0.
- Все шесть файлов пересобраны из текущих исходников. Полный headless CLI build,
  Windows Release/Debug native tests и offline supply validation прошли.
- Exact Windows setup candidate 29 ещё должен пройти установку, обновление,
  service restart/reboot, активное соединение при удалении, Windows 10,
  sleep/resume, forced-kill и IPv6 в изолированной VM.
- Candidate 29 APK требует точный install/launch/byte-identity и физический
  ARM64 runtime. Результат эмулятора за host-туннелем не является доказательством
  AWG, DNS или egress.
- Физический ARM64-телефон должен проверить exact APK отдельно на Wi-Fi и
  Билайне: default/fallback, AWG 3.1, AWG2, WARP, Smart DNS, Private DNS,
  IPv4/IPv6/leak, Doze/OEM и endurance.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Собственной криптографии нет. xHTTP и Hysteria2 требуют отдельного interop,
  network и rollback evidence и не являются обязательной поставкой 1.2.0.
- AWG и Smart DNS source-level evidence не заменяет live candidate 29 Android /
  Windows interop, in-app Smart DNS selection, physical DoH/leak/load и
  авторизованные ChatGPT/Gemini/Xbox sessions.
- Оба немецких delivery endpoint описывают одну физическую серверную ноду.
  Доступность каждого адреса у каждого мобильного оператора не гарантируется.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Действует `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Только
  реально выполненные hosted jobs считаются `PASS`.
- Private candidate supply-chain имеет локальный PASS, но tracked candidate
  input ещё не подписан main-only Ed25519 signer. Ни input, ни будущая подпись
  сами по себе не разрешают promotion.
- До go/no-go остаются exact Windows runtime, physical Android, отдельные
  current/brain/RU origins, payment-provider E2E, Operator OIDC/RBAC,
  legal/commercial approval, rollback rehearsal и итоговый Gate F.
