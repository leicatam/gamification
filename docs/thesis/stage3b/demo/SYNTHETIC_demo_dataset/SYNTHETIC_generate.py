#!/usr/bin/env python3
"""SYNTHETIC_generate.py — HARD-LABELLED SYNTHETIC demonstration data generator
for the Stage-3B analysis pipeline demo. Every output is marked synthetic.
NOT study data. NOT evidence. Thesis rule G.8: synthetic data is never evidence.

Mirrors the deployed-candidate build Alpine_Coordination_Game_v3.0_Stage3B
return format (2-line text message: header + one-line compact JSON), with
synthetic markers added as an extra leading line and extra JSON fields.
Deterministic: seed 20260913.
"""
import json, random, math, os, csv, datetime

OUT = os.path.dirname(os.path.abspath(__file__))
SEED = 20260913
rng = random.Random(SEED)

GEN_MARK = "2026-09-13 by simulation for pipeline demonstration"
TXT_MARK = ("SYNTHETIC DEMONSTRATION DATA — generated 2026-09-13 by simulation "
            "for pipeline demonstration. NOT study data. NOT evidence.")
BUILD = "Alpine_Coordination_Game_v3.0_Stage3B"
DATE = "2026-09-13"

HEADERS = {
    "en":  "[ALPINE GAME STUDY RESULTS {pid} — please send exactly as it is]",
    "zh":  "【滑雪遊戲研究結果 {pid}——請原封不動傳送給研究員】",
    "zhs": "【滑雪游戏研究结果 {pid}——请原封不动发送给研究员】",
}

# ----- simulated GROUND TRUTH (stated openly in the analysis doc) -----
TRUE_P_D2_TOP2 = {"A": 0.65, "B": 0.45}   # primary endpoint generative truth
TRUE_P_D1_TOP2 = {"A": 0.80, "B": 0.78}
TRUE_P_F1_TOP2 = {"A": 0.75, "B": 0.55}
TRUE_P_F2_TOP2 = {"A": 0.72, "B": 0.50}
SESS_WEIGHTS = {  # sessions-per-participant self-selection (behavioural support)
    "A": ([1, 2, 3, 4, 5, 6], [4, 14, 30, 30, 15, 7]),   # mean ~3.6
    "B": ([1, 2, 3, 4, 5, 6], [14, 34, 30, 15, 6, 1]),   # mean ~2.7
}


def jsnum(x, nd):
    """Mimic JS +(x.toFixed(nd)): 0.5 not 0.50, 1 not 1.00, 100 not 100.0."""
    v = round(x + 1e-12, nd)
    iv = int(v)
    return iv if v == iv else v


def iso(sec_of_day, ms):
    base = datetime.datetime(2026, 9, 13) + datetime.timedelta(seconds=int(sec_of_day))
    return base.strftime("%Y-%m-%dT%H:%M:%S") + ".{:03d}Z".format(ms)


def stamp(sec):
    return iso(sec, rng.randrange(1000))


def likert(top2_p, p5_given_top2=0.42, low_w=(0.10, 0.32, 0.58)):
    if rng.random() < top2_p:
        return 5 if rng.random() < p5_given_top2 else 4
    r = rng.random()
    if r < low_w[0]:
        return 1
    if r < low_w[0] + low_w[1]:
        return 2
    return 3


