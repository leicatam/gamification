#!/usr/bin/env python3
"""Build the consolidated Synapep v0.4 Business Plan & Valuation Word (.docx) document."""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

NAVY = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x55, 0x55, 0x55)

doc = Document()
normal = doc.styles["Normal"]
normal.font.name = "Calibri"; normal.font.size = Pt(10.5)
for lvl, sz in [("Heading 1", 16), ("Heading 2", 13), ("Heading 3", 11.5)]:
    st = doc.styles[lvl]; st.font.name = "Calibri"; st.font.size = Pt(sz)
    st.font.color.rgb = NAVY; st.font.bold = True


def para(text="", size=10.5, bold=False, italic=False, color=None, align=None, space_after=6):
    p = doc.add_paragraph()
    if align: p.alignment = align
    r = p.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if color: r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(space_after)
    return p


def bullet(text, bold_lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if bold_lead:
        r = p.add_run(bold_lead); r.bold = True; p.add_run(text)
    else:
        p.add_run(text)
    return p


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        run = t.rows[0].cells[i].paragraphs[0].add_run(h); run.bold = True; run.font.size = Pt(9.5)
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            run = cells[i].paragraphs[0].add_run(str(val)); run.font.size = Pt(9.5)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows: row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


# Title page
doc.add_paragraph().paragraph_format.space_after = Pt(60)
para("SYNAPEP", size=34, bold=True, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Business Plan & Valuation", size=18, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
para("AI-personalised regenerative aesthetic medicine — physician-configured peptide treatments",
     size=12, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Powered by CodeLife.AI (proprietary model) · IT-EXO® · SynExo",
     size=11, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)
para("Joint Venture: WBI (Wellbiz International) 70%  ·  Eyesel (manufacturing) 30%",
     size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Draft v0.4  ·  Prepared 6 June 2026", size=10, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=40)
para("CONFIDENTIAL — for internal planning and discussion only. Illustrative projections, not an "
     "offer of securities and not investment, legal, or tax advice.",
     size=8.5, italic=True, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_page_break()

# 1 Executive summary
doc.add_heading("1. Executive Summary", level=1)
para("Synapep delivers AI-personalised regenerative aesthetic treatments. Physicians use "
     "CodeLife.AI — our proprietary aesthetic-medicine model — to configure peptide-based "
     "microneedling and intramuscular (IM) treatment kits to each clinical purpose, delivered as "
     "registered medical devices and powered by IT-EXO® (immune-tolerant stealth exosomes) and "
     "SynExo (synthetic recombinant exosomes).")
para("The wedge is a razor-and-blades business — an applicator device placed in clinics plus "
     "recurring personalised treatment kits (~$30–35 ex-factory). The durable asset is the AI "
     "engine and the data it compounds: peptides engineered to outperform generalised, off-the-"
     "shelf products, validated by our own AI quality-and-analytics tools. The long-run vision is "
     "a data-science company in aesthetic medicine built on our own large model.")
para("Why now / why this works.", bold=True, space_after=2)
bullet(" medical aesthetics ≈ $17–18.5B (2024), ~10–13% CAGR → ~$56B by 2033; injectables >40% of "
       "revenue. Korea is a global aesthetic hub; Hong Kong a gateway.", "Large, growing market:")
bullet(" Korea MFDS \"modified device\" path (same intended use / mechanism / raw materials → "
       "~3 months), then Hong Kong's light, voluntary MDACS listing. Personalised by purpose, not "
       "per individual, so variants stay inside a registered family.", "Regulatory speed:")
bullet(" AI-personalised regenerative devices sit beside (not replace) HA fillers and botox.",
       "New category:")
para("Structure & scope.", bold=True, space_after=2)
para("JV — WBI 70% (IP: CodeLife.AI / IT-EXO / SynExo + R&D) and Eyesel 30% (manufacturing). Valued "
     "standalone at the ex-factory line; distributors are separate, non-consolidated.")
para("Economics & ask.", bold=True, space_after=2)
para("~65% blended gross margin; revenue $5.3M (2027) → $20.3M (2028) → $30.2M (2029) → $39.9M "
     "(2030); EBITDA-positive in the launch year. Raising $1.0M to kick off at $5–7M pre-money "
     "($6M midpoint → $1M ≈ 14.3%). The AI/data-platform thesis underpins a premium, "
     "institutional-AI Series A in 2028.")

# 2 Technology & AI moat
doc.add_heading("2. Technology & the AI Moat", level=1)
para("Three pillars — the AI pillar is the spine; devices and kits are the wedge and the "
     "data-capture layer.")
table(["Pillar", "What it is / why it matters"],
      [["1 — AI engine & data flywheel", "CodeLife.AI designs personalised peptides engineered to "
        "OUTPERFORM generalised products (differentiator is performance, not just personalisation). "
        "A proprietary AI quality-&-analytics suite validates every batch/variant and improves the "
        "model from each treatment — a compounding data flywheel. Built as physician decision-support "
        "within a cleared envelope to manage SaMD exposure."],
       ["2 — Devices & kits (revenue wedge)", "An applicator device placed/sold to clinics (also the "
        "data-capture endpoint) plus recurring personalised treatment kits (~$30–35 ex-factory), "
        "CodeLife-configured within an approved device family."],
       ["3 — Data monetisation (future upside)", "Licensing the model/insights, physician outcome "
        "analytics, and R&D partnerships — the institutional-AI-investor story. Not in the base P&L."]],
      widths=[1.9, 4.6])
table(["Core technology", "What it is"],
      [["CodeLife.AI", "Proprietary AI platform/model designing peptides & proteins and optimising "
        "delivery within an approved envelope; basis of the data-science-company vision."],
       ["IT-EXO®", "Immune-tolerant layer: surface HLA-G suppresses NK/T-cell attack, so efficacy "
        "compounds rather than declines."],
       ["SynExo", "Synthetic recombinant exosome (salmon-derived) carrying growth-factor/peptide "
        "cargo; ~20B particles/mL, 30–150 nm, >95% purity; 12-month stability at −80 °C."]],
      widths=[1.7, 4.8])

# 3 Vision
doc.add_heading("3. Vision — From Devices to a Data-Science Company", level=1)
para("Devices and kits are the wedge that puts CodeLife into clinics and starts the data flywheel. "
     "As personalised treatments and outcomes accumulate, Synapep builds a proprietary "
     "aesthetic-medicine dataset and its own large model — the durable, compounding asset. The "
     "endpoint is a data-science company in aesthetic medicine: AI-designed, outcome-validated, "
     "continuously improving — and fundable by institutional AI investors.")

# 4 Regulatory
doc.add_heading("4. Regulatory Strategy (Korea → Hong Kong)", level=1)
bullet(" register the microneedling/topical applicator + kit as a device family; CodeLife variants "
       "register as \"modified devices\" (same intended use / mechanism / raw materials) on the fast "
       "path (Class I ≈ 15 business days; Class II \"modified\" via conformity bodies; ~3 months "
       "realistic).", "Korea (MFDS) first —")
bullet(" light, voluntary MDACS listing; move while the voluntary window is open (a statutory "
       "framework is coming).", "Hong Kong next —")
bullet(" personalise via device parameters (delivery, depth, concentration within an approved "
       "range, a menu of pre-cleared options), NOT by changing the active molecule, which would "
       "break the \"same raw materials\" test.", "Keep the fast path valid —")
bullet(" microneedling/topical line carries the device fast-path; the IM injectable line runs on a "
       "separate drug/cosmetic pathway (see Risks).", "Two tracks —")

# 5 GTM
doc.add_heading("5. Go-to-Market", level=1)
bullet(" aesthetic/derm physicians & clinics — Korea first, then Hong Kong.", "Customers —")
bullet(" place/sell the applicator device, then earn recurring revenue on personalised kits; "
       "CodeLife + outcome data make the relationship sticky.", "Model —")
bullet(" a focused clinical/KOL salesforce in two concentrated markets; physician advocates and "
       "head-to-head efficacy data drive adoption.", "Build —")

# 6 Financials
doc.add_heading("6. Financial Model", level=1)
para("Bottom-up by clinics (~100–125 kits/clinic/month at maturity). Kit unit economics: "
     "COGS = 20%×EXW + $4.50 material = $11.00 at $32.50 → GP $21.50, 66.2%. Device ASP $3,000 at "
     "40% GM. All figures USD; illustrative.")
table(["Driver", "2026 prep", "2027", "2028", "2029", "2030"],
      [["Clinics (cumulative)", "0", "150", "400", "700", "1,000"],
       ["New clinics (devices sold)", "0", "150", "250", "300", "300"],
       ["Treatment kits (000s)", "0", "148", "600", "900", "1,200"]],
      widths=[2.0, 0.9, 0.8, 0.8, 0.8, 0.8])
doc.add_heading("6.1 P&L ($ thousands)", level=2)
table(["Line", "2026", "2027", "2028", "2029", "2030"],
      [["Kit revenue ($32.50)", "0", "4,810", "19,500", "29,250", "39,000"],
       ["Device revenue ($3k ASP)", "0", "450", "750", "900", "900"],
       ["Total revenue", "0", "5,260", "20,250", "30,150", "39,900"],
       ["Kit gross profit (66.2%)", "0", "3,182", "12,900", "19,350", "25,800"],
       ["Device gross profit (40%)", "0", "180", "300", "360", "360"],
       ["Total gross profit", "0", "3,362", "13,200", "19,710", "26,160"],
       ["Blended gross margin", "—", "63.9%", "65.2%", "65.4%", "65.6%"],
       ["OpEx (sales, reg, R&D incl. AI, G&A)", "700", "2,600", "6,000", "8,200", "10,000"],
       ["EBITDA", "(700)", "762", "7,200", "11,510", "16,160"]],
      widths=[2.1, 0.8, 0.8, 0.85, 0.85, 0.85])
doc.add_heading("6.2 Scenarios (2029)", level=2)
table(["Scenario", "Clinics", "EXW", "Revenue", "Gross profit"],
      [["Conservative", "~500", "$30", "~$22M", "~$14M"],
       ["Base", "700", "$32.50", "$30.2M", "$19.7M"],
       ["Upside", "~850", "$35", "~$38M", "~$25M"]],
      widths=[1.3, 1.0, 0.9, 1.1, 1.1])
para("Pillar-3 data monetisation (model/insight licensing, outcome analytics) is excluded from the "
     "base P&L and treated as upside.", italic=True, size=9.5)

# 7 Valuation
doc.add_heading("7. Valuation — Two Lenses", level=1)
para("Lens A — device + consumables business (the floor; sets the kickoff price).", bold=True, space_after=2)
para("Recommend $5–7M pre-money / $6–8M post, $6M midpoint → $1.0M buys ~14.3%. Three methods "
     "reconcile: seed convention for an IP-owning JV ($5–7M); DCF (40% discount, 8× EBITDA exit) "
     "≈ $35M un-risk-adjusted EV → ~$5–7M risk-adjusted; forward multiple. Recurring medical "
     "consumables + regulatory moat support the upper half and a higher revenue multiple (3–6×).")
para("Lens B — AI / data-science company (the prize; attracts institutional AI capital).", bold=True, space_after=2)
para("With a proprietary model, an AI-QA/analytics suite, and a compounding data flywheel, the "
     "comparables shift from medtech to AI/data platforms — much higher multiples. This does not "
     "change the $1M kickoff price (priced on Lens A) but raises the valuation ceiling and reframes "
     "the 2028 Series A as a premium, institutional AI round.")
doc.add_heading("7.1 Cap table (post-raise, $6.0M pre-money)", level=2)
table(["Holder", "Contribution", "Founder %", "% post-raise"],
      [["WBI", "IP (CodeLife.AI/IT-EXO/SynExo) + R&D", "70.0%", "60.0%"],
       ["Eyesel", "Manufacturing (production, fill-finish, QA)", "30.0%", "25.7%"],
       ["Kickoff investor(s)", "$1.0M cash", "—", "14.3%"],
       ["Total", "", "100%", "100%"]],
      widths=[1.5, 3.0, 1.0, 1.0])
para("Recommendation: price the kickoff on Lens A ($6M midpoint); pitch Lens B as the prize and the "
     "Series A thesis. Optionally test institutional-AI appetite for a larger round.", italic=True, size=9.5)

# 8 Risks
doc.add_heading("8. Key Risks", level=1)
for lead, rest in [
    ("Device-vs-drug classification (#1) — ", "an IM injectable peptide is very likely a "
     "drug/biologic, not a device, in Korea and HK. Lead the device fast-path with the "
     "microneedling/topical line + applicator system; run the IM/injectable line on a separate track."),
    ("\"Same raw materials\" constraint — ", "personalise via device parameters within an approved "
     "envelope; changing the active molecule can break the fast path."),
    ("AI substantiation — ", "the \"outperforms generalised products\" and data-moat claims need "
     "head-to-head efficacy evidence and a real ML capability/dataset behind the \"own large model.\""),
    ("SaMD exposure — ", "CodeLife may be regulated as Software as a Medical Device; keep the "
     "physician in the loop within a cleared envelope."),
    ("Incumbents — ", "HA/botox (~$5–6.5B, still growing) are not displaced — position as a new "
     "adjacent category."),
    ("Capital adequacy — ", "$1M kicks off; multi-market registration + clinical salesforce + AI "
     "team likely need a 2028 Series A."),
]:
    bullet(rest, lead)

# 9 Next steps
doc.add_heading("9. What Would Make This Investment-Grade", level=1)
for lead, rest in [
    ("Confirm the regulatory split ", "— microneedling/topical (device fast-path) vs IM injectable (drug)."),
    ("Produce head-to-head efficacy data ", "(AI-personalised vs generalised) and define the AI/data "
     "team and dataset plan behind the \"own large model.\""),
    ("Document the IP-contribution scope ", "WBI assigns into the JV."),
    ("Confirm device ASP/GM, clinic ramp, kits/clinic/month; ", "name the core team and an "
     "anchor-clinic pipeline in Korea/HK."),
]:
    bullet(rest, lead)
doc.add_paragraph()
para("Sources — medical aesthetics market: MarketsandMarkets, P&S Intelligence, DataM. Korea MFDS "
     "modified-device path: Emergo by UL, ElendiLabs, MedDeviceGuide. Hong Kong MDACS: mdd.gov.hk, "
     "Asia Actual. Botox/HA: Future Market Insights, Allied Market Research, Grand View Research.",
     italic=True, size=9, color=GREY)

out = "/home/user/gamification/synexo/Synapep_Business_Plan_and_Valuation.docx"
doc.save(out)
print("Saved:", out)
