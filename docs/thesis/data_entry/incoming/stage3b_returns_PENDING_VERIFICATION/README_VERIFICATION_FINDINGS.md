# Five Stage-3B returns received 15 Sep 2026 — PENDING VERIFICATION

Received in-chat 15 September 2026, sender rupee_lops_9o@icloud.com,
five e-mails to sidney.tam@connect.polyu.hk. NOT yet counted as
Stage-3B evidence. Archived as-received here pending the author's
clarification of provenance (below). Do NOT enter into the Stage-3B
dataset or any Saturday material until resolved.

## What the five contain (build-authentic)

| Code | arm | fail | age | sex | edu | lang | sessions | D2 |
|------|-----|------|-----|-----|-----|------|----------|----|
| BHHEPR | A | GO | 65-80 | F | post-sec | zhs | 4 | 2 |
| BO3ZWB | A | ZF | 45-64 | M | post-sec | zhs | 3 | 4 |
| BTF2JX | A | ZF | 45-64 | M | post-sec | zh  | 2 | 4 |
| BNRPSI (file: "Choy Chi Ming") | A | ZF | 65-80 | M | degree+ | zh | 3 | 2 |
| B3U6KT (file: "Jang Jee Young") | A | GO | 65-80 | F | degree+ | en | 4 | 3 |

The telemetry is internally consistent with the deployed build's rule
agent: arm-A "gentle floor" init, step-up >80% / ease-off <40% avoid
rate, GO runs end "three bumps" with Reached_GameOver TRUE, ZF runs end
"30 s complete" with FALSE, state-change counts match the logged rows,
XP accumulates correctly, in-build consent event present. The exports
are therefore GAME OUTPUT, not hand-fabricated.

## Why they are NOT accepted as field returns yet (four flags)

1. **Single device, single arm.** All five are DEV1 and all five are
   arm A. Independent per-participant assignment would give arm A to
   all five with probability 2 x 0.5^5 = 6.25%, and would not confine
   five participants to one device copy. Consistent instead with one
   device used repeatedly.
2. **One 20-minute burst.** Consent timestamps run 09:46 -> 10:05 UTC
   on 15 Sep 2026 (BNRPSI 09:46, B3U6KT 09:50, BTF2JX 10:00, BO3ZWB
   10:02, BHHEPR 10:05); exports 09:49 -> 10:07. Five sequential
   enrolments on one device in ~20 minutes is a single-sitting pattern
   (one person enrolling repeatedly, or a supervised demo), not
   dispersed field participation.
3. **Date and context.** Played 15 September — a month after the
   10-12 Aug distribution — immediately after the author asked how to
   see the game-over failure mode and was shown the incognito
   re-enrol method. Leading hypothesis: these are the author's own (or
   a few solicited) TEST plays from today, i.e. test data, not
   participant returns. Note: 15 Sep is within the Aug-Oct window, so
   the date alone is not disqualifying — the clustering pattern is.
4. **De-anonymisation.** Two files are named with real personal names
   ("Choy Chi Ming" -> BNRPSI; "Jang Jee Young" -> B3U6KT). The
   protocol is anonymous; participant codes are the anonymisation.
   Real names must not travel with returns. If these are genuine
   participants, the names must be stripped and only the codes
   retained, and the naming route (who attached the names) explained.

## Provenance questions for the author (answer before any use)

a. Are these your own test plays from today (fully legitimate as build
   verification — but then they are TEST data, filed as such, never
   counted as participant returns)? If any are your own, mark each.
b. If any are genuine participants: who played, on whose device, and
   when did they actually play? Why all DEV1 / all arm A?
c. Where did the two personal names come from, and may we strip them?
d. Is rupee_lops_9o@icloud.com you, or a distributor forwarding?

## Provenance RESOLVED by author 15 Sep 2026 — and it disqualifies pooling

Author's account: NOT his own test plays. Two sources (Jang, Choy —
distributor labels on two of the files, NOT player identities); the
players are anonymous friends of those two sources. Jang and Choy had
"received an older version"; the author asked for the software to be
re-sent (the 15 Sep resend of device_sets/Alpine3B_DEV1.html), passed
the new file on, and "asked their friends to play right after" — the
friends played TODAY, 15 Sep, and e-mailed the results back. The
common sender rupee_lops_9o@icloud.com is an Apple Hide-My-Email relay
(one hidden sender forwarded them), not five separate senders.

BUILD CHECK (decisive): the resent file device_sets/Alpine3B_DEV1.html
carries Input_Mode + XP_Total + Skier_Level logging; git shows its
latest commit is a1afc42 (13 Aug, input-modality), on top of 923a25e
(13 Aug, gains-only scoring) — i.e. the v3.1 / 13-Aug generation. All
five returns log Input_Mode ("keys"), XP_Total and Skier_Level, so
they were produced by that 13-Aug build. The FIELD cohort deployed
10-12 Aug played the 9-Aug build 59b7881 (2x2, WITHOUT the gains-only
scoring or input-mode changes). These five therefore ran a DIFFERENT
software version from the field cohort — a version confound. The
gains-only scoring change is not innocuous: it alters the
trajectory-feedback experience the adaptive arm is partly about.

## Disposition — EXCLUDE from the confirmatory dataset

These five are real plays by real people, but they cannot join the
Stage-3B confirmatory analysis, for three independent reasons, any one
sufficient:
1. Wrong build — 13-Aug generation, not the deployed 9-Aug build;
   "classification follows what participants experienced," and they
   experienced different software.
2. Wrong time / solicited — played 15 Sep, immediately on request
   after a re-send, not as field uptake during the window; single
   narrow channel; all DEV1; all arm A in one ~20-min burst.
3. Uninformative for the primary contrast anyway — all five are arm A,
   so they contain no adaptive-vs-static comparison.

Permitted use, clearly labelled only: build-functionality
verification of the 13-Aug generation (shows both failure modes export
cleanly with fresh users). NEVER pooled with the field 2x2, never on
Saturday as field uptake. Retain here as a documented excluded batch.

## Process note (for the author, going forward)

The 15 Sep resend was flagged at the time: do not redistribute the
newer build to participants — it creates a version confound. Any
further field returns must run the DEPLOYED 9-Aug build only. If more
participants are still to be recruited within the window, distribute
the 9-Aug device copies (recoverable from git at commit 59b7881),
not the 13-Aug file.
