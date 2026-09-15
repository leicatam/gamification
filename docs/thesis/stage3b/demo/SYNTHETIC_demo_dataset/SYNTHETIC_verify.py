#!/usr/bin/env python3
"""SYNTHETIC_verify.py — integrity checks for the hard-labelled synthetic
demonstration dataset. Confirms: all 40 return files parse, arm counts are
20/20, and every record carries the synthetic markers. Exits non-zero on any
failure."""
import json, os, sys, csv

OUT = os.path.dirname(os.path.abspath(__file__))
GEN_MARK = "2026-09-13 by simulation for pipeline demonstration"
TXT_MARK_PREFIX = "SYNTHETIC DEMONSTRATION DATA — generated 2026-09-13 by simulation"

errors = []
arms = {"A": 0, "B": 0}
n_missing_quest = 0
n_runs = 0

expected = ["SYN-P{:03d}".format(i) for i in range(1, 41)]
for pid in expected:
    fname = "SYNTHETIC_return_{}.txt".format(pid)
    path = os.path.join(OUT, fname)
    if not os.path.exists(path):
        errors.append("MISSING FILE: " + fname)
        continue
    lines = open(path, encoding="utf-8").read().splitlines()
    if len(lines) < 3:
        errors.append(fname + ": fewer than 3 lines")
        continue
    if not lines[0].startswith(TXT_MARK_PREFIX):
        errors.append(fname + ": line 1 lacks the synthetic marker")
    if pid not in lines[1]:
        errors.append(fname + ": header line does not carry the participant ID")
    try:
        d = json.loads(lines[2])
    except Exception as e:
        errors.append(fname + ": JSON parse failed: " + str(e))
        continue
    if d.get("synthetic") is not True:
        errors.append(fname + ': "synthetic": true missing')
    if d.get("generated") != GEN_MARK:
        errors.append(fname + ': "generated" marker wrong/missing')
    if d.get("participant_code") != pid:
        errors.append(fname + ": participant_code mismatch")
    if not pid.startswith("SYN-P"):
        errors.append(fname + ": participant ID not in SYN-P range")
    arm = d.get("arm")
    if arm in arms:
        arms[arm] += 1
    else:
        errors.append(fname + ": invalid arm " + repr(arm))
    ss = d.get("sessions") or []
    if len(ss) < 1:
        errors.append(fname + ": no sessions")
    n_runs += len(ss)
    for s in ss:
        if s.get("Lives_Lost") != 0 or s.get("Reached_GameOver") != "FALSE" or s.get("Post_FRA_Index") != "":
            errors.append(fname + ": session invariant violated (Lives_Lost/Reached_GameOver/Post_FRA_Index)")
        if s.get("Participant_ID") != pid or s.get("Arm") != arm:
            errors.append(fname + ": session Participant_ID/Arm mismatch")
    if len(d.get("state_logs") or {}) != len(ss):
        errors.append(fname + ": state_logs keys do not match session count")
    if d.get("questionnaire") is None:
        n_missing_quest += 1

# combined CSV
csv_path = os.path.join(OUT, "SYNTHETIC_combined.csv")
if not os.path.exists(csv_path):
    errors.append("MISSING FILE: SYNTHETIC_combined.csv")
else:
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
    if len(rows) != 40:
        errors.append("CSV: expected 40 rows, found {}".format(len(rows)))
    bad = [r["participant_id"] for r in rows
           if r.get("synthetic") != "TRUE" or r.get("generated") != GEN_MARK]
    if bad:
        errors.append("CSV rows missing synthetic markers: " + ", ".join(bad))

# every filename in the directory starts with SYNTHETIC_
stray = [f for f in os.listdir(OUT)
         if not f.startswith("SYNTHETIC_") and not f.startswith(".")]
if stray:
    errors.append("Files not prefixed SYNTHETIC_: " + ", ".join(sorted(stray)))

print("SYNTHETIC dataset verification — {}".format(OUT))
print("  return files found/parsed : {}/40".format(sum(1 for p in expected
      if os.path.exists(os.path.join(OUT, "SYNTHETIC_return_{}.txt".format(p))))))
print("  arm counts                : A={} B={} (expected 20/20)".format(arms["A"], arms["B"]))
print("  synthetic marker          : line-1 text marker + \"synthetic\": true + \"generated\" checked in every file")
print("  total runs across dataset : {}".format(n_runs))
print("  missing questionnaires    : {} (planted for missing-data demo)".format(n_missing_quest))
if arms["A"] != 20 or arms["B"] != 20:
    errors.append("Arm counts not 20/20: A={} B={}".format(arms["A"], arms["B"]))
if errors:
    print("RESULT: FAIL — {} problem(s)".format(len(errors)))
    for e in errors:
        print("  - " + e)
    sys.exit(1)
print("RESULT: PASS — all checks OK (40 files parse; arms 20/20; every record hard-labelled synthetic)")
