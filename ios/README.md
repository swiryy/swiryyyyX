# swiryyyyX iOS — Swiftgram baseline

User-selected upstream: https://github.com/Swiftgram/Telegram-iOS
Pinned 24 October 2026: cf8b23beaaac4126a396337ac2d5be13f9f76b66 (master).
The pinned versions.json specifies app 12.9.2, Xcode 26.2 and macOS 26. This is a verified source baseline, not a claim that an iOS build or feature port has passed.

On the Mac, run `python3 prepare_mac.py` for a read-only toolchain check; add `--clone` to fetch the pinned baseline. Existing destinations are not overwritten. It does not install Xcode, sign in, change system settings or obtain certificates.

The Android Java/TDLib implementation cannot be copied directly into Swiftgram's TelegramEngine/Swift app. First verify an unmodified simulator build with our own configuration, bundle ID and Telegram app credentials. Never use upstream maintainers' signing repositories, credentials, App Groups, push endpoints or signing profiles. Signing and real iPhone validation require the owner's Apple account on the Mac. Do not commit credentials or session data.

Port order:
1. Independent swiryyyyX identity/configuration; verified login, ordinary chats and upstream gift/payment UI.
2. Account-specific hidden chats, with exclusion from lists, search, unread counters and notifications.
3. Forward Saved Messages to a reviewed folder snapshot; original-sender/caption options; serialized acknowledged delivery and server cooldown handling.
4. Fixed local folder ordering and the bounded mentions/replies inbox with exact-message navigation.
5. Folder transfer via Telegram folder links and native join previews. Links work across Android/iOS, subject to Telegram's limits and invite permissions. Membership, private chats and per-account IDs are not blindly copied.

Scheduled automatic forwarding is Android-only by explicit user request. No iOS recurring scheduler is planned in this revision.

A linked-folder ecosystem that propagates additions is a separate follow-up: it needs durable template identity/revisions and an additions review on each destination account. Creating a one-time invite link is not continuous synchronization. A 230-chat rule-based folder may exceed the chosen-chat/export limits; read actual server limits and report unsupported items rather than silently truncating or bypassing them.

Current state: preparation files only. Native iOS integration, simulator compile, device signing, push setup, feature ports and IPA are pending. Android build33 remains the last verified APK until the next CI run passes.
