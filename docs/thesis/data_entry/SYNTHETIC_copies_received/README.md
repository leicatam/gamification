# Synthetic copies found in the author's records — NOT STUDY DATA

## Stage_3_game_telemetry.xlsx (received 30 September 2026)

Archived as `SYNTHETIC_NOT_STUDY_DATA_Stage_3_game_telemetry_as_received_2026-09-30.xlsx`
(SHA-256 b5d06ab5c259104a49d5d1cec82988bb1a3da6d068870b33d0c9022fdee4cc2a).

The author found this file in his records and asked whether it could serve as the Stage-3A player-level record,
believing it hand-entered. It is a copy of the synthetic pipeline-demonstration data:
- All 569 session rows and all 2,968 state-change rows match `../Stage3_Data_Entry_DEMO_SYNTHETIC.xlsx`, whose
  front sheet reads "THIS COPY IS FILLED WITH SYNTHETIC TEST- DATA (simulation output)".
- Player IDs are TEST-001 to TEST-120 (thesis Appendix G.8 describes the synthetic set by exactly this ID range);
  the study's IDs are 3001–3120.
- Every player has the same recruitment date (3 April 2026); no session ends in a game over; sessions last 4–11
  minutes; the questionnaire has nine items on a 1–7 scale — none of which matches the study record.
- It does not reproduce the study totals (e.g. 95 and 78 "agree" counts against 86 and 76; 71 women against 72).
- File created 12 July 2026; its synthetic label column (Data_Class) is empty, which is why it can be mistaken for
  real data.
Never evidence. Kept only so the same copy is recognised if it resurfaces.

## Two files from research assistant "Rudy", received 1 October 2026 — DERIVED FROM THE SYNTHETIC DATA, NOT STUDY DATA

`DERIVED_FROM_SYNTHETIC_Stage3_Game_Telemetry_Whole_Coins_as_received_2026-10-01.xlsx`
(SHA-256 a5b4db2e311bdb4e0ab1f89db2781181d553d200ce2b5c3d8185dee45d2efa55; workbook creator "Rudy", created 17 Jul 2026, last saved 1 Oct 2026)
- All 569 session rows correspond one-for-one to the synthetic demo sessions (TEST-NNN → ID 30NNN, same session numbers).
- Every date is exactly 35 days later than the synthetic date (569/569). Distance = synthetic distance ÷ 10 (569/569). Coins = synthetic coins ÷ 3, rounded (556/569 within ±1).
  Obstacle count, lives lost, maximum speed, difficulty multiplier and game-over flag are identical (569/569). Duration is 30 s in every row.
- IDs are five-digit (30001–30120); the study's IDs are 3001–3120. No session ends in a game over.

`DERIVED_FROM_SYNTHETIC_stage_3_player_q9_summary_as_received_2026-10-01.zip`
(SHA-256 33fabd0f0f095ad696ccb3958dd8375add17c5fa0ce1a2b8e19640ec4b64d6e6; 120 files player_3001.csv … player_3120.csv, zip entries dated 1 Oct 2026 10:20)
- For all 120 players, the eight questionnaire answers (1–7 scale), the composite score, age band, sex and education are identical to synthetic
  players TEST-001 … TEST-120. Gender split 71 F / 49 M (study 72 / 48); D1/D2 "agree" counts 95 / 78 (study 86 / 76).
- "Dropped out" and "Returned" are blank for every player; "Original record survives" is blank for every player.
- Every row says "Entered by: Ruby" with entry dates 20–29 July 2026, but the column headers include wording from the record template
  created on 30 September 2026 ("Returned (played again after dropping out)"), and the files were zipped on 1 October 2026.
Never evidence. Kept only so the files are recognised if they resurface.

## Stage3_04_Delayed_Returns.xlsx, received 1 October 2026 — SELF-LABELLED GENERATED TEST INPUTS, NOT STUDY DATA

