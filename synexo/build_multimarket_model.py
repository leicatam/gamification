#!/usr/bin/env python3
"""Multi-market revenue model — SAME Korean-developed personalised product family across all markets.

One product (applicator device + CodeLife-configured peptide/exosome kit) developed for Korean
physicians is exported as-is. Personalisation = physician purpose within the same approved
envelope; NO separate per-market product development. Unit economics are therefore identical in
every market; only the clinic base and timing differ.

Outputs: multimarket-model.csv, multimarket-model.md, Synapep_MultiMarket_Model.docx
"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

DIR = "/home/user/gamification/synexo/"
NAVY = RGBColor(0x1F, 0x3A, 0x5F); GREY = RGBColor(0x55, 0x55, 0x55)

# ---- shared assumptions (identical product everywhere) ----
EXW = 32.50                 # ex-factory kit price, USD
KIT_GM = 0.662              # kit gross margin (GP 21.50)
DEVICE_ASP = 3000.0         # applicator ex-factory ASP
DEVICE_GM = 0.40
KITS_PER_CLINIC_YR = 1400   # ~117/month at maturity (within 100-125 band)
YEARS = [2027, 2028, 2029, 2030]
OPEX = {2026: 800, 2027: 3000, 2028: 7000, 2029: 11000, 2030: 16000}  # $000s [ASSUMPTION]

# ---- cumulative clinics per market per year (same product sold into each) ----
# wave: Korea anchor 2027; Wave1 HK/VN/SG 2027-28; Wave2 ASEAN+GCC 2028-29; Wave3 TW/CN 2029-30
CLINICS = {  # market: {year: cumulative clinics}
    "Korea (anchor)":        {2027: 120, 2028: 250, 2029: 400, 2030: 550},
    "Hong Kong":             {2027: 20,  2028: 60,  2029: 100, 2030: 140},
    "Vietnam":               {2027: 10,  2028: 50,  2029: 110, 2030: 180},
    "Singapore":             {2027: 10,  2028: 35,  2029: 60,  2030: 85},
    "Thailand":              {2027: 0,   2028: 40,  2029: 120, 2030: 220},
    "Malaysia":              {2027: 0,   2028: 20,  2029: 70,  2030: 130},
    "Indonesia":             {2027: 0,   2028: 15,  2029: 70,  2030: 150},
    "Philippines":           {2027: 0,   2028: 10,  2029: 45,  2030: 100},
    "Saudi Arabia (SFDA)":   {2027: 0,   2028: 20,  2029: 70,  2030: 140},
    "UAE (MOHAP)":           {2027: 0,   2028: 15,  2029: 50,  2030: 95},
    "Taiwan":                {2027: 0,   2028: 0,   2029: 35,  2030: 90},
    "China (Hainan->NMPA)":  {2027: 0,   2028: 0,   2029: 40,  2030: 140},
}

def cum(market, year):
    return CLINICS[market].get(year, 0)

def prev_cum(market, year):
    idx = YEARS.index(year)
    return cum(market, YEARS[idx - 1]) if idx > 0 else 0

# ---- compute consolidated P&L ----
totals = {y: {} for y in YEARS}
for y in YEARS:
    cum_total = sum(cum(m, y) for m in CLINICS)
    prev_total = sum(prev_cum(m, y) for m in CLINICS)
    new_clinics = cum_total - prev_total
    avg_clinics = (prev_total + cum_total) / 2.0
    kits = avg_clinics * KITS_PER_CLINIC_YR
    kit_rev = kits * EXW
    dev_rev = new_clinics * DEVICE_ASP
    tot_rev = kit_rev + dev_rev
    kit_gp = kit_rev * KIT_GM
    dev_gp = dev_rev * DEVICE_GM
    tot_gp = kit_gp + dev_gp
    ebitda = tot_gp - OPEX[y] * 1000
    totals[y] = dict(cum=cum_total, new=new_clinics, kits=kits, kit_rev=kit_rev, dev_rev=dev_rev,
                     tot_rev=tot_rev, tot_gp=tot_gp, gm=tot_gp / tot_rev, ebitda=ebitda)

def k(x):  # to $000s int
    return round(x / 1000.0)

# ---------------------------------------------------------------- CSV
with open(DIR + "multimarket-model.csv", "w") as f:
    f.write("Synapep Multi-Market Model — SAME Korean-developed product across all markets (USD)\n")
    f.write("Assumptions,EXW $%.2f,KitGM %.1f%%,DeviceASP $%.0f,DeviceGM %.0f%%,Kits/clinic/yr %d\n"
            % (EXW, KIT_GM * 100, DEVICE_ASP, DEVICE_GM * 100, KITS_PER_CLINIC_YR))
    f.write("\nCUMULATIVE CLINICS BY MARKET," + ",".join(str(y) for y in YEARS) + "\n")
    for m in CLINICS:
        f.write(m + "," + ",".join(str(cum(m, y)) for y in YEARS) + "\n")
    f.write("TOTAL CLINICS," + ",".join(str(totals[y]["cum"]) for y in YEARS) + "\n")
    f.write("\nP&L ($000s)," + ",".join(str(y) for y in YEARS) + "\n")
    f.write("New clinics (devices)," + ",".join(str(totals[y]["new"]) for y in YEARS) + "\n")
    f.write("Treatment kits (000s)," + ",".join(str(k(totals[y]["kits"])) for y in YEARS) + "\n")
    f.write("Kit revenue," + ",".join(str(k(totals[y]["kit_rev"])) for y in YEARS) + "\n")
    f.write("Device revenue," + ",".join(str(k(totals[y]["dev_rev"])) for y in YEARS) + "\n")
    f.write("Total revenue," + ",".join(str(k(totals[y]["tot_rev"])) for y in YEARS) + "\n")
    f.write("Total gross profit," + ",".join(str(k(totals[y]["tot_gp"])) for y in YEARS) + "\n")
    f.write("Blended gross margin," + ",".join("%.1f%%" % (totals[y]["gm"] * 100) for y in YEARS) + "\n")
    f.write("OpEx [ASSUMPTION]," + ",".join(str(OPEX[y]) for y in YEARS) + "\n")
    f.write("EBITDA," + ",".join(str(k(totals[y]["ebitda"])) for y in YEARS) + "\n")

# ---------------------------------------------------------------- Markdown
def md_row(label, vals):
    return "| " + label + " | " + " | ".join(vals) + " |\n"

with open(DIR + "multimarket-model.md", "w") as f:
    f.write("# Synapep — Multi-Market Revenue Model\n\n")
    f.write("> **Same product, more markets.** One product family — the applicator **device** + "
            "**CodeLife-configured peptide/exosome kit** developed for **Korean physicians** — is "
            "exported **as-is**. Personalisation is by *physician purpose within the same approved "
            "envelope*; there is **no separate per-market product development**. Unit economics are "
            "therefore **identical in every market**; only the clinic base and timing differ. "
            "Illustrative; figures USD.\n\n")
    f.write("## Why one product across markets matters\n\n")
    f.write("- **Same unit economics everywhere:** EXW $%.2f, kit GP $21.50 (%.1f%%); device ASP "
            "$%.0f at %.0f%% GM.\n" % (EXW, KIT_GM * 100, DEVICE_ASP, DEVICE_GM * 100))
    f.write("- **Manufacturing scale:** one production line + one QC/stability spec serves all "
            "markets — scale lowers cost and concentrates the cold-chain fix on a single SKU family.\n")
    f.write("- **Richer data flywheel:** the same product used across 12 markets yields a larger, "
            "more comparable outcomes dataset than a fragmented per-market portfolio.\n")
    f.write("- **Regulatory:** the Korean technical file is the master dossier; each market is a "
            "reliance/recognition filing of the *same* device family (see `export-strategy.md`).\n\n")
    f.write("## Cumulative clinics by market (same product sold into each)\n\n")
    f.write(md_row("Market", [str(y) for y in YEARS]))
    f.write("|" + "---|" * (len(YEARS) + 1) + "\n")
    for m in CLINICS:
        f.write(md_row(m, [str(cum(m, y)) for y in YEARS]))
    f.write(md_row("**Total clinics**", ["**%d**" % totals[y]["cum"] for y in YEARS]))
    f.write("\n## Consolidated P&L ($000s)\n\n")
    f.write(md_row("Line", [str(y) for y in YEARS]))
    f.write("|" + "---|" * (len(YEARS) + 1) + "\n")
    f.write(md_row("New clinics (devices sold)", [str(totals[y]["new"]) for y in YEARS]))
    f.write(md_row("Treatment kits (000s)", ["{:,}".format(k(totals[y]["kits"])) for y in YEARS]))
    f.write(md_row("Kit revenue", ["{:,}".format(k(totals[y]["kit_rev"])) for y in YEARS]))
    f.write(md_row("Device revenue", ["{:,}".format(k(totals[y]["dev_rev"])) for y in YEARS]))
    f.write(md_row("**Total revenue**", ["**{:,}**".format(k(totals[y]["tot_rev"])) for y in YEARS]))
    f.write(md_row("Total gross profit", ["{:,}".format(k(totals[y]["tot_gp"])) for y in YEARS]))
    f.write(md_row("Blended gross margin", ["%.1f%%" % (totals[y]["gm"] * 100) for y in YEARS]))
    f.write(md_row("OpEx `[ASSUMPTION]`", ["{:,}".format(OPEX[y]) for y in YEARS]))
    f.write(md_row("**EBITDA**", ["**{:,}**".format(k(totals[y]["ebitda"])) for y in YEARS]))
    f.write("\n*Kits = average active clinics in year × %d kits/clinic/yr (first-year clinics "
            "ramp, approximated by averaging opening and closing clinic counts). Devices = new "
            "clinics × $%.0f. Distributors are arm's-length and non-consolidated; revenue is booked "
            "at the ex-factory line.*\n\n" % (KITS_PER_CLINIC_YR, DEVICE_ASP))
    f.write("## Vs. the single-market (Korea-only) base\n\n")
    f.write("The Korea-only v0.4 base reached ~$39.9M revenue by 2030 from ~1,000 clinics. Selling "
            "the **same product** into 12 markets lifts the clinic base to ~%d and revenue to "
            "~$%.1fM by 2030 — the uplift comes entirely from **distribution reach, not new "
            "products**, so margins are unchanged and R&D is not duplicated.\n"
            % (totals[2030]["cum"], totals[2030]["tot_rev"] / 1e6))
    f.write("\n**Caveats:** clinic ramps per market are assumptions pending anchor-clinic evidence; "
            "the kit's regulatory class varies by market (cosmetic/device/drug) and exosome claims "
            "are restricted — see `export-strategy.md` and business-plan §9. Cold-chain/stability "
            "must be solved on the single product spec before Wave 1.\n")

# ---------------------------------------------------------------- Word
def new_doc():
    doc = Document()
    n = doc.styles["Normal"]; n.font.name = "Calibri"; n.font.size = Pt(10.5)
    for lvl, sz in [("Heading 1", 16), ("Heading 2", 13)]:
        st = doc.styles[lvl]; st.font.name = "Calibri"; st.font.size = Pt(sz)
        st.font.color.rgb = NAVY; st.font.bold = True
    return doc

def para(doc, text="", size=10.5, bold=False, italic=False, color=None, align=None, after=6):
    p = doc.add_paragraph()
    if align: p.alignment = align
    r = p.add_run(text); r.font.size = Pt(size); r.bold = bold; r.italic = italic
    if color: r.font.color.rgb = color
    p.paragraph_format.space_after = Pt(after); return p

def bullet(doc, text, lead=None):
    p = doc.add_paragraph(style="List Bullet")
    if lead:
        r = p.add_run(lead); r.bold = True
    p.add_run(text); return p

def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Light Grid Accent 1"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        r = t.rows[0].cells[i].paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5)
    for row in rows:
        c = t.add_row().cells
        for i, v in enumerate(row):
            rr = c[i].paragraphs[0].add_run(str(v)); rr.font.size = Pt(9.5)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows: row.cells[i].width = Inches(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2); return t

doc = new_doc()
para(doc, "SYNAPEP", size=26, bold=True, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
para(doc, "Multi-Market Revenue Model", size=15, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, after=2)
para(doc, "Same Korean-developed personalised product family, exported across markets. Illustrative.",
     size=9, italic=True, color=GREY, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
para(doc, "Same product, more markets.", bold=True, after=2)
para(doc, "One product family — the applicator device + CodeLife-configured peptide/exosome kit "
          "developed for Korean physicians — is exported as-is. Personalisation is by physician "
          "purpose within the same approved envelope; there is no separate per-market product "
          "development. Unit economics are identical in every market; only the clinic base and "
          "timing differ.")
para(doc, "Why one product across markets matters", bold=True, after=2)
bullet(doc, " EXW $%.2f, kit GP $21.50 (%.1f%%); device ASP $%.0f at %.0f%% GM."
       % (EXW, KIT_GM * 100, DEVICE_ASP, DEVICE_GM * 100), "Same unit economics everywhere —")
bullet(doc, " one production line + one QC/stability spec serves all markets; scale lowers cost and "
            "focuses the cold-chain fix on a single SKU family.", "Manufacturing scale —")
bullet(doc, " the same product across 12 markets yields a larger, comparable outcomes dataset.", "Richer data flywheel —")
bullet(doc, " the Korean technical file is the master dossier; each market is a reliance filing of "
            "the same device family.", "Regulatory —")

doc.add_heading("Cumulative clinics by market", level=2)
table(doc, ["Market"] + [str(y) for y in YEARS],
      [[m] + [str(cum(m, y)) for y in YEARS] for m in CLINICS]
      + [["TOTAL"] + [str(totals[y]["cum"]) for y in YEARS]],
      widths=[2.2, 0.9, 0.9, 0.9, 0.9])

doc.add_heading("Consolidated P&L ($000s)", level=2)
table(doc, ["Line"] + [str(y) for y in YEARS],
      [["New clinics (devices sold)"] + [str(totals[y]["new"]) for y in YEARS],
       ["Treatment kits (000s)"] + ["{:,}".format(k(totals[y]["kits"])) for y in YEARS],
       ["Kit revenue"] + ["{:,}".format(k(totals[y]["kit_rev"])) for y in YEARS],
       ["Device revenue"] + ["{:,}".format(k(totals[y]["dev_rev"])) for y in YEARS],
       ["Total revenue"] + ["{:,}".format(k(totals[y]["tot_rev"])) for y in YEARS],
       ["Total gross profit"] + ["{:,}".format(k(totals[y]["tot_gp"])) for y in YEARS],
       ["Blended gross margin"] + ["%.1f%%" % (totals[y]["gm"] * 100) for y in YEARS],
       ["OpEx [ASSUMPTION]"] + ["{:,}".format(OPEX[y]) for y in YEARS],
       ["EBITDA"] + ["{:,}".format(k(totals[y]["ebitda"])) for y in YEARS]],
      widths=[2.1, 1.1, 1.1, 1.1, 1.1])
para(doc, "Kits = average active clinics × %d kits/clinic/yr (first-year clinics ramp, approximated "
          "by averaging opening/closing counts). Devices = new clinics × $%.0f. Distributors are "
          "arm's-length, non-consolidated; revenue is booked at the ex-factory line."
     % (KITS_PER_CLINIC_YR, DEVICE_ASP), italic=True, size=9, color=GREY)

doc.add_heading("Vs. the single-market (Korea-only) base", level=2)
para(doc, "The Korea-only v0.4 base reached ~$39.9M revenue by 2030 from ~1,000 clinics. Selling the "
          "SAME product into 12 markets lifts the clinic base to ~%d and revenue to ~$%.1fM by 2030 "
          "— uplift from distribution reach, not new products, so margins are unchanged and R&D is "
          "not duplicated." % (totals[2030]["cum"], totals[2030]["tot_rev"] / 1e6))
para(doc, "Caveats: per-market clinic ramps are assumptions pending anchor-clinic evidence; the "
          "kit's regulatory class varies by market (cosmetic/device/drug) and exosome claims are "
          "restricted (see Export Strategy and business-plan §9). Cold-chain/stability must be "
          "solved on the single product spec before Wave 1.", italic=True, size=9, color=GREY)
doc.save(DIR + "Synapep_MultiMarket_Model.docx")

print("2030 total clinics:", totals[2030]["cum"])
for y in YEARS:
    print(y, "rev $%.2fM" % (totals[y]["tot_rev"] / 1e6), "GP $%.2fM" % (totals[y]["tot_gp"] / 1e6),
          "EBITDA $%.2fM" % (totals[y]["ebitda"] / 1e6), "GM %.1f%%" % (totals[y]["gm"] * 100))
print("Saved multimarket-model.csv, multimarket-model.md, Synapep_MultiMarket_Model.docx")
