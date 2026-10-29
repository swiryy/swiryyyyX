# Android Test update — 29 October 2026

Package remains ua.swiryyyyx.client.test (swiryyyyX Test), installed alongside the stable client.

- Settings → Неактивні групи й канали: joined channels and supergroups ordered by last message, with date and seven-day activity. Manual batches of 20 sample up to 100 messages per chat. ≥ is an incomplete lower bound; unknown data never appears as zero. Leave requires explicit confirmation. No automatic exits or history deletion. Server membership limits are unchanged.
- Compact mentions/replies cards with sender avatars, local unseen filter and direct message navigation. Excludes Telegram bots, inline-bot messages and non-personal mentions. Long press hides an author locally. Ordinary-account spam cannot reliably be identified as a bot. Old records without sender metadata stay saved but do not appear in the people filter; refresh imports recent unread mentions.
- One-time per-account migration to native bubble rendering in channels; later manual presentation choices are preserved.
- Startup discovery is limited to two main-list pages and one archive page with an existing priority index, eight/two on first discovery. Cached personal-chat restoration remains. Does not preload histories or falsely dismiss network Updating state.
- Fixes previous build #34 compilation: Worker stop(int) name collision and cross-package TDLib job reference access.
- Existing hide chats, folder order, forwarding options, gift flows and Android periodic forwarding are retained. iOS files unchanged.

Local validation: generated pinned TDLib policy checks, inbox v1 migration and metadata persistence, activity estimate bounds, production startup/presentation method harness, existing visibility/folder checks, Java syntax and XML resources. Android compilation and phone rendering still require CI/device verification. No real sends, purchases or group exits were performed during checks.
