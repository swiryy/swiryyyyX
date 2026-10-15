# swiryyyyX

**Android Telegram client by [swiryy](https://github.com/swiryy), based on Telegram X.**

A personal project focused on convenient chat management, folder forwarding and a refreshed dark interface. This is an independent community client, not an official Telegram or Nicegram app.

## Download

Current beta: **build 23 · 15 October 2026 · Android ARM64**.

[Open the successful APK build](https://github.com/swiryy/swiryyyyX/actions/runs/38696055306) → **Artifacts → swiryyyyX-arm64-debug** → extract the ZIP and install the APK. GitHub sign-in and repository access are currently required; Actions artifacts are retained for 7 days. A permanent public APK release is being prepared.

## Features

- Local hidden chats with account-specific settings.
- Paged chat loading with priority for personal conversations.
- Forward Saved Messages to eligible chats in a selected folder, with a recipient review before sending.
- The forwarding picker closes after Send; the active queue continues while the app process remains available.
- A 200 ms pause after delivery acknowledgement between chats, with server cooldowns respected. This is not a guarantee against Telegram account restrictions.
- Forwarding options to hide the original sender and remove media captions.
- A profile gift gallery and Telegram Stars balance.
- New gift purchases with Stars and transfers of eligible owned collectible gifts, with recipient and cost confirmation.

## Beta status

The Android build and automated checks pass. Folder forwarding has been tested by the project owner on a Galaxy A35. Gift purchases and transfers still need real-device validation; no real payments were made during automated tests. Some upstream message types and Nicegram-style interface details remain incomplete.

Android ARM64 only; this APK does not run on iPhone. This is currently a debug build. Updates must use the same signing key; if Android rejects an update, report the error before uninstalling or clearing app data.

## Source and build

This repository stores the cumulative modifications in `swiryyyyX.patch`. `UPSTREAM_COMMIT` pins the official [Telegram X source](https://github.com/TGX-Android/Telegram-X). The workflow fetches that source, applies the patch and builds `assembleLatestArm64Debug`. The patch includes the project tests.

Required repository Actions secrets:

- `TELEGRAM_API_ID` and `TELEGRAM_API_HASH`: your own Telegram application credentials.
- `GOOGLE_SERVICES_JSON`: Firebase Android configuration for `ua.swiryyyyx.client`.
- `ANDROID_DEBUG_KEYSTORE_BASE64`: an existing saved debug keystore for consistent update signing. Without it, the runner generates a fresh debug key.

Never commit credentials, `local.properties`, Firebase configuration, keystores or account/session data. Do not post those files in bug reports.

## Feedback

Report the app build, phone model, Android version, exact steps and expected result. Redact phone numbers, login codes, messages and other private details from screenshots.

## Credits and license

Built on Telegram X by TGX-Android and TDLib. Upstream copyright notices and GPL-3.0 licensing apply to the Telegram X source and modifications. Keep all upstream notices and dependency licenses when redistributing. This project is maintained by swiryy.
