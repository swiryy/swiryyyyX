# swiryyyyX

Personal Android Telegram client based on Telegram X.

This build repository keeps a patch against the pinned upstream commit. The GitHub workflow fetches the official source, applies the patch and builds an ARM64 debug APK for Galaxy A35. Full Nicegram layout and on-device performance validation are still pending.

Configure these repository Actions secrets before running **Build swiryyyyX APK**:
- `TELEGRAM_API_ID`
- `TELEGRAM_API_HASH`
- `GOOGLE_SERVICES_JSON`: complete Firebase Android configuration for package `ua.swiryyyyx.client`.

The workflow never uploads local.properties, build caches or credentials. Download the APK from the workflow run artifacts. A debug APK is signed by the debug key generated on the runner; save the debug keystore as `ANDROID_DEBUG_KEYSTORE_BASE64` to retain install/update compatibility across runs. An existing saved secret is reused automatically; otherwise a fresh debug key is generated.

Telegram X source and changes are GPL-3.0. Keep upstream license and attribution.
