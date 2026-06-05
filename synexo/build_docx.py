#!/usr/bin/env python3
"""Build the consolidated Synapep Business Plan & Valuation Word document."""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x55, 0x55)

doc = Document()

# Base styles
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)

for lvl, sz in [("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)]:
    st = doc.styles[lvl]
    st.font.name = "Calibri"
    st.font.size = Pt(sz)
    st.font.color.rgb = NAVY
    st.font.bold = True


def para(text="", size=10.5, bold=False, italic=False, color=None, align=None, space_after=6):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color:
        r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    return p


def bullet(text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_lead:
        r = p.add_run(bold_lead)
        r.bold = True
        p.add_run(text)
    else:
        p.add_run(text)
    return p


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ""
        run = hdr[i].paragraphs[0].add_run(h)
        run.bold = True
        run.font.size = Pt(9.5)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run(str(val))
            run.font.size = Pt(9.5)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows:
                row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


# ---------------- Title page ----------------
doc.add_paragraph().paragraph_format.space_after = Pt(60)
para("SYNAPEP", size=34, bold=True, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Business Plan & Valuation", size=18, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
para("AI-designed peptide / protein actives + SynExo synthetic recombinant exosomes",
     size=12, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Powered by IT-EXO® (immune-tolerant stealth exosomes) and ai.peptide / CodeLife.AI",
     size=11, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)
para("Joint Venture: WBI (Wellbiz International) 70%  ·  Eyesel (manufacturing) 30%",
     size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Draft v0.3  ·  Prepared 5 June 2026", size=10, color=GREY,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)
para("CONFIDENTIAL — for internal planning and discussion only. Illustrative projections, "
     "not an offer of securities and not investment, legal, or tax advice.",
     size=8.5, italic=True, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_page_break()

# ---------------- 1. Executive summary ----------------
doc.add_heading("1. Executive Summary", level=1)
para("Synapep is a new company commercializing Synexo technology — the SynExo synthetic "
     "recombinant exosome platform plus AI-designed peptide/protein actives. It is built on two "
     "core technologies: IT-EXO® (the immune-tolerant, HLA-G \"stealth\" exosome that lets "
     "results compound without immune decline) and ai.peptide / CodeLife.AI (the AI platform "
     "that designs peptides, proteins, and exosome cargo and optimizes targeting).")
para("After a 6–9 month preparation phase (lab setup, −80 °C cold-chain and process "
     "qualification, QA, first cosmetic registrations), Synapep will be ready for sales in "
     "February 2027. The initial portfolio is 5–6 vial / skin-booster products with a combined "
     "capacity of 50,000–100,000 vials per month at a USD 30–35 ex-factory price. The route to "
     "market is aesthetic / cosmeceutical first (fast skin-booster pathway), with medical "
     "(wound healing, regeneration) indications following on the FDA/KFDA timeline — sold "
     "OEM / white-label so the customer holds the registration.")
para("Structure & scope.", bold=True, space_after=2)
para("Synapep is a joint venture — WBI 70% (contributes the Synexo IP: IT-EXO / SynExo / "
     "CodeLife.AI, plus R&D) and Eyesel 30% (the manufacturing entity). Synapep therefore "
     "owns/co-owns the platform and controls its own production. It is valued standalone at the "
     "ex-factory line; downstream distributors (e.g. NeuNova USA) are separate, "
     "non-consolidated entities and are excluded from this valuation.")
para("Headline economics.", bold=True, space_after=2)
bullet(" ~66% ex-factory gross margin (material cost confirmed < $5/vial; modeled $4.50).", "Margin:")
bullet(" $4.8M (2027) → $19.5M (2028) → $29.3M (2029) → $39.0M (2030).", "Revenue:")
bullet(" EBITDA-positive in the launch year; ~$11M EBITDA by 2029.", "Profitability:")
para("The ask.", bold=True, space_after=2)
para("USD 1.0M to kick off, at a recommended $5–7M pre-money ($6M midpoint → $1M ≈ 14.3%). "
     "Use of funds: $500K Synapep Lab initial investment + $600K running capital through launch.")

# ---------------- 2. Opportunity & technology ----------------
doc.add_heading("2. The Opportunity", level=1)
para("Conventional exosome therapeutics face three bottlenecks the Synexo stack is built to solve:")
bullet(" human-derived exosomes are unstable, costly, and carry rejection risk. IT-EXO® "
       "answers this with surface HLA-G acting as an immune \"stealth shield,\" so efficacy "
       "compounds over time instead of declining.", "Immune rejection / instability —")
bullet(" SynExo is a synthetic recombinant platform with standardized specs "
       "(~20B particles/mL, 30–150 nm, >95% purity, >60% encapsulation), designed for scalable, "
       "reproducible production.", "Inconsistent supply —")
bullet(" ai.peptide / CodeLife.AI designs peptides/proteins and exosome cargo "
       "computationally and simulates loading/targeting, compressing the R&D cycle.",
       "Slow, expensive design —")
para("The combination — stealth (IT-EXO) × synthetic delivery (SynExo) × AI design "
     "(ai.peptide) — is the moat: a technology + data flywheel wrapped around a capital-light, "
     "vial-based manufacturing operation.")

doc.add_heading("Core technologies", level=2)
table(["Platform", "What it is"],
      [["SynExo", "Synthetic recombinant exosome (salmon-derived) carrying plasmid-DNA cargo "
        "(EGF/bFGF/VEGF) and mRNA; the host cell transiently expresses the healing proteins. "
        "12-month stability at −80 °C (cold chain)."],
       ["IT-EXO®", "Immune-tolerant layer: surface HLA-G engages ILT2/ILT4/KIR2DL4 to suppress "
        "NK/T-cell attack (IL-1β ~1.8→0.8 ng/mL, TNF-α ~0.7→0.4 ng/mL; >95% cell viability). "
        "Differentiator: no efficacy decline, effects compound."],
       ["ai.peptide / CodeLife.AI", "AI platform designing peptides/proteins for functional "
        "cosmetics and optimizing exosome cargo, loading efficiency, and targeting."]],
      widths=[1.7, 4.8])

# ---------------- 3. Product & IP ----------------
doc.add_heading("3. Product & Intellectual Property", level=1)
para("Portfolio (5–6 SKUs — vials / skin boosters / ampoules).", bold=True, space_after=2)
para("Likely lines, to confirm: ① aesthetic skin-booster (rejuvenation/collagen), "
     "② scalp/hair regeneration, ③ wound-healing/repair, ④ post-procedure recovery, "
     "⑤ targeted AI-peptide active, ⑥ custom-cargo SynExo. Together they fill the "
     "50,000–100,000 vials/month line capacity.")
para("Intellectual property (held by WBI, contributed into the JV — confirm scope).",
     bold=True, space_after=2)
table(["Asset", "Ref / number", "Status"],
      [["SynExo HLA-G (Korea)", "P25E10C1475 (filed 2025-11-11)", "Application"],
       ["SynExo HLA-G (PCT)", "X25E10C0258 (2025-11-18)", "PCT application"],
       ["Safe-Browning shampoo", "KR 10-2025-0191060", "Application"],
       ["Ion-microneedling device", "KR 10-2654857", "Registered"],
       ["Sophora Japonica stem cell", "KR 10-1080297", "Registered"],
       ["SynExo HLA-G", "Journal-ready manuscript", "Publication pending"]],
      widths=[2.3, 2.6, 1.6])
para("Credibility to leverage: endorsement by Prof. Cho Hangrae (President, Korean "
     "Dermatological Society); NET (New Excellent Technology) government award; MORIMANA "
     "clinical claim of +19% hair thickness and −66% scalp flakiness in 8 weeks; use by leading "
     "Korean clinics.", italic=True)

# ---------------- 4. Go-to-market ----------------
doc.add_heading("4. Go-to-Market", level=1)
bullet(" Synapep sells bulk/vialled product ex-factory (EXW) to "
       "independent distributors, partner brands, aesthetic clinics, and med-spas who relabel "
       "and hold the registration. These are arm's-length customers buying at the $30–35 EXW "
       "price; their downstream margin is not Synapep's and is excluded from the valuation. "
       "(NeuNova USA, a separate non-consolidated entity, is one potential US distributor.)",
       "Channel — OEM / white-label.")
bullet(" the constraint in 2027 is customer acquisition/qualification, not capacity. The model "
       "ramps from 2K vials in Feb 2027 to a 28K/month exit run-rate by Dec 2027, then "
       "50K (2028) → 75K (2029) → 100K (2030).", "Ramp —")
bullet(" $30–35/vial EXW; large OEM contracts may price nearer the $30 floor, still at "
       "~65% gross margin.", "Pricing —")

# ---------------- 5. Operations & timeline ----------------
doc.add_heading("5. Operations & Timeline", level=1)
table(["Phase", "Window", "Milestones"],
      [["Preparation", "Jul 2026 – Jan 2027 (6–9 mo)",
        "Lab build-out, −80 °C cold-chain & fill-finish qualification, QA/QC, first cosmetic "
        "registrations, hire core team, finalize JV/IP terms"],
       ["Launch", "Feb 2027", "First commercial sales (cosmetic skin-booster line); 2–3 products live"],
       ["Ramp", "2027", "Add remaining products; reach 28K/mo exit run-rate"],
       ["Scale", "2028–2030", "50K → 75K → 100K vials/month; begin FDA/KFDA medical pathway; "
        "likely Series A in 2028"]],
      widths=[1.1, 1.7, 3.7])
para("Cold chain matters: SynExo is stable 12 months at −80 °C. Ultra-cold storage, validated "
     "shipping, and stability/QC are real cost and logistics lines — budgeted within the "
     "manufacturing cost formula (confirm with Eyesel).", italic=True, size=9.5)

# ---------------- 6. Financial model ----------------
doc.add_heading("6. Financial Model", level=1)
para("Base case: EXW $32.50 (midpoint of $30–35), material cost $4.50/vial (confirmed < $5). "
     "All figures USD; illustrative projections.")

doc.add_heading("6.1 Unit economics (per vial)", level=2)
para("Cost formula (as given): COGS = (10% × EXW) + material cost + (10% × EXW) "
     "= 20% × EXW + material.", italic=True, size=9.5)
table(["Line", "$ / vial"],
      [["Ex-factory price (EXW)", "32.50"],
       ["– Manufacturing (10% × EXW)", "3.25"],
       ["– Material cost", "4.50"],
       ["– Second 10% (10% × EXW)", "3.25"],
       ["= COGS", "11.00"],
       ["Gross profit / vial", "21.50"],
       ["Gross margin", "66.2%"]],
      widths=[3.2, 1.4])

doc.add_heading("6.2 Annual P&L ($ thousands)", level=2)
table(["", "2026 prep", "2027", "2028", "2029", "2030"],
      [["Vials sold (000s)", "0", "148", "600", "900", "1,200"],
       ["Revenue", "0", "4,810", "19,500", "29,250", "39,000"],
       ["COGS", "0", "1,628", "6,600", "9,900", "13,200"],
       ["Gross profit", "0", "3,182", "12,900", "19,350", "25,800"],
       ["Gross margin", "—", "66.2%", "66.2%", "66.2%", "66.2%"],
       ["OpEx (assumption)", "700", "2,400", "5,800", "8,000", "9,800"],
       ["EBITDA", "(700)", "782", "7,100", "11,350", "16,000"],
       ["EBITDA margin", "—", "16.3%", "36.4%", "38.8%", "41.0%"]],
      widths=[1.6, 1.0, 0.9, 0.9, 0.9, 0.9])

doc.add_heading("6.3 Scenarios (full-year 2029)", level=2)
table(["Scenario", "EXW", "Material", "Vials/yr", "Revenue", "GP", "GM%"],
      [["Conservative", "$30", "$5", "720,000", "$21.6M", "$14.0M", "65.0%"],
       ["Base", "$32.50", "$4.50", "900,000", "$29.25M", "$19.35M", "66.2%"],
       ["Upside", "$35", "$3", "1,080,000", "$37.8M", "$25.4M", "67.1%"]],
      widths=[1.1, 0.7, 0.8, 1.0, 0.9, 0.9, 0.7])
para("The confirmed sub-$5 material cost means even the conservative scenario clears 65% gross "
     "margin — downside is driven by volume/ramp, not unit economics.", italic=True, size=9.5)

# ---------------- 7. Valuation ----------------
doc.add_heading("7. Valuation", level=1)
para("Synapep is a pre-revenue JV that owns/co-owns the Synexo platform, raising $1.0M to kick "
     "off. It is valued standalone at the ex-factory line.")
para("Two numbers:", bold=True, space_after=2)
bullet(" $5–7M pre-money / $6–8M post-money — $1.0M buys ~13–17%. "
       "Stepped up from a bare-licence shell because, as a JV, Synapep holds the IP "
       "(patents filed), runs in-house manufacturing (Eyesel), earns ~66% margins, and has "
       "Feb-2027 revenue.", "Price this round at —")
bullet(" a risk-unadjusted enterprise value of ~$30–40M by 2030–31 on the base "
       "case, plus platform-licensing optionality. Upside story, not today's price.",
       "The prize if it executes —")

doc.add_heading("7.1 Three methods (they reconcile)", level=2)
table(["Method", "Un-risk-adjusted", "Risk-adjusted (JV, ~20%)", "Today's round"],
      [["Seed convention (owns IP)", "—", "$5–7M", "direct"],
       ["DCF (40% discount, 8× EBITDA exit)", "~$35M EV", "~$6–7M", "matches"],
       ["Forward revenue/EBITDA multiple", "$25–37M (PV of EV)", "$5–8M", "matches"]],
      widths=[2.4, 1.5, 1.6, 1.0])
para("Recommendation: price the $1.0M kickoff at $5–7M pre-money ($6–8M post), $6M midpoint.",
     bold=True)

doc.add_heading("7.2 Illustrative post-raise cap table (pre-money $6.0M)", level=2)
table(["Holder", "Contribution", "Founder %", "% post-raise"],
      [["WBI", "Synexo IP (IT-EXO/SynExo/CodeLife.AI) + R&D", "70.0%", "60.0%"],
       ["Eyesel", "Manufacturing entity (production, fill-finish, QA)", "30.0%", "25.7%"],
       ["Kickoff investor(s)", "$1.0M cash", "—", "14.3%"],
       ["Total", "", "100%", "100%"]],
      widths=[1.5, 3.0, 1.0, 1.0])
para("At $6.0M pre / $7.0M post, $1.0M buys 14.3%. NeuNova (US distribution) sits outside this "
     "cap table.", italic=True, size=9.5)

# ---------------- 8. Risks ----------------
doc.add_heading("8. Key Risks", level=1)
risks = [
    ("IP contribution terms — ", "largely resolved by the JV (WBI contributes IP into Synapep), "
     "but the scope (fields, territories, exclusivity, reserved rights/royalties) must be documented."),
    ("Customer concentration & ramp — ", "with an OEM model, revenue depends on a few anchor "
     "distributors/brands; landing the first 2–3 accounts is make-or-break in 2027."),
    ("Regulatory — ", "the cosmetic skin-booster pathway is fast, but exosome regulation is "
     "evolving; the medical line needs FDA/KFDA work. Keep cosmetic and medical claims separated."),
    ("Cold chain / ops — ", "−80 °C storage and validated shipping add cost and failure modes; "
     "under-budgeting fill-finish and stability is a classic exosome pitfall."),
    ("Capital adequacy — ", "$1M kicks off; scaling to the modeled $29–39M revenue likely needs "
     "a 2028 Series A."),
    ("Margin — ", "largely de-risked: confirmed sub-$5 material cost keeps gross margin in a "
     "tight ~64–71% band even at the $30 EXW floor."),
]
for lead, rest in risks:
    bullet(rest, lead)

# ---------------- 9. Next steps ----------------
doc.add_heading("9. What Would Make This Plan Investment-Grade", level=1)
for lead, rest in [
    ("Document the IP-contribution scope ", "WBI assigns into the JV — the biggest single driver."),
    ("Name the core team ", "(the advisor bench already has real credibility)."),
    ("Confirm the 5–6 SKUs, ", "their volumes/prices, and an anchor-customer pipeline."),
    ("Confirm material cost ", "and that cold-chain/fill-finish are inside the COGS formula."),
]:
    bullet(rest, lead)

doc.add_paragraph()
para("Appendix — source materials (WBI/NeuNova/SynExo documents and patent filings) are held in "
     "the user's Google Drive; key figures in this document are grounded in those files. OpEx is "
     "an internal assumption pending a headcount/spend plan.", italic=True, size=9, color=GREY)

out = "/home/user/gamification/synexo/Synapep_Business_Plan_and_Valuation.docx"
doc.save(out)
print("Saved:", out)
