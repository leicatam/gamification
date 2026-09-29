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

## Update 29 September 2026 (later) — PXG3R9 received; R8 counts verified

`Alpine3BPRO_PRO-SELF_PXG3R9_v3_202609200352.csv` added (SHA-256 in the checksum file). Build
v4.1.1 "change_player", exported 2026-09-20 03:52 UTC; age band 65-80, F, post-secondary,
prior play "no"; 3 visits, 5 runs (1 practice, 1 warm-up, 3 checks), 0 decisions, 1 skipped
feedback; same self-test metadata as the other files. A second copy of PFWU9V v1 was sent at the
same time; it is byte-identical to the file already held (SHA-256 22fdcd07…), so it is not stored twice.

All six files together reproduce every R8 count that the raw data can test:

| R8 statement | Six files |
|---|---|
| 34 distinct runs | 34 ✓ |
| 11 software visits | 11 ✓ |
| 14 practice / 6 warm-ups / 14 checks | 14 / 6 / 14 ✓ |
| 8 decisions, all local rules | 8 ✓ |
| 14 feedback: 8 answered, 6 skipped | 8 / 6 ✓ |
| prior play: 3 yes, 1 no | 3 / 1 ✓ |
| 3 paired pre/post checks | P8P2Z9 visits 1 and 4, PFWU9V visit 1 ✓ |
| all touch | all touch ✓ |

Only the file count cannot be confirmed: R8 says eight exports and 62 run appearances; six distinct
files hold 37. Because exports are cumulative, the two further files would add only repeats of
runs already counted. Earlier P8P2Z9 exports taken after visit 2 (11 runs) and visit 3 (14 runs)
would give exactly 62, which suggests that is what they were. They change no count in the paper.

Still open: the roster of who held each code (the software labels all four as researcher self-test),
and the choice between this set and the Batch 01 set for thesis Appendix I.

## Author's decision, 29 September 2026

The reported Pro record (thesis Appendix I; Paper 3 R9) is the Batch 01 set: five codes (P8P2Z9, PT8FJC,
PEVNZ8, PZTPCG, PU5K58), 42 runs. PFWU9V and PXG3R9 are archived here as received but lie outside that set.

## Author's decision, 29 September 2026 (later) — count all seven codes

Superseding the note above: the reported Pro record counts all seven codes. The exports were received by
different routes and on different dates, and the Batch 01 reports were written before all had arrived.
Seven-code totals (thesis V47 Appendix I.5; Paper 3 R10): 12 exports, 53 distinct runs, 16 visits
(10 warm-ups, 21 practice, 22 checks), 12 decisions (9 local-rule, 3 player overrides), 21 practice-feedback
records (12 answered, 9 skipped), 6 paired checks across 5 codes. Batch 01 figures come from the reports;
PFWU9V and PXG3R9 figures come from the raw exports here.

## Update 29 September 2026 (later) — PT8FJC and PZTPCG received

`Alpine3BPRO_PRO-SELF_PT8FJC_v1_202609191040.csv` and `Alpine3BPRO_PRO-SELF_PZTPCG_v1_202609191427.csv` added
(SHA-256 in the checksum file). Both reproduce the Batch 01 report exactly:
- PT8FJC: 1 visit, 8 runs (1 W, 1 Pre, 5 P, 1 Post), touch, pair 7043 → 7043m 95% → 100%; 4 decisions whose stored
  offline proposals (easier 1.20→1.08; same 1.30; harder 1.40→1.50; same 1.50) and final sources (player choice ×3,
  local rules ×1) match the report's decision audit; 5 feedback records (4 answered, 1 skipped).
- PZTPCG: 1 visit, 4 runs (W, Pre, P, Post), keyboard input, pair 100% → 100%, no decisions, 1 skipped feedback.
Raw exports are now on file for six of the seven codes; PEVNZ8 (named in the report as share5214078768679196894.csv)
is the only one outstanding. All files carry researcher-self-test metadata.

Author's roster note received the same day: "September 22 - 28 date to play. Data collection is different date."
Not yet reconciled: every export's internal timestamps (consent, run start and end, export) fall on 19–20 September
2026 UTC. The note does not yet say who played under each code.

Resolved 29 September 2026: the author confirms the play dates were 19–20 September 2026, matching the export
timestamps; the earlier "22–28 September" note was a mix-up. The roster of who played under each code is still open.
