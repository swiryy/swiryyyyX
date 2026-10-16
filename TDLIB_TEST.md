# TDLib migration test — 16 October 2026

Base: known-working swiryyyyX build 24, upstream b5f81630f070d1100673029682914ff3672769b0.

Latest official TGX Java/native bundle checked with git ls-remote: 1094df0caf4e5b59f6b247f8d9eb8896022cb379.
Underlying TDLib source: c15d3f5a5de6e3ba5839822c451152e5e18bb700.
Main tdlib/td HEAD at verification was a94b83d67ab4c8397c6245e541b31a4131ea2f79, newer than the bundle. This test uses the latest available TGX bundle, not a claim to build the newest core commit.

Changes: NDK 30.0.16248370, platform-scoped native library/OpenSSL paths, updated Java constructors; static native collectible symbol patterns, rounded gift actions and folder selection; owned collectible listing in Stars and removal through SetGiftResalePrice; fresh server eligibility/price bounds, explicit confirmation, serialized writes, no auto financial retries.

Existing hidden chats, fixed folder order, single-chat archive, 200 ms folder forwarding, sender/caption options and Stars pages retained.

Local checks: 400-chat stores/load/queue, 200-chat fixed slice order; sender, task and gift purchase/transfer code compile against the new generated TDLib API; resale price overflow, bounds, cooldown and write serialization. Java syntax/XML checks pass. Android build and phone validation pending. No real gift purchases, transfers or listings were made.

Manual test: cold start/login, main folders and locked order, one-chat archive, hidden chats/counters, forwarding preview and delivery, received gifts and symbol patterns, transfer recipient/fee confirmation, sale price validation/cancel, listing readback. Do not clear app data to work around a signing mismatch.

Build 25 failed in vkryl/td Kotlin helpers. Follow-up aligns tdlib-utils with upstream 61d4ea0b66cfdeed9352ba0a84e5746e528559d5 and adds the three upstream TON comparison types to the generator configuration. The generator retains the existing annotation API. No app feature is removed. Android compilation still pending.

Also ports upstream API handling in 17 app Java files for new TON content/entity/update types. All 219 generated compile guards referenced by the app now match the selected bundle/utility definitions. New TON content uses upstream unsupported-message fallback; this is not a TON wallet implementation.

Build 26 passed the Kotlin helper stage and stopped at Java compilation with two missing TON entity/link constants. The follow-up adds both upstream declarations and includes TON addresses in the selectable text entity mask. Full Android build remains unverified.

Build 27 passed Java and failed in the old WebRTC candidate.h setter: Clang 21 rejects a lifetimebound attribute on a void-returning function. The next build pins the official WebRTC commit 7b03082ff07aa442bcbb09ea54b8c33b4fef7e6d used by current TGX; its setter removes that invalid annotation.

Side-by-side installation: configure.py now sets ua.swiryyyyx.client.test, app.name=swiryyyyX Test and app.experimental=true. The original ua.swiryyyyx.client application stays separate. App storage, account databases, content providers, sync account type and notification services derive from the new application ID. A fresh Telegram login is required in Test. No Firebase configuration is fabricated or reused under another package name; Firebase push is unavailable for this Test package until its Android app registration is configured.


Gift sheet revision (after build 28):
- Open gifts in a rounded bottom popup over the profile, with dismiss handle, close control and fixed Done button. Scroll content independently on small displays.
- Compact native animated hero; radial collectible backdrop and actual symbol; grouped property table and independent rarity badges.
- Hide/show, transfer and Stars sale action tiles. Server cooldown dates explain disabled actions. Copy collectible link without routing into an unsupported internal-link handler.
- Gift payment flows belong to the profile: dismiss the sheet before opening a recipient picker or price dialog, without destroying the payment flow. Profile destruction cleans the popup and both flows.
- Save state revision prevents a stale gift read from overwriting a completed profile-visibility change. Initial read has a 30s timeout.
- Compact square gallery cells and consistent regular-gift panels; grid uses still frames, only the opened gift animates.
Validation: local regression/API payment checks and Java syntax/resources pass; Android CI and device visual checks pending. This is a custom native TGX sheet, not a full port of Telegram Android gifts.

Tab crash hotfix: rebuild metrics on insertion/removal, clamp selection, retain an owned list, recover stale width metrics in onMeasure. Regression executes the real methods for the reported 1244 -> 901 crash, empty lists and 200 tab changes. Included in stable and Test patches.
