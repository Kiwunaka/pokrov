# POKROV 1.2.0 — direct beta candidate 7

Это точный закрытый кандидат прямого beta-релиза Android и Windows. Он
привязан к platform `af259f377ec7a3cd757f0f43762154dd25e09f94`, client
`b2497af7704d0aa6901541e175ce154b0eab05d7` и Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. Candidate 7 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go по оставшимся воротам.

## Что изменилось после candidate 6

Бинарники не пересобирались: client и Core не менялись, поэтому candidate 7
использует те же проверенные байты build `1.2.0+4046`. Изменился platform — в
него добавлен fail-closed валидатор точного набора поставки. Исправлены
CycloneDX SBOM и SLSA provenance: удалена устаревшая Flutter-зависимость,
зафиксированы актуальные четыре Git-ревизии, точные Core AAR/DLL и все восемь
файлов Windows runtime. Strict-v2 handoff и локальный supply-chain gate прошли
на этих точных данных.

`awg2_lab`, `awg31_lab`, bounded Hysteria2 и direct-DoH/Smart-DNS варианты
остаются закрытыми и выключенными по умолчанию. AWG 2 и AWG 3.1 уже имеют
положительные pre-candidate проверки handshake, TUN, DNS, egress и cleanup,
но для candidate 7 нужна отдельная привязка device evidence к точным файлам.
Smart DNS имеет строгий source-contract для OpenAI/ChatGPT, Gemini и Xbox, но
живой управляемый resolver пока не развёрнут, поэтому доступ без VPN не
обещается.

## Android

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `3e3e27eb48f4351b9f8bf3f6bd386faf05ae058322de29ee8b3c94d53ef996d6`;
- размер: `295370385` байт;
- версия: `1.2.0`, build `4046`, min SDK `24`.

ARM64 APK для физического устройства:

- файл: `pokrov-android-arm64-v8a.apk`;
- SHA-256: `b583205db9e197c6de873264821319ef1108a2786f1ee5466501712568147296`;
- размер: `101366934` байт.

Store-handoff AAB подписан тем же production-сертификатом:

- файл: `pokrov-android-market.aab`;
- SHA-256: `676ee2b1f5480d0bd66e58662399b758466ad1472862db5c87a145d2d44e05c1`;
- размер: `126269864` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

AAB входит в точный набор поставки, но загрузка в Google Play не выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `18a0b4293930959b31dfb41df55b94caad87ce2d574b4dfa2d12832e80307643`;
- размер: `28931862` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Установщик нужно запускать только из официального канала POKROV после сверки
SHA-256. Исключение не разрешает заявления `trusted`, `signed`, Store или
broad stable. Для exact candidate 7 ещё требуется чистый Windows 10/11 host:
install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и uninstall.

## Точная поставка

Strict-v2 handoff связывает шесть файлов с одним source tuple, исправленными
CycloneDX SBOM и SLSA provenance. Локальный source quality gate прошёл 15 из
15 проверок, а offline supply-chain validator подтвердил 6/6 артефактов и 8/8
Windows runtime файлов. Продвижение обязано использовать те же байты без
пересборки. Актуальные ручные и инфраструктурные ограничения перечислены в
`pokrov-1.2.0-candidate.7-known-issues-ru.md`.
