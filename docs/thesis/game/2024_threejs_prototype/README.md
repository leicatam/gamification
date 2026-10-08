# 2024 Three.js browser prototype — records as received 3 October 2026

Supplied by the author on 3 October 2026 from his own records; archived unaltered (SHA-256 in CHECKSUMS_as_received_2026-10-03.txt).

| File | What it is | Internal date |
|---|---|---|
| Automatic_evaluation_and_difficulty_adjustment_system_for_skiing_games_2024-08-29_…pdf | Design specification of the prototype: Three.js/Cannon.js 3D ski game; pre-game ability-assessment form (age, sex, single-leg stand, sit-to-stand, pace, reaction time, gait stability, leg strength); difficulty-adjustment module; post-game analysis and recommendation module "developed using LangChain and OpenAI API"; data structure; test data for a synthetic 72-year-old female profile; **Appendix: the large-model prompt** (analysis-and-recommendation prompt). | PDF created 29 Aug 2024 (pdfcpu) |
| ski-game-threejs.js_code_print_2024-08-30_…pdf | One-page browser print of the prototype's Three.js game script (slope, skier, coins, obstacles, keyboard input, game loop). | Printed 30 Aug 2024 |
| game_v1_threejs_prototype_…html | Earlier runnable page of the same prototype (73,101 bytes; received 3 Oct 2026, second batch): identical assessment form and difficulty formulas; keyboard arrow or A/D steering; post-game analysis computed **locally by rule-based functions** (no server call); GLTF models and textures from the same project server. The v1→v2 difference is confined to the analysis module: v2 adds the server-side `/analyze` request (the LangChain/OpenAI module of the 29 Aug 2024 specification). | undated (2024 line) |
| game_v2_threejs_prototype_…html | Runnable prototype page (Chinese UI, 75,344 bytes): assessment form → deterministic difficulty formulas (obstacle, speed, balance) → Three.js game with GLTF models loaded from a project server → post-game analysis requested from a server-side `/analyze` endpoint (the LLM call is server-side; **no API credential is embedded**; the file names a project server IP, which is not reproduced in the thesis). No internal date. | undated (2024 line) |
| Intelligent_skiing_balance_training_game_system_overview_2026-07-12_…pdf | Seven-page overview of the same Three.js line: core features, keyboard controls, planned AGI-generated elements, application value, future outlook. Descriptive/marketing register; no data. | PDF created 12 Jul 2026 |

## What these records establish for the thesis (Appendix G, items G.0A and G.7)
- A **browser prototype generation in Three.js existed in August 2024**, alongside the Tux Racer input-coupling demonstration of 27 August 2024 (item G.10). It used keyboard input (arrow or A/D keys), a pre-game ability form, deterministic difficulty formulas in the page, and a server-side large-language-model analysis module. It is a predecessor generation, not the deployed Stage-2 Pygame build and not a Stage-3 build.
- The **prompt template** of that prototype's analysis module is on record (29 Aug 2024 specification, Appendix). The endpoint family is named (LangChain + OpenAI API, server-side). The **model version and run-time settings are not on record**, and the prompt template actually used by the deployed Stage-2 build is not on record; the thesis therefore still makes no operational claim for Layer 2 in Stage 2.
- The 29 Aug 2024 specification's worked example (synthetic 72-year-old female profile; correct-response rate 0.6; mean reaction time 2 s) is the prototype's own counterpart of the §5.3.5 worked example.

## What they do not establish
- No participant played these prototypes; no logs were retained; no result in the thesis rests on them.
