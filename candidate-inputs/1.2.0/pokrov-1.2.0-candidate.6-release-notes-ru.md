# POKROV 1.2.0 — direct beta candidate 6

Это точный закрытый кандидат прямого beta-релиза Android и Windows. Он собран
из platform `5713324c1c0c2566befadf527bc09ec0ecf84a4e`, client
`b2497af7704d0aa6901541e175ce154b0eab05d7` и Core
`a45d69e40ed7d892619a2b5c4592a527f630665e`. Candidate 6 не является
публичным `v1.2.0`, не опубликован в магазинах и не разрешает stable-продвижение
без отдельного go/no-go по оставшимся воротам.

## Что изменилось после candidate 5

Пересобран весь набор `1.2.0+4046`: четыре APK, один AAB и Windows x64
installer. Android-файлы подписаны production-сертификатом POKROV. Windows
installer остаётся без Authenticode по принятому владельцем исключению для
direct beta и поэтому может показывать Microsoft Defender SmartScreen и
`Unknown publisher`.

Исправлен выбор resolver для закрытых AWG-профилей. `awg2_lab` и `awg31_lab`
остаются выключенными по умолчанию и не выдаются как обычные публичные
протоколы. Точные pre-candidate ARM64/x86_64 bytes успешно проходили AWG 2 и
AWG 3.1 handshake, TUN, DNS, egress и disconnect cleanup на LDPlayer и
физическом Beeline-устройстве. Для candidate 6 эти результаты должны быть
привязаны к точным артефактам отдельной device evidence; они не превращают
лабораторные варианты в стабильные настройки.

Добавлен строгий source-contract для внешнего Smart DNS: allowlist покрывает
точные домены OpenAI/ChatGPT, Gemini и Xbox и их поддомены; похожие посторонние
домены отвергаются; AAAA/HTTPS/SVCB и прочие неподдерживаемые типы не получают
синтетического A-ответа. Режим выключен по умолчанию. Живой управляемый
резолвер не развёрнут: у текущих семи узлов нет свободного подтверждённого
публичного TCP/443 endpoint, а покупка новой инфраструктуры владельцем не
разрешена. Поэтому candidate 6 не обещает доступ к AI/gaming-сервисам без VPN.

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

AAB входит в точный набор поставки, но загрузка в Google Play для candidate 6
не выполнялась.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `18a0b4293930959b31dfb41df55b94caad87ce2d574b4dfa2d12832e80307643`;
- размер: `28931862` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Установщик нужно запускать только из официального канала POKROV после сверки
SHA-256. Исключение не разрешает заявления `trusted`, `signed`, Store или
broad stable. Для exact candidate 6 ещё требуется чистый Windows 10/11 host:
install, SCM service, authenticated IPC, TUN, DNS, egress, recovery и uninstall.

## Точная поставка

Strict-v2 handoff связывает шесть файлов с одним source tuple, CycloneDX SBOM
и SLSA provenance. Локальный quality gate для этих исходников прошёл 15 из 15
проверок. Продвижение обязано использовать те же байты без пересборки.
Актуальные ручные и инфраструктурные ограничения перечислены в
`pokrov-1.2.0-candidate.6-known-issues-ru.md`.
