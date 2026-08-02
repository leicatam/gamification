# Incoming Stage-3 batches — staged, provenance pending

Files received as candidate participant-level returns, held here
as-received. NOT admitted to the logbook analysis sheets until each
file's provenance wrapper arrives: (1) channel-map line for the
distributor; (2) transmittal evidence (e-mail/Drive/USB, dated);
(3) where applicable, the distributor's original per-session files.

| File | Received | Internal checks | Provenance |
|---|---|---|---|
| `Telemetry_2544_Lucas_batch5_P3032P3038.csv` | 3 Aug 2026 | PASS — engine-consistent (score arithmetic, physics, difficulty steps, state-change counts, monotonic dates); NOT a slice of the known simulation (0/35 rows match) | PENDING — awaiting Lucas channel-map line + transmittal evidence |
| `Telemetry_6580_Kevin_Au_batch4_P3105P3112.csv` | 3 Aug 2026 | PASS — 0/32 simulation matches; 32/32 score arithmetic; monotonic dates; dropout/return patterns consistent with 65-80 register (3 completers, 2 dropout-returns, 3 permanent) | PENDING — awaiting Kevin Au transmittal evidence + channel-map line |
| `2544_Daisy_batch1_P3001P3008.csv` | 3 Aug 2026 | PASS — 0/40 simulation matches; 40/40 score arithmetic; monotonic dates; all 8 complete (consistent with zero-dropout 25-44 band) | PENDING — awaiting Daisy transmittal evidence + channel-map line |

Content checks can disqualify a file but never qualify one: the game
engine generates real and replayed data identically. Admission is by
provenance only.

## What telemetry batches alone cannot provide

Session CSVs yield dropout / return / retention. They contain NO
questionnaire answers (D1 endorsement, D2 intention) and NO enrolment
data (age band, gender, education). Each distributor's pile must also
include those returns — the register's endorsement (86) and intention
(76) counts are uncomputable from telemetry.
