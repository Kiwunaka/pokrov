# POKROV 1.2.0 candidate 21 — известные ограничения

- Windows EXE не подписан Authenticode. Ожидаются SmartScreen и `Unknown
  publisher`; owner exception действует только для exact direct beta 1.2.0.
- Точный Windows setup прошёл upgrade из проблемного committed-state candidate
  20, startup recovery, `11/11` file identity, обычный UI, SCM `LocalSystem`
  service, default connect, TUN, DNS, authenticated DE egress и точный rollback
  после disconnect на изолированной Windows 11 VM.
- Свежая принудительная остановка уже установленной candidate 21 службы не
  выполнялась: UAC был отменён до остановки процесса. Это `NOT_RUN`, а не FAIL.
  Windows 10, sleep/resume, connected reboot/uninstall, AWG 3.1/AWG2 на Windows
  и интерактивный SmartScreen остаются отдельными проверками.
- Candidate 20 отклонён и не должен публиковаться: после принудительной остановки
  новый процесс SCM не завершал committed recovery journal. Его ранее прошедшие
  default Windows 11, public-1.1.6 migration и connected-reboot срезы остаются
  ограниченной историей и не заменяют candidate 21 evidence.
- Candidate 21 APK ещё не прошёл точный LDPlayer install/launch/byte-identity и
  физический ARM64 runtime. Результат эмулятора за host-туннелем не будет
  доказательством AWG, DNS или egress.
- Физический ARM64-телефон должен проверить exact candidate 21 APK отдельно на
  Wi-Fi и Билайне: default/fallback, AWG 3.1, AWG2, WARP, Smart DNS, Private DNS,
  IPv4/IPv6/leak, Doze/OEM и endurance.
- `awg2_lab`, `awg31_lab` и bounded Hysteria2 lane выключены по умолчанию.
  Собственной криптографии нет. xHTTP и Hysteria2 требуют отдельного interop,
  network и rollback evidence и не являются обязательной поставкой 1.2.0.
- AWG `72/72` control-plane, `2/2` materialization и Smart DNS `18/18` routing /
  `2/2` UI являются source-only evidence. Live candidate 21 Android/Windows AWG,
  in-app Smart DNS selection, physical DoH/leak/load и authenticated
  ChatGPT/Gemini/Xbox sessions остаются открыты.
- Оба немецких delivery endpoint описывают одну физическую серверную ноду.
  Доступность каждого адреса у каждого мобильного оператора не гарантируется.
- Android AAB не загружен в Google Play. Нет тега `v1.2.0`, GitHub Release,
  публичных assets, stable pointer или store submission.
- Владелец отказался от платного GitHub-плана и branch protection. Действует
  `OWNER_SOLO_EXCEPTION`; независимый review не заявляется. Только реально
  выполненные hosted jobs считаются `PASS`.
- Tracked candidate input не является подписанным кандидатом. До отдельного
  main-only Ed25519 signer receipt статус остаётся reviewed freeze input.
- До go/no-go остаются exact physical Android gates, отдельные current/brain/RU
  origins, payment-provider E2E, Operator OIDC/RBAC, legal/commercial approval,
  rollback rehearsal и итоговый Gate F.
