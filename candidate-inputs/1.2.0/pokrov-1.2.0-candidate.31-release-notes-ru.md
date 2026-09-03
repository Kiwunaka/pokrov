# POKROV 1.2.0 — direct beta candidate 31

Candidate 31 — новый приватный кандидат `1.2.0+4053`. Android и Windows
артефакты побайтно совпадают с уже проверенной CLI-сборкой; для них заново
созданы и проверены привязанные к candidate 31 SBOM, provenance и strict-v2
handoff. Platform зафиксирован на
`84837ce68a028f0c81580a5f1beefddba584de6d`, client — на
`7e3e771fe36333a75244cbfd828c60beb84c7ff1`, Core — на
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 31 заменяет candidate 30, у которого проверка обнаружила устаревшие
внутренние ссылки в supply metadata. Бинарные файлы candidate 30 не были
причиной отказа; новый кандидат исправляет именно неизменяемый комплект
метаданных поставки.

## Проверенный комплект

- Android APK: `arm64-v8a`, `armeabi-v7a`, `x86_64`, universal;
- Android AAB: market bundle с тремя ABI Core;
- Windows: setup x64 и manifest из `11/11` обязательных runtime-файлов;
- canonical artifact-set SHA-256:
  `dce1c4e43aa1729e87f6620da9f655482dd3a6113bb67006e319c090e0b02b9e`;
- SBOM SHA-256:
  `e5d9eb85bacb778e225d5d909832cd3e7d42c9d19fa1ebc44092456ec9da56a5`;
- provenance SHA-256:
  `1075c286fea33b7ddc5451d3d3da47e63f9c9077d4543dd7e0b498c830ad8dc0`;
- release-handoff SHA-256:
  `095af12c8b335e86b8e8590259946a33cec5c356eaaacc9e93f2e09698193a48`.

Offline supply-chain validator: `PASS`, `6/6` артефактов и `11/11` Windows
runtime-файлов. В candidate 31 нет ссылок на номера предыдущих кандидатов
в SBOM/provenance.

## Статус тестов

Побайтно идентичный Windows setup ранее прошёл headless Windows 11 upgrade,
проверку службы, direct TUN/DNS connect/disconnect и connected guest reboot.
Эти результаты относятся к тем же байтам, но не заменяют новый managed
transport retest после разрешённого platform deploy.

Android APK/AAB подписаны production-сертификатом и прошли проверку целостности.
В текущем CLI-сеансе ADB не видел телефон или LDPlayer, поэтому физический и
эмуляторный Android runtime test остаётся `NOT_RUN`.

Candidate 31 не является публичным `v1.2.0`, не развёрнут в production, не
опубликован в магазинах и не разрешает stable-продвижение.
