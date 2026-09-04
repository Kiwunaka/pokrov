# POKROV 1.2.0 — direct beta candidate 33

Candidate 33 — новый приватный кандидат `1.2.0+4053`, собранный из слитых
основных линий platform/client и неизменного exact Core. Он заменяет candidate
32 и включает исправление возврата Windows-окна на передний план при повторном
запуске. Android и Windows заново собраны через production CLI-процессы.

Точный source tuple:

- platform: `f5300053026d32826e54c02202303e1f68c65bc1`;
- client: `6ab1bcaf39c61a0ae0c9d8328e6c95382885735e`;
- Core: `cd8f0f4169d570d693992a959d81d17c2c44884d`;
- pre-candidate release-index: `7a6b2ce859b34b074e877851ba50aae7e80854a3`.

## Проверенный комплект

- Android arm64 APK: `1eca4cbe8d36cbec2aca3dd92f27b7b369fb1199a13e6110a2447fad265acda5`;
- Android armeabi-v7a APK: `cee69c797e5e73b929ee1ad7b56d4c0918d81d0b25b42cfc0903801b16450734`;
- Android market AAB: `9f3ad01d92fcde54d93d88b0df9a04e9b7b531362029d1df4beab86ded5fac2c`;
- Android universal APK: `51b86f66bd5c79fdf8a8e51d7607315a6ea3f8dfe9c36c4656034aac3b4583f2`;
- Android x86_64 APK: `fe1fa2d2efb3c20530ed4af7ef48d74e05b6b89e213410f976d180c58c473168`;
- Windows setup x64: `250622f7e4bf9bea39a9456004d4cfeb2340a987c622c46f70b3af07aaec3580`.

Все Android-файлы подтверждены production-сертификатом SHA-256
`0a0602a7df5d96a0b427909d004f3ddf26def86587634bf16694da8d654b2500`.
Market AAB имеет корректную JAR-подпись и содержит Core для `armeabi-v7a`,
`arm64-v8a` и `x86_64`. Windows setup остаётся unsigned direct beta по
owner exception; предупреждение SmartScreen/Unknown publisher обязательно.

Для candidate 33 заново созданы и независимо проверены:

- canonical artifact-set: `1858db3491effa6224d3816763f7bd90a16429ae6b21c6fc97275d84f5d31978`;
- CycloneDX 1.5 SBOM, `352` компонента: `3b586c6e2b63e802ecb6cdfadf5cdac5cd8b7957a5112da4ed9d0a86f6646125`;
- SLSA v1 provenance, `6` subjects: `9aadcb1dfa8973c08ca4682238e91baa17f4aa952f4d03eb78ebdfea733aeb08`;
- strict-v2 release handoff: `30d9d04437caa51c0fafb533a77589d745c66cd7ce5c17843d5b3a1e37e72c81`;
- Windows runtime manifest: `0f93211e254076fad5de8cf88d0817897313c2fd3f3b2daa6d1253628da63a5b`.

Offline supply-chain validator: `PASS`, `6/6` application artifacts и `11/11`
Windows runtime-файлов. В SBOM и provenance отсутствуют ссылки на номера
предыдущих кандидатов.

Exact merged-main CLI contour прошёл Flutter `413/413`, Android Gradle release,
Windows analyze/build и native Release CTest `7/7`. Проверка возврата фокуса
на повторном запуске ранее прошла на обычном Windows 11 VM source-build; её
нужно повторить на exact candidate 33. Локальные результаты не заменяют
exact-candidate проверки на физическом Android и изолированной Windows VM.

Candidate 33 не является публичным `v1.2.0`, не развёрнут в production, не
загружен в магазины и не разрешает stable-продвижение.
