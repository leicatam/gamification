# SYNTHETIC demonstration analysis — Stage-3B pipeline demo

> SYNTHETIC DEMONSTRATION DATA — generated 2026-09-13 by simulation for pipeline demonstration. NOT study data. NOT evidence.
>
> Thesis rule G.8: synthetic data is never evidence. This document exists only to
> demonstrate that the pre-specified Stage-3B analysis pipeline runs end-to-end and
> recovers a KNOWN simulated input. No conclusion here says anything about the real study.

Generator: `SYNTHETIC_generate.py`, seed `20260913`, N = 40 (SYN-P001..SYN-P040),
arms 20 adaptive (A) / 20 static (B), silent 50/50 assignment mirroring the build.

## Simulated ground truth (the KNOWN input the pipeline should recover)

- **Primary endpoint** P(D2 top-two-box): adaptive arm **0.65**, static arm **0.45** (simulated true difference +0.20).
- Secondary items: F1 0.75 vs 0.55; F2 0.72 vs 0.50; D1 ~0.80 both arms (no simulated effect).
- Behavioural: sessions/participant drawn with mean ≈ 3.6 (A) vs ≈ 2.7 (B).
- Missing data planted deliberately: 3 participants with no questionnaire (SYN-P001, SYN-P002, SYN-P008), 3 participants with an early-ended run.

## 1. Dataset overview

**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**

| | Adaptive (A) | Static (B) | Total |
|---|---|---|---|
| Randomised | 20 | 20 | 40 |
| Questionnaire complete | 19 | 18 | 37 |
| Questionnaire missing | 1 | 2 | 3 |
| Total runs recorded | 68 | 52 | 120 |
| Age 25-44 / 45-64 / 65-80 | 3/4/13 | 1/6/13 | 4 / 10 / 26 |

## 2. PRIMARY pre-specified contrast — D2 top-two-box, adaptive vs static

D2 = "I would be willing to play this game regularly" (1-5 Likert); top-two-box = response 4 or 5.
Analysis set: questionnaire completers (missing questionnaires excluded, counts shown above —
this is the missing-data handling the demo exercises).

**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**

| Arm | Top-two-box | n | Proportion |
|---|---|---|---|
| Adaptive (A) | 12 | 19 | 63.2% |
| Static (B) | 8 | 18 | 44.4% |

- Difference in proportions (A − B): **+18.7%** (simulated truth: +20.0%)
- 95% CI for the difference (Newcombe hybrid-Wilson): **[-12.4%, +45.3%]**
- Fisher's exact test (two-sided, scipy.stats.fisher_exact): odds ratio 2.14, **p = 0.3300**

Read-out for the demo: the realised difference of +18.7 points sits near the planted +20-point
truth, and the CI covers it — the pipeline recovers the known input. At n≈20/arm the Fisher p
illustrates the expected power situation at this sample size; that is a property of the
simulation, not a study finding (G.8).

## 3. Behavioural support — sessions per participant (self-selected replays)

**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**

| Arm | n | Mean (SD) | Median | Range | Total runs |
|---|---|---|---|---|---|
| Adaptive (A) | 20 | 3.40 (1.23) | 3 | 1–6 | 68 |
| Static (B) | 20 | 2.60 (1.14) | 3 | 1–5 | 52 |

- Mann–Whitney U = 278.5, two-sided p = 0.0269 (simulated truth: A mean ≈ 3.6 vs B ≈ 2.7).

## 4. Exploratory — all four questionnaire items by arm

**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**

| Item | A top-2 | B top-2 | A mean (SD) | B mean (SD) |
|---|---|---|---|---|
| D1 good coordination challenge | 18/19 (95%) | 12/18 (67%) | 4.21 (0.54) | 3.67 (1.24) |
| D2 would play regularly (PRIMARY) | 12/19 (63%) | 8/18 (44%) | 3.68 (1.11) | 3.17 (1.20) |
| F1 matched my ability | 15/19 (79%) | 12/18 (67%) | 3.89 (1.15) | 3.78 (1.06) |
| F2 progress made me continue | 11/19 (58%) | 10/18 (56%) | 3.68 (1.20) | 3.72 (0.75) |

**SYNTHETIC DEMONSTRATION — NOT STUDY DATA**

D2 top-two-box by age band (exploratory, tiny cells — display only):

| Age band | Arm | Top-two-box / n |
|---|---|---|
| 25-44 | A | 3/3 |
| 25-44 | B | 1/1 |
| 45-64 | A | 2/3 |
| 45-64 | B | 3/5 |
| 65-80 | A | 7/13 |
| 65-80 | B | 4/12 |

## 5. Missing-data handling demonstrated

- No questionnaire (excluded from the primary analysis set, retained in behavioural counts): SYN-P001, SYN-P002, SYN-P008.
- Early-ended run present ("ended early by staff" in Notes; run retained with its true duration): SYN-P003, SYN-P008, SYN-P009.
- One dropout pattern (SYN-P008) has a single early-ended run below the 200 m goal (no +50 bonus) and no questionnaire.

---
SYNTHETIC DEMONSTRATION DATA — generated 2026-09-13 by simulation for pipeline demonstration. NOT study data. NOT evidence.
