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
