# Stage-3 Wrapper Kit — how the last data block gets done

TEMPLATES ONLY. Every example row is a watermarked placeholder. The kit
moves evidence; it never creates it. A blank cell with an explanation is
always admissible; an invented value never is.

## Why this block exists

The thesis reports a Stage-3 register (120 participants; 38/41/41 by
band; 86 endorsement; 76 intention). The register was compiled from
returns that arrived through a two-tier snowball: direct e-mail returns
plus distributor-compiled piles (e-mail, Google Drive, USB). The
integrated master file built earlier is NOT admissible (integration is
unverifiable), so the auditable record must be rebuilt from the
AS-RECEIVED inputs. Content checks can only disqualify a file (the game
engine writes real and replayed data identically); admission rests on
the provenance wrapper alone.

## What one admitted pile looks like

1. The distributor's file(s), byte-for-byte as received, in
   `data_entry/incoming/` — never edited, merged or re-typed.
2. One `Channel_Map` row (who, relationship, target range, invitation
   date + evidence, distribution method, return method + date, ID range,
   self-play exclusion).
3. `Transmittal_Log` rows: one per file, each pointing at a dated
   evidence artifact — reply e-mail screenshot, Drive details-panel
   screenshot, or a signed one-line USB origin note.
4. Questionnaire + enrolment returns for that chain, recorded in
   `Questionnaire_Returns` exactly as returned (D1, D2, age band,
   gender, education). Telemetry alone cannot produce the register's
   endorsement/intention/demographic counts.
5. A completed `Distributor_Cover_Sheet` with the author's declaration.

## Files in this kit

| File | Use |
|---|---|
| `Stage3_Wrapper_Kit_TEMPLATE.xlsx` | READ_ME + Channel_Map + Transmittal_Log + Questionnaire_Returns sheets, with watermarked example rows to delete. |
| `Distributor_Cover_Sheet_TEMPLATE.docx` | One per pile; ends in the author's signed declaration. |
| `USB_Drive_Origin_Note_TEMPLATE.docx` | Dated origin record for USB/Drive piles when no screenshot exists. |

## Pipeline after the wrappers arrive

incoming/ (as-received) → wrapper check (map row + transmittal + returns
present?) → engine-consistency check (can only disqualify) → ADMITTED →
logbook compilation (participant-level, per admitted pile) → open
reconciliation against the register (counts that match, match; counts
that don't are reported as discrepancies, not adjusted away).

## Current pile status (7 Aug 2026)

| Chain | Telemetry | Transmittal | Questionnaire/enrolment | Status |
|---|---|---|---|---|
| Daisy (family, 25-44, P3001-P3008) | staged, PASS | MISSING (invitation ≠ return) | MISSING | wrapper pending |
| Kevin Au (65-80, P3105-P3112) | staged, PASS | MISSING | MISSING | wrapper pending |
| Lucas (25-44, P3032-P3038) | staged, PASS | MISSING | MISSING | wrapper pending |
| Ms Tang (45+, invited 8 Apr) | none attributed | — | — | identify her IDs |
| Direct returns (author's circle) | — | .eml files needed | — | not yet supplied |
| Remaining ≈90 participants | unaccounted | — | — | Drive/USB piles to retrieve |
