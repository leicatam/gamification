#!/usr/bin/env python3
"""Render the Synapep plan as a single self-contained HTML file (for Drive -> Google Doc)."""

CSS = """
body{font-family:Calibri,Arial,sans-serif;font-size:11pt;color:#222;line-height:1.4;}
h1{font-size:20pt;color:#1F3A5F;margin:0;}
h2{font-size:15pt;color:#1F3A5F;border-bottom:1px solid #1F3A5F;padding-bottom:2px;margin-top:22px;}
h3{font-size:12.5pt;color:#1F3A5F;margin-top:14px;}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:10pt;}
th,td{border:1px solid #9bb;padding:4px 7px;text-align:left;vertical-align:top;}
th{background:#1F3A5F;color:#fff;}
.sub{color:#555;font-size:12pt;}
.note{color:#555;font-style:italic;font-size:9.5pt;}
.center{text-align:center;}
ul{margin:4px 0 10px 0;}
"""

def tbl(headers, rows):
    h = "".join(f"<th>{c}</th>" for c in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table><tr>{h}</tr>{body}</table>"

P = []
A = P.append

A(f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>")

# Title block
A("<div class='center'>")
A("<h1>SYNAPEP</h1>")
A("<p class='sub'>Business Plan &amp; Valuation</p>")
A("<p><i>AI-designed peptide / protein actives + SynExo synthetic recombinant exosomes</i></p>")
A("<p class='note'>Powered by IT-EXO&reg; (immune-tolerant stealth exosomes) and "
  "ai.peptide / CodeLife.AI</p>")
A("<p><b>Joint Venture: WBI (Wellbiz International) 70% &middot; Eyesel (manufacturing) 30%</b></p>")
A("<p class='note'>Draft v0.3 &middot; Prepared 5 June 2026 &middot; CONFIDENTIAL — internal "
  "planning only; illustrative projections, not an offer of securities or investment advice.</p>")
A("</div><hr>")

# 1 Executive summary
A("<h2>1. Executive Summary</h2>")
A("<p>Synapep is a new company commercializing Synexo technology — the SynExo synthetic "
  "recombinant exosome platform plus AI-designed peptide/protein actives. It is built on two "
  "core technologies: <b>IT-EXO&reg;</b> (the immune-tolerant, HLA-G “stealth” exosome "
  "that lets results compound without immune decline) and <b>ai.peptide / CodeLife.AI</b> "
  "(the AI platform that designs peptides, proteins, and exosome cargo and optimizes targeting).</p>")
A("<p>After a 6–9 month preparation phase (lab setup, −80&nbsp;°C cold-chain and "
  "process qualification, QA, first cosmetic registrations), Synapep will be ready for sales in "
  "<b>February 2027</b>. The initial portfolio is 5–6 vial / skin-booster products with a "
  "combined capacity of 50,000–100,000 vials per month at a USD 30–35 ex-factory price. "
  "Route to market: aesthetic / cosmeceutical first, then medical (FDA/KFDA) — sold OEM / "
  "white-label so the customer holds the registration.</p>")
A("<p><b>Structure &amp; scope.</b> Synapep is a joint venture — <b>WBI 70%</b> (contributes "
  "the Synexo IP: IT-EXO / SynExo / CodeLife.AI, plus R&amp;D) and <b>Eyesel 30%</b> (the "
  "manufacturing entity). Synapep owns/co-owns the platform and controls its own production. It "
  "is valued <b>standalone at the ex-factory line</b>; downstream distributors (e.g. NeuNova "
  "USA) are separate, non-consolidated entities and excluded from this valuation.</p>")
A("<p><b>Headline economics.</b></p><ul>"
  "<li><b>Margin:</b> ~66% ex-factory gross margin (material cost confirmed &lt; $5/vial; "
  "modeled $4.50).</li>"
  "<li><b>Revenue:</b> $4.8M (2027) &rarr; $19.5M (2028) &rarr; $29.3M (2029) &rarr; $39.0M (2030).</li>"
  "<li><b>Profitability:</b> EBITDA-positive in the launch year; ~$11M EBITDA by 2029.</li></ul>")
A("<p><b>The ask.</b> USD 1.0M to kick off, at a recommended <b>$5–7M pre-money</b> "
  "($6M midpoint &rarr; $1M &asymp; 14.3%). Use of funds: $500K Synapep Lab + $600K running "
  "capital through launch.</p>")

# 2 Opportunity & tech
A("<h2>2. The Opportunity &amp; Technology</h2>")
A("<p>Conventional exosome therapeutics face three bottlenecks the Synexo stack solves:</p><ul>"
  "<li><b>Immune rejection / instability</b> — human exosomes are unstable, costly, and carry "
  "rejection risk. IT-EXO&reg; adds surface HLA-G as an immune “stealth shield,” so "
  "efficacy compounds rather than declines.</li>"
  "<li><b>Inconsistent supply</b> — SynExo is a synthetic recombinant platform with standardized "
  "specs (~20B particles/mL, 30–150&nbsp;nm, &gt;95% purity, &gt;60% encapsulation).</li>"
  "<li><b>Slow, expensive design</b> — ai.peptide / CodeLife.AI designs peptides/proteins and "
  "exosome cargo computationally and simulates loading/targeting.</li></ul>")
A(tbl(["Platform", "What it is"], [
    ["SynExo", "Synthetic recombinant exosome (salmon-derived) carrying plasmid-DNA cargo "
     "(EGF/bFGF/VEGF) and mRNA; host cell transiently expresses healing proteins. 12-month "
     "stability at −80&nbsp;°C (cold chain)."],
    ["IT-EXO&reg;", "Immune-tolerant layer: surface HLA-G engages ILT2/ILT4/KIR2DL4 to suppress "
     "NK/T-cell attack (IL-1β ~1.8→0.8 ng/mL, TNF-α ~0.7→0.4 ng/mL; &gt;95% "
     "cell viability). No efficacy decline; effects compound."],
    ["ai.peptide / CodeLife.AI", "AI platform designing peptides/proteins for functional "
     "cosmetics and optimizing exosome cargo, loading efficiency, and targeting."],
]))

# 3 Product & IP
A("<h2>3. Product &amp; Intellectual Property</h2>")
A("<p><b>Portfolio (5–6 SKUs — vials / skin boosters / ampoules).</b> Likely lines, to "
  "confirm: ① aesthetic skin-booster, ② scalp/hair regeneration, ③ wound-healing/"
  "repair, ④ post-procedure recovery, ⑤ targeted AI-peptide active, ⑥ custom-cargo "
  "SynExo — together filling the 50,000–100,000 vials/month capacity.</p>")
A("<p><b>Intellectual property</b> (held by WBI, contributed into the JV — confirm scope):</p>")
A(tbl(["Asset", "Ref / number", "Status"], [
    ["SynExo HLA-G (Korea)", "P25E10C1475 (filed 2025-11-11)", "Application"],
    ["SynExo HLA-G (PCT)", "X25E10C0258 (2025-11-18)", "PCT application"],
    ["Safe-Browning shampoo", "KR 10-2025-0191060", "Application"],
    ["Ion-microneedling device", "KR 10-2654857", "Registered"],
    ["Sophora Japonica stem cell", "KR 10-1080297", "Registered"],
    ["SynExo HLA-G", "Journal-ready manuscript", "Publication pending"],
]))
A("<p class='note'>Credibility: endorsement by Prof. Cho Hangrae (President, Korean "
  "Dermatological Society); NET government award; MORIMANA clinical claim of +19% hair thickness "
  "and −66% scalp flakiness in 8 weeks; use by leading Korean clinics.</p>")

# 4 GTM
A("<h2>4. Go-to-Market</h2><ul>"
  "<li><b>Channel — OEM / white-label.</b> Synapep sells bulk/vialled product ex-factory (EXW) "
  "to independent distributors, partner brands, aesthetic clinics, and med-spas who relabel and "
  "hold the registration. Arm's-length customers buy at $30–35 EXW; their downstream margin "
  "is excluded from the valuation. (NeuNova USA, a separate non-consolidated entity, is one "
  "potential US distributor.)</li>"
  "<li><b>Ramp</b> — the 2027 constraint is customer acquisition, not capacity: 2K vials "
  "(Feb 2027) &rarr; 28K/mo exit run-rate (Dec 2027) &rarr; 50K (2028) &rarr; 75K (2029) &rarr; "
  "100K (2030).</li>"
  "<li><b>Pricing</b> — $30–35/vial EXW; large contracts near the $30 floor still ~65% GM.</li></ul>")

# 5 Ops
A("<h2>5. Operations &amp; Timeline</h2>")
A(tbl(["Phase", "Window", "Milestones"], [
    ["Preparation", "Jul 2026 – Jan 2027 (6–9 mo)", "Lab build-out, −80&nbsp;°C "
     "cold-chain &amp; fill-finish qualification, QA/QC, first cosmetic registrations, hire team, "
     "finalize JV/IP terms"],
    ["Launch", "Feb 2027", "First commercial sales (cosmetic skin-booster line); 2–3 products live"],
    ["Ramp", "2027", "Add remaining products; reach 28K/mo exit run-rate"],
    ["Scale", "2028–2030", "50K → 75K → 100K vials/month; begin FDA/KFDA medical "
     "pathway; likely Series A in 2028"],
]))
A("<p class='note'>Cold chain: SynExo is stable 12 months at −80&nbsp;°C. Ultra-cold "
  "storage, validated shipping, and stability/QC are real cost lines — budgeted within the "
  "manufacturing cost formula (confirm with Eyesel).</p>")

# 6 Financials
A("<h2>6. Financial Model</h2>")
A("<p>Base case: EXW $32.50 (midpoint of $30–35), material cost $4.50/vial (confirmed "
  "&lt; $5). All figures USD; illustrative projections.</p>")
A("<h3>6.1 Unit economics (per vial)</h3>")
A("<p class='note'>COGS = (10% × EXW) + material + (10% × EXW) = 20% × EXW + material.</p>")
A(tbl(["Line", "$ / vial"], [
    ["Ex-factory price (EXW)", "32.50"], ["– Manufacturing (10% × EXW)", "3.25"],
    ["– Material cost", "4.50"], ["– Second 10% (10% × EXW)", "3.25"],
    ["= COGS", "11.00"], ["Gross profit / vial", "21.50"], ["Gross margin", "66.2%"],
]))
A("<h3>6.2 Annual P&amp;L ($ thousands)</h3>")
A(tbl(["", "2026 prep", "2027", "2028", "2029", "2030"], [
    ["Vials sold (000s)", "0", "148", "600", "900", "1,200"],
    ["Revenue", "0", "4,810", "19,500", "29,250", "39,000"],
    ["COGS", "0", "1,628", "6,600", "9,900", "13,200"],
    ["Gross profit", "0", "3,182", "12,900", "19,350", "25,800"],
    ["Gross margin", "—", "66.2%", "66.2%", "66.2%", "66.2%"],
    ["OpEx (assumption)", "700", "2,400", "5,800", "8,000", "9,800"],
    ["EBITDA", "(700)", "782", "7,100", "11,350", "16,000"],
    ["EBITDA margin", "—", "16.3%", "36.4%", "38.8%", "41.0%"],
]))
A("<h3>6.3 Scenarios (full-year 2029)</h3>")
A(tbl(["Scenario", "EXW", "Material", "Vials/yr", "Revenue", "GP", "GM%"], [
    ["Conservative", "$30", "$5", "720,000", "$21.6M", "$14.0M", "65.0%"],
    ["Base", "$32.50", "$4.50", "900,000", "$29.25M", "$19.35M", "66.2%"],
    ["Upside", "$35", "$3", "1,080,000", "$37.8M", "$25.4M", "67.1%"],
]))

# 7 Valuation
A("<h2>7. Valuation</h2>")
A("<p>Synapep is a pre-revenue JV that owns/co-owns the Synexo platform, raising $1.0M to kick "
  "off, valued <b>standalone at the ex-factory line</b>.</p><ul>"
  "<li><b>Price this round at:</b> $5–7M pre-money / $6–8M post-money — $1.0M buys "
  "~13–17%. Stepped up from a bare-licence shell because, as a JV, Synapep holds the IP "
  "(patents filed), runs in-house manufacturing (Eyesel), earns ~66% margins, and has Feb-2027 "
  "revenue.</li>"
  "<li><b>The prize if it executes:</b> ~$30–40M risk-unadjusted enterprise value by "
  "2030–31, plus platform-licensing optionality.</li></ul>")
A("<h3>7.1 Three methods (they reconcile)</h3>")
A(tbl(["Method", "Un-risk-adjusted", "Risk-adjusted (JV, ~20%)", "Today's round"], [
    ["Seed convention (owns IP)", "—", "$5–7M", "direct"],
    ["DCF (40% discount, 8× EBITDA exit)", "~$35M EV", "~$6–7M", "matches"],
    ["Forward revenue/EBITDA multiple", "$25–37M (PV of EV)", "$5–8M", "matches"],
]))
A("<p><b>Recommendation: price the $1.0M kickoff at $5–7M pre-money ($6–8M post), "
  "$6M midpoint.</b></p>")
A("<h3>7.2 Illustrative post-raise cap table (pre-money $6.0M)</h3>")
A(tbl(["Holder", "Contribution", "Founder %", "% post-raise"], [
    ["WBI", "Synexo IP (IT-EXO/SynExo/CodeLife.AI) + R&amp;D", "70.0%", "60.0%"],
    ["Eyesel", "Manufacturing entity (production, fill-finish, QA)", "30.0%", "25.7%"],
    ["Kickoff investor(s)", "$1.0M cash", "—", "14.3%"],
    ["Total", "", "100%", "100%"],
]))
A("<p class='note'>At $6.0M pre / $7.0M post, $1.0M buys 14.3%. NeuNova (US distribution) sits "
  "outside this cap table.</p>")

# 8 Risks
A("<h2>8. Key Risks</h2><ul>"
  "<li><b>IP contribution terms</b> — resolved by the JV, but scope (fields, territories, "
  "exclusivity, royalties) must be documented.</li>"
  "<li><b>Customer concentration &amp; ramp</b> — landing the first 2–3 anchor accounts is "
  "make-or-break in 2027.</li>"
  "<li><b>Regulatory</b> — cosmetic pathway is fast, but exosome regulation is evolving; the "
  "medical line needs FDA/KFDA work. Keep cosmetic/medical claims separated.</li>"
  "<li><b>Cold chain / ops</b> — −80&nbsp;°C storage and validated shipping add cost "
  "and failure modes.</li>"
  "<li><b>Capital adequacy</b> — $1M kicks off; scaling likely needs a 2028 Series A.</li>"
  "<li><b>Margin</b> — largely de-risked: sub-$5 material cost keeps GM ~64–71%.</li></ul>")

# 9 Next steps
A("<h2>9. What Would Make This Plan Investment-Grade</h2><ul>"
  "<li><b>Document the IP-contribution scope</b> WBI assigns into the JV — biggest single driver.</li>"
  "<li><b>Name the core team</b> (the advisor bench already has real credibility).</li>"
  "<li><b>Confirm the 5–6 SKUs</b>, their volumes/prices, and an anchor-customer pipeline.</li>"
  "<li><b>Confirm material cost</b> and that cold-chain/fill-finish are inside the COGS formula.</li></ul>")
A("<p class='note'>Source materials (WBI/NeuNova/SynExo documents and patent filings) are held "
  "in the user's Google Drive; figures here are grounded in those files. OpEx is an internal "
  "assumption pending a headcount/spend plan.</p>")

A("</body></html>")

html = "".join(P)
with open("/home/user/gamification/synexo/Synapep_Business_Plan_and_Valuation.html", "w") as f:
    f.write(html)
print("HTML bytes:", len(html))