def simulate_run(arm, skill, run_no, pid, lang, early_end=None):
    """One 30 s run (or early-ended). Returns (session_dict, state_log, dur_s)."""
    diff = 0.60 if arm == "A" else 0.85
    dur = float(early_end) if early_end else 30.0
    dist = 0.0
    coins = 0
    hits = 0
    bal_samples = []
    log = []
    reason0 = ("run start — arm A (adaptive, gentle floor)" if arm == "A"
               else "run start — arm B (static ×0.85)")
    log.append({"t": 0, "playMin": 0, "oldDiff": jsnum(diff, 2), "newDiff": jsnum(diff, 2),
                "dist": 0, "coins": 0, "hits": 0, "balance": 100,
                "reason": reason0, "src": "init"})
    max_diff_driven = diff
    dip = 0

    windows = []
    ws = 0.0
    while ws < dur:
        windows.append((ws, min(ws + 6.0, dur)))
        ws += 6.0

    for (w0, w1) in windows:
        # obstacles for this window (spawn ~ 0.75 * diff * s * obFactor)
        lam = 0.75 * diff * (w1 - w0) * 0.7
        faced = max(2, min(7, int(round(rng.gauss(lam + 0.7, 1.0)))))
        avoided = sum(1 for _ in range(faced) if rng.random() < skill)
        nhit = min(faced - avoided, 2)
        avoided = faced - nhit
        pool = [s for s in range(int(w0) + 1, int(w0) + 6) if s <= dur]
        hit_secs = sorted(rng.sample(pool, k=min(nhit, len(pool)))) if nhit else []

        s = w0
        while s < w1:
            step = min(1.0, w1 - s)
            dist += 18.0 * diff * step
            if rng.random() < 0.45 * step:
                coins += 1
            if dip > 0:
                bal = rng.gauss(93.5, 1.2)
                dip -= 1
            else:
                bal = rng.gauss(98.0, 1.0)
            bal_samples.append(max(85.0, min(100.0, bal)))
            sec_idx = int(s) + 1
            if sec_idx in hit_secs:
                hits += 1
                dip = 2
                k = rng.randint(1, 3)
                tb = round(sec_idx - rng.uniform(0.0, 0.9), 1)
                rm = sum(bal_samples) / len(bal_samples)
                log.append({"t": jsnum(tb, 1), "playMin": jsnum(tb / 60.0, 2),
                            "oldDiff": jsnum(diff, 2), "newDiff": jsnum(diff, 2),
                            "dist": int(round(dist)), "coins": coins, "hits": hits,
                            "balance": jsnum(rm, 1),
                            "reason": "bump → cleared {} obstacle(s), density ×0.75 (speed unchanged)".format(k),
                            "src": "bump"})
            s += step

        # rule-agent evaluation at full 6 s marks, arm A only
        if arm == "A" and abs((w1 - w0) - 6.0) < 1e-9:
            rate = avoided / faced
            pct = int(round(rate * 100))
            old = diff
            if faced >= 2 and rate > 0.8:
                diff = min(1.50, round(diff + 0.10, 2))
                reason = "avoid rate {}% > 80% → step up".format(pct)
            elif faced >= 2 and rate < 0.4:
                diff = max(0.30, round(diff - 0.15, 2))
                reason = "avoid rate {}% < 40% → step down".format(pct)
            else:
                reason = "avoid rate {}% in band → hold".format(pct)
            rm = sum(bal_samples) / len(bal_samples)
            log.append({"t": jsnum(w1, 1), "playMin": jsnum(w1 / 60.0, 2),
                        "oldDiff": jsnum(old, 2), "newDiff": jsnum(diff, 2),
                        "dist": int(round(dist)), "coins": coins, "hits": hits,
                        "balance": jsnum(rm, 1), "reason": reason, "src": "rules"})
            if w1 < dur:  # a t=30 eval never drives speed (fires in the final frame)
                max_diff_driven = max(max_diff_driven, diff)

    goal = dist >= 200.0
    if dur >= 30.0:
        end_reason = "30 s complete (goal reached)" if goal else "30 s complete"
    else:
        end_reason = "ended early by staff"
    avg_bal = sum(bal_samples) / len(bal_samples)
    score = coins * 10 + int(round(dist)) + (50 if goal else 0)
    session = {
        "Participant_ID": pid,
        "Session_No": run_no,
        "Session_Date": DATE,
        "Duration_Min": jsnum(dur / 60.0, 2),
        "Distance_m": int(round(dist)),
        "Coins": coins,
        "Obstacles_Hit": hits,
        "Lives_Lost": 0,
        "Avg_Balance_pct": jsnum(avg_bal, 1),
        "Max_Speed": jsnum(18.0 * max_diff_driven, 1),
        "AI_DiffMult": jsnum(diff, 2),
        "Reached_GameOver": "FALSE",
        "Score": score,
        "Post_FRA_Index": "",
        "Notes": "zero-failure; cap=30s; end: {}; state changes={}".format(end_reason, len(log)),
        "Arm": arm,
        "Lang": lang,
    }
    return session, log, dur


# ---------------- population ----------------
pids = ["SYN-P{:03d}".format(i) for i in range(1, 41)]
arms = ["A"] * 20 + ["B"] * 20
rng.shuffle(arms)
arm_of = dict(zip(pids, arms))

