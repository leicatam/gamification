# Validation record — v4.1 self-test

Prepared 19 September 2026. Runtime: Node.js 24.19.0. All test examples are synthetic software fixtures. No learner outcomes or real Jev responses were collected.

## Completed checks

`npm test`: **29 passed, 0 failed**.

- **19 core checks:** feedback-sensitive local actions, matching-settings history, retained partial runs, upward bounds, request consent and whitelisting, typed Jev response parsing, uncertainty/error handling, credential isolation, policy-copy parity, JavaScript syntax, and local HTTP serving/origin restrictions.
- **10 isolated session checks:** actual HTML script boot and three-language updates; explicit acceptance before a run starts; no inference without opt-in; consented request filtering and audit export; uncertain/malformed fallback; cancellation and late-response rejection; simulated request timeout; fresh opt-in after reload; interruption recovery and previous-version storage preservation; configured-service labelling.
- The session harness uses the actual inline script with **stubbed DOM, canvas, audio, animation and timers**. It checks state transitions and callbacks. It cannot establish rendering quality, accessibility, input usability or browser compatibility.
- The fixed-course generator and warm-up staircase were compared directly with the supplied v4.0 file and are byte-for-byte unchanged in those source regions. Failure mode remains `GO`; participant release remains disabled.
- The local server was started without credentials and reported offline operation. Automated HTTP checks fetched the actual game and health endpoint and verified that source/configuration files are not served.

Source-region SHA-256 values, shared by the supplied and upgraded files:

| Region | SHA-256 |
|---|---|
| Fixed-course generator and schedule | `e63218dbe78bf0b16fbf05cfa25955145cd50daf625aac541639c32b696e8de7` |
| Warm-up staircase | `764da2d32897136b5e607aa2ff88e8cc7e7eca32d8312f7c20c0b551e3d168ef` |

Supplied v4.0 file SHA-256: `b1bbf026e22f3d73fa9c759573a990917d113ec584692c80a40113773192d96f`.

## Outstanding checks

- **Live Jev:** no TypeSafe API key was available. Endpoint/schema integration follows the current official documentation, but account authentication, live model availability, latency, costs and recommendation quality have not been verified. `npm run check-jev` provides a synthetic connectivity check after configuring a key locally.
- **Real browser/device:** a local Chromium download timed out, and the available cloud browser blocked opening the local game under its file-access policy. No browser screenshots or end-to-end visual passes are claimed.
- **Human effectiveness:** the rules and confidence thresholds are provisional. No evidence yet establishes that these changes improve intrinsic motivation, useful persistence, skill retention or transfer.

## Focused device check before use

1. Open the game on the intended browser/device. Check English, Traditional Chinese and Simplified Chinese; confirm that all feedback and plan controls remain readable and reachable.
2. Complete the warm-up and fixed-course check, then play a practice run. Check keyboard/touch input, the practice cue, pause/resume and finishing early.
3. Report boredom and inspect the offered focus; explicitly accept or change it. Confirm the next run uses the displayed settings. Try a frustration report and a pause choice separately.
4. If using Jev, configure the included local server, run the synthetic connectivity check, and explicitly opt in after a practice run. Check the recorded model/source in Research tools. Stop the session while a request is pending and confirm it stays stopped.
5. Export JSON and CSV. Confirm the run, player report, decision source, chosen action and applied settings correspond to the observed session. Keep this self-test data separate from any participant dataset.

For effectiveness evaluation, compare Jev and offline proposals using the same available information and local bounds, then measure voluntary participation and player experience separately from fixed-course performance and delayed retention. Software tests and model confidence do not establish learning benefit.
