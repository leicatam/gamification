# "Intelligent Skiing Rehabilitation Training Game" build — received 4 October 2026

Three files supplied by the author on 4 October 2026 with the words "It's the early Stage 3. Right?" Archived unaltered (SHA-256 in CHECKSUMS_as_received_2026-10-04.txt). Status: provenance pending the author's answers below; not yet cited.

| File | What it is |
|---|---|
| index_…html (57,297 bytes) | A runnable single-file Three.js (r134) game, English UI: assessment screen (age group 18–35/36–55/56+, self-assessed balance low/medium/high, rehabilitation goal), 3 lives, 5-trial sessions with a trial-by-trial report, "P" to pause, "Train Again", rule-based "AI Training Recommendation" text (no model call, no network request). Input: arrow keys or A/D, mouse position, gamepad stick or D-pad. |
| generate_demo_video_…py | A Python script that renders a synthetic animated demo (title card, pre-scripted gameplay with planned collisions, game-over card, report screen, end card) with PIL and imageio. Font paths are macOS. |
| skiing_game_demo_SYNTHETIC_RENDER_…mp4 (1,168,670 bytes; 1280 × 720; 26.5 s) | The output of that script. **It is a synthetic animation, not gameplay footage and not a screen recording of the game.** |

## Relation to the thesis
The game's `CONFIG` block and hit rules match **Table 5.0 and the §5.2A state-machine description value for value**: slope 30 m × 2000 m at 12°; base move speed 8 and forward speed 12 m/s (cap 30); balance decay 0.02, turn penalty 0.15, recovery 0.08, collision penalty; obstacle density 0.4/m, spawn 120 m ahead, despawn 30 m behind; coin density 0.3/m, value 10, spawn 100 m ahead; +0.15 difficulty per 200 m; three lives, 1.5-s cooldown, first hit speed × 0.7, second hit obstacle spacing × 0.4 with 60% of obstacles ahead cleared; mouse deadzone 0.08, gamepad deadzone 0.15, clamp 1.5×; age multipliers 1.1 / 1.0 / 0.7 and balance multipliers 0.6 / 1.0 / 1.3; states Assessment → Playing → Paused → Game Over, "Train Again". The thesis currently attributes these to "the Stage-2 build" (via the G.14 workbook, not deposited) and separately refers to "the programme's archived successor build in the same design lineage" as the source of the Figure 5.1B screenshots (item G.6).

It is **not** the distributed Stage-3A research build v1.0 of April 2026 (`Alpine_Coordination_Game_Stage31_v1.0…`, a different code base with different parameter names), nor the 2024 Three.js prototype (`2024_threejs_prototype/`, Chinese UI, GLTF assets from a project server). Its title matches the 12 July 2026 overview PDF ("Intelligent skiing rehabilitation training game system", item G.7 folder).

## Open questions for the author (answers decide how §5.2A, Table 5.0, G.6, G.14 and G.0A are worded)
1. When was this index.html created, and by which tool (ChatGPT / Claude Code)?
2. Is it the "archived successor build" from which the Figure 5.1B screenshots (item G.6) were taken?
3. Was Game_States_and_Parameters.xlsx (item G.14) written from this file, or this file from the workbook?
4. Did any participant ever play this build — the Stage-2 residents in 2025 (with the mat as arrow keys), or any Stage-3A player?
5. Does any file of the game the Stage-2 residents actually played survive? If not, Table 5.0 and the state machine will be re-labelled as the successor-build specification, not verified against the deployed Stage-2 build.
