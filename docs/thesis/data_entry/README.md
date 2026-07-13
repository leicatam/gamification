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
