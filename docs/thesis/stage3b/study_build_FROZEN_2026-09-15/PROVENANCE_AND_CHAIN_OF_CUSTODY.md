# Stage-3B clean run — provenance & chain of custody

## The rule (one line)

Every counted return must have at least ONE independent link in its
chain — a sender or a witness who is NOT the researcher. A return whose
only source is the researcher's own device and the researcher's own
e-mail has no independent provenance and cannot be distinguished from
self-generated data.

## Why "dispatch my own devices, default sender = my e-mail" is a problem

If the researcher hands out devices logged into the researcher's own
mail account, every "Send results" e-mail goes researcher-device ->
researcher-address. Even if every play is genuine, the record shows no
independent party anywhere in the loop. An examiner or reviewer cannot
tell such returns from data the researcher entered — and this
programme is already under explicit provenance scrutiny (examiner
Q3 on response provenance; the §8 demand for a traceable chain from
primary records to analysis; the quarantine of unverifiable returns).
It is not a legal dispute; it is a credibility failure at exactly the
point being examined. Do not collect the primary dataset this way.

Note: sending from the researcher's address does NOT breach player
anonymity (no player name is captured). The failure is the opposite —
too little independent evidence, not too much identifying detail.

## The gold standard already on file

B9V8YA (Huang, 15 Aug): participant played on her own device and sent
from her own e-mail, with her own address, timestamp and message. That
independent sender is what makes the return verifiable. Aim for this.

## Two acceptable collection modes

### Mode 1 — PREFERRED: participant's own device + own e-mail
Snowball distribution (forward the frozen file). The participant plays
on their own phone/computer and presses "Send results" from their own
e-mail. Independent sender = built-in provenance. Most returns should
be this. No researcher device involved.

### Mode 2 — dispatched or shared device (only if a participant has no device)
Do NOT rely on the researcher's mail account. Instead:
- An INDEPENDENT facilitator (a distributor — not the researcher) runs
  the session and keeps a short contemporaneous log: date, which device
  copy (DEV1-5), and the anonymous participant code shown by the game
  for each play (no names). The game's per-device archive / harvest
  panel stores each play on the device for the facilitator to collect.
- The facilitator forwards the results (from the facilitator's own
  e-mail) or hands over the saved files together with the log.
- The facilitator's dated log is the independent link that replaces the
  participant's own e-mail.
If no independent facilitator is available, do not dispatch a
researcher-owned, researcher-e-mail device for counted data — use
Mode 1.

## What makes a clean-run return verifiable

1. The build stamp inside the export = Alpine..._FROZEN20260915
   (confirms the frozen study build).
2. An independent link: the participant's own sending e-mail (Mode 1),
   or an independent facilitator's contemporaneous log (Mode 2).
3. Consent event present in the export; anonymous participant code; no
   personal name attached in transit.
A return missing (1) or (2) is handled as pilot/verification, not
counted in the primary dataset.
