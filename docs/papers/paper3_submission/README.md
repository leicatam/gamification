# Paper 3 — figure files for submission

Companion to `../Paper3_R3_Aligned_V24.docx`. The manuscript embeds all
three figures at their callouts; this package holds the separate
production files (PNG + LZW TIFF, 300 dpi metadata), mirroring the
Paper-2 submission discipline.

| File | In manuscript at | Pixels | Notes |
|---|---|---|---|
| Figure1_Coordination_Game.png/.tif | §III.A | 2000 x 2298 | Archived HTML build, Stage-3 design lineage. Re-captured 13 Aug 2026 — see below. |
| Figure2_Participant_Flow.png/.tif | §IV | 1734 x 1076 | Preliminary aggregate record (N = 120). |
| Figure3_Age_Gradient.png/.tif | §V.B | 1503 x 1015 | Initial dropout vs return-after-dropout by age band. |

`Paper3_Figures_TIFF.zip` bundles the three TIFFs for one-shot upload.

## Figure 1 provenance (re-captured 13 Aug 2026)

The original composite was 644 x 745 px (too small for large
placements; upscaling was ruled out because interpolation fabricates
detail). Figure 1 was therefore RE-CAPTURED from the same archived
build — `docs/thesis/game/Alpine_Coordination_Game_Stage3_v2.2.html`
(byte-identical to `..._Stage3_v2.html`) — via headless Chromium at
3x device-pixel-ratio: one live run per difficulty level with the
rule agent frozen at the staged multiplier (x0.40/x0.65/x0.90/x1.15/
x1.40) and the display distance staged, exactly as the original figure
was produced. Same six-panel layout (five levels + legend). Capture
script: `../scripts/capture_paper3_fig1.js`. The superseded original
is archived at `../figures/paper3_fig1_game.png`; the new master is
`../figures/paper3_fig1_game_hires.png`, and the manuscript's embedded
copy was replaced with it (aspect ratio 0.87 vs 0.86 — no layout
shift).

One legend correction was made during re-capture: the original legend
said the skier is steered "by lateral weight shift" — the Stage-2
pressure-panel description. The archived Stage-3 build's actual inputs
are keyboard arrows / controller / foot pad, and the legend now says
so ("lateral movement (keyboard arrows, controller or foot pad)"),
matching the manuscript's account of remote unsupervised play. Do not
substitute frames from the v2.3+ or v3.0 successor builds — different
artifact generation; the caption declares Stage-3 design lineage.

## Tables

Paper 3's three tables remain embedded in the manuscript (editable Word
tables with captions); no separate table files are needed unless the
target journal's system requests them.

## Do not upload

- Paper-2 figure sets (`figures_submission/`, `jmir_submission/`) —
  different paper, different callouts.
- Any figure containing withdrawn statistics (the `EXCLUDED_*` files
  under `../figures/`).
