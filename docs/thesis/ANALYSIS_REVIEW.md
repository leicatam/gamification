# Data-Analysis Review — Stage 2 & Stage 3 (V6 revision)

**Data reviewed:** `FRA_Raw_Data_N30.xlsx` (Stage 2), `FRA_32_Data_set_updated.docx`
(dataset legend), `Stage3_Data_Logbook_120cases.xlsx` (Stage 3).
**Output:** `Tam_V6_EngD_Thesis_Final_Revision_Draft.docx`.

## 1. Verdict on the Cox / Kaplan-Meier approach

**The author's instinct is correct: the survival framing must go.** The Stage-2
archive holds one row per participant — gender, age, pre/post FRA index,
symptoms, cycle count, self-reported change, satisfaction, verification — and
**no dates or timestamps of any kind**. Cox regression and Kaplan-Meier
estimation both require an observed time-to-event variable; none exists here.
This also resolves the anomaly found in the V5 review: the reported
HR = 3.24 (95% CI 1.89–5.56) was statistically impossible for N = 30, and it is
now clear why — it could not have been computed from this dataset. All survival
language (HR, KM, hazard) has been withdrawn from the Abstract, §5.1 (H1),
§5.5, §6.10, Table 6.5, §8.3 and Chapter 9.

## 2. What the raw data reproduce — and what they don't

Reproduced exactly from the archive (thesis values confirmed):

| Claim | Archive result |
|---|---|
| N = 30 elderly (+2 younger controls, ages 36/53) | ✔ 32 rows, 30 elderly |
| Age 71.1 ± 5.9, range 62–84; 17 F / 13 M | ✔ |
| 21/30 low engagement (≤3 cycles); 8 single-session; 9 sustained | ✔ |
| Completers 42.0 ± 8.3 → 48.9 ± 9.4; paired d_z = 2.22 | ✔ (exact 95% CI 0.95–3.46) |

Not reproducible — corrected or flagged:

- **Pooled d = 0.78 and zero-imputation d = 0.57** — do not reproduce. All 30
  participants have real pre/post values (no imputation was ever needed). The
  true all-30 paired change is **+4.0 points (95% CI 0.5–7.6; d_z = 0.42,
  95% CI 0.05–0.79; t(29) = 2.31, p = .028; Wilcoxon p = .015)**. Withdrawn and
  replaced.
- **Motivational-orientation OR = 31.5 (Table 5.3)** — no orientation variable
  exists in the archive. Flagged: supply the coding records or withdraw.
- **18.4-hour median to disengagement (§5.8)** — no timestamps; removed.

New reproducible findings added to §5.5:

- Satisfaction is strongly associated with sustained engagement: 9/9 sustained
  participants satisfied vs 11/21 low-engagement (Fisher's exact p = .013).
- Self-reported improvement 18/30 (60.0%); association with engagement in the
  same direction but not significant (7/9 vs 11/21, p = .25).
- Sustained-vs-low index-change difference (+6.9 vs +2.8) is **not** reliable
  (Welch p = .13; Mann-Whitney p = .051) — the "improvement concentrated in
  completers" claim is weakened accordingly.
- The archived form of the paradox: among 8 single-session participants, 5
  recorded a positive index change, only 2 reported improvement, none returned.
- Neither gender (p = .69) nor age (ρ = −0.18, p = .34) predicted cycles.
- Excluding the one unverified record changes nothing.

## 3. ⚠ Critical open question: FRA index direction

The dataset legend states: *"FRA index: lower number is higher performer;
higher number is lower performer."* If that is correct, the recorded increases
(+6.9 among completers) indicate **deterioration**, and the thesis narrative —
including the objective-score-improvement/non-return paradox — inverts. If the
legend is mistaken (higher = better, as the thesis assumes), the narrative
stands. This cannot be decided from the data; a highlighted placeholder in
§5.5 asks the author to confirm the convention against the InBody
documentation. **This is the single most consequential item to resolve.**

## 4. Verdict on QFD

QFD is the right tool for the right job — and the wrong tool for the job it
was suggested to replace. It is a requirements-translation method (voice of
the user → technical characteristics), not a statistical model, so it cannot
substitute for hypothesis testing. The V6 revision implements it accordingly:

- §3.2 now names the QFD pipeline (Akao, 1990; Chan & Wu, 2002) as the bridge
  from evidence to design, explicitly complementing the statistics.
- New §5.5A presents the pipeline and **Table 5.4**, a QFD deployment matrix:
  six user needs (each anchored to a specific archived finding and a
  TAM/STAM/Octalysis construct) mapped onto five game features (adaptive
  difficulty, loss-free states, trajectory display, coin loop, coaching) with
  ●/◐ relationship strengths. Each cell is a testable claim for the next
  evaluation cycle.
- The author's four limitations (small sample/diversity, short-term
  evaluation, measurement constraints, feedback/survey bias) are written into
  §5.9 and bound the QFD claims.

## 5. Stage 3: the logbook is empty

`Stage3_Data_Logbook_120cases.xlsx` contains the full field structure
(Participants, Game Telemetry ×5 sessions, Q4 Responses, Outcomes, Aggregates
for IDs 3001–3120) but **no entered records**. The Chapter 6 results (65.2%
return, 6.7% non-return, 71.7% endorsement, 63.3% intention) therefore cannot
yet be reproduced from an archive. A placeholder in §6.4 and Appendix G item
G.3 marks the Stage-3 claims as unverified until the logbook is populated.

## 6. Figures

- **Figure 5.4** is no longer a Kaplan-Meier plot. It is now a real,
  embedded participant-level pre/post slope chart (30 participants, by
  engagement group) generated from the archive — exactly the participant-level
  plot the examiner review required.
- Figure 6.1 remains the chart regenerated from Table 6.2 (V5).

## 7. Remaining author inputs after this pass

1. **FRA index direction convention** (§5.5) — decides the interpretation.
2. Motivational-orientation coding records, or withdraw Table 5.3 / OR = 31.5.
3. Populate the Stage-3 logbook (unlocks all of Chapter 6).
4. Session-level telemetry with timestamps, if it exists (would allow the
   temporal analysis the thesis originally wanted; otherwise §8.9 records that
   it was not retained).
5. The V5 items unchanged: ethics number, instruments, codebook, photographs.
