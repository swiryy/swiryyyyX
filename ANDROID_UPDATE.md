# Android Test: message bubbles, Saved shortcut and folder transfer

This update targets the separate **swiryyyyX Test** application (`ua.swiryyyyx.client.test`). Stable and iOS source files are unchanged. TDLib stays pinned to the Test #37 bundle. Test #37 completed successfully, but its appearance and folder transfer did not satisfy device testing.

## Corrections

- Message presentation now migrates once to the bubble layout, including channels, with outgoing messages on the right. The new migration also applies over the classic mode forced by Test #37. Later manual appearance choices are preserved. This uses the existing Telegram X bubble renderer; it is not a full port of Telegram Android UI.
- Saved Messages is prioritised in every forwarding picker folder. Folder recipient review adds a visible Saved shortcut at the first position, without selecting it or changing the reviewed recipient snapshot. Hidden Saved chats stay excluded.
- Duplicate source-list add events now update an existing row instead of inserting it twice and potentially failing during sorted insertion.
- Folder transfer now detects automatic include/exclude filters, which Telegram does not support in shared folder links. A reviewed static copy is offered with only public supergroups/channels and private supergroups/channels where the source account can manage invite links. The source folder is not edited. Basic groups and private conversations are excluded rather than converted.
- Large copies are divided into manually chosen parts using the current account folder limit. Each part requires review and confirmation; creating a copy uses a folder slot. Server membership, invite and folder limits remain enforced.
- Copy creation has a duplicate-request guard, timeout and late-callback protection. Uncertain completion explicitly asks the user to check existing folders before retrying. No automatic retries or actual account changes are performed by the tests.
- Import setup displays the selected account and reports sign-in problems, server errors and timeouts. The last generated link can be reopened within the same screen without creating another link. The native Telegram X bottom sheet is opened with its own show method rather than ordinary page navigation; joining still requires separate confirmation.

## Validation and limits

Local checks exercise the actual presentation migration, the real picker display method, duplicate chat-list events, cold folder metadata, filter routing, account-limit partitioning, copy request cancellation/timeouts and server-limit errors. Existing inbox, hidden-chat, tab-width and gift checks are retained in CI.

No live folders were created and no groups were joined or left during tests. Real-device appearance and cross-account import still require testing with the produced APK. The new Android build is checked in GitHub Actions, including the separate Test package identity.

Scheduled and bulk delivery logic is not modified or claimed to be verified by this change.
