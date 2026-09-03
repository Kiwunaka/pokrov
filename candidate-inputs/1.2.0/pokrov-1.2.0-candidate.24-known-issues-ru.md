# POKROV 1.2.0 candidate 24 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact direct beta 1.2.0.
- Exact Windows setup candidate 24 ещё не установлен в VM: headless guest-сеанс
  не имеет прав администратора. Сборка, manifest `11/11`, статическая проверка и
  Debug native CTest `8/8` выполнены без перехвата основного компьютера.
- Fresh install, upgrade поверх candidate 23, активное соединение при удалении,
  Windows 10, sleep/resume, forced-kill и connected reboot остаются ручными
  runtime-проверками точных байтов candidate 24.
- Candidate 23 сохранён как неизменяемая история и не заменяет candidate 24
  evidence.
- Candidate 24 APK требует точный LDPlayer install/launch/byte-identity и
  физический ARM64 runtime. Результат эмулятора за host-туннелем не является
  доказательством AWG, DNS или egress.
- Физический ARM64-телефон должен проверить exact APK отдельно на Wi-Fi и
  Билайне: default/fallback, AWG 3.1, AWG2, WARP, Smart DNS, Private DNS,
  IPv4/IPv6/leak, Doze/OEM и endurance.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Собственной криптографии нет. xHTTP и Hysteria2 требуют отдельного interop,
  network и rollback evidence и не являются обязательной поставкой 1.2.0.
- AWG и Smart DNS source-level evidence не заменяет live candidate 24 Android /
  Windows interop, in-app Smart DNS selection, physical DoH/leak/load и
  авторизованные ChatGPT/Gemini/Xbox sessions.
- Оба немецких delivery endpoint описывают одну физическую серверную ноду.
  Доступность каждого адреса у каждого мобильного оператора не гарантируется.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Только реально
  выполненные hosted jobs считаются `PASS`.
- Private candidate supply-chain имеет PASS, но tracked candidate input ещё не
  подписан main-only Ed25519 signer. Ни этот input, ни будущая подпись сами по
  себе не разрешают promotion.
- До go/no-go остаются exact Windows runtime, physical Android, отдельные
  current/brain/RU origins, payment-provider E2E, Operator OIDC/RBAC,
  legal/commercial approval, rollback rehearsal и итоговый Gate F.
