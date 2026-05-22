#!/usr/bin/env python3
"""Builds the 1.5-hour DTL training deck on valuing deep-tech ventures.

Run:  python3 build_deck.py
Output:  Valuing_Deep_Tech_Ventures_DTL_Training.pptx
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ----------------------------------------------------------------------
# Theme
# ----------------------------------------------------------------------
NAVY   = RGBColor(0x0F, 0x2A, 0x4A)
NAVY2  = RGBColor(0x16, 0x3A, 0x5E)
ACCENT = RGBColor(0xE0, 0x8E, 0x2B)   # amber
TEAL   = RGBColor(0x1B, 0x9E, 0x8A)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT  = RGBColor(0xEE, 0xF1, 0xF4)
PANEL  = RGBColor(0xEC, 0xF0, 0xF4)
GREY   = RGBColor(0x5A, 0x6B, 0x7B)
DARK   = RGBColor(0x1F, 0x2A, 0x36)
FONT   = "Calibri"
MONO   = "Consolas"

DECK_NAME = "Valuing Deep-Tech Ventures  ·  Deep-Tech Lab (DTL) Training"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]

_counter = {"n": 0}


# ----------------------------------------------------------------------
# Primitives
# ----------------------------------------------------------------------
def _noline(shape):
    shape.line.fill.background()
    try:
        shape.shadow.inherit = False
    except Exception:
        pass


def rect(slide, l, t, w, h, color, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, Inches(l), Inches(t), Inches(w), Inches(h))
    s.fill.solid()
    s.fill.fore_color.rgb = color
    _noline(s)
    return s


def textbox(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tb.text_frame.word_wrap = True
    return tb


def run(p, text, size, color=DARK, bold=False, italic=False, name=FONT):
    r = p.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color
    r.font.name = name
    return r


def footer(slide):
    _counter["n"] += 1
    fb = textbox(slide, 0.55, 7.04, 9.5, 0.34)
    run(fb.text_frame.paragraphs[0], DECK_NAME, 8.5, GREY)
    nb = textbox(slide, 12.1, 6.98, 0.75, 0.4)
    p = nb.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run(p, str(_counter["n"]), 12, NAVY, bold=True)


def header(slide, kicker, title):
    rect(slide, 0, 0, 13.333, 1.06, NAVY)
    rect(slide, 0, 1.06, 13.333, 0.055, ACCENT)
    kb = textbox(slide, 0.55, 0.13, 12.0, 0.32)
    run(kb.text_frame.paragraphs[0], kicker.upper(), 12, ACCENT, bold=True)
    tb = textbox(slide, 0.55, 0.40, 12.25, 0.64)
    run(tb.text_frame.paragraphs[0], title, 25, WHITE, bold=True)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def callout(slide, top, body, label="KEY IDEA"):
    box = rect(slide, 0.55, top, 12.23, 1.0, PANEL, MSO_SHAPE.ROUNDED_RECTANGLE)
    box.adjustments[0] = 0.06
    rect(slide, 0.55, top, 0.10, 1.0, ACCENT)
    tb = textbox(slide, 0.85, top + 0.10, 11.7, 0.82)
    tf = tb.text_frame
    p = tf.paragraphs[0]
    run(p, label + "   ", 11, ACCENT, bold=True)
    run(p, body, 12.5, DARK)


def bullets(slide, items, top=1.38, height=4.0):
    """items: list of (level, text) or (level, text, bold)."""
    tb = textbox(slide, 0.6, top, 12.2, height)
    tf = tb.text_frame
    for i, item in enumerate(items):
        lvl, text = item[0], item[1]
        bold = item[2] if len(item) > 2 else False
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if lvl == 0:
            p.space_after = Pt(9)
            p.space_before = Pt(2)
            run(p, "▪  ", 16, ACCENT, bold=True)
            run(p, text, 15.5, DARK, bold=bold)
        else:
            p.space_after = Pt(5)
            run(p, "        –  ", 13, ACCENT)
            run(p, text, 13, GREY)


def table(slide, headers, rows, top, col_widths, fsize=11.5, height=None):
    ncols = len(headers)
    nrows = len(rows) + 1
    total_w = sum(col_widths)
    left = (13.333 - total_w) / 2
    if height is None:
        height = 0.42 + 0.40 * len(rows)
    gtab = slide.shapes.add_table(nrows, ncols, Inches(left), Inches(top),
                                  Inches(total_w), Inches(height))
    tbl = gtab.table
    tbl.first_row = True
    for j, w in enumerate(col_widths):
        tbl.columns[j].width = Inches(w)
    # header
    for j, h in enumerate(headers):
        c = tbl.cell(0, j)
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        c.margin_left = c.margin_right = Inches(0.09)
        c.margin_top = c.margin_bottom = Inches(0.04)
        p = c.text_frame.paragraphs[0]
        run(p, h, fsize + 0.5, WHITE, bold=True)
    # body
    for i, rowdata in enumerate(rows):
        for j, val in enumerate(rowdata):
            c = tbl.cell(i + 1, j)
            c.fill.solid()
            c.fill.fore_color.rgb = WHITE if i % 2 == 0 else LIGHT
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.margin_left = c.margin_right = Inches(0.09)
            c.margin_top = c.margin_bottom = Inches(0.035)
            p = c.text_frame.paragraphs[0]
            run(p, str(val), fsize, DARK, bold=(j == 0))
    return tbl


def new_slide():
    return prs.slides.add_slide(BLANK)


# ----------------------------------------------------------------------
# Slide builders
# ----------------------------------------------------------------------
def content_slide(kicker, title, items, callout_text=None, notes_text=""):
    s = new_slide()
    header(s, kicker, title)
    if callout_text:
        bullets(s, items, top=1.42, height=3.9)
        callout(s, 5.62, callout_text)
    else:
        bullets(s, items, top=1.50, height=5.2)
    footer(s)
    notes(s, notes_text)
    return s


def table_slide(kicker, title, lead, headers, rows, col_widths,
                callout_text=None, notes_text="", fsize=11.5):
    s = new_slide()
    header(s, kicker, title)
    top = 1.40
    if lead:
        tb = textbox(s, 0.6, 1.28, 12.2, 0.5)
        run(tb.text_frame.paragraphs[0], lead, 13, GREY, italic=True)
        top = 1.78
    table(s, headers, rows, top, col_widths, fsize=fsize)
    if callout_text:
        callout(s, 6.0, callout_text)
    footer(s)
    notes(s, notes_text)
    return s


def formula_slide(kicker, title, formula_lines, legend, callout_text, notes_text=""):
    s = new_slide()
    header(s, kicker, title)
    box = rect(s, 1.4, 1.62, 10.53, 1.62, NAVY2, MSO_SHAPE.ROUNDED_RECTANGLE)
    box.adjustments[0] = 0.08
    tb = textbox(s, 1.6, 1.74, 10.1, 1.4)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, line in enumerate(formula_lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.CENTER
        p.space_after = Pt(4)
        run(p, line, 19 if i == 0 else 14, WHITE if i == 0 else ACCENT,
            bold=(i == 0), name=MONO)
    lb = textbox(s, 0.85, 3.5, 11.6, 2.3)
    tf = lb.text_frame
    run(tf.paragraphs[0], "where", 12.5, NAVY, bold=True)
    for sym, desc in legend:
        p = tf.add_paragraph()
        p.space_after = Pt(5)
        run(p, "   " + sym + "  ", 13, ACCENT, bold=True, name=MONO)
        run(p, desc, 13, DARK)
    callout(s, 5.9, callout_text)
    footer(s)
    notes(s, notes_text)
    return s


def divider(section_no, kicker, title, subtitle, notes_text=""):
    s = new_slide()
    rect(s, 0, 0, 13.333, 7.5, NAVY)
    rect(s, 0, 0, 13.333, 0.18, ACCENT)
    big = textbox(s, 0.85, 1.55, 11.0, 2.4)
    run(big.text_frame.paragraphs[0], section_no, 150, NAVY2, bold=True)
    rect(s, 0.95, 4.05, 1.7, 0.12, ACCENT)
    kb = textbox(s, 0.95, 3.55, 11.0, 0.4)
    run(kb.text_frame.paragraphs[0], kicker.upper(), 14, ACCENT, bold=True)
    tb = textbox(s, 0.92, 4.25, 11.4, 1.2)
    run(tb.text_frame.paragraphs[0], title, 38, WHITE, bold=True)
    sb = textbox(s, 0.95, 5.35, 11.2, 1.0)
    run(sb.text_frame.paragraphs[0], subtitle, 16, RGBColor(0xAE, 0xC2, 0xD6))
    footer(s)
    notes(s, notes_text)
    return s


# ======================================================================
# SLIDE 1 — Title
# ======================================================================
s = new_slide()
rect(s, 0, 0, 13.333, 7.5, NAVY)
rect(s, 0, 0, 0.32, 7.5, ACCENT)
eb = textbox(s, 1.1, 1.30, 11.0, 0.45)
run(eb.text_frame.paragraphs[0], "DEEP-TECH LAB (DTL)  ·  TRAINING SERIES", 15,
    ACCENT, bold=True)
tb = textbox(s, 1.05, 1.95, 11.3, 2.0)
tf = tb.text_frame
run(tf.paragraphs[0], "Valuing Deep-Tech Ventures", 52, WHITE, bold=True)
p = tf.add_paragraph()
run(p, "A Practitioner's Framework for Researchers & Scientists", 24,
    RGBColor(0xC6, 0xD4, 0xE2))
rect(s, 1.12, 4.25, 3.0, 0.10, ACCENT)
mb = textbox(s, 1.1, 4.55, 11.2, 1.7)
tf = mb.text_frame
for txt in [
    "90-minute training  ·  six connected methods, assembled into one master model",
    "From milestone roadmap and use-of-funds, through benchmarking and uncertainty,",
    "to stakeholder rights and dilution.",
]:
    p = tf.paragraphs[0] if txt.startswith("90") else tf.add_paragraph()
    p.space_after = Pt(3)
    run(p, txt, 14, RGBColor(0xAE, 0xC2, 0xD6))
ab = textbox(s, 1.1, 6.35, 11.2, 0.5)
run(ab.text_frame.paragraphs[0],
    "Audience: research scientists and venture founders  |  Tone: professional and academic",
    12, GREY, italic=True)
notes(s, "Welcome. This 90-minute session turns valuation from a black box into a "
         "constructed, defensible argument. We use real Deep-Tech Lab ventures as "
         "worked references throughout. All figures shown are illustrative worked "
         "examples, not investment advice.")
_counter["n"] = 1  # title counts as slide 1

# ======================================================================
# SLIDE 2 — The valuation gap
# ======================================================================
content_slide(
    "Why this training", "The valuation gap for scientist-founders",
    [
        (0, "Deep-tech ventures are valued years before revenue — earnings, "
            "book value and cash flow are near zero, so standard accounting "
            "methods return little that is meaningful."),
        (0, "Yet valuation is unavoidable: it sets how much equity you exchange "
            "for the capital needed to reach your next scientific milestone."),
        (0, "A defensible valuation is not a guess — it is an argument that "
            "links three things:"),
        (1, "the science you will do (milestones),"),
        (1, "the funds you will spend to do it (use of funds), and"),
        (1, "the market evidence that prices the result (benchmarking)."),
        (0, "This session builds that argument in six connected methods, then "
            "assembles them into a single master model."),
    ],
    callout_text="A deep-tech valuation is a risk-adjusted, milestone-indexed "
                 "estimate of future value — not a statement of present fact.",
    notes_text="Scientists often feel valuation is arbitrary. The message: it is "
               "a structured argument. If any of the three legs — milestones, "
               "funds, market evidence — is missing, the number cannot be "
               "defended in a negotiation.")

# ======================================================================
# SLIDE 3 — Agenda
# ======================================================================
content_slide(
    "90-minute run of show", "Agenda and learning objectives",
    [
        (0, "1  ·  The milestone roadmap to a valuation — 10 min"),
        (0, "2  ·  Use of funds → value creation → the math — 20 min"),
        (0, "3  ·  Benchmarking: market, competition, valuation references — 15 min"),
        (0, "4  ·  Matching method: use of funds tested against the market — 10 min"),
        (0, "5  ·  Uncertainty: downside/upside across the Golden Triangle — 15 min"),
        (0, "6  ·  Stakeholders: rights, protections, controls, future dilution — 12 min"),
        (0, "7  ·  The master model + comparison with other financial approaches — 8 min"),
    ],
    callout_text="Objectives — by the end you can: (i) build a milestone-indexed "
                 "valuation; (ii) defend it with benchmarking; (iii) state its "
                 "downside and upside; (iv) read how a term sheet changes your value.",
    notes_text="Walk the audience through the arc. Stress that sections build on "
               "one another — each method feeds the master model in Section 7.")

# ======================================================================
# SECTION 1
# ======================================================================
divider("01", "Section One", "The Milestone Roadmap to a Valuation",
        "Valuation is a process indexed to scientific and commercial milestones — "
        "not a single number fixed at one date.",
        "Section 1 establishes the mental model: value is created step by step as "
        "risk is removed at each milestone.")

content_slide(
    "Section 1  ·  The milestone roadmap",
    "Valuation is a process, not a number",
    [
        (0, "A deep-tech venture's value is the present value of a future outcome "
            "that is still uncertain — the uncertainty is what milestones resolve."),
        (0, "Map the venture on the Technology Readiness Level (TRL) ladder, from "
            "TRL 1 (basic principles) to TRL 9 (proven in operation)."),
        (0, "Each rung pairs a TRL step with a value inflection — a point at "
            "which a specific risk is removed and the venture is worth materially more."),
        (0, "Examples of value-inflection milestones in DTL ventures:"),
        (1, "a working prototype or validated assay (engineering / feasibility risk);"),
        (1, "clinical or field-validation data (efficacy / scientific risk);"),
        (1, "regulatory clearance, e.g. an FDA 510(k) for a Class II device;"),
        (1, "first paying customer or signed commercial contract (market risk)."),
        (0, "The roadmap defines WHEN value is created; the later sections quantify "
            "HOW MUCH."),
    ],
    notes_text="Scientists already think in TRL terms — anchor valuation to that "
               "familiar ladder. The Illuminatio MRI venture, for example, targets "
               "a 510(k) clearance as a defining regulatory milestone.")

table_slide(
    "Section 1  ·  The milestone roadmap",
    "From idea to value: the milestone ladder",
    "An illustrative roadmap; each venture customises the milestones and the method used to value it.",
    ["Stage", "TRL", "Defining milestone", "Risk removed", "Primary valuation method"],
    [
        ["Concept", "1–3", "Proof of principle, IP filed", "Scientific basis", "Qualitative scorecard"],
        ["Prototype", "4–6", "Working prototype / validated assay", "Engineering feasibility", "Use-of-funds rNPV"],
        ["Validation", "7–8", "Clinical or field validation data", "Efficacy / performance", "rNPV + comparables"],
        ["Regulatory", "8", "Clearance / approval (e.g. 510(k))", "Regulatory risk", "Benchmarked exit value"],
        ["Commercial", "9", "First revenue / signed contracts", "Market acceptance", "Revenue & earnings multiples"],
        ["Scaling", "9", "Repeatable growth, positive margin", "Execution / scale", "DCF + capital-market multiples"],
    ],
    [1.4, 0.8, 3.5, 2.3, 3.4],
    callout_text="The valuation method should follow the venture's TRL stage — "
                 "using a revenue multiple on a pre-revenue venture is a category error.",
    notes_text="Emphasise the last column: method choice is stage-dependent. We "
               "revisit this matrix in Section 7.")

content_slide(
    "Section 1  ·  The milestone roadmap",
    "De-risking equals value creation",
    [
        (0, "Picture the venture's eventual exit value as a fixed prize, visible "
            "but discounted today by the probability it is never reached."),
        (0, "Every milestone has a probability of success (POS). Before any "
            "milestones, the venture is worth the prize multiplied by the product "
            "of all the POS figures — a small fraction of the prize."),
        (0, "Achieving a milestone removes its risk: that POS term disappears from "
            "the discount, and the venture's value jumps by the factor 1 / POS."),
        (0, "So value is not created smoothly — it is created in steps, each "
            "step coinciding with a milestone."),
        (0, "This is why a venture can raise at a much higher price after a result "
            "that cost relatively little: the result removed a large risk."),
    ],
    callout_text="Value creation = risk removal. The job of a funding round is to "
                 "buy the milestones that remove the most risk per dollar.",
    notes_text="This is the conceptual core of the whole deck. The 1/POS jump is "
               "made concrete with numbers in Section 2's worked example.")

# ======================================================================
# SECTION 2
# ======================================================================
divider("02", "Section Two", "From Use of Funds to Value — the Math",
        "How a funding round creates value: funds drive tasks, tasks remove risk, "
        "and removed risk accumulates into valuation.",
        "Section 2 is the quantitative heart of the training. Take time on the "
        "rNPV formula and the worked example.")

content_slide(
    "Section 2  ·  Use of funds",
    "Step 1 — use of funds as the unit of analysis",
    [
        (0, "Start not with a valuation number, but with the use of funds: the "
            "itemised plan of what the next round of capital will be spent on."),
        (0, "A credible use of funds is structured around milestones, not line "
            "items — it states which milestones the money will deliver."),
        (0, "Typical use-of-funds categories for a DTL venture:"),
        (1, "R&D and prototyping — the core technical work;"),
        (1, "validation, clinical or pilot studies — generating evidence;"),
        (1, "regulatory and IP — filings, approvals, freedom-to-operate;"),
        (1, "team and operations — hiring the people who execute;"),
        (1, "go-to-market — first commercial activity."),
        (0, "Each category funds tasks; each task is chosen because it removes a "
            "specific, nameable risk."),
    ],
    callout_text="The use of funds is the bridge between the laboratory and the "
                 "valuation: it is the list of risks the round will buy down.",
    notes_text="Insist that the use of funds is milestone-led. 'We will spend $2.5M' "
               "is not a plan; 'we will spend $2.5M to reach prototype and "
               "validation' is.")

content_slide(
    "Section 2  ·  Value creation",
    "How funded tasks create value",
    [
        (0, "Trace the causal chain for every dollar:  funds → task → "
            "milestone → risk removed → value created."),
        (0, "A task creates value only if it changes a probability of success or "
            "the size of the eventual prize — otherwise it is cost, not "
            "investment."),
        (0, "Worked mapping for an imaging-diagnostics venture:"),
        (1, "funds the prototype build → raises engineering POS from ~0.4 to ~0.7;"),
        (1, "funds the clinical study → raises efficacy POS from ~0.3 to ~0.5;"),
        (1, "funds the regulatory submission → raises clearance POS toward ~0.6."),
        (0, "Tasks that only maintain the status quo (rent, admin) are necessary "
            "but do not, by themselves, create valuation — they are the cost "
            "of keeping the option alive."),
    ],
    callout_text="Test every funded task with one question: which probability does "
                 "it move, and by how much? If the answer is 'none', it is overhead.",
    notes_text="This reframes budgeting for scientists: spending is an investment "
               "only when it shifts a POS or expands the market.")

content_slide(
    "Section 2  ·  Value accumulation",
    "How value accumulates across tasks",
    [
        (0, "Milestones compound. Achieving milestone A and then milestone B "
            "removes both risks — value multiplies by (1/POS_A) × (1/POS_B)."),
        (0, "Accumulation example — a round that funds two milestones:"),
        (1, "before the round, four milestones remain; cumulative POS = "
            "0.7 × 0.5 × 0.6 × 0.8 = 16.8%;"),
        (1, "the round funds and achieves the first two; remaining cumulative "
            "POS = 0.6 × 0.8 = 48%;"),
        (1, "the risk-adjusted value rises by roughly 48% / 16.8% ≈ 2.9×, "
            "before accounting for the shorter remaining time to exit."),
        (0, "The capital deployed is modest relative to the value step it unlocks "
            "— that ratio is the entire valuation argument for the round."),
    ],
    callout_text="Value accumulates multiplicatively across milestones. The round's "
                 "story is the gap between dollars spent and value steps unlocked.",
    notes_text="Set up the numbers used on the worked-example slide. The 2.9x is "
               "before the discount-for-time effect, which adds further uplift.")

formula_slide(
    "Section 2  ·  The math",
    "The math of valuation — risk-adjusted NPV (rNPV)",
    [
        "rNPV₀  =  Σₜ [ CPOSₜ × CFₜ / (1+r)ₜ ]  −  Σₜ [ Costₜ / (1+r)ₜ ]",
        "value step on milestone success:   V  →  V × (1 / POS)",
    ],
    [
        ("CPOSₜ", "cumulative probability of reaching year t — the product of every milestone POS up to t"),
        ("CFₜ", "projected cash flow or exit value in year t — sized by benchmarking (Section 3)"),
        ("Costₜ", "use of funds deployed in year t — the spending plan from Step 1"),
        ("r", "venture discount rate: stage-dependent cost of capital, typically 15–40% for early deep tech"),
    ],
    "rNPV (also called eNPV) is the standard intrinsic method for risk-laden, "
    "milestone-driven ventures. It makes de-risking measurable.",
    notes_text="Do not rush this slide. The first sum is the risk-adjusted reward; "
               "the second is the cost. Stress the discipline: once a milestone is "
               "achieved you DROP its POS from CPOS — you do not also keep an "
               "inflated r, or you double-count the risk.")

table_slide(
    "Section 2  ·  Worked example",
    "Worked example — a milestone-funded venture",
    "Illustrative figures for a diagnostic-imaging venture raising a US$2.5M round to fund the first two milestones.",
    ["Item", "Value", "Basis"],
    [
        ["Benchmarked exit value (Year 5)", "US$80M", "comparable med-tech exits — see Section 3"],
        ["M1 — working prototype", "POS 70%", "engineering / feasibility risk"],
        ["M2 — clinical validation data", "POS 50%", "efficacy / scientific risk"],
        ["M3 — regulatory clearance (510(k))", "POS 60%", "regulatory risk"],
        ["M4 — first commercial revenue", "POS 80%", "market-acceptance risk"],
        ["Cumulative POS (all four)", "16.8%", "0.70 × 0.50 × 0.60 × 0.80"],
        ["Venture discount rate r", "25%", "early-stage cost of capital"],
        ["Risk-adjusted value today (pre-money)", "≈ US$4.4M", "0.168 × 80 ÷ 1.25⁵"],
        ["Value after M1 + M2 funded & achieved", "≈ US$19.7M", "0.48 × 80 ÷ 1.25³"],
    ],
    [4.6, 1.7, 5.4],
    callout_text="A US$2.5M round that buys M1 + M2 lifts risk-adjusted value from "
                 "~US$4.4M to ~US$19.7M — about 4.5×. That multiple, not the "
                 "cash, is the valuation argument.",
    fsize=11,
    notes_text="Walk each row. 1.25^5 = 3.05; 1.25^3 = 1.95. The uplift combines two "
               "effects: risk removed (16.8% -> 48%) and time shortened (5 yrs -> 3). "
               "All figures are illustrative.")

# ======================================================================
# SECTION 3
# ======================================================================
divider("03", "Section Three", "The Benchmarking Approach",
        "Anchoring the venture to external evidence: market size, competitive "
        "position, qualitative quality, and current valuation references.",
        "Section 3 supplies the exit value and the sense-checks that the rNPV needs. "
        "Without benchmarking, the intrinsic model floats free.")

content_slide(
    "Section 3  ·  Benchmarking",
    "Benchmarking — triangulating value from the market",
    [
        (0, "The rNPV needs an exit value (CFₜ). Benchmarking supplies it from "
            "outside evidence, so the number is not merely the founder's hope."),
        (0, "Four benchmarking lenses, used together:"),
        (1, "the market — how large is the addressable opportunity?"),
        (1, "competitive analysis — who else is there, and how do you compare?"),
        (1, "qualitative quality — the team, IP and execution 'good views';"),
        (1, "valuation references — what have comparable ventures been valued at?"),
        (0, "Triangulation matters: any single lens can mislead, but agreement "
            "across all four produces a defensible exit value."),
        (0, "Benchmarking is top-down (from the market inward); the use-of-funds "
            "rNPV is bottom-up (from the venture outward). Section 4 reconciles them."),
    ],
    callout_text="Benchmarking answers 'what is the prize, and is it credible?' — "
                 "it anchors the intrinsic model to observable market evidence.",
    notes_text="Frame the four lenses as a checklist. Each appears on its own slide "
               "next.")

table_slide(
    "Section 3  ·  The market",
    "Market sizing — TAM, SAM, SOM",
    "Size the prize from the outside in; cite the source and date of every figure.",
    ["Layer", "Definition", "DTL worked reference"],
    [
        ["TAM — Total Addressable Market",
         "Total demand if you served everyone",
         "Liver-disease diagnostics market ≈ US$30.6B (2020), ~6.7% CAGR"],
        ["SAM — Serviceable Available Market",
         "The slice your product and channel can reach",
         "Non-invasive MRI-based liver-fibrosis testing in target geographies"],
        ["SOM — Serviceable Obtainable Market",
         "The share you can realistically win",
         "Early hospital and pharma adopters reachable in the first 3–5 years"],
    ],
    [3.3, 3.7, 5.4],
    callout_text="Investors discount an unsupported TAM heavily. A credible SOM, "
                 "built bottom-up from named customers, carries far more weight.",
    fsize=11,
    notes_text="The liver-diagnostics figures come from the Illuminatio venture file. "
               "Teach the audience to move from the big TAM headline to a defensible, "
               "bottom-up SOM.")

table_slide(
    "Section 3  ·  Competition & quality",
    "Competitive analysis and the qualitative 'good views'",
    "A benchmarking scorecard — the dimensions DTL reviewers actually use to grade ventures.",
    ["Dimension", "What it benchmarks", "Strong signal"],
    [
        ["Technology content", "Depth, defensibility, IP position", "Granted patents; clear performance edge"],
        ["Team / founder readiness", "Capability and commitment to execute", "Domain track record; full-time founders"],
        ["Commercialisation potential", "Route to revenue and scale", "Named customers; validated demand"],
        ["Feasibility & sustainability", "Can it be delivered and funded", "Credible milestones; realistic capital plan"],
        ["Competitive position", "Advantage vs named rivals", "Direct measurement vs indirect proxies"],
    ],
    [3.0, 4.0, 4.4],
    callout_text="The 'good views' are qualitative but not arbitrary — a "
                 "structured scorecard turns judgement into a comparable benchmark.",
    fsize=11,
    notes_text="These five dimensions are taken from the DTL interview scorecard. "
               "For Illuminatio, the competitive edge is direct macromolecule "
               "measurement versus competitors' indirect stiffness proxies "
               "(Resoundant, Echosens, Perspectum).")

content_slide(
    "Section 3  ·  Valuation references",
    "Current valuation references — reading the comparables",
    [
        (0, "Valuation references are observed prices: recent funding rounds, "
            "acquisitions and licensing deals for comparable ventures."),
        (0, "Three reference types, in decreasing order of availability:"),
        (1, "comparable financing rounds — pre-money valuations at the same stage;"),
        (1, "comparable transactions — acquisition prices for similar assets;"),
        (1, "comparable public companies — listed peers' trading multiples."),
        (0, "Adjust every reference for differences in stage, geography, TRL and "
            "deal terms before applying it — raw comparables are rarely "
            "like-for-like."),
        (0, "Date every reference. Venture valuations move with the financing "
            "cycle, so a comparable more than 12–18 months old must be treated "
            "with caution."),
        (0, "Comparables give a defensible exit value and a reality check on the "
            "rNPV — they rarely give the answer outright."),
    ],
    callout_text="A comparable is evidence, not a verdict. Adjust it for stage, "
                 "terms and date — then let it inform a range, not a point.",
    notes_text="Acknowledge the data problem: deep-tech comparables are scarce and "
               "deal terms are seldom disclosed. Hence triangulation, not reliance "
               "on one number.")

# ======================================================================
# SECTION 4
# ======================================================================
divider("04", "Section Four", "The Matching Method",
        "Reconciling the bottom-up use of funds with the top-down benchmarking — "
        "and testing the funding plan against market evidence.",
        "Section 4 is the reconciliation step. Two independent estimates that agree "
        "are far more persuasive than either alone.")

content_slide(
    "Section 4  ·  Matching",
    "Matching — reconciling bottom-up and top-down",
    [
        (0, "Two independent estimates of value now exist:"),
        (1, "bottom-up — the use-of-funds rNPV, built from milestones and POS;"),
        (1, "top-down — the benchmarked exit value, built from market evidence."),
        (0, "The matching method places them side by side and asks whether they "
            "tell a consistent story."),
        (0, "If the two agree, confidence is high and the overlap defines the "
            "defensible valuation range."),
        (0, "If they diverge, one assumption is wrong — matching forces you to "
            "find it: an over-optimistic POS, an inflated TAM, a stale comparable, "
            "or a use of funds that does not reach the milestones it claims."),
        (0, "Two estimates that converge from different directions are far more "
            "persuasive in a negotiation than either estimate alone."),
    ],
    callout_text="Matching is a consistency test. Convergence builds confidence; "
                 "divergence locates the flawed assumption.",
    notes_text="The point of matching is not to average two numbers — it is to "
               "diagnose. A gap is informative; it tells you where to dig.")

table_slide(
    "Section 4  ·  Matching",
    "The matching worksheet",
    "Place each funded milestone against the market evidence that prices it.",
    ["Use of funds (milestone)", "Value mechanism", "Market evidence that tests it", "Match?"],
    [
        ["Prototype build", "Engineering POS 0.4→0.7", "Comparable seed rounds post-prototype", "Aligned"],
        ["Clinical validation study", "Efficacy POS 0.3→0.5", "Valuations after comparable validation data", "Aligned"],
        ["Regulatory submission (510(k))", "Clearance POS → 0.6", "Re-rating of cleared comparable devices", "Aligned"],
        ["Go-to-market / first contract", "Unlocks revenue, market risk", "Revenue multiples of early-commercial peers", "Review"],
    ],
    [3.5, 2.7, 4.3, 1.2],
    callout_text="Each row links a dollar of spend to a milestone, to a value step, "
                 "to the market evidence that confirms or challenges it.",
    fsize=10.5,
    notes_text="The worksheet is the practical deliverable of matching. A 'Review' "
               "flag means the bottom-up and top-down views disagree and the "
               "assumption must be re-examined.")

content_slide(
    "Section 4  ·  Matching",
    "Articulating use of funds and testing it against the market",
    [
        (0, "Articulation — state the use of funds so each item is explicitly "
            "tied to a milestone, a probability shift, and a value step."),
        (0, "Examination — hold each articulated item against the market "
            "evidence and ask three questions:"),
        (1, "Is the milestone one the market actually re-prices? (some are invisible "
            "to investors);"),
        (1, "Is the probability shift consistent with base rates from comparable "
            "programmes?"),
        (1, "Does the implied value step match observed valuations of comparable "
            "ventures at that stage?"),
        (0, "Where the answers align, the use of funds is validated and the round "
            "is 'priced' by the market, not by assertion."),
        (0, "Where they do not, revise the plan — reallocate funds toward the "
            "milestones the market genuinely rewards."),
    ],
    callout_text="A use of funds is well-articulated when every dollar is traceable "
                 "to a milestone the market is observed to pay for.",
    notes_text="This slide closes the loop between Sections 2 and 3. The practical "
               "advice: if the market does not reward a milestone, question why you "
               "are funding it now.")

# ======================================================================
# SECTION 5
# ======================================================================
divider("05", "Section Five", "Uncertainty — Downside vs Upside",
        "A deep-tech valuation is a distribution, not a point. Frame its spread "
        "with the Golden Triangle: technology, organisation and commercial risk.",
        "Section 5 forces the deck away from single numbers. The Golden Triangle "
        "is the organising device for risk.")

content_slide(
    "Section 5  ·  Uncertainty",
    "The Golden Triangle — the three sources of risk",
    [
        (0, "Every deep-tech venture's uncertainty resolves into three vertices, "
            "the Golden Triangle:"),
        (1, "Technology — does the science work, at scale, reproducibly, "
            "with freedom to operate?"),
        (1, "Organisation — can the team, governance and capital plan actually "
            "execute and survive?"),
        (1, "Commercial (the market) — will customers adopt, pay and stay, "
            "against competition and regulation?"),
        (0, "A venture is only as valuable as its weakest vertex — brilliant "
            "science with no commercial route, or a strong market with an unproven "
            "team, both cap the valuation."),
        (0, "Every milestone, every funded task and every risk in the rNPV maps "
            "onto one of these three vertices."),
    ],
    callout_text="Technology · Organisation · Commercial — the Golden "
                 "Triangle. Value is constrained by the weakest of the three.",
    notes_text="Researchers tend to over-weight the technology vertex. Stress that "
               "investors price all three, and that organisation and commercial "
               "risk are where scientist-led ventures most often fail.")

table_slide(
    "Section 5  ·  Uncertainty",
    "Scenario analysis — downside, base and upside",
    "Replace the single number with three explicit, fully-described scenarios.",
    ["Scenario", "Narrative", "Illustrative value", "Probability"],
    [
        ["Downside", "Key milestone slips or fails; partial recovery via asset sale or pivot", "US$8M", "30%"],
        ["Base", "Plan delivered roughly on time and on budget", "US$25M", "50%"],
        ["Upside", "Faster validation, larger market capture, strategic interest", "US$70M", "20%"],
    ],
    [1.8, 6.1, 2.2, 1.5],
    callout_text="Expected value  E[V]  =  0.30×8 + 0.50×25 + 0.20×70  "
                 "≈  US$28.9M  —  the mean sits above the base case.",
    fsize=11,
    notes_text="The deliberate asymmetry — upside far above base, downside not "
               "far below — is characteristic of deep tech. The mean exceeds the "
               "mode; this is the option-like payoff structure.")

table_slide(
    "Section 5  ·  Uncertainty",
    "Mapping uncertainty across the Golden Triangle",
    "For each vertex, name the specific downside and the specific upside — do not leave risk abstract.",
    ["Vertex", "Downside driver", "Upside driver"],
    [
        ["Technology",
         "Fails to reproduce or scale; blocked by third-party IP",
         "Performance exceeds target; platform spawns multiple products"],
        ["Organisation",
         "Key person leaves; runs out of cash before next milestone",
         "Senior hires land; non-dilutive grants extend the runway"],
        ["Commercial",
         "Slow adoption; reimbursement or regulation tightens; new entrant",
         "Strategic partner or anchor customer; faster path to scale"],
    ],
    [2.3, 5.3, 5.3],
    callout_text="Quantify, do not just list: attach a probability and a value "
                 "impact to each driver so it feeds the scenario weights.",
    fsize=10.5,
    notes_text="This slide makes the scenario probabilities defensible. Each "
               "downside/upside driver should be traceable to a milestone POS in "
               "the rNPV.")

formula_slide(
    "Section 5  ·  Uncertainty",
    "Expected value and probability weighting",
    [
        "E[V]  =  p_down × V_down  +  p_base × V_base  +  p_up × V_up",
        "0.30 × 8  +  0.50 × 25  +  0.20 × 70   =   US$28.9M",
    ],
    [
        ("p_x", "probability of scenario x — grounded in the Golden-Triangle driver analysis"),
        ("V_x", "venture value in scenario x — each scenario fully narrated, not just a number"),
        ("E[V]", "probability-weighted expected value — the single figure, if one is needed"),
    ],
    "Report the range and the probabilities, not only E[V]. The spread between "
    "downside and upside is itself decision-useful information.",
    notes_text="Caution: E[V] collapses the distribution back to one number. Always "
               "present it alongside the range. A negotiation is really about whose "
               "probabilities are correct.")

# ======================================================================
# SECTION 6
# ======================================================================
divider("06", "Section Six", "Stakeholders — Rights, Protections, Control & Dilution",
        "Enterprise value is not value received. Term-sheet rights, protections, "
        "controls and future dilution decide who actually gets what.",
        "Section 6 separates the headline valuation from the value each stakeholder "
        "realises. This is where scientist-founders are most often surprised.")

content_slide(
    "Section 6  ·  Stakeholders",
    "The cap table — who holds the value",
    [
        (0, "The capitalisation table records who owns the venture: founders, "
            "employees (the option pool), and investors by round."),
        (0, "The headline valuation prices the whole company; the cap table and "
            "term sheet decide how that value is divided."),
        (0, "Two distinct dimensions are negotiated:"),
        (1, "economic rights — who receives cash, and in what order, on an exit;"),
        (1, "control rights — who can decide, veto or force key actions."),
        (0, "A scientist-founder must read both. The same headline valuation can "
            "leave founders with very different outcomes once rights and controls "
            "are applied."),
        (0, "Ownership percentage alone is an incomplete picture — a minority "
            "investor with strong protective provisions can hold decisive control."),
    ],
    callout_text="The headline valuation sizes the pie. Rights, controls and "
                 "dilution decide the slice each stakeholder actually eats.",
    notes_text="Introduce the distinction economics vs control — it is the "
               "spine of the next two slides.")

table_slide(
    "Section 6  ·  Stakeholders",
    "Investor rights, protections and controls",
    "Common term-sheet provisions — and how each one changes the value you actually receive.",
    ["Provision", "What it does", "Effect on founder value"],
    [
        ["1× liquidation preference", "Investor recovers capital first on exit", "Reduces common-share value at low/mid exits"],
        ["Participating preferred", "Preference AND a share of the remainder", "'Double dip' — materially cuts founder proceeds"],
        ["Anti-dilution (weighted-avg.)", "Re-prices investor shares if a later round is lower", "Shifts down-round dilution onto founders"],
        ["Pro-rata / pre-emptive rights", "Investor may keep its % in future rounds", "Constrains who you can admit later"],
        ["Board seats & protective provisions", "Veto over budget, hiring, financing, sale", "Control independent of ownership %"],
        ["Founder vesting & drag-along", "Re-earn your shares; can be forced into a sale", "Aligns — and limits — founder economics"],
    ],
    [3.3, 4.2, 4.4],
    callout_text="Two ventures can carry an identical headline valuation yet deliver "
                 "very different value to founders — the terms decide.",
    fsize=10.5,
    notes_text="Walk participating preferred carefully — it is the term that most "
               "often surprises founders. A 1x non-participating preference is the "
               "founder-friendly norm.")

content_slide(
    "Section 6  ·  Stakeholders",
    "Future development and dilution",
    [
        (0, "Deep-tech ventures need several rounds to cross all milestones — "
            "so dilution is not a one-off event but a planned sequence."),
        (0, "Each new round issues new shares: existing holders' percentages fall, "
            "even as the value of their stake can rise."),
        (0, "The option pool is usually created or topped up pre-money — so it "
            "dilutes the founders, not the incoming investor. Negotiate its size "
            "deliberately."),
        (0, "Plan the full financing path in advance: model how founder ownership "
            "evolves across seed, Series A and beyond, against the milestone roadmap."),
        (0, "The goal is not to minimise dilution — it is to maximise the value "
            "of the founders' retained stake. A smaller slice of a de-risked, "
            "larger company can be worth far more."),
    ],
    callout_text="Dilution is the price of de-risking capital. Judge it by the "
                 "value of the slice retained, never by the percentage given up.",
    notes_text="Reassure founders: dilution is normal and healthy if each round "
               "buys milestones that raise the whole company's value faster than "
               "ownership falls.")

formula_slide(
    "Section 6  ·  Stakeholders",
    "Pre-money, post-money and the dilution math",
    [
        "Post-money  =  Pre-money  +  New Investment",
        "Investor %  =  New Investment / Post-money        "
        "Founder stake after  =  Founder stake before × (Pre-money / Post-money)",
    ],
    [
        ("Pre-money", "the venture's agreed value immediately before the new investment"),
        ("Post-money", "value immediately after — the basis for the investor's ownership %"),
        ("Example", "Pre US$4.4M + raise US$2.5M → Post US$6.9M → investor owns ≈ 36.2%"),
        ("Note", "a pre-money option pool dilutes founders further — model it explicitly"),
    ],
    "Always confirm whether a quoted valuation is pre- or post-money — the "
    "same headline number implies different ownership depending on which it is.",
    notes_text="The pre- vs post-money confusion is a classic, costly error. Make "
               "the audience compute the example: 2.5 / 6.9 = 36.2%.")

# ======================================================================
# SECTION 7
# ======================================================================
divider("07", "Section Seven", "The Master Model",
        "Assembling the six methods into one integrated model — and comparing "
        "it with the other financial approaches.",
        "Section 7 is the synthesis. Show how every prior section becomes a layer "
        "of one coherent model.")

content_slide(
    "Section 7  ·  The master model",
    "The master model — integrating the six methods",
    [
        (0, "Layer 1 — Milestone roadmap: defines the value-inflection timeline "
            "and the exit horizon."),
        (0, "Layer 2 — Use of funds / rNPV: the bottom-up intrinsic value of "
            "reaching the next milestones."),
        (0, "Layer 3 — Benchmarking: the top-down, market-anchored exit value "
            "and reference valuations."),
        (0, "Layer 4 — Matching: reconciles Layers 2 and 3 into one defensible "
            "valuation range."),
        (0, "Layer 5 — Uncertainty: Golden-Triangle scenarios convert the range "
            "into a probability-weighted distribution."),
        (0, "Layer 6 — Stakeholder terms: convert enterprise value into value "
            "per stakeholder, after rights and dilution."),
        (0, "Output: a valuation range, with an explicit risk profile and a "
            "resulting ownership outcome — not a single unexplained number."),
    ],
    callout_text="The master model is not a seventh method — it is the disciplined "
                 "assembly of the previous six into one defensible argument.",
    notes_text="This is the payoff slide. Each layer is one prior section. The "
               "deliverable of the whole training is the ability to build this.")

table_slide(
    "Section 7  ·  The master model",
    "Master model walkthrough — one venture, end to end",
    "Illustrative: a diagnostic-imaging venture carried through all six layers.",
    ["Layer", "Method applied", "Result"],
    [
        ["1  Roadmap", "TRL 4 → 9; four milestones to exit", "exit horizon: Year 5"],
        ["2  Use of funds", "US$2.5M funds M1+M2; CPOS 16.8%; r 25%", "intrinsic pre-money ≈ US$4.4M"],
        ["3  Benchmarking", "Liver-diagnostics TAM US$30.6B; comparable exits", "exit value ≈ US$80M"],
        ["4  Matching", "Bottom-up vs top-down reconciled", "defensible pre-money US$4–6M"],
        ["5  Uncertainty", "Down/Base/Up = 8 / 25 / 70; E[V] ≈ US$29M", "a range, not a point"],
        ["6  Stakeholder terms", "US$2.5M at US$4.5M pre; 1× pref; pool pre-money", "investors ≈ 36%; founders retain majority"],
    ],
    [2.4, 5.4, 4.4],
    callout_text="Six layers, one argument: a valuation range, its risk profile, "
                 "and the cap-table outcome — all traceable to stated assumptions.",
    fsize=10.5,
    notes_text="This consolidates every worked number used in the deck. Every figure "
               "traces back to a named assumption — that traceability is what "
               "makes the valuation defensible.")

table_slide(
    "Section 7  ·  Comparison",
    "Comparison — other financial valuation approaches",
    "The master model is the spine; these established methods are cross-checks for different stages.",
    ["Approach", "Essence", "Best used when", "Caveat for deep tech"],
    [
        ["Revenue multiple", "EV = Revenue × sector multiple", "Early commercial revenue exists", "Silent pre-revenue; multiples volatile"],
        ["Earnings / P/E", "Equity = Net profit × P/E", "Profitable, comparable listed peers", "Not applicable while pre-profit"],
        ["EV/EBITDA & market multiples", "EV = EBITDA × peer multiple", "Scaling, near-peer financials", "Needs illiquidity & stage discounts"],
        ["DCF / rNPV", "Σ risk-adjusted CF ÷ (1+r)ₜ", "Any stage — the intrinsic anchor", "Highly sensitive to assumptions"],
        ["VC method", "EV = Exit value ÷ target return", "Pricing a priced round", "Depends on exit & target-multiple inputs"],
        ["Comparable transactions", "Apply observed deal metrics", "Reference deals exist", "Deal terms rarely fully disclosed"],
    ],
    [2.6, 3.0, 3.2, 3.6],
    callout_text="These methods are cross-checks, not rivals. WBI was valued by DCF "
                 "(WACC 12%, terminal growth 3%) at US$55.6M, then sense-checked "
                 "against an industry P/E of 50–60×.",
    fsize=9.8,
    notes_text="The WBI case is a real DTL-adjacent valuation: DCF gave US$55.6M, "
               "cross-checked at 38x 2024 P/E versus a 50-60x industry norm. The "
               "lesson — capital-market multiples leverage listed peers but must "
               "be discounted for illiquidity, stage and control.")

table_slide(
    "Section 7  ·  Comparison",
    "Choosing the right method by venture stage",
    "Method selection follows TRL stage — the same matrix introduced in Section 1.",
    ["Stage / TRL", "Primary method", "Secondary cross-check"],
    [
        ["Concept (TRL 1–3)", "Milestone roadmap + qualitative scorecard", "Comparable seed rounds"],
        ["Prototype (TRL 4–6)", "Use-of-funds rNPV + VC method", "Benchmarked exit value"],
        ["Validation (TRL 7–8)", "rNPV + comparable transactions", "Revenue multiple, if pilot revenue"],
        ["Early commercial (TRL 9)", "Revenue & EV/EBITDA multiples", "DCF"],
        ["Scaling", "DCF + capital-market multiples", "P/E versus listed peers"],
    ],
    [3.0, 4.6, 4.4],
    callout_text="No single method is correct — the master model is correct "
                 "because it uses the right method at each stage and reconciles them.",
    fsize=11,
    notes_text="Close the loop with Section 1's ladder. Reinforce: stage drives "
               "method.")

# ======================================================================
# CLOSING
# ======================================================================
content_slide(
    "Closing  ·  Caveats",
    "Common pitfalls and academic caveats",
    [
        (0, "Single-point valuations — deep tech is a distribution; always "
            "present a range with its probabilities."),
        (0, "Confusing headline valuation with value received — terms and "
            "dilution can outweigh the price."),
        (0, "Double-counting risk — once a milestone is achieved, remove its "
            "POS from CPOS; do not also keep an inflated discount rate."),
        (0, "Optimistic POS — use base rates from comparable programmes, not "
            "the founder's confidence."),
        (0, "Stale benchmarks — venture references age quickly; date and "
            "adjust every comparable."),
        (0, "Ignoring the option pool — it is usually created pre-money and "
            "dilutes founders, not investors."),
    ],
    callout_text="A valuation is only as honest as its weakest assumption. State "
                 "assumptions explicitly so others can challenge them.",
    notes_text="These are the recurring errors in DTL venture reviews. Honesty "
               "about assumptions is what makes a valuation survive due diligence.")

content_slide(
    "Closing  ·  Workshop",
    "Workshop exercise — build a valuation for your venture",
    [
        (0, "Work with your own venture, or a DTL case provided by the facilitator."),
        (0, "1  —  Draw the milestone roadmap from today's TRL to a credible exit."),
        (0, "2  —  State the next round's use of funds and the milestones it buys."),
        (0, "3  —  Find three market references for the exit value."),
        (0, "4  —  Build the rNPV, then reconcile it with benchmarking (matching)."),
        (0, "5  —  Write the downside and upside across the Golden Triangle."),
        (0, "6  —  Set a pre-money, a raise amount, and show the resulting cap table."),
    ],
    callout_text="Deliverable: a one-page valuation memo — a value range, the "
                 "six layers behind it, and every assumption stated.",
    notes_text="Run as a take-away exercise or a breakout. The one-page memo is the "
               "real test of whether the training landed.")

content_slide(
    "Closing  ·  Summary",
    "Key takeaways and further reading",
    [
        (0, "Valuation is an argument built from milestones, funds and market "
            "evidence — it is assembled, not guessed."),
        (0, "rNPV makes de-risking measurable; benchmarking anchors it to the "
            "market; matching reconciles the two."),
        (0, "Always express uncertainty as a downside/upside range across the "
            "Golden Triangle — technology, organisation, commercial."),
        (0, "Stakeholder terms decide who receives the value — read them as "
            "carefully as the headline number."),
        (1, "Damodaran, A. — Valuing Young, Start-up and Growth Companies (NYU Stern)."),
        (1, "Metrick & Yasuda — Venture Capital and the Finance of Innovation."),
        (1, "Razgaitis, R. — Valuation and Dealmaking of Technology-Based IP."),
        (1, "Deep-Tech Lab (DTL) venture files — internal references used in this session."),
    ],
    callout_text="All figures in this deck are illustrative worked examples for "
                 "training purposes — they are not investment advice.",
    notes_text="Close by restating the four takeaways. Point to the reading list "
               "for participants who want the academic underpinnings.")

# ----------------------------------------------------------------------
out = "Valuing_Deep_Tech_Ventures_DTL_Training.pptx"
prs.save(out)
print("Saved", out, "with", len(prs.slides.__iter__.__self__._sldIdLst), "slides")
