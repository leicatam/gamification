#!/usr/bin/env python3
"""Build the investor deck -> Synapep_Investor_Deck.pptx. Numbers single-sourced from the model."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
import build_multimarket_model as mm

DIR = "/home/user/gamification/synexo/"
NAVY = RGBColor(0x1F, 0x3A, 0x5F); ACCENT = RGBColor(0x2E, 0x86, 0xC1)
GREY = RGBColor(0x55, 0x55, 0x55); LIGHT = RGBColor(0xED, 0xF1, 0xF5)
WHITE = RGBColor(0xFF, 0xFF, 0xFF); RED = RGBColor(0xC0, 0x39, 0x2B)
Y = mm.YEARS; R = mm.RESULTS

prs = Presentation()
prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = prs.slide_width, prs.slide_height


def _set(tf_para, text, size, bold=False, color=NAVY, italic=False):
    tf_para.text = text
    for r in tf_para.runs:
        r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
        r.font.italic = italic; r.font.name = "Calibri"


def box(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(l, t, w, h); tb.text_frame.word_wrap = True
    return tb.text_frame


def rect(slide, l, t, w, h, color):
    from pptx.enum.shapes import MSO_SHAPE
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = color; sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


def header(slide, title, n):
    rect(slide, 0, 0, SW, Inches(1.15), NAVY)
    rect(slide, Inches(0.5), Inches(0.35), Inches(0.12), Inches(0.45), ACCENT)
    tf = box(slide, Inches(0.75), Inches(0.22), Inches(11.8), Inches(0.75))
    _set(tf.paragraphs[0], title, 26, bold=True, color=WHITE)
    fn = box(slide, Inches(12.0), Inches(7.05), Inches(1.1), Inches(0.35))
    _set(fn.paragraphs[0], str(n), 11, color=GREY); fn.paragraphs[0].alignment = PP_ALIGN.RIGHT


def bullets(slide, items, left=Inches(0.85), top=Inches(1.5), width=Inches(11.6), height=Inches(5.4),
            size=17):
    tf = box(slide, left, top, width, height)
    for i, it in enumerate(items):
        txt, lvl = it if isinstance(it, tuple) else (it, 0)
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = lvl
        run = p.add_run(); run.text = ("•  " if lvl == 0 else "–  ") + txt
        run.font.size = Pt(size - lvl * 2); run.font.name = "Calibri"
        run.font.color.rgb = NAVY if lvl == 0 else GREY
        p.space_after = Pt(9)
    return tf


def content_slide(title, n, items, size=17):
    s = prs.slides.add_slide(BLANK); header(s, title, n); bullets(s, items, size=size); return s


def lead_bullets(slide, items, top=Inches(1.5), size=16):
    """items: list of (lead, rest)."""
    tf = box(slide, Inches(0.85), top, Inches(11.6), Inches(5.4))
    for i, (lead, rest) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r1 = p.add_run(); r1.text = "•  " + lead; r1.font.bold = True
        r1.font.size = Pt(size); r1.font.color.rgb = NAVY; r1.font.name = "Calibri"
        r2 = p.add_run(); r2.text = rest; r2.font.size = Pt(size); r2.font.color.rgb = GREY
        r2.font.name = "Calibri"; p.space_after = Pt(10)
    return tf


def table_slide(title, n, headers, rows, col_w=None, fs=13, highlight_last=False):
    s = prs.slides.add_slide(BLANK); header(s, title, n)
    nr, nc = len(rows) + 1, len(headers)
    total_w = Inches(11.8); left = Inches(0.75); top = Inches(1.5)
    gt = s.shapes.add_table(nr, nc, left, top, total_w, Inches(0.4 * nr)).table
    if col_w:
        for i, w in enumerate(col_w): gt.columns[i].width = Inches(w)
    for j, h in enumerate(headers):
        c = gt.cell(0, j); c.text = h
        c.fill.solid(); c.fill.fore_color.rgb = NAVY
        for p in c.text_frame.paragraphs:
            for r in p.runs: r.font.size = Pt(fs); r.font.bold = True; r.font.color.rgb = WHITE
    for i, row in enumerate(rows, start=1):
        for j, v in enumerate(row):
            c = gt.cell(i, j); c.text = str(v)
            c.fill.solid(); c.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
            if highlight_last and i == len(rows):
                c.fill.fore_color.rgb = RGBColor(0xDD, 0xEA, 0xF4)
            for p in c.text_frame.paragraphs:
                for r in p.runs:
                    r.font.size = Pt(fs); r.font.color.rgb = NAVY
                    r.font.bold = (j == 0) or (highlight_last and i == len(rows))
    return s


# ---------------- 1 Title
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, SW, SH, NAVY)
rect(s, Inches(0.9), Inches(2.6), Inches(0.18), Inches(1.7), ACCENT)
tf = box(s, Inches(1.25), Inches(2.5), Inches(11), Inches(1.4))
_set(tf.paragraphs[0], "SYNAPEP", 54, bold=True, color=WHITE)
tf = box(s, Inches(1.3), Inches(3.9), Inches(11), Inches(1.0))
_set(tf.paragraphs[0], "AI-Personalised Aesthetic Medical Devices", 24, color=RGBColor(0xCF, 0xDD, 0xEA))
tf = box(s, Inches(1.3), Inches(4.7), Inches(11), Inches(0.8))
_set(tf.paragraphs[0], "Korea-anchored, export-led  •  Investor Deck", 16, italic=True,
     color=RGBColor(0x9F, 0xB6, 0xCB))
tf = box(s, Inches(1.3), Inches(6.6), Inches(11), Inches(0.5))
_set(tf.paragraphs[0], "Illustrative — not investment advice. Figures are v0.4 scenario estimates.",
     11, color=RGBColor(0x7F, 0x97, 0xAE))

# ---------------- 2 Opportunity
content_slide("The opportunity", 2, [
    "Medical aesthetics ≈ $17–18.5B (2024), ~10–13% CAGR → ~$56B by 2033",
    "Injectables >40% of revenue; Korea a global hub, Hong Kong a gateway",
    ("Commodity injectables (HA, botox) still grow but commoditise — buyers want differentiated, "
     "regenerative, personalised outcomes", 1),
    "Opening: an AI-personalised, physician-configured regenerative category — a new lane beside "
    "HA/botox, not a replacement",
])

# ---------------- 3 Solution
content_slide("The solution — device + recurring kits + AI", 3, [
    "Applicator device placed in clinics + recurring, CodeLife-configured peptide/exosome treatment "
    "kits, registered as a medical-device family",
    ("Personalised by physician purpose within an approved envelope — fast 'modified-device' "
     "registration, not bespoke per-patient devices", 1),
    "Razor-and-blades: device is the wedge and the data-capture endpoint; kits are the recurring "
    "revenue",
    ("Kit ~$30–35 ex-factory; ~64–67% gross margin; device ASP $3,000", 1),
])

# ---------------- 4 The moat
content_slide("The moat — AI efficacy + data flywheel", 4, [
    "Differentiator is performance, not merely personalisation: peptides engineered to outperform "
    "generalised, off-the-shelf products",
    "Proprietary AI-QA/analytics validate every batch and feed continuous improvement",
    ("Closed loop: treatment inputs/outcomes → better model → better peptides → deeper clinic "
     "lock-in", 1),
    "Vision: a data-science company in aesthetic medicine — devices/kits are the data layer",
    ("Honest framing: the day-one asset is the consented dataset + data-rights + analytics, not a "
     "foundation model", 1),
])

# ---------------- 5 Same product, more markets
s = prs.slides.add_slide(BLANK); header(s, "Same product, more markets", 5)
lead_bullets(s, [
    ("One product family — ", "the Korean-developed device + CodeLife kit is exported as-is"),
    ("No per-market R&D — ", "personalisation is by physician purpose within the same approved envelope"),
    ("Identical unit economics everywhere — ", "the only variables are clinic base and timing"),
    ("Scale + data benefits — ", "one production/QC/stability spec; one comparable global dataset"),
    ("Regulatory — ", "the Korean technical file is the master dossier for every reliance filing"),
], size=17)

# ---------------- 6 Regulatory
table_slide("Regulatory strategy (Korea → Hong Kong → export)", 6,
            ["Product line", "Pathway", "Speed / note"],
            [["Microneedling/topical kit + applicator", "Korea MFDS modified-device; HK MDACS listing",
              "Fast (~months) — the lead family"],
             ["IM / injectable peptide", "Drug/biologic (separate) or cosmetic", "Slower — doesn't gate launch"],
             ["CodeLife software", "Config/decision-support in cleared envelope", "Manages SaMD exposure"]],
            col_w=[4.2, 4.4, 3.2], fs=13)

# ---------------- 7 Export springboard
table_slide("Export springboard — KFDA reliance", 7,
            ["Tier", "Markets", "KFDA leverage"],
            [["Tier 1: ASEAN + Hong Kong", "HK, Vietnam, Singapore → Thailand, Malaysia, Indonesia, "
              "Philippines", "MDACS reference; VN accepts MFDS; ASEAN CSDT cascade"],
             ["Tier 2: GCC + Greater China", "Saudi, UAE; Taiwan; China", "SFDA regional reference; "
              "TFDA uses Korean data; China via Hainan"]],
            col_w=[3.0, 5.0, 3.8], fs=12.5)

# ---------------- 8 Financials chart
s = prs.slides.add_slide(BLANK); header(s, "Multi-market revenue — 3 scenarios", 8)
cd = CategoryChartData(); cd.categories = [str(y) for y in Y]
for scn in mm.ORDER:
    cd.add_series(scn, tuple(R[scn][0][y]["tot_rev"] / 1e6 for y in Y))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.7), Inches(1.4), Inches(8.2),
                        Inches(5.4), cd)
chart = gf.chart; chart.has_legend = True; chart.legend.position = XL_LEGEND_POSITION.BOTTOM
chart.legend.include_in_layout = False
chart.value_axis.has_title = True; chart.value_axis.axis_title.text_frame.text = "Revenue ($M)"
for i, scn in enumerate(mm.ORDER):
    ser = chart.series[i]; ser.format.fill.solid()
    ser.format.fill.fore_color.rgb = [GREY, ACCENT, NAVY][i]
tf = box(s, Inches(9.2), Inches(1.6), Inches(3.7), Inches(5.0))
for i, scn in enumerate(mm.ORDER):
    r = R[scn][0][2030]
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    run = p.add_run(); run.text = "%s 2030" % scn
    run.font.bold = True; run.font.size = Pt(15); run.font.color.rgb = NAVY; run.font.name = "Calibri"
    p2 = tf.add_paragraph(); r2 = p2.add_run()
    r2.text = "  %s rev  •  %s EBITDA\n  %s clinics  •  %.0f%% GM" % (
        "$%.0fM" % (r["tot_rev"] / 1e6), "$%.0fM" % (r["ebitda"] / 1e6),
        "{:,}".format(r["cum"]), r["gm"] * 100)
    r2.font.size = Pt(12); r2.font.color.rgb = GREY; r2.font.name = "Calibri"; p2.space_after = Pt(12)

# ---------------- 9 Scenario assumptions table
table_slide("Scenario assumptions (product unchanged)", 9,
            ["Lever", "Conservative", "Base", "Upside"],
            [["Markets", "11 (China excl.)", "12", "12"],
             ["Clinic ramp vs base", "0.62×", "1.00×", "1.30×"],
             ["Kit EXW", "$30.00", "$32.50", "$35.00"],
             ["Kit gross margin", "%.0f%%" % (mm.kit_gm(30) * 100), "%.0f%%" % (mm.kit_gm(32.5) * 100),
              "%.0f%%" % (mm.kit_gm(35) * 100)],
             ["Device GM", "35%", "40%", "42%"],
             ["Kits/clinic/yr", "1,200", "1,400", "1,500"]],
            col_w=[3.4, 2.9, 2.8, 2.7], fs=13)

# ---------------- 10 Valuation
s = prs.slides.add_slide(BLANK); header(s, "Valuation — two lenses", 10)
lead_bullets(s, [
    ("Lens A (priced today) — ", "device/consumables floor: $5–7M pre; $6M midpoint for the $1M kickoff"),
    ("Lens B (upside) — ", "AI/data-science company: medtech → AI multiples; premium Series A in 2028"),
], top=Inches(1.5), size=17)
gt = s.shapes.add_table(4, 3, Inches(0.85), Inches(3.4), Inches(7.0), Inches(2.2)).table
for j, h in enumerate(["Holder", "Pre", "Post-raise"]):
    c = gt.cell(0, j); c.text = h; c.fill.solid(); c.fill.fore_color.rgb = NAVY
    for p in c.text_frame.paragraphs:
        for r in p.runs: r.font.color.rgb = WHITE; r.font.bold = True; r.font.size = Pt(13)
for i, row in enumerate([["WBI", "70.0%", "60.0%"], ["Eyesel", "30.0%", "25.7%"],
                         ["Investor (SAFE)", "—", "14.3%"]], start=1):
    for j, v in enumerate(row):
        c = gt.cell(i, j); c.text = v; c.fill.solid()
        c.fill.fore_color.rgb = LIGHT if i % 2 else WHITE
        for p in c.text_frame.paragraphs:
            for r in p.runs: r.font.size = Pt(13); r.font.color.rgb = NAVY

# ---------------- 11 The ask
content_slide("The ask — milestone-gated SAFE", 11, [
    "US$1.0M kickoff — post-money SAFE, $6.0M cap, 20% discount, MFN",
    ("Two tranches: $400k at close · $600k on milestones", 1),
    "Conditions precedent: WBI IP into the JV; verify the $25M sample; clinic data-rights clause",
    "Milestones: cold-chain spec + COGS BOM; 5–10 anchor clinics w/ reorders; one prospective "
    "readout; classification memo",
    "Use of funds: Korea launch + Wave-1 export (HK/Vietnam/Singapore); CodeLife v1; QC/stability",
])

# ---------------- 12 What we'll prove (honest slide)
s = prs.slides.add_slide(BLANK); header(s, "What we will prove (diligence-ready)", 12)
lead_bullets(s, [
    ("RED — cold chain & COGS: ", "reformulate to 2–8 °C / ambient; publish a bottom-up BOM"),
    ("Validation pack: ", "the $25M at entity/product/channel level + reorder cohorts"),
    ("Formulation envelope: ", "clean AND clinically differentiating within the approved family"),
    ("Exosome discipline: ", "non-human (salmon/synthetic) origin; function-based claims"),
    ("Data moat: ", "CodeLife v1 demo + data-rights in the clinic contract"),
], size=16)

# ---------------- 13 Roadmap
table_slide("Roadmap", 13, ["Phase", "Markets", "Milestones"],
            [["2027 — Anchor", "Korea", "Registration; anchor clinics; CodeLife v1"],
             ["2027–28 — Wave 1", "Hong Kong, Vietnam, Singapore", "Reliance filings; reorder evidence"],
             ["2028–29 — Wave 2", "Thailand, Malaysia, Indonesia, Philippines; Saudi, UAE",
              "ASEAN CSDT cascade; SFDA; Series A"],
             ["2029–30 — Wave 3", "Taiwan, China (Hainan→NMPA)", "Greater-China entry"]],
            col_w=[2.6, 5.4, 3.8], fs=12.5)

# ---------------- 14 Closing
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, SW, SH, NAVY)
rect(s, Inches(0.9), Inches(2.7), Inches(0.18), Inches(1.5), ACCENT)
tf = box(s, Inches(1.25), Inches(2.6), Inches(11), Inches(1.2))
_set(tf.paragraphs[0], "Same product. More markets. A data moat.", 34, bold=True, color=WHITE)
tf = box(s, Inches(1.3), Inches(3.9), Inches(11.2), Inches(1.6))
_set(tf.paragraphs[0],
     "Base case ~$%.0fM revenue / ~$%.0fM EBITDA by 2030 across 12 markets on one Korean-developed "
     "product. $1M milestone-gated kickoff." % (R["Base"][0][2030]["tot_rev"] / 1e6,
                                                R["Base"][0][2030]["ebitda"] / 1e6),
     18, color=RGBColor(0xCF, 0xDD, 0xEA))

prs.save(DIR + "Synapep_Investor_Deck.pptx")
print("Saved Synapep_Investor_Deck.pptx — %d slides" % len(prs.slides._sldIdLst))