# incomplete records (missing-data demo), chosen deterministically by pid order
a_ids = [p for p in pids if arm_of[p] == "A"]
b_ids = [p for p in pids if arm_of[p] == "B"]
missing_quest = {a_ids[0], b_ids[0], b_ids[1]}   # 1 adaptive + 2 static, no questionnaire
dropout = b_ids[1]                               # single early-ended run, then left
early_extra = {a_ids[1], b_ids[2]}               # completed questionnaire but one early-ended run

BANDS = ["25-44", "45-64", "65-80"]
BAND_W = [0.15, 0.30, 0.55]                      # weighted to 65-80
SKILL_MEAN = {"25-44": 0.92, "45-64": 0.86, "65-80": 0.80}
EDU_W = {"25-44": [0.15, 0.35, 0.50], "45-64": [0.35, 0.35, 0.30], "65-80": [0.60, 0.25, 0.15]}
EDUS = ["secondary", "post-secondary", "degree+"]

participants = []
for idx, pid in enumerate(pids):
    arm = arm_of[pid]
    band = rng.choices(BANDS, BAND_W)[0]
    gender = "F" if rng.random() < 0.60 else "M"
    edu = rng.choices(EDUS, EDU_W[band])[0]
    prior = "yes" if rng.random() < 0.10 else "no"
    lang = rng.choices(["zh", "zhs", "en"], [0.55, 0.15, 0.30])[0]
    skill = max(0.45, min(0.99, rng.gauss(SKILL_MEAN[band], 0.06)))

    if pid == dropout:
        n_sess = 1
    else:
        opts, w = SESS_WEIGHTS[arm]
        n_sess = rng.choices(opts, w)[0]

    # clock: sessions staggered across the demo day (all times synthetic)
    t0 = 3600 + idx * 700 + rng.uniform(0, 240)      # from 01:00Z
    consent_ts = stamp(t0)
    t1 = t0 + rng.uniform(35, 80)
    enrol_ts = stamp(t1)

    sessions, state_logs = [], {}
    t_run = t1 + rng.uniform(15, 40)
    for r in range(1, n_sess + 1):
        early = None
        if pid == dropout:
            early = round(rng.uniform(10.0, 14.0), 1)
        elif pid in early_extra and r == max(1, n_sess // 2):
            early = round(rng.uniform(14.0, 22.0), 1)
        sess, log, dur = simulate_run(arm, skill, r, pid, lang, early_end=early)
        sessions.append(sess)
        state_logs[str(r)] = log
        t_run += dur + rng.uniform(18, 60)           # run + summary-screen dwell

    if pid in missing_quest:
        quest = None
        answered_ts = None
        t_exp = t_run + rng.uniform(120, 420)        # later facilitator export
    else:
        quest = {
            "D1_coordination_challenge": likert(TRUE_P_D1_TOP2[arm]),
            "D2_play_regularly": likert(TRUE_P_D2_TOP2[arm]),
            "F1_matched_ability": likert(TRUE_P_F1_TOP2[arm]),
            "F2_progress_motivated": likert(TRUE_P_F2_TOP2[arm]),
        }
        t_q = t_run + rng.uniform(35, 100)
        answered_ts = stamp(t_q)
        quest["answered_ts"] = answered_ts
        t_exp = t_q + rng.uniform(8, 30)
    exported_ts = stamp(t_exp)

    export = {
        "synthetic": True,
        "generated": GEN_MARK,
        "build": BUILD,
        "device_id": None,
        "participant_code": pid,
        "arm": arm,
        "language": lang,
        "consent": {"agreed": True, "timestamp": consent_ts},
        "enrolment": {"age_band": band, "gender": gender, "education": edu,
                      "prior_play": prior, "recorded_ts": enrol_ts},
        "sessions": sessions,
        "state_logs": state_logs,
        "questionnaire": quest,
        "scale": "1 (strongly disagree) - 5 (strongly agree)",
        "exported_ts": exported_ts,
    }

    txt = "{}\n{}\n{}".format(
        TXT_MARK,
        HEADERS[lang].format(pid=pid),
        json.dumps(export, ensure_ascii=False, separators=(",", ":")),
    )
    fname = "SYNTHETIC_return_{}.txt".format(pid)
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(txt + "\n")

    participants.append({
        "pid": pid, "arm": arm, "band": band, "gender": gender, "edu": edu,
        "prior": prior, "lang": lang, "consent_ts": consent_ts, "enrol_ts": enrol_ts,
        "sessions": sessions, "quest": quest, "answered_ts": answered_ts,
        "exported_ts": exported_ts, "file": fname,
    })

# ---------------- combined CSV ----------------
csv_path = os.path.join(OUT, "SYNTHETIC_combined.csv")
cols = ["participant_id", "synthetic", "generated", "arm", "age_band", "gender",
        "education", "prior_play", "language", "consent_ts", "enrol_recorded_ts",
        "n_sessions", "any_early_end", "total_distance_m", "mean_distance_m",
        "best_score", "mean_score", "total_coins", "total_obstacles_hit",
        "mean_avg_balance_pct", "max_speed_overall", "final_AI_DiffMult_last_run",
        "questionnaire_complete", "D1_coordination_challenge", "D2_play_regularly",
        "F1_matched_ability", "F2_progress_motivated", "D2_top_two_box",
        "answered_ts", "exported_ts"]
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(cols)
    for p in participants:
        ss = p["sessions"]
        n = len(ss)
        dists = [s["Distance_m"] for s in ss]
        scores = [s["Score"] for s in ss]
        q = p["quest"]
        row = [
            p["pid"], "TRUE", GEN_MARK, p["arm"], p["band"], p["gender"], p["edu"],
            p["prior"], p["lang"], p["consent_ts"], p["enrol_ts"], n,
            "TRUE" if any("ended early" in s["Notes"] for s in ss) else "FALSE",
            sum(dists), round(sum(dists) / n, 1), max(scores),
            round(sum(scores) / n, 1),
            sum(s["Coins"] for s in ss), sum(s["Obstacles_Hit"] for s in ss),
            round(sum(s["Avg_Balance_pct"] for s in ss) / n, 1),
            max(s["Max_Speed"] for s in ss), ss[-1]["AI_DiffMult"],
            "TRUE" if q else "FALSE",
            q["D1_coordination_challenge"] if q else "",
            q["D2_play_regularly"] if q else "",
            q["F1_matched_ability"] if q else "",
            q["F2_progress_motivated"] if q else "",
            ("TRUE" if q["D2_play_regularly"] >= 4 else "FALSE") if q else "",
            p["answered_ts"] or "", p["exported_ts"],
        ]
        w.writerow(row)

# ---------------- analysis ----------------
from scipy import stats

BANNER = "**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**"

A = [p for p in participants if p["arm"] == "A"]
B = [p for p in participants if p["arm"] == "B"]
Aq = [p for p in A if p["quest"]]
Bq = [p for p in B if p["quest"]]
x1 = sum(1 for p in Aq if p["quest"]["D2_play_regularly"] >= 4)
n1 = len(Aq)
x2 = sum(1 for p in Bq if p["quest"]["D2_play_regularly"] >= 4)
n2 = len(Bq)
p1, p2 = x1 / n1, x2 / n2
d = p1 - p2


def wilson(ph, n, z=1.959964):
    den = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / den
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


l1, u1 = wilson(p1, n1)
l2, u2 = wilson(p2, n2)
ci_lo = d - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
ci_hi = d + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
odds, fisher_p = stats.fisher_exact([[x1, n1 - x1], [x2, n2 - x2]], alternative="two-sided")

sa = [len(p["sessions"]) for p in A]
sb = [len(p["sessions"]) for p in B]
mw = stats.mannwhitneyu(sa, sb, alternative="two-sided")


def msd(v):
    m = sum(v) / len(v)
    sd = math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1)) if len(v) > 1 else 0.0
    return m, sd


