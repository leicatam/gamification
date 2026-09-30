# Stage 3B returns — as-received archive

Same admission discipline as the Stage-3 pipeline: files kept
byte-for-byte as received; content checks can only disqualify;
admission is by provenance. Stage 3B additionally records the BUILD
FORMAT VERSION per return (see version-drift note below).

## Return 1 — B9V8YA (received 15 Aug 2026)

**File:** `Return_B9V8YA_Huang_Renee_email_2026-08-15.pdf` (e-mail
print, as received)

| Check | Result |
|---|---|
| Provenance | Direct e-mail from participant (Renee Huang, renee_nz@163.com, subject "from Huang") to sidney.tam@connect.polyu.hk — the e-mail itself is the dated transmittal ✓ |
| Identity | Author identifies participant as Huang Renee, 59, F — consistent with enrolment (age_band 45-64, gender F); anonymous code B9V8YA; prior_play "no" (screening ✓) |
| Device / assignment | DEV2 · arm B (static ×0.85) · failure_mode ZF · language zhs — state log consistent with arm B (diff 0.85 throughout, init + 2 bump entries only, no rule-agent steps) ✓ |
| Score arithmetic | 7 coins ×10 + 459 m + 50 goal bonus = 579 = reported ✓ (v3.0 formula) |
| Timeline | consent 08:00:55Z → enrolment 08:01:02Z → run (30 s, goal reached) → questionnaire 08:02:21Z → export 08:03:29Z — coherent single sitting; e-mail timestamp (01:06 local) consistent with a UTC-7 client three minutes after export |
| Session window | 2026-08-15, inside the Aug–Oct 2026 Stage 3B window ✓ |
| Questionnaire | D1=2, D2=1, F1=2, F2=2 (negative responder — recorded as returned) |
| Format version | **v3.0 JSON export (pre-CSV build)** — lacks Combo_Max/Dodges/Coins_Missed/Input_Mode/XP columns; header line garbled in PDF print (encoding), content intact |
| Status | CHECKS PASS — admission pending launch-gate confirmation (see PENDING_ITEMS: Benny protocol sign-off + ethics-scope snapshot check were still open when this return arrived) |

## Version-drift rule (v3.0 JSON vs v3.1 CSV)

The fleet was upgraded on 13 Aug 2026 (CSV export, gains-only scoring
with combo/dodges/XP). Returns will arrive in BOTH formats until every
device copy is replaced. Rules:

1. Both formats are admissible; the logbook records
   `Build_Format` (v3.0-json / v3.1-csv) per participant.
2. **Scores are not comparable across versions** (v3.1 coin values
   carry the combo multiplier). Any score-based analysis uses the
   version-invariant derived score: `Distance_m + Coins×10 +
   50×(goal reached)` — computable from raw fields in both formats.
3. The pre-specified confirmatory outcomes (D2 top-two-box;
   sessions played) do not involve the score and are unaffected.
4. Arm/failure-mode assignment logic is identical across versions.

## Post-cut-off clean-run returns — FROZEN20260915 build (received 29 Sep 2026)

Three CSV exports supplied by the author on 29 September 2026, archived byte-for-byte
(SHA-256 in `CHECKSUMS_FROZEN_returns_2026-09-29.txt`). All three carry the frozen build string
`Alpine_Coordination_Game_v3.1s_Stage3B_FROZEN20260915` and distributor tag D01, and were played
on 29 September 2026, inside the clean-run window (15 Sep – 15 Oct) but AFTER the thesis cut-off of
26 September. Under the 26 September decision they are archived as received and may be reported
only as a dated addendum outside the thesis evidence base. They are the first returns on record
from the frozen build.

| Code | Consent → export (UTC) | Arm | Mode | Age band / sex / education | Prior play | Input | Run | D1 D2 F1 F2 |
|---|---|---|---|---|---|---|---|---|
| BVSU69 | 12:51:23 → 12:52:25 | B static ×0.85 | GO | 45-64 / M / degree+ | yes | touch | 30 s, goal reached, 0 hits | 5 5 5 5 |
| B7GRDA | 14:35:03 → 14:36:25 | B static ×0.85 | GO | 45-64 / M / degree+ | no | touch | 30 s, goal reached, 0 hits | 3 3 3 4 |
| BZ323A | 14:38:01 → 14:40:24 | A adaptive | GO | 45-64 / F / post-secondary | no | touch | 30 s, goal reached, 1 hit | 4 4 3 4 |

Content checks (can only disqualify; none did):
- Build string and D01 tag match the frozen distributor copy D01.
- State logs match the assigned arm: both arm-B files hold 0.85 throughout (init entry only, no
  hits); BZ323A starts at the arm-A gentle floor 0.60 and steps to 0.80 under the rules, matching
  AI_DiffMult 0.8.
- Scores are consistent with the frozen formula (distance + coin score + 5 × dodges + 50 goal
  bonus): implied coin scores 130, 410 and 20 are within the combo-multiplier bounds for 7, 16 and
  1 coins.
- Each is a single coherent sitting of one to two and a half minutes.

Not yet established (provenance is what admits a return):
- Who transmitted each file, by what channel and on what date; the B7GRDA file arrived under a
  phone share-sheet name.
- Who distributed D01 and whether all three played on one device: B7GRDA and BZ323A were consented
  three minutes apart on the same D01 copy.
- All three played ONLY one 30-second session and gave no second visit, so the files carry no
  learning-over-time information. BVSU69 answered prior play "yes".
- Neither of the two ZF-mode cells has a return, so the 2×2 remains empty in two cells.

## Fourth clean-run return — B59AGN (received 30 Sep 2026; played 29 Sep 2026)

`Return_B59AGN_D01_FROZEN_filenamed_xls_as_received_2026-09-30.xls` — a CSV text export saved under an .xls name,
archived byte-for-byte. FROZEN20260915, D01, arm B (static ×0.85), zero-failure mode, 45-64 / M / degree+, prior play
"no"; consent 17:34:32Z; three 30-s sessions (touch, keys, keys), all goal reached; questionnaire complete (D1 3, D2 2,
F1 3, F2 3). Checks pass: arm-B state log 0.85 throughout; session-3 bumps reduce obstacle density with speed unchanged
(zero-failure behaviour); scores reconcile with distance + coin score + 5 × dodges + 50 (implied coin scores 250, 480,
260 within bounds for 9, 18, 11 coins); XP_Total cumulative 794 → 1803 → 2602. First zero-failure and first
multi-session clean-run return. Re-sent copies of BVSU69, B7GRDA and BZ323A on 30 Sep were byte-identical to the
files archived on 29 Sep and are not stored twice.
