# Known limitation — chat-app in-app viewers (NOT a build defect)

## Symptom reported
Opening the game file directly inside WhatsApp / WeChat shows the page
but the language buttons do not respond.

## Cause (verified 16 Sep 2026)
Chat apps open a received .html file in their own built-in
preview/webview, which does not run the interactive page. It is a
limitation of those apps, common to all interactive HTML — not a fault
in this game.

Headless-browser check of the frozen build
(Alpine3B_STUDY_DEV1_FROZEN_2026-09-15.html): the language button
binds and advances to the consent screen, with no JavaScript errors.
The localStorage access is already wrapped in try/catch (loadP3B /
saveP3B), so a storage-blocked context degrades gracefully. The build
is sound.

## Consequence for the freeze
This is NOT a defect, so it does NOT trigger the "restart the window
on a corrected build" rule. No code change is made; the frozen build
stands.

## Fix (behavioural)
The game must be opened in a REAL browser (Safari / Chrome), not inside
WhatsApp/WeChat. Either:
- the helper opens the file in a browser (WeChat/WhatsApp "..." menu ->
  open in browser), once per device; or
- the game is served from a web link (hosted), so a tap opens it in the
  browser directly and it can be added to the home screen as a one-tap
  icon. Hosting removes the file-handling step entirely; the frozen
  build stamp still identifies every return.