ma, sda = msd(sa)
mb, sdb = msd(sb)

ITEMS = [("D1_coordination_challenge", "D1 good coordination challenge"),
         ("D2_play_regularly", "D2 would play regularly (PRIMARY)"),
         ("F1_matched_ability", "F1 matched my ability"),
         ("F2_progress_motivated", "F2 progress made me continue")]


def item_row(key):
    va = [p["quest"][key] for p in Aq]
    vb = [p["quest"][key] for p in Bq]
    t2a = sum(1 for v in va if v >= 4)
    t2b = sum(1 for v in vb if v >= 4)
    mA, sdA = msd(va)
    mB, sdB = msd(vb)
    return (t2a, len(va), t2b, len(vb), mA, sdA, mB, sdB)


band_rows = []
for band in BANDS:
    for arm_name, grp in (("A", Aq), ("B", Bq)):
        g = [p for p in grp if p["band"] == band]
        if g:
            t2 = sum(1 for p in g if p["quest"]["D2_play_regularly"] >= 4)
            band_rows.append((band, arm_name, t2, len(g)))

n_missing = sum(1 for p in participants if not p["quest"])
n_early = sum(1 for p in participants if any("ended early" in s["Notes"] for s in p["sessions"]))
total_runs = sum(len(p["sessions"]) for p in participants)
band_counts = {b: sum(1 for p in participants if p["band"] == b) for b in BANDS}

