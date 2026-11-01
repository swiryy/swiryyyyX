# Android Test: replies, folders and stable chat order

This update remains the separate `ua.swiryyyyx.client.test` application, labelled **swiryyyyX Test**. Stable installation and iOS code are preserved. TDLib is unchanged from Test #35.

## Changes

- Restore classic message presentation with sender avatars/names. Applied once per account; later appearance choices remain available.
- Inactive groups/channels: tap to select, add the next 50 repeatedly, review the rows, then confirm leaving the selected chats. Requests run sequentially; stop, timeout and server errors halt the remaining queue. Chat history is not deleted.
- Replies inbox: fetch the original message and verify that its sender is your account. Plain mentions, bot senders, inline-bot messages and legacy unverified entries are excluded. Hidden-chat and ignored-author filters remain. Replies whose original message is unavailable cannot be verified and are omitted. Manual refresh checks up to 20 unread mention/reply candidates per group; it is not a complete historical search.
- Folder forwarding: explicit folder IDs are loaded directly, with missing chat metadata resolved in up to eight parallel requests. Remove the full-info request for every supergroup before showing recipients. Rule-based folder membership still comes from paged TDLib loading. Fresh source-message properties and send-time error handling remain.
- Folder transfer: load complete membership before asking Telegram for invite eligibility, then hydrate eligible chat metadata before review, including a cold cache. Transfer is still limited to chats Telegram allows in a shared folder; private chats, inaccessible groups, permissions and account limits cannot be bypassed.
- Folder/schedule tools: dedicated configure, review, confirm, cancel and pause controls, Ukrainian status text and recipient review. Android schedules remain approximately every 30 minutes and can be delayed by the OS.
- Saved Messages sorts first when present in the current list and allowed by its filter. Existing Saved chat metadata is requested at startup without loading its history or changing Telegram pins.
- Fixed order defaults across main list, archive and folders. Manual activity sorting estimates recent activity from up to 100 messages over seven days, then saves that order locally. New messages do not reshuffle it; new chats append. Hidden chats remain excluded.

## Validation

Production-code JVM checks cover 400 cold-cache folder recipients, rule-based pagination, cancellation, timeout and account isolation; 130 selected chat exits with no live network operations; stop-on-error and request spacing; Saved-first and persistent ordering; verified reply policy; presentation migration; existing queue, worker, gift and tab-width regressions. Java syntax and XML parsing are checked locally. The Android build and package identity are verified in GitHub Actions. Device testing is still required for appearance and startup latency.
