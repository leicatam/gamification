# Stage 3 (3A) game builds — what is on record

| File | Label | How it entered the record | Status |
|---|---|---|---|
| Alpine_Coordination_Game_Stage31_v1.0_as_received_2026-09-30.html (SHA-256 3200618c0bc70863b559aee294116e667b661dc9e0ef7e5ab3716e4e48edb346, 21,521 bytes) | "STAGE 3 RESEARCH BUILD v1.0" | Found by the author in his records; supplied 30 Sep 2026 as file "Alpine_Coordination_Game_Stage31.html" | Candidate for the build distributed from April 2026 — author to confirm where found, file date, and that it was the file sent to players |
| Alpine_Coordination_Game_Stage3_v2.html / _v2.2.html (byte-identical, SHA-256 42bc3df6…) | "Stage 3 Short-Run Build v2.2" | CREATED in this repository on 13 Jul 2026 ("Redesign Stage-3 game", v2 → v2.1 → v2.2 the same day) | A July redesign. Not established as the build any Stage 3A player used; returns ran to July, so late players may have received it — author to confirm |

## v1.0 as coded (inspection of the file)
- Participant ID field (placeholder 3001), session number 1–7, run length 400 / 800 / 1200 m (default 800 m); run ends at the
  distance goal, or in classic mode after the third hit. No time cap.
- Zero-failure checkbox, ticked by default: a bump slows the skier to 45% speed for 1.4 s and the run continues. Unticked =
  "Classic mode (3 hits end run)" — a game over. This matches the author's account that some players had a version that could end.
- "Agentic AI difficulty" checkbox, ticked by default: every 20 s the page calls the Anthropic API with aggregate run numbers.
  The file carries no API key, so from a normal browser the call fails and the built-in rule agent takes over (step up 0.10 above
  80% avoidance, ease off 0.15 below 40%); each decision is logged with its source (rules / fallback / Claude).
- Input: keyboard arrows or a gamepad / foot pad through the browser Gamepad API. No touch controls.
- No questionnaire and no consent screen inside the game.
- Export: two CSVs per run, `session_<ID>_s<N>.csv` (Participant_ID, Session_No, Session_Date, Duration_Min, Distance_m,
  Coins, Obstacles_Hit, Lives_Lost, Avg_Balance_pct, Max_Speed, AI_DiffMult, Reached_GameOver, Post_FRA_Index, Notes) and
  `states_<ID>_s<N>.csv`. No Score column. Notes read "zero-failure" or "classic", plus "; state changes=N".

## Differences from the July v2.2 (the file Paper 3 R8–R15 described)
v2.2 has 200 / 400 m runs with 30-s / 60-s time caps, a Score column, a 6-s adjustment interval, and in zero-failure mode a
bump does NOT slow the player (it thins obstacles instead). v1.0 has 400 / 800 / 1200 m runs, no cap, no Score, 20-s interval,
and zero-failure bumps DO slow the player.

## Consequence for the batch CSVs
All distributor batch files (3 Aug and 13 Sep 2026) carry "cap=30s", 200 m distances and a Score column — the v2.x format,
which v1.0 cannot produce. Dated March 2026, they were produced with the July build and remain excluded from evidence.
