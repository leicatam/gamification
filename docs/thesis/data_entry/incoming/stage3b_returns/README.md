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
