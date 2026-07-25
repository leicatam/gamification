# Stage-3 Data-Entry Kit

Purpose: get game state-table exports and staff records into the Stage-3
logbook **without typing values one by one**, with definitions centralised,
outcomes derived automatically, and quality checks live.

## Files

| File | What it is |
|---|---|
| `Stage3_Data_Entry_Template.xlsx` | The clean entry template. Use this one. |
| `stage3_import.py` | Loads game exports (CSV/JSON) into the template's RAW sheets automatically. |
| `Stage3_Data_Entry_DEMO_SYNTHETIC.xlsx` | The template filled with the SYNTHETIC TEST- dataset — pipeline demonstration only, watermarked. Never bind. |
| `build_entry_template.py` | Rebuilds the template from scratch (for maintenance). |

## Workflow

1. **ENTRY_Participants** — type enrolment data once (IDs 3001–3120 pre-filled,
   Age_Band auto-derives, dropdowns constrain categories).
2. **RAW_Sessions / RAW_GameStates / RAW_Questionnaire** — paste the game's
   exports directly (columns already match), or run:
   ```
   python stage3_import.py --sessions sessions.csv --states states.json \
       --questionnaire q4.csv --participants participants.csv
   ```
   Headers are matched case/space-insensitively, so raw export headers work as-is.
3. **ENTRY_Observations** — transcribe staff-observed dropout/return events
   from the session logs. These take precedence over telemetry, because a
   participant can drop out, come back, and still complete all five sessions —
   telemetry alone cannot see that.
4. **AUTO_Outcomes** — computes itself (green cells are formulas): sessions,
   completion, telemetry signals, staff records, FINAL dropout/return with the
   precedence rule, endorsement/intention from questionnaire thresholds, and
   the pre/post FRA change.
5. **CHECKS** — 14 live quality flags (duplicates, orphans, out-of-range,
   staff-vs-telemetry conflicts). Every flag must be 0 before data moves on.
6. Copy the validated values into the master logbook
   (`Stage3_Data_Logbook_120cases_with_Reconciliation.xlsx`), whose
   Reconciliation sheet compares your totals with the published Paper 3 figures.

## Definitions live on the Config sheet

Five-attempt rule, return-gap days, endorsement/intention items and
thresholds, study window. Change definitions there once — never in formulas —
and record any change in the thesis (§6.2/§8.9). Note the open scale question:
thesis Appendix D says 5-point Likert (endorse = 4–5), the logbook codebook
says 1–7 (default here: ≥5). Confirm against the actual questionnaire before
entering data.

## Validation

The full pipeline was tested end-to-end on the synthetic TEST- dataset:
imported 120 participants, 569 sessions, 2,968 state changes and 120
questionnaires; the derived FINAL outcomes matched the synthetic ground truth
**120/120 on all four outcome fields** (35 dropouts, 23 returns, 95
endorsements, 78 intents) with all CHECKS clean. The synthetic file's only
legitimate role — proving the pipeline — is hereby fulfilled.

## Provenance rule

The template and script move data; they never create it. RAW and ENTRY sheets
may contain only values exported from the game or transcribed from primary
records.

## Provenance log — rejected uploads (July 2026)

Three files supplied as Stage-3 study data were examined and NOT admitted to
the logbook analysis sheets. They are retained here, renamed to state their
status, so the audit trail is complete:

| Archived file | Received | Finding |
|---|---|---|
| `UNVERIFIED_Gameplay_Summary_19072026_provenance_unconfirmed.xlsx` | 19 Jul 2026 | Aggregate summary whose totals match the register but whose per-band indicators contradict it in 10 places (gender 52/68 vs register 48/72; dropouts 0/6/17 vs 0/7/16; intention 38/24/14 vs 25/28/23; band labelled "65-85"); contains construction annotations. Staged read-only in the logbook's RAW_Import_UNVERIFIED sheet with warnings. |
| `SYNTHETIC_Constrained_Simulation_21072026_NOT_STUDY_DATA.xlsx` | 21 Jul 2026 | Participant-level dataset whose own Validation sheet declares "Dataset status: Synthetic / constrained simulation"; all 26 indicators PASS by construction (targets were inputs, not outcomes). |
| `SYNTHETIC_Constrained_Simulation_V2_relabelled_21072026_NOT_STUDY_DATA.xlsx` | 25 Jul 2026 | Presented as "the clean version". Cell-level comparison against the file above: Q4 Responses, Outcomes and Registered Results sheets byte-identical; Participants differs only in 94 renamed Recruit_Channel labels; Game Telemetry differs only in 6 edited session dates (introducing a new anomaly — participant 3005's sessions 2-5 all dated 2026-03-07); the single substantive change is the Validation "Dataset status" cell, edited from "Synthetic / constrained simulation" to "converted from game state CVS raw dataset". The construction notes ("Participant IDs: Randomly distributed across behavioural groups"; retention target "implemented") remain. Same dataset, relabelled. |

Author's account (25 Jul 2026): the workbooks were produced by exporting
game state memory to CSV and then asking ChatGPT to "formulate the file"
against this kit's template. This explains the findings: an LLM given raw
telemetry plus the registered targets generates whatever the CSV does not
contain (demographics, Q4 questionnaire responses, staff-observed
dropout/return events — none of which exist in game state memory) and
fits the result to the targets, which is exactly what the file's own
Validation notes describe ("Randomly distributed across behavioural
groups"; retention target "implemented"). The workbooks are therefore an
inseparable mixture of possibly-real telemetry and generated content, and
remain inadmissible. Resolution path: import the untouched CSV exports
directly via `stage3_import.py`, and transcribe questionnaire/enrolment/
staff-log fields from their paper records; fields with no surviving
primary record are left blank and disclosed.

Ruling (standing): relabelling a synthetic dataset does not change its
provenance, and a dataset generated under the registered targets cannot
verify those targets — the reasoning is circular. The logbook analysis
sheets remain empty pending transcription from primary records (paper
questionnaires, staff session logs, terminal exports), and the thesis
continues to rest on the preliminary aggregate register (38/41/41), which
it reports accurately.
