# Thesis Final-Revision Memo — Tam V5 EngD Draft

**Input:** `Tam_V4_EngD_Thesis_Academic_Revision_Draft_11072026.docx`
**Output:** `Tam_V5_EngD_Thesis_Final_Revision_Draft.docx`
**Date:** 11 July 2026

This memo records every change applied in the V4 → V5 revision pass, and lists
the data items that only the author can supply. No statistics, ethics records,
instrument wordings or reliability figures were invented anywhere in the
revision: wherever real data is required, the document now carries a clearly
highlighted placeholder instead.

Placeholder conventions used in the document:

- **Yellow highlight — `[AUTHOR INPUT REQUIRED: …]`** — data or records only the
  author can supply.
- **Green highlight — `[INSERT PHOTOGRAPH/SCREENSHOTS/FIGURE HERE: …]`** — a
  reserved position for an image, each with a ready-made caption beneath it.

---

## 1. AUTHOR ACTION REQUIRED blocks — all resolved or converted (12 blocks)

| Location | What was done |
|---|---|
| §3.4 Ethics | Rewritten into final prose; placeholder for the HSESC approval number, date and coverage statement. PIPL statute citation added. |
| §5.5 Cox model | Rewritten; immortal-time-bias handling (time-varying covariate) specified; **the previously reported CI (1.89–5.56) was flagged as statistically impossible for N=30** (it implies ≈50+ events) and withheld pending re-fit from the participant-level survival file. The HR point estimate is retained. Abstract, §9 summary, Table 6.5, Figure 5.4 caption and the List of Figures were made consistent. |
| §5.5 Cohen's d | Approximate 95% CIs computed from the reported summary statistics (normal approximation) and labelled as such: d = 2.22 (1.00–3.44), d = 0.78 (0.37–1.19), d = 0.57 (0.18–0.96). Zero-change analysis now explicitly labelled a conservative sensitivity analysis, not ITT. Placeholder for the participant-level pre/post change plot (suggested Figure 5.4B). |
| §5.5 Figure 5.4 | Green placeholder box with a full generation specification (strata, numbers at risk, censoring marks, axis labels). |
| §5.5 Table 5.3 | Placeholder requiring raw counts and denominators (7/8 vs 4/22 sustained; the 85.7% FRA-change figure implies 6/7 — denominators to confirm), the classification rubric, coders and inter-coder agreement. Reverse-causality caution merged into the main prose. |
| §5.6 / Appendix B | The 13-attribute vs 0–10 range discrepancy converted into a defined requirement: state the item-to-composite mapping rule; Appendix B prose finalised accordingly. |
| §6.4 | Editorial sentence converted to a placeholder (recruitment sources, eligibility, staff scripts, software-version differences). |
| Table 6.3 | Placeholder for the missing per-age-band coordination-endorsement percentages (only the 71.7% total exists). |
| §8.9 Reproducibility | Rewritten into final prose; placeholders for the exact AI endpoint record and the outstanding appendix documentation. |
| Appendices A, B, C, D | Each AUTHOR ACTION converted to a specific highlighted placeholder (verbatim bilingual instrument wordings, back-translation record, inter-rater statistics, coding rules table, Cohen's κ, worked examples, consent script, sample transcript, scale reliability α). |
| Appendix G | Restructured into items G.1–G.7 with per-item placeholders (datasets, photographs, screenshots, AI-prompt archive). |

## 2. Missing figures

- **Figure 5.4 (Kaplan-Meier)** — confirmed absent at file level (13 images vs 15
  listed figures; the image following the 5.4 caption is actually the Figure 5.5
  flow diagram). A generation-spec placeholder now marks the position. It cannot
  be produced without the participant-level survival dataset (item G.2).
- **Figure 6.1 (Stage-3 retention by age band)** — also found to be missing.
  Because its data are fully reported in Table 6.2, the chart was **regenerated
  from the thesis's own reported counts** and embedded, with a note asking the
  author to confirm it against the Stage-3 records.

## 3. Photograph placeholders added (per author request)

| Figure | Position | Content |
|---|---|---|
| 4.1B | §4.1A, after the FRA architecture figure | The InBody FRA510S machine in situ (Guangzhou) |
| 5.1A | §5.3.1 | The Stage-2 play station (pressure panel + display) |
| 5.1B | §5.3.3, after Figure 5.1 | Game artefact: screenshots at difficulty levels 1–5 |
| 5.3A | §5.4 | Participants playing the game (consented) |
| 6.0A | §6.4 | Stage-3 Hong Kong community deployment |
| App G.4–G.6 | Appendix G | Deployment photographs and screenshots |

A note at the head of the List of Figures reminds the author to regenerate the
list and page numbers after insertion.

## 4. Citation and reference audit

- **~40 orphaned reference entries** (listed but never cited) were repaired by
  inserting in-text citations at their natural anchor points across §§1.3, 1.4,
  2.2.3, 2.3.1, 2.4.2, 2.5.5, 2.6.2B, 2.7.1, 2.7.2, 2.7.4, 3.4, 3.6, 4.4, 8.6A,
  8.8 and 9.8C. Every entry in the reference list is now cited in the body, and
  every in-text citation resolves to an entry.
- **Verified against publisher records** (web check):
  - *Altmeyer, Lessel & Krüger (2018)* — **pages and DOI were wrong**; corrected
    to pp. 453–458, doi:10.1145/3196709.3196799.
  - *Park et al. (2019)* — full eight-author list inserted (APA 7 forbids
    "et al." in the reference list); DOI added.
  - *An, Cheung & Willoughby (2024)* — "Article 123456" confirmed as the genuine
    article number (not a placeholder); DOI added.
  - *An, Cheung & Lo (2025)*, *Kim, Kim & Won (2018)* — confirmed; DOIs added.
  - *Locke & Latham (2002)* and *Ryan & Deci (2000)* — verified classics;
    bracketed author notes removed.
- **Added:** WHO (2024) *Ageing and health* fact sheet (anchors the §1.3
  demographic claim, which previously had no source).
- **Removed:** the meta-commentary paragraph at the head of the reference list.

## 5. Internal consistency repairs

- The Layer-2 AI vendor contradiction (§5.3 said "OpenAI API", §5.3.4 said
  "Claude API", Appendix E said "OpenAI") is harmonised to neutral wording, with
  one placeholder in §8.9/Appendix G requiring the actual deployed endpoint,
  model version, prompts and settings.
- All editorial voice ("The final thesis must report…", "this discrepancy must
  be resolved…") converted to normal academic prose or explicit placeholders.

## 6. Consolidated author-input request list (15 highlighted placeholders)

Data/records needed to close the document — nothing else blocks binding:

1. HSESC ethics approval reference number, date and coverage statement (§3.4).
2. Participant-level Stage-2 survival dataset → re-fit Cox model; regenerate
   the CI/p-value and the Figure 5.4 Kaplan-Meier plot (§5.5, G.2).
3. Participant-level FRA index pre/post data → exact Cohen's d CIs and the
   change plot (§5.5).
4. Table 5.3 raw counts/denominators + classification rubric + inter-coder
   agreement (§5.5).
5. FIAS 13-item → 0–10 mapping rule and full coding table (§5.6, Appendix B).
6. Stage-3 recruitment/eligibility/protocol documentation (§6.4).
7. Table 6.3 per-band endorsement percentages (§6.5).
8. AI endpoint record: vendor, model, version, prompts, settings (§8.9, G.7).
9. Appendix A: Mandarin item wording, back-translation, inter-rater stats.
10. Appendix B: coding rules table, Cohen's κ, worked examples.
11. Appendix C: bilingual wording, consent script, sample transcript.
12. Appendix D: trilingual item wording, scale reliability (α).
13. Appendix G: the three datasets and the prompt archive (G.1–G.3, G.7).
14. Photographs: FRA machine, play station, participants, Stage-3 site (green boxes).
15. Screenshots of the game at each difficulty level (Figure 5.1B, G.6).
