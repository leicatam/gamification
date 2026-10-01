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
