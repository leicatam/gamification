# Stage-2 records — as-received archive

## FRA_32_Data_set_updated (received 5 Sep 2026)

32-row participant table: Gender, Age, Before/After index, Fall Risk
symptoms, Game Cycle, Symptoms improvement, Satisfaction, Verified.

### Reconciliation against the thesis record (V38) — PASS

The 32 rows = 30 study participants + 2 CONTROL rows (M 36 and F 53,
"Control" in the symptoms column — the development/control persons,
cycles 4 and 5). With controls excluded, every thesis headline
number reproduces exactly:

| Quantity | This record | Thesis |
|---|---|---|
| Study N / ages | 30 / 62–84 | 30 / 62–84 ✓ |
| Sustained (≥4 cycles) | 9 | 9 ✓ |
| Low engagement (≤3) | 21 | 21 ✓ |
| Single-session exits | 8 | 8 ✓ |
| Mean index change, all 30 | +4.0 | +4.0 ✓ |
| Mean change, sustained | +6.9 | +6.9 ✓ |
| Mean change, low | +2.8 | +2.8 ✓ |
| Satisfied/very satisfied | 20/30 | 20/30 ✓ |
| Sustained satisfied | 9/9 | 9/9 ✓ |
| Low-engagement satisfied | 11/21 | 11/21 ✓ |

The "more than 9 sustained" reading counts the two control rows
(≥4-cycle rows total 11 including controls; study cohort exactly 9).

### Open items from this record

1. MINOR ROUNDING DISCREPANCY: Figure 5.4's caption group means for
   the low-engagement group (44.8 → 47.6) versus this table
   (44.71 → 47.52). Reconcile against the archived CSV (G.2) — one
   cell may differ between the Word table and the CSV, or the caption
   rounded from different source values.
2. ONE ROW Verified = "No" (F, 72, 1 cycle, Dissatisfied). The
   verification meaning and the handling of this row must be stated
   in the source-to-result manifest (G.0).
3. CONTROL ROWS mixed into the participant table: for any appendix
   use, the two control rows must be separated and labelled — control
   persons are not study participants, and the control person's
   consent record is a separate pending item (G.8).
4. The Before/After columns are per-participant pre/post index values
   — the record the examiner's point 5 asks about. The MEASUREMENT
   TIMING account (when the post-value was taken, esp. for the 8
   single-session participants who never returned to play) still
   needs the author's statement for §5.5.
5. Provenance wrapper for this file itself: author to state source
   (facility records? compiled when? by whom?) for the manifest row.
