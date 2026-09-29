# Stage 3B Pro v4.1 — raw exports as received (29 September 2026)

Five Pro v4.1 exports supplied by the author on 29 September 2026 (09:22 UTC), archived
unchanged; SHA-256 in `CHECKSUMS_as_received_2026-09-29.txt`. They are the first raw Pro
exports deposited in this repository: the Batch 01 folder (26 September) holds only the two
author-supplied PDF reports, whose README lists the raw exports as "not yet deposited".

| File | Code | Exported (UTC) | Runs | Visits | Decisions | Feedback (answered/skipped) | Prior play |
|---|---|---|---|---|---|---|---|
| Alpine3BPRO_PRO-SELF_P8P2Z9_v4_202609200321.json | P8P2Z9 | 2026-09-20 03:21 | 18 | 4 | 6 | 6 / 3 | yes |
| Alpine3BPRO_PRO-SELF_PFWU9V_v1_202609191030.csv | PFWU9V | 2026-09-19 10:30 | 6 | 1 | 2 | 2 / 1 | yes |
| Alpine3BPRO_PRO-SELF_PU5K58_v1_202609191608.json | PU5K58 | 2026-09-19 16:08 | 1 | 1 | 0 | 0 / 0 | yes |
| Alpine3BPRO_PRO-SELF_PU5K58_v2_202609191732.json | PU5K58 | 2026-09-19 17:32 | 2 | 2 | 0 | 0 / 0 | yes |
| Alpine3BPRO_PRO-SELF_PU5K58_v3_202609191735.json | PU5K58 | 2026-09-19 17:35 | 5 | 3 | 0 | 0 / 1 | yes |

The three PU5K58 files are cumulative exports of one browser state (v3 contains v1 and v2).
Run appearances across the five files: 32; distinct Run_IDs: 29 (P8P2Z9 18, PFWU9V 6,
PU5K58 5). By stage: 13 practice, 5 warm-ups, 11 fixed-course checks. All runs record touch
input. P8P2Z9 visit 4 (four runs) is stamped build v4.1.1 "change_player"; all other runs v4.1.

## Software metadata common to all five files

`data_kind = researcher-self-test`, `device_id = PRO-SELF`, consent event `mode = self-test`,
`participantApproved = false`, `ethicsReference = null`, `cloudConfigured = false`,
`Decision_Provider = local-rules` or none, `Jev_Model` empty. The software therefore records
every file as a researcher self-test with no participant release and no external-model call.
Any statement that a code belonged to a volunteer rests on the author's account, not on the
export (Paper 3 R8 already words it that way).

## Reconciliation with Paper 3 R8 (eight exports, four codes)

| R8 statement | Five files on hand | Implied content of the three missing exports |
|---|---|---|
| 8 exports, 4 codes (P8P2Z9, PFWU9V, PU5K58, PXG3R9) | 5 exports, 3 codes | ≥1 export for PXG3R9; 2 further exports |
| 62 run appearances → 34 distinct runs, 11 visits | 32 appearances → 29 distinct, 8 visits | 30 appearances, 5 distinct runs, 3 visits |
| 14 practice / 6 warm-ups / 14 checks | 13 / 5 / 11 | 1 / 1 / 3 |
| 8 decisions, all local rules | 8 (6 + 2 + 0) — matches | 0 |
| 14 feedback: 8 answered, 6 skipped | 13: 8 answered, 5 skipped | 1 skipped |
| prior play: 3 yes, 1 no | 3 yes | PXG3R9 = no |
| all touch input | all touch | — |

Every R8 count that the five files can test is consistent with them; the remainder can only
be attributed to PXG3R9 and to the two unnamed exports. Verification of the 34-run total,
the 11 visits and the third check pair therefore stays open until the missing three files are
deposited.

## Difference from the Batch 01 reports (20 September)

Batch 01 (`../batch01/`) describes TEN exports and FIVE codes: P8P2Z9 (18 runs), PT8FJC (8),
PEVNZ8 (7), PZTPCG (4, keyboard), PU5K58 (5) — 42 runs, 10 decision chains, 5 paired checks.
P8P2Z9 and PU5K58 agree run-for-run with the files here. PFWU9V (visit 10:22–10:30 UTC on
19 September) and PXG3R9 do not appear in Batch 01; PT8FJC, PEVNZ8 and PZTPCG do not appear in
R8's set. Which set is the intended Pro development record is the author's call; the thesis
(V45 Appendix I.5–I.6; §9.12) currently follows Batch 01.

## Still required from the author

1. The three remaining exports named in R8 (at least one for PXG3R9), unaltered.
2. The role behind each stored code (researcher / volunteer), the device, and the consent basis,
   as a dated roster; the software records all of them as self-test.
3. A decision on whether the thesis Appendix I keeps the Batch 01 set or moves to the R8 set.
