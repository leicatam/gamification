# V15 Validation Addendum — verification of the V14 Change Record and the v13→v14 Correction Schedule

Prepared 19 July 2026, against `Full_version_V14_EngD_Thesis_Submission_Draft.docx`
(uploaded) and `Full_version_V15_EngD_Thesis_Submission_Draft.docx` (current).

## A. Change Record claims — independently verified

| Claim | Result |
|---|---|
| V14 built from v12, body text identical | CONFIRMED (independent full-text diff) |
| 1,455 paragraphs | CONFIRMED exactly (970 body + 485 table-cell) |
| ~41,742 words | CONFIRMED (~41.9k by token count; counting-method difference) |
| Rebuilt figures present: 29.3 pp ×12, 85.4% ×6, 56.1% ×7, 39.0% ×3, 14.6% ×4 | CONFIRMED — exact match with independent count |
| Stale figures (35.6 / 86.7 / 51.1 / 71.4 / 17.5 / 95.0 / 35-40-45): 0 occurrences | **FAILED in one spot** — §3.2 still read "0 of 35 younger versus 16 of 45 older"; the sweep patterns did not catch the phrase form. Fixed at V15 ("0 of 38 … 16 of 41"). |
| No decimal "13.3" as a result | CONFIRMED (0 occurrences; the citation is "13(3)", not "13.3") |
| Figures 6.1/6.3 are the v12-generation images | CONFIRMED by MD5: embedded image24.png ≡ figure_6_1_v12.png, image25.png ≡ figure_6_3_v12.png |
| "One visual check required" (Fig 6.1 = 38/41/41; Fig 6.3 = 85.4 vs 56.1, 29.3 pp) | **CLOSED** — both images visually inspected 19 Jul 2026; values correct |
| Appendix G.4–G.7 placeholders exist; title page reads "June 2026" | CONFIRMED (submission month still to be decided by author) |
| v13 Drive parts superseded | CONFIRMED and endorsed — they also carry withdrawn statistics (Cox HR 3.24 with CI 1.89–5.56, Table 5.3 odds ratio), not only pre-rebuild figures |
| §8.9 data-loss disclosure "Present" | Was present in V14; **SUPERSEDED at V15** — see C below |
| "2.1 times" intention-ratio family confirmed | Vacuous for V14 — the phrase family exists only in the v13 lineage (0 occurrences in V14/V15); arithmetic itself is correct (56.1/26.7 = 2.1) |

## B. Correction Schedule (v13→v14) — arithmetic audit of all 22 edits

Every number recomputed from the outcome counts (which are unchanged:
dropouts 23 = 0+7+16, returns 15 = 0+5+10, permanent 8 = 0+2+6,
endorsement 86, intention 76 = 25+28+23):

- Band sizes 38 + 41 + 41 = 120 ✓
- Dropout: 0/38 = 0.0%, 7/41 = 17.1%, 16/41 = 39.0% ✓
- Permanent non-return: 0/38 = 0.0%, 2/41 = 4.9%, 6/41 = 14.6% ✓
- Retention: 100.0%, 39/41 = 95.1%, 35/41 = 85.4% ✓
- Intention: 25/38 = 65.8%, 28/41 = 68.3%, 23/41 = 56.1% ✓
- Commitment gap: 85.4 − 56.1 = 29.3 pp ✓
- Ratios: 56.1/26.7 = 2.1 ✓; 71.7/26.7 = 2.7 and 63.3/26.7 = 2.4 ✓
- "Do NOT change" list: 19.2% (23/120), 12.5% (15/120), 6.7% (8/120),
  93.3% (112/120), 65.2% (15/23), 62.5% (10/16), 71.7% (86/120),
  63.3% (76/120), 100.0% ✓ all correct
- Tests at the new denominators: Fisher 0/38 vs 16/41 p ≈ 5.8×10⁻⁶
  (reported "p < 0.0001" ✓); chi-square across bands 19.56, p ≈ 6×10⁻⁵
  (reported "p < 0.001" ✓); Wilson CIs 6/41: 6.9–28.4%, 23/41: 41.0–70.1% ✓
- The warning that two different figures both read "35.6" in v13 (gap in pp
  vs 65–80 dropout %) is correct and important ✓

Verdict: the schedule's 22-item cascade is arithmetically correct and
complete for the v13 lineage, with one exception (C.1).

## C. Items in these records now SUPERSEDED by the author's V15 correction

1. **Correction Schedule Edit 18** ("Data-loss statement" for §8.9) must NOT
   be applied anywhere. Per the author (19 Jul 2026): Stage-3 data was well
   collected; preliminary aggregates were released and reported; the full
   participant-level analysis is in progress. V15 carries this framing in all
   six locations; no data-loss statement remains in the thesis.
2. Change Record check row "§8.9 data-loss disclosure Present" — historic
   for V14, no longer true of V15 (by design).
3. Change Record item "Stage3_Data_Logbook_120cases_with_Reconciliation_v2.xlsx —
   Published_Summary corrected to the rebuilt register": **caution.** The
   Published_Summary sheet is a verbatim transcription of Paper 3 and must
   keep the printed 35/40/45 with a dated reconciliation note (as in the
   repository copy); silently "correcting" a verbatim transcription would
   misrepresent the published record. Use the repository logbook as
   authoritative and discard or align any `_v2` copy.

## D. Ground-truth caveat on 38 / 41 / 41

Everything above verifies internal consistency, not provenance. 38/41/41
rests on the author's register; the published Paper 3 (Table 1) printed
35/40/45. Final verification is mechanical: when the participant-level
transcription from the primary records is complete, the Reconciliation
sheet must show MATCH on all indicators, including the three band counts.
A brief corrigendum note to the journal for Paper 3 remains advisable.
