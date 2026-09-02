# POKROV 1.2.0 — direct beta candidate 23

Это точный закрытый кандидат Android и Windows `1.2.0+4052`. Он заменяет
candidate 22 и привязан к platform
`5ba4dba3db0f900466d2f36d84d981a0a9c9fe68`, client
`df9ed85bb0e7fd7bf1e1c43d033825212c2f6354` и Core artifact source
`cd8f0f4169d570d693992a959d81d17c2c44884d`.

Candidate 23 не является публичным `v1.2.0`, не опубликован в магазинах и не
разрешает stable-продвижение без отдельного go/no-go.

## Что исправлено после candidate 22

Windows-клиент исправляет порядок connected-uninstall: перед удалением файлов
останавливаются UI, активный туннель и служба, после чего проверяется отсутствие
процессов, службы, install root и остаточного туннеля. Это устраняет причину,
из-за которой предыдущий кандидат нельзя было честно продвинуть дальше.

Точный setup candidate 23 установлен на изолированной Windows 11 VM. Проверены
совпадение хеша установщика, `11/11` обязательных runtime-файлов, запущенная
служба и отсутствие туннеля в исходном состоянии. Native Windows CTest прошёл
`7/7`; статический скан самого набора и установленного payload не нашёл
определённых секретов. Полный replay удаления во время активного соединения
остаётся обязательным ручным gate именно для неизменяемых байтов candidate 23.

## Android artifacts

Для прямой установки предназначен universal APK:

- файл: `pokrov-android-universal.apk`;
- SHA-256: `596f37f78606f9aab63f1fc17c6244bfec59273f063c5d318886c052adf90bef`;
- размер: `295370161` байт;
- версия: `1.2.0`, build `4052`, min SDK `24`.

ABI APK:

- `pokrov-android-arm64-v8a.apk` — `08406f372513a0925e6b730f8c98554f8f9ba4e65ab2c7394633a4520891cb42`, `101366678` байт;
- `pokrov-android-armeabi-v7a.apk` — `006fe1060c82f6e986c3f293150bbe3613fb6c3c6f61061be0b6ec8865ef2257`, `90778788` байт;
- `pokrov-android-x86_64.apk` — `9fa6727fa93a6406315198789989f367cb5061f6cc2d06c48827db0d49487e4f`, `109951989` байт.

Store AAB:

- файл: `pokrov-android-market.aab`;
- SHA-256: `d8b462ba634c5ea61fd54d6cfa60db4b42724cb9fbcf8c09baf30d087734417a`;
- размер: `126263402` байт;
- ABI: `armeabi-v7a`, `arm64-v8a`, `x86_64`.

Все APK production-signed, release/non-debuggable. AAB сохраняет JAR signature
integrity и production upload-key fingerprint. Google Play submission не
выполнялся.

Точные candidate 23 APK требуют отдельного LDPlayer install/launch и
физического ARM64 runtime на Wi-Fi и Билайне: default/fallback, AWG 3.1, AWG2,
Smart DNS, WARP, IPv4/IPv6/leak, Doze/OEM и endurance.

## Windows

- файл: `pokrov-windows-setup-x64.exe`;
- SHA-256: `ded8c4479e3f890a14298e30291693b8499ea78960813862e649354a597fa291`;
- размер: `29146140` байт;
- версия: `1.2.0+4052`;
- подпись: `NotSigned` / `SKIPPED_BY_OWNER` только для direct beta 1.2.0.

Manifest `f92c007da3132e34a0d92856fde998c12654e99e4a286f77a57a3902811fb877`
связывает `11/11` обязательных файлов. Owner exception сохраняет обязательное
предупреждение SmartScreen/`Unknown publisher` и не разрешает trusted, Store или
broad-stable claim.

## Протоколы и Smart DNS

VLESS/Reality остаётся стабильной основой. AWG 3.1 — приоритетный закрытый
UDP-lab transport, AWG2 — совместимый rollback/fallback. Оба lab-профиля
выключены по умолчанию, собственной криптографии и отдельного бренда AWG нет.

AWG control-plane, client materialization и Smart DNS имеют ограниченные
source-level доказательства предыдущих точных ревизий. Они не заменяют live
interop точного APK candidate 23. In-app выбор Smart DNS, физический DoH/leak/load
и реальные авторизованные ChatGPT/Gemini/Xbox sessions остаются открыты. xHTTP
и Hysteria2 не переводятся в обязательную линию 1.2.0.

## Точная поставка

Strict-v2 handoff и offline validator связали `6/6` артефактов и `11/11`
Windows runtime-файлов. SBOM SHA-256:
`0c789b50747ff753aad5c8d6e5f24fc21f68660749639891c983644476724493`.
Provenance SHA-256:
`71f2d6ec899cffbe67a7431eefe6f2252e15ed3591e064f7f21205abab112c1b`.
Release-handoff SHA-256:
`457bbf7134d169f80c4d15e75f516d1366741ad107fdf68ae516c865b91bef50`.

Tracked input сам по себе не является подписанным кандидатом. Main-only signer
должен связать zero-commit placeholder с точным release-index `main`, создать
Ed25519 signature и сохранить receipt. Даже после подписи кандидат не создаёт
тег, GitHub Release, публичные assets, store submission или stable pointer.
