# TDLib migration test — 16 October 2026

Base: known-working swiryyyyX build 24, upstream b5f81630f070d1100673029682914ff3672769b0.

Official TGX Java/native bundle verified on 16 October: 1094df0caf4e5b59f6b247f8d9eb8896022cb379.
Underlying TDLib source: c15d3f5a5de6e3ba5839822c451152e5e18bb700.
Main tdlib/td HEAD at verification was a94b83d67ab4c8397c6245e541b31a4131ea2f79, newer than the bundle. This test pins that verified bundle; it does not claim to use the newest core commit.

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

Regular-gift actions revision:
- Upgrade through UpgradeGift, with fresh owned gift/price/balance, explicit confirmation, original sender/message checkbox, prepaid upgrade cost zero, and new confirmation if the quote changes.
- Convert a regular gift through SellGift, using receivedGift.sellStarCount (never the catalog default), an explicit irreversible-operation confirmation, and a fresh conversion-value check before writing.
- A single account write gate now covers purchase, transfer, listing, upgrade and conversion. No automatic financial retry.
- Native gift sharing, original sender/recipient/details, collectible supply, and server-provided regular-gift backgrounds.
- CI now executes core chat, tab mutation, gift purchase/transfer, resale and upgrade/conversion tests before the Android build.
Local tests pass against the pinned Java API. No real purchase, transfer, conversion, upgrade or listing was executed. Full Telegram feature parity is not claimed: collections, gift messages on sending, TON marketplace/export and advanced craft/auction flows are still pending.


24 October revision — mentions and peer profiles:
- Settings > Mentions and replies: a compact local inbox showing group name, sender, time and message preview. Tapping opens that exact message. New Telegram-confirmed mentions/replies are collected from live updates without full-history scans.
- Store up to 500 recent entries per account; persist across restart, deduplicate, update edited text and remove deleted messages. Hidden chats are excluded from the inbox. Viewing the list does not mark Telegram chats read.
- Manual Refresh imports up to 20 unread mentions/replies per group from main/archive chat metadata, one request at a time; errors stop the refresh and timeouts release it. This is not a complete historical search. An account must remain a member to receive future group updates.
- Other users' profile pages now expose their visible gifts. Foreign receipts do not expose own-gift hide, transfer, upgrade, conversion or sale controls; no other user's Stars balance is requested.
- Account information displays only Telegram-provided registration month/year and phone-number country when available. It does not infer creation location or estimate dates from IDs.
- Profile tab removal now removes the actual indexed tab rather than always deleting the last tab, in addition to the existing width-cache crash fix.
Validation: core mention persistence/account isolation/edit/delete/dedup/latest-500/concurrency tests and existing chat/gift checks passed locally. Full Android compile and real-device checks are pending for this revision. Real financial actions were not executed.

A newer ready-made TGX TDLib bundle was verified on 24 October: 7ec241d026ee3563e615c25a700117c2abbaea19 (core ea3f69ce11aef458bfbb09869b809ede4447486f). This revision intentionally retains the last compiled 1094df0 bundle; migration of new message/proxy/update API types is still pending. Stars invoice/paid-media checkout and full Telegram gift feature parity are not implemented by this revision.


24 October folder tools revision (after successful build33):
- Android Settings > Folder transfer and schedule. Review all recipient names in a scrollable list before enabling.
- One device-local schedule per account, first run after approximately 30 minutes, repeating every 30 minutes through WorkManager subject to battery/network delays. It fetches the latest standalone Saved Message on each run, even if unchanged. Albums are deliberately unsupported in this first revision. No Stars payment is authorized.
- Recipient snapshot is fixed at user confirmation, at most 1000 groups. Hidden/inaccessible recipients, account changes, server errors, interrupted runs or uncertain delivery pause the schedule. A durable in-flight marker prevents automatic replay after process death. Existing acknowledged forwarding queue, account gate, 200ms gap and server cooldowns are reused. Stop is available at the top of the tools page; logout cancels the schedule.
- Transfer creates a Telegram folder invite only after reviewing eligible supergroups/channels, then offers the other logged-in account's native join preview or sharing to another device. Basic groups are excluded to avoid silently converting them to supergroups. Private chats and restricted groups are not transferred. Telegram chosen-chat/shared-folder limits and rule-based-folder restrictions still apply. This is one-time transfer, not continuous cross-account template synchronization; the latter remains pending.
- Swiftgram iOS baseline selected and pinned separately; preparation script/toolchain requirements and port matrix added. No iOS periodic scheduler. The full iOS port/IPA requires macOS/Xcode and has not been built in this Linux workspace.
Validation: actual Android worker compiles against pinned TdApi and passes simulated 230-group scheduling, first delay, free forwarding, interruption recovery, hidden/account/album guards, server-error pause, stop and stale-worker isolation. Existing sender/task delivery tests and core syntax/resources pass. Android full CI/device testing pending for this revision. No real messages were sent by tests.
