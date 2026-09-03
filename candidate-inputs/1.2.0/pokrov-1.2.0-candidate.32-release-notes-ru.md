# POKROV 1.2.0 — direct beta candidate 32

Candidate 32 — новый приватный кандидат `1.2.0+4053`, собранный из текущих
основных линий platform/client/Core. Он заменяет candidate 31 и включает
исправленный production-процесс Android с четырьмя APK и market AAB, а также
повторную CLI-сборку Windows из exact client `main`.

Точный source tuple:

- platform: `d0dd37c1003198ba08cffc49a040a77e21621a86`;
- client: `2d6adfcebc37f2109ef339276be6a1569cb7aa1e`;
- Core: `cd8f0f4169d570d693992a959d81d17c2c44884d`;
- pre-candidate release-index: `4de2e9f8620b5aac2f538dc8a052a44ad2a563a5`.

## Проверенный комплект

- Android arm64 APK: `fe8d82289a4903958fe7ed4cf7f8a472e417760a72c95930328a9b9ec3a285f9`;
- Android armeabi-v7a APK: `71de150a4b411c8711146123f0255a88eb6201d6cb19037144baf65f9214aaef`;
- Android market AAB: `53de5d9b9d0a64ef4e7a8cfaf2e6f1972f8ce21c1b723a764b03edd14894bf7f`;
- Android universal APK: `a5ddfa5a5e35f828df4c1817256658c4b569e61d12e4742107fa43c30c506d05`;
- Android x86_64 APK: `00e792ab69e1d0e0c165e3e94be9c9bd4c1b66e9e2dbf706363987b45791d4f5`;
- Windows setup x64: `22689e3e61be82f90b1ba9530cba37628ec546022338fc87018b2d460c020574`.

Все Android-файлы подтверждены production-сертификатом SHA-256
`0a0602a7df5d96a0b427909d004f3ddf26def86587634bf16694da8d654b2500`.
Market AAB имеет корректную JAR-подпись и содержит Core для `armeabi-v7a`,
`arm64-v8a` и `x86_64`. Windows setup остаётся unsigned direct beta по
owner exception; предупреждение SmartScreen/Unknown publisher обязательно.

Для candidate 32 заново созданы и независимо проверены:

- canonical artifact-set: `1392133caa1cb52f59c058a918ba5006d6aefded048fc0927052e4ff51575fb0`;
- CycloneDX 1.5 SBOM, `352` компонента: `5ddf2a96244e70ad1284409f0cea6f5838fab5bfbca5c5b96a245f0716de2893`;
- SLSA v1 provenance, `6` subjects: `4785cd005791a8872f4c8a45202ba2d35c9d1ba65737f5683ee17d0b927c53e6`;
- strict-v2 release handoff: `df85e2ee1a03133ac79bb36064d47518f9067cd188e7624d70fd349011422bef`;
- Windows runtime manifest: `43bd310e2fb287d2ada339d8938fbe2304261fe23c9d8608124417d05af9e7dd`.

Offline supply-chain validator: `PASS`, `6/6` application artifacts и `11/11`
Windows runtime-файлов. В SBOM и provenance отсутствуют ссылки на номера
предыдущих кандидатов.

Exact-main CLI contour прошёл Flutter `413/413`, Android Gradle release,
Windows analyze/build и native Release CTest `7/7`; staged Windows bundle
совпал `302/302` с предыдущей воспроизводимой сборкой. Эти локальные результаты
не заменяют exact-candidate проверки на физическом Android и изолированной
Windows VM.

Candidate 32 не является публичным `v1.2.0`, не развёрнут в production, не
загружен в магазины и не разрешает stable-продвижение.
