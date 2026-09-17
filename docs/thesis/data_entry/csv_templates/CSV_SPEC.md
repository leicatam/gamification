# Game CSV Log Files — Reference Specification

Five CSV files carry all Stage-3 data from the field into the entry template.
Each template in this folder contains the exact header row plus one
`SAMPLE-DELETE-ME` example row showing the expected formats — **delete the
sample rows before real use**.

Conventions everywhere: dates `YYYY-MM-DD`; booleans `TRUE`/`FALSE`; decimal
point (not comma); UTF-8; one header row. `stage3_import.py` matches headers
case- and space-insensitively, so `participant id` and `PARTICIPANT_ID` also
work — but keeping these exact headers is simplest.

---

## 1. `sessions.csv` — one row per completed or attempted session
Written by the game at session end (see `game_logger.py`).

| Column | Type | Range / values | Notes |
|---|---|---|---|
| Participant_ID | text | 3001–3120 | Entered at the Assessment screen |
| Session_No | integer | 1–5 (≥6 = extra visits) | Five-attempt rule |
| Session_Date | date | within study window | |
| Duration_Min | decimal | 0–30 | Active play time |
| Distance_m | integer | 0–2000 | Slope is 2000 m |
| Coins | integer | ≥0 | |
| Obstacles_Hit | integer | 0–3 | 3 ⇒ Game Over state |
| Lives_Lost | integer | 0–3 | |
| Avg_Balance_pct | decimal | 0–100 | Mean of the in-game balance meter |
| Max_Speed | decimal | 0–30 | m/s, capped at 30 |
| AI_DiffMult | decimal | 0.30–1.50 | Multiplier at close of run |
| Reached_GameOver | boolean | TRUE/FALSE | Terminal state reached? |
| Post_FRA_Index | decimal | 0–100 | Silent clinician-side value; blank if not measured that session |
| Notes | text | free | Optional |

## 2. `state_changes.csv` — one row per L2 difficulty adjustment
Written by the game each time the adaptive layer changes difficulty.
Evidences the adaptive-learning mechanism (§5.3.5) — keep it.

| Column | Type | Notes |
|---|---|---|
| Participant_ID / Session_No | as above | |
| Play_Time_s | integer | Seconds into the session at the change |
| Old_DiffMult / New_DiffMult | decimal 0.30–1.50 | |
| Reason | text | e.g. `success rate 86% > 80% -> step up` |

## 3. `participants.csv` — one row per participant, at enrolment
| Column | Values |
|---|---|
| Participant_ID | 3001–3120 |
| Recruit_Date | date |
| Age | 25–80 |
| Age_Band | 25-44 / 45-64 / 65-80 (may be left blank — template derives it) |
| Gender | M / F / Other / NA |
| Education | Primary / Secondary / Tertiary / Postgrad |
| Recruit_Channel | free text |
| Prior_FRA_Use | Yes / No / Unknown |
| Pre_FRA_Index | 0–100 (silent, clinician-side) |
| Pre_FES_I | 16–64 (optional) |
| Consent_Signed | TRUE/FALSE |
| Withdrawn / Withdrawn_Reason | TRUE/FALSE / free text |

## 4. `questionnaire.csv` — one row per participant, post-study
Q1–Q8 are Likert integers (confirm the scale — 1–7 default, or 1–5 per
Appendix D — and set the template's Config sheet to match). Q9 fields are
open text.

## 5. `staff_observations.csv` — one row per participant with an observed event
The primary evidence for dropout and voluntary return. Transcribed from the
staff session log, **not** derived from the game.

| Column | Values |
|---|---|
| Participant_ID | 3001–3120 |
| Staff_Dropout_Observed | TRUE/FALSE |
| Dropout_Date | date (blank if none) |
| Staff_Return_Observed | TRUE/FALSE |
| Return_Date | date (blank if none) |
| Observer_Initials | staff initials |
| Notes | what was said/observed — valuable qualitative evidence |

---

## Import command

```
python stage3_import.py \
    --participants participants.csv \
    --sessions sessions.csv \
    --states state_changes.csv \
    --questionnaire questionnaire.csv \
    --observations staff_observations.csv \
    --out Stage3_Data_Entry_FILLED.xlsx
```

## Provenance rule

These files may contain only values produced by the game at run time or
transcribed from primary records. The `SAMPLE-DELETE-ME` rows exist to show
formats and must be removed before any real data is added.