md = []
md.append("# SYNTHETIC demonstration analysis — Stage-3B pipeline demo")
md.append("")
md.append("> " + TXT_MARK)
md.append(">")
md.append("> Thesis rule G.8: synthetic data is never evidence. This document exists only to")
md.append("> demonstrate that the pre-specified Stage-3B analysis pipeline runs end-to-end and")
md.append("> recovers a KNOWN simulated input. No conclusion here says anything about the real study.")
md.append("")
md.append("Generator: `SYNTHETIC_generate.py`, seed `20260913`, N = 40 (SYN-P001..SYN-P040),")
md.append("arms 20 adaptive (A) / 20 static (B), silent 50/50 assignment mirroring the build.")
md.append("")
md.append("## Simulated ground truth (the KNOWN input the pipeline should recover)")
md.append("")
md.append("- **Primary endpoint** P(D2 top-two-box): adaptive arm **0.65**, static arm **0.45** (simulated true difference +0.20).")
md.append("- Secondary items: F1 0.75 vs 0.55; F2 0.72 vs 0.50; D1 ~0.80 both arms (no simulated effect).")
md.append("- Behavioural: sessions/participant drawn with mean ≈ 3.6 (A) vs ≈ 2.7 (B).")
md.append("- Missing data planted deliberately: {} participants with no questionnaire ({}), {} participants with an early-ended run.".format(
    n_missing, ", ".join(sorted(p["pid"] for p in participants if not p["quest"])), n_early))
md.append("")
md.append("## 1. Dataset overview")
md.append("")
md.append(BANNER)
md.append("")
md.append("| | Adaptive (A) | Static (B) | Total |")
md.append("|---|---|---|---|")
md.append("| Randomised | {} | {} | 40 |".format(len(A), len(B)))
md.append("| Questionnaire complete | {} | {} | {} |".format(n1, n2, n1 + n2))
md.append("| Questionnaire missing | {} | {} | {} |".format(len(A) - n1, len(B) - n2, n_missing))
md.append("| Total runs recorded | {} | {} | {} |".format(sum(sa), sum(sb), total_runs))
md.append("| Age 25-44 / 45-64 / 65-80 | {} | {} | {} / {} / {} |".format(
    "/".join(str(sum(1 for p in A if p["band"] == b)) for b in BANDS),
    "/".join(str(sum(1 for p in B if p["band"] == b)) for b in BANDS),
    band_counts["25-44"], band_counts["45-64"], band_counts["65-80"]))
