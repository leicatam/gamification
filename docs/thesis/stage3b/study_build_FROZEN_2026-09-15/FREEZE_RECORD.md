# Stage-3B study build — FROZEN 15 September 2026

## Decision

For the clean Stage-3B collection running **15 September – 15 October
2026**, one single software edition is frozen as *the* study build.
No further code edits are made to it during the collection window.
Author's decision (15 Sep 2026): freeze the September edition.

## What was frozen

- Source: the September edition held in
  `docs/thesis/stage3b/device_sets/Alpine3B_DEV1..5.html` — the
  13-August generation (git commits 923a25e gains-only scoring +
  a1afc42 input-mode logging), which had carried the internal label
  `v3.0` even though its code is the v3.1 generation.
- Only change at freeze: the build identifier string was set to
  `Alpine_Coordination_Game_v3.1s_Stage3B_FROZEN20260915` (three
  occurrences), so every export self-identifies as this run. Verified
  by diff: nothing else changed — game logic is byte-identical to the
  working September edition that produced clean exports on 15 Sep.
- Five tagged copies (DEV1..DEV5) for five distribution channels, so
  returns trace to a channel. SHA-256 in `CHECKSUMS.txt`.

## Why this matters (the version rule)

Every participant in the clean run must play THIS build only. Mixing
software editions across a study is not permitted — comparison
requires one instrument. Returns carrying any other build string
(e.g. the August field build, or the bare `v3.0` label) are NOT part
of this run and are handled separately.

## Relationship to earlier data

- **August field deployment (9-Aug build 59b7881, distributed
  10–12 Aug):** the initial soft launch / pilot. One verified return
  to date (B9V8YA, Huang, 15 Aug). Reported honestly as a pilot on an
  earlier sub-edition; not pooled with the frozen run.
- **Five plays received 15 Sep (build `v3.0`, all DEV1, all arm A):**
  excluded — solicited test plays on the pre-freeze September edition;
  see `../../data_entry/incoming/stage3b_returns_PENDING_VERIFICATION/`.
  They are build-verification only, never counted.
- **Clean run (this frozen build, from 15 Sep):** the primary Stage-3B
  data collection. Returns self-identify by the `FROZEN20260915` label.

## Pre-specification held constant

The protocol and the pre-specified analysis hierarchy are
repository-dated 8–9 August 2026 (unchanged): one confirmatory
contrast — adaptive vs static on D2 top-two-box, pooled across failure
modes; failure-mode factor and interaction exploratory. The framing
rule is fixed on the observed N before analysis. All pre-specified
outcomes reported regardless of direction.

## Integrity rule for the window

No edits to any frozen copy until 15 October. If a defect forces a
change, the window restarts on the corrected build and prior returns
become a pilot — a change is never made silently mid-run.


## Addendum — 26 September 2026 (author's decision; see ../DECISION_2026-09-26_Stage3B_not_used_as_adaptive_learning_test.md)

Stage 3B is no longer used as the test of the adaptive-learning proposition; the thesis (V43)
reports the study as a descriptive record at a stated cut-off of 26 September 2026 (Appendix I).
This addendum changes nothing above: the frozen edition, its checksums and the clean-run window
(15 September – 15 October 2026) stand as recorded. Clean-run returns on record at the cut-off:
none. Any return received after the cut-off is archived as received and may be reported only as a
dated addendum outside the thesis evidence base.
