# Paper 3 — figure files for submission

Companion to `../Paper3_R3_Aligned_V24.docx`. The manuscript embeds all
three figures at their callouts; this package holds the separate
production files (PNG + LZW TIFF, 300 dpi metadata), mirroring the
Paper-2 submission discipline.

| File | In manuscript at | Pixels | Notes |
|---|---|---|---|
| Figure1_Coordination_Game.png/.tif | §III.A | 644 x 745 | Archived HTML build, Stage-3 design lineage. **RESOLUTION CAVEAT** — see below. |
| Figure2_Participant_Flow.png/.tif | §IV | 1734 x 1076 | Preliminary aggregate record (N = 120). |
| Figure3_Age_Gradient.png/.tif | §V.B | 1503 x 1015 | Initial dropout vs return-after-dropout by age band. |

`Paper3_Figures_TIFF.zip` bundles the three TIFFs for one-shot upload.

## Figure 1 resolution caveat

Figure 1 is 644 x 745 px — at 300 dpi that is ~2.1 x 2.5 inches,
acceptable for a narrow single-column placement but BELOW comfortable
size for anything larger. It must NOT be upscaled (interpolation
fabricates detail). If the target journal requires larger art, the
correct fix is to RE-SCREENSHOT the same archived HTML build at a
higher viewport/device-pixel-ratio, verifying the re-captured frames
show the identical build (same difficulty stages, same HUD) as the
figure reviewers have already seen. Do not substitute frames from the
v2.3+ or v3.0 successor builds — different artifact generation, and the
caption declares Stage-3 design lineage.

## Tables

Paper 3's three tables remain embedded in the manuscript (editable Word
tables with captions); no separate table files are needed unless the
target journal's system requests them.

## Do not upload

- Paper-2 figure sets (`figures_submission/`, `jmir_submission/`) —
  different paper, different callouts.
- Any figure containing withdrawn statistics (the `EXCLUDED_*` files
  under `../figures/`).