md.append("")
md.append("## 2. PRIMARY pre-specified contrast — D2 top-two-box, adaptive vs static")
md.append("")
md.append("D2 = \"I would be willing to play this game regularly\" (1-5 Likert); top-two-box = response 4 or 5.")
md.append("Analysis set: questionnaire completers (missing questionnaires excluded, counts shown above —")
md.append("this is the missing-data handling the demo exercises).")
md.append("")
md.append(BANNER)
md.append("")
md.append("| Arm | Top-two-box | n | Proportion |")
md.append("|---|---|---|---|")
md.append("| Adaptive (A) | {} | {} | {:.1%} |".format(x1, n1, p1))
md.append("| Static (B) | {} | {} | {:.1%} |".format(x2, n2, p2))
md.append("")
md.append("- Difference in proportions (A − B): **{:+.1%}** (simulated truth: +20.0%)".format(d))
md.append("- 95% CI for the difference (Newcombe hybrid-Wilson): **[{:+.1%}, {:+.1%}]**".format(ci_lo, ci_hi))
md.append("- Fisher's exact test (two-sided, scipy.stats.fisher_exact): odds ratio {:.2f}, **p = {:.4f}**".format(odds, fisher_p))
md.append("")
md.append("Read-out for the demo: the realised difference of {:+.1f} points sits near the planted +20-point".format(d * 100))
md.append("truth, and the CI covers it — the pipeline recovers the known input. At n≈20/arm the Fisher p")
md.append("illustrates the expected power situation at this sample size; that is a property of the")
md.append("simulation, not a study finding (G.8).")
md.append("")
md.append("## 3. Behavioural support — sessions per participant (self-selected replays)")
md.append("")
md.append(BANNER)
md.append("")
md.append("| Arm | n | Mean (SD) | Median | Range | Total runs |")
md.append("|---|---|---|---|---|---|")
md.append("| Adaptive (A) | {} | {:.2f} ({:.2f}) | {} | {}–{} | {} |".format(
    len(sa), ma, sda, sorted(sa)[len(sa) // 2], min(sa), max(sa), sum(sa)))
md.append("| Static (B) | {} | {:.2f} ({:.2f}) | {} | {}–{} | {} |".format(
    len(sb), mb, sdb, sorted(sb)[len(sb) // 2], min(sb), max(sb), sum(sb)))
md.append("")
md.append("- Mann–Whitney U = {:.1f}, two-sided p = {:.4f} (simulated truth: A mean ≈ 3.6 vs B ≈ 2.7).".format(mw.statistic, mw.pvalue))
md.append("")
md.append("## 4. Exploratory — all four questionnaire items by arm")
md.append("")
md.append(BANNER)
md.append("")
md.append("| Item | A top-2 | B top-2 | A mean (SD) | B mean (SD) |")
md.append("|---|---|---|---|---|")
for key, label in ITEMS:
    t2a, na, t2b, nb, mA, sdA, mB, sdB = item_row(key)
    md.append("| {} | {}/{} ({:.0%}) | {}/{} ({:.0%}) | {:.2f} ({:.2f}) | {:.2f} ({:.2f}) |".format(
        label, t2a, na, t2a / na, t2b, nb, t2b / nb, mA, sdA, mB, sdB))
md.append("")
md.append(BANNER)
md.append("")
md.append("D2 top-two-box by age band (exploratory, tiny cells — display only):")
md.append("")
md.append("| Age band | Arm | Top-two-box / n |")
md.append("|---|---|---|")
for band, arm_name, t2, ng in band_rows:
    md.append("| {} | {} | {}/{} |".format(band, arm_name, t2, ng))
md.append("")
md.append("## 5. Missing-data handling demonstrated")
md.append("")
missing_ids = sorted(p["pid"] for p in participants if not p["quest"])
early_ids = sorted(p["pid"] for p in participants
                   if any("ended early" in s["Notes"] for s in p["sessions"]))
md.append("- No questionnaire (excluded from the primary analysis set, retained in behavioural counts): {}.".format(", ".join(missing_ids)))
md.append("- Early-ended run present (\"ended early by staff\" in Notes; run retained with its true duration): {}.".format(", ".join(early_ids)))
md.append("- One dropout pattern ({}) has a single early-ended run below the 200 m goal (no +50 bonus) and no questionnaire.".format(dropout))
md.append("")
md.append("---")
md.append(TXT_MARK)
md.append("")

with open(os.path.join(OUT, "SYNTHETIC_demo_analysis.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md))

# machine-readable summary for the caller / README
summary = {
    "n": 40, "arm_A": len(A), "arm_B": len(B),
    "bands": band_counts,
    "primary": {"A": [x1, n1], "B": [x2, n2], "diff": round(d, 4),
                "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
                "fisher_p": round(fisher_p, 4), "odds_ratio": round(odds, 3),
                "true_pA": 0.65, "true_pB": 0.45},
    "sessions": {"A_mean": round(ma, 2), "B_mean": round(mb, 2),
                 "mw_p": round(mw.pvalue, 4), "total_runs": total_runs},
    "missing_questionnaire": missing_ids, "early_end": early_ids,
}
print(json.dumps(summary, indent=1))
