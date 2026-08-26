# POKROV 1.2.0 — direct beta candidate 1

Это точный кандидат прямого beta-релиза Android и Windows. Он не является
широким stable-релизом, не опубликован в Microsoft Store или Google Play и не
разрешает продвижение без отдельного go/no-go по оставшимся ручным воротам.

## Что вошло

- production-signed Android-клиент и service-first Windows-клиент;
- 7 локаций и четыре варианта подключения для Санкт-Петербурга: обычный и три
  режима «Белые списки»;
- DNS-over-HTTPS: автоматически, Cloudflare, Google, AdGuard и собственный
  HTTPS DoH-адрес;
- ограниченные маршруты для AI-сервисов, игр/Xbox, видео, соцсетей и RU-direct;
- Core 1.1.0, строгий release-handoff v2, CycloneDX SBOM и SLSA provenance;
- отдельные default-off контракты `awg2_lab` и `awg31_lab`.

AI и Games направляют ограниченный набор доменов через активный VPN. Это не
DNS-only обход и не обещание доступа без VPN. AWG 3.1 остаётся выключенной
лабораторной возможностью: отдельный принадлежащий POKROV endpoint ещё не
доказан, поэтому публичное включение запрещено.

## Android

Все APK и AAB подписаны production-сертификатом POKROV. Для обычной прямой
установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `c03a5dea38cc031086e15cfabee95b403f1f5fa662583edd7d804be8401f26f2`;
- размер: `295018413` байт.

Exact x86_64 APK побайтно проверен на LDPlayer 14. Все локации отображались,
обычный Санкт-Петербург поднял `tun0` и дал HTTPS 204. Типы 2 и 3 завершились
без ложного «Подключено», TUN и crash. Эмулятор не заменяет проверку exact
4030-байтов на физическом Android и мобильной сети.

## Windows

Windows-установщик не имеет Authenticode-подписи. Microsoft Defender
SmartScreen может показать предупреждение о неизвестном издателе. Запускайте
его только из официального релиза POKROV после сверки SHA-256.

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `730428bf6ff157502069d79fed3d89e17814bfff4cd023b9cfd404c838a038de`;
- размер: `28890834` байт;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Исключение не разрешает trusted, signed, Store или broad-stable заявления.
Clean-host TUN/DNS/egress/recovery остаётся обязательным ручным gate.

## Проверяемость

Публичный signed manifest связывает точные SHA-256, размеры, исходные коммиты,
SBOM и provenance. Продвижение обязано использовать те же байты без пересборки.
Актуальные ограничения перечислены в `pokrov-1.2.0-candidate.1-known-issues-ru.md`.
