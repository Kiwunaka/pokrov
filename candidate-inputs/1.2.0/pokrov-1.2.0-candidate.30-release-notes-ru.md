# POKROV 1.2.0 — direct beta candidate 30

Это новый приватный кандидат `1.2.0+4053`, собранный полностью через CLI и
привязанный к platform
`7c4133343871ed52257a850e829e906608412753`, client
`7e3e771fe36333a75244cbfd828c60beb84c7ff1` и Core
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 30 не является публичным `v1.2.0`, не развёрнут в production, не
опубликован в магазинах и не разрешает stable-продвижение.

## Главное изменение

Platform теперь сохраняет подтверждённый `UserNode` mapping сразу после
успешной синхронизации каждой панели. Медленная или недоступная отдельная нода
больше не стирает уже подтверждённый прогресс всего first-run provisioning.
Последующий managed profile может использовать здоровое подтверждённое
подмножество, а проблемная нода остаётся для повторной синхронизации.

## Проверки CLI и Windows VM

- все client release-контракты и Flutter/Dart модули прошли;
- Windows widget: `23/23`;
- Android direct/store Gradle unit tests: PASS;
- Windows native Release CTest: `7/7`;
- Windows native Debug CTest: `8/8`;
- exact headless Windows 11 upgrade: `11/11` файлов;
- direct TUN/DNS connect/disconnect: PASS;
- connected guest reboot и полное восстановление route/DNS: PASS.

VM тест использовал синтетический direct-профиль без реквизитов managed-ноды и
не подменяет live transport checks после развёртывания backend-исправления.

## Android artifacts

- `pokrov-android-universal.apk` —
  `52b700583795ece401e0af57df1db535ad20ce68c3622ddfe4f9e15c6837804a`,
  `295370161` байт;
- `pokrov-android-arm64-v8a.apk` —
  `74c7bc2e19f59d496e6047880bda749700ad946f1d3e50120d366d5304c6f224`,
  `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` —
  `5138c3951290cc8e4e794ae0fdf64cc388cf65f3c6e05bdcc77bc1be6645bd3b`,
  `90778788` байт;
- `pokrov-android-x86_64.apk` —
  `5d0bca3c90d6b0cb1856184bb411002697be2dd1bbb9403d01be8ea996f47ff6`,
  `109951989` байт;
- `pokrov-android-market.aab` —
  `51fe1559f77e02ad073f19772715a1ab1253a2338d5ca378e1f2ed71702e384f`,
  `126263380` байт.

Все APK production-signed. AAB подписан тем же self-managed upload key;
целостность JAR-подписи, fingerprint, manifest и три ABI Core проверены.

## Windows

- `pokrov-windows-setup-x64.exe` —
  `a6512bb6bbac328c62497ebad234b97a2794cb178a1949d35362e919f0d6adf0`,
  `29147936` байт;
- manifest —
  `b73b48f584d8d7e436d2801447a3cf0ab0c13eee652a82c9464377c8ab94e6ee`,
  `11/11` обязательных файлов;
- Authenticode: `NotSigned` / `SKIPPED_BY_OWNER`, direct beta only.

## Точная поставка

Strict-v2 handoff и offline validator связали `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`f0e2d8a337dc219f709abbbc1c5723b2cc734c5693127ad1eb25602f39de74b7`.
Provenance SHA-256:
`ffe0abf35423684a43853ff412c689ebc5cd2a829320c221e7dd9942782be45e`.
Release-handoff SHA-256:
`7be4c7d1f264e6653bf05dd9fecfb6f2231809135abbd7c66cc15026ed2e1aec`.

Следующий технический шаг после подписи input — отдельное разрешение на deploy
platform `7c413334…`, затем новый fresh-trial и managed Windows/Android retest.