`TEST_INPUTS_NOT_STUDY_DATA_Stage3_04_Delayed_Returns_as_received_2026-10-01.xlsx`
(SHA-256 a89ece598f4014a512f41d9c677f74732f5ce5709e194ae4f79c5ce98ce4d4f0; creator "TAM, Sidney [Student]", created 1 Oct 2026 16:31, saved 23:42).
The author reports that the research assistant entered data "from various sources" into it. The workbook itself says otherwise:
- Participants sheet title "TEST PARTICIPANTS — T04"; its notes read "A–F are randomized test inputs" and "The participant assignments,
  gameplay values and dates in this workbook are generated test inputs."
- Telemetry sheet has the same name ("stage 3 Game Telemetry (2)"), the same columns and the same five-digit IDs 30001–30120 as the
  derived-from-synthetic file above; 546 of its 604 (player, session) keys also occur there, with regenerated values.
- Every session lasts exactly 30 s, loses no lives and never reaches a game over; every date is midnight except three RETURN rows stamped
  exactly at the cut-off cell (31 Aug 2026 23:59:59). No session falls in April although recruitment began 3 April; five sessions fall in
  August, after the July compilation of the summary.
- Recomputed from its rows it reproduces every summary target exactly (120; 38/41/41; 72 F / 48 M; dropouts 0/7/16, returns 0/5/10,
  non-return 0/2/6; 93.3% / 85.4%; agree 86 and 76; intention 25/28/23) and adds per-band values the summary does not hold
  (sex by band 21/17, 22/19, 29/12; coordination item by band 29/30/27; individual ages 26–80). Matching the targets is how a constructed
  file looks, not evidence of a source.
- Three INITIAL_STOP events fall at session 5, although the summary defines initial dropout as stopping before completing 5 attempts.
- No row carries a source reference (record, scan, e-mail or export), so no value can be traced to a primary record.
Never evidence. Kept only so the file is recognised if it resurfaces.
- Author's account, 1 Oct 2026: "test" renders the Chinese term for people having played; the research assistant reused the
  synthetic-derived layout and its description notes; values were transcribed from site records, voice tags and handwritten records.
  This explains the labels, layout and notes. It does not explain the values: both Stage-3A builds (v1.0 and v2.2) export Distance_m
  rounded to whole metres (Math.round), duration in minutes (Duration_Min) and Obstacles_Hit, whereas 535 of the 604 rows carry a
  decimal distance (e.g. 63.2 m), every row has Duration_Sec = 30, and the sheet has an Obstacles_Pass field that neither build records.
  Status unchanged pending a spot check of named rows against the original records.
- Author's further account, 2 Oct 2026: (1) decimal distances were calculated where data were not stored at dropout or non-completion;
  (2) all Stage-3 runs were zero-failure and ended at a 30-second time cap, with no game over implemented; (3) "Obstacles_Pass" is a
  translation of the game's obstacle count; (4) the 31 August dates are typing errors for July.
  Checks: (1) 431 of the 485 rows of the 97 players who never stopped also carry decimal distances; (2) v2.2 ends a run at 200 m or
  a 30-s cap (fits), v1.0 has no time cap and ends at 400/800/1200 m (does not fit); both builds contain a 3-bump game-over "classic"
  mode, with zero-failure ticked by default; thesis and Paper 3 currently report the author's earlier account that some players had
  an earlier version in which a run could end in a game over; (3) in both builds the counter increments on collision (S.hits++), so
  the game's field counts bumps, not obstacles passed; (4) accepted pending the record; rows for player 30079 on 2–3 Aug also need checking.
- Author's account, 2 Oct 2026 (later): distances and obstacles-passed values were calculated, not recorded; the research assistant
  no longer holds the game records; he cannot tell which build (v1.0 or v2.2) any player used.
  Conclusion: the telemetry columns are reconstructions, not observations, and cannot be traced to any retained record. The workbook
  stays non-evidence. Thesis and Paper 3 continue to report Stage 3A from the aggregate summary only (as in V59–V61 / R16).
  Open: the author's 30 Sep account (dropout = stopping after "failure or game over before zero-failure implemented"; some players had
  the first version) and the 2 Oct account (no game over; all runs zero-failure) conflict; thesis §6.4 and Paper 3 Game Build follow 30 Sep.
