#!/usr/bin/env python3
"""Render the Synapep v0.4 plan as a single self-contained HTML file (for Drive -> Word .doc)."""

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

P = []; A = P.append
A("<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word'>")
A(f"<head><meta charset='utf-8'><title>Synapep Business Plan and Valuation</title><style>{CSS}</style></head><body>")

# Title
A("<div class='center'>")
A("<h1>SYNAPEP</h1>")
A("<p class='sub'>Business Plan &amp; Valuation</p>")
A("<p><i>AI-personalised regenerative aesthetic medicine — physician-configured peptide treatments</i></p>")
A("<p class='note'>Powered by CodeLife.AI (proprietary model) · IT-EXO&reg; · SynExo</p>")
A("<p><b>Joint Venture: WBI (Wellbiz International) 70% &middot; Eyesel (manufacturing) 30%</b></p>")
A("<p class='note'>Draft v0.4 &middot; Prepared 6 June 2026 &middot; CONFIDENTIAL — internal planning only; illustrative projections, not an offer of securities or investment advice.</p>")
A("</div><hr>")

# 1 Executive summary
A("<h2>1. Executive Summary</h2>")
A("<p><b>Synapep Labs</b> is a <b>physician co-development lab</b> for regenerative aesthetic "
  "medicine. Elite, globally competitive <b>Korean aesthetic doctors</b> bring their clinical "
  "experience into the lab and <b>co-design purpose-built products</b> — personalised to the "
  "<b>physician's clinical case, not the individual patient</b> — powered by <b>CodeLife.AI</b>, "
  "<b>IT-EXO&reg;</b> (immune-tolerant exosomes) and <b>SynExo</b> (synthetic recombinant "
  "exosomes), delivered via an applicator device plus physician-personalised treatment kits.</p>")
A("<p>The company runs on <b>two co-equal moats</b>: (A) an <b>AI engine + compounding data "
  "flywheel</b> — peptides engineered to <b>outperform generalised products</b>, validated by "
  "proprietary AI quality/analytics; and (B) a <b>physician co-development engine</b> — elite "
  "Korean KOLs, a fast/cheap regulatory <b>‘modification engine’</b> that turns each doctor's "
  "request into a registered SKU, and a <b>compliance-first benefit-sharing flywheel</b>. The "
  "wedge is razor-and-blades (applicator device + recurring kits, ~$30–35 ex-factory); the "
  "long-run vision is a data-science company on a <b>portfolio of doctor-originated SKUs</b>.</p>")
A("<p><b>Why now / why this works.</b></p><ul>"
  "<li><b>Large, growing market:</b> medical aesthetics ≈ $17–18.5B (2024), ~10–13% CAGR → ~$56B "
  "by 2033; injectables are &gt;40% of revenue. Korea is a global aesthetic hub; Hong Kong a gateway.</li>"
  "<li><b>Regulatory speed:</b> a <b>modification engine</b> — minor changes to approved products "
  "on Korea's improved-device / <b>negative-list</b> regime and functional-cosmetic/quasi-drug "
  "routes (target <b>&lt;3% change, ~3-month cycle, &lt;$30K per SKU</b>). ~6 months → <b>~20 "
  "registered SKUs</b> across KFDA-recognising Asia. <i>(Working assumptions — to be validated.)</i></li>"
  "<li><b>Doctor-driven flywheel:</b> the inventing physician champions each SKU to peers; "
  "benefit-shared as an <b>FMV royalty for genuine IP co-invention, decoupled from the doctor's "
  "own usage</b> (K-Sunshine compliant).</li>"
  "<li><b>New category, not a me-too:</b> regenerative, doctor-personalised devices/kits sit "
  "beside (not replace) HA fillers and botox.</li></ul>")
A("<p><b>Structure &amp; scope.</b> JV — <b>WBI 70%</b> (IP: CodeLife.AI / IT-EXO / SynExo + R&amp;D) "
  "and <b>Eyesel 30%</b> (manufacturing). Valued <b>standalone at the ex-factory line</b>; "
  "distributors are separate, non-consolidated.</p>")
A("<p><b>Economics &amp; ask.</b> ~65% blended gross margin; revenue $5.3M (2027) → $20.3M (2028) → "
  "$30.2M (2029) → $39.9M (2030); EBITDA-positive in the launch year. Raising <b>$1.0M</b> to kick "
  "off at <b>$5–7M pre-money</b> ($6M midpoint → $1M ≈ 14.3%). The AI/data-platform thesis is the "
  "basis for a premium, institutional-AI <b>Series A in 2028</b>.</p>")

# 2 Technology & AI moat
A("<h2>2. Technology &amp; the AI Moat</h2>")
A("<p>Three pillars — the AI pillar is the spine; devices and kits are the wedge and the "
  "data-capture layer.</p>")
A(tbl(["Pillar", "What it is / why it matters"], [
    ["1 — AI engine &amp; data flywheel", "<b>CodeLife.AI</b> designs personalised peptides "
     "engineered to <b>outperform generalised products</b> (the differentiator is performance, not "
     "just personalisation). A proprietary <b>AI quality-&amp;-analytics suite</b> validates every "
     "batch/variant and improves the model from each treatment — a compounding <b>data flywheel</b> "
     "(inputs/outcomes → better model → better peptides). Built as physician decision-support "
     "within a cleared envelope to manage SaMD exposure."],
    ["2 — Devices &amp; kits (revenue wedge)", "An <b>applicator device</b> placed/sold to clinics "
     "(also the data-capture endpoint) plus recurring <b>personalised treatment kits</b> "
     "(consumables) at ~$30–35 ex-factory, CodeLife-configured within an approved device family."],
    ["3 — Data monetisation (future upside)", "Licensing the model/insights, physician outcome "
     "analytics, and R&amp;D partnerships — the institutional-AI-investor story. Upside; not in the "
     "base P&amp;L."],
]))
A(tbl(["Core technology", "What it is"], [
    ["CodeLife.AI", "Proprietary AI platform / model designing peptides &amp; proteins and "
     "optimising delivery within an approved envelope; the basis of the data-science-company vision."],
    ["IT-EXO&reg;", "Immune-tolerant layer: surface HLA-G suppresses NK/T-cell attack, so efficacy "
     "compounds rather than declines."],
    ["SynExo", "Synthetic recombinant exosome (salmon-derived) carrying growth-factor/peptide cargo; "
     "standardized specs (~20B particles/mL, 30–150 nm, &gt;95% purity); proprietary stabilisation "
     "(lyophilised) gives an ambient-/2–8 °C-stable clinic format — <b>no −80 °C cold chain</b>."],
]))

# 3 Vision
A("<h2>3. Vision — From Devices to a Data-Science Company</h2>")
A("<p>Devices and kits are the wedge that puts CodeLife into clinics and starts the data flywheel. "
  "As personalised treatments and their outcomes accumulate, Synapep builds a proprietary "
  "aesthetic-medicine dataset and <b>its own large model</b> — the durable, compounding asset. "
  "The endpoint is a <b>data-science company in aesthetic medicine</b>: AI-designed, "
  "outcome-validated, continuously improving — and fundable by institutional AI investors.</p>")

# 4 Regulatory strategy
A("<h2>4. Regulatory Strategy (Korea → Hong Kong)</h2>")
A("<ul>"
  "<li><b>Korea (MFDS) first.</b> Register the <b>microneedling/topical applicator + kit</b> as a "
  "device family; CodeLife variants register as <b>“modified devices”</b> (same intended use / "
  "mechanism / raw materials) on the fast path (Class I notification ≈ 15 business days; Class II "
  "“modified” via conformity bodies; ~3 months realistic).</li>"
  "<li><b>Hong Kong next.</b> Light, voluntary <b>MDACS</b> listing; move while the voluntary "
  "window is open (a statutory framework is coming).</li>"
  "<li><b>Keep the fast path valid:</b> personalise via <b>device parameters</b> (delivery, depth, "
  "concentration within an approved range, a menu of pre-cleared options) — <b>not</b> by changing "
  "the active molecule, which would break the “same raw materials” test.</li>"
  "<li><b>Two tracks:</b> the <b>microneedling/topical</b> line carries the device fast-path; the "
  "<b>IM injectable</b> line is handled on a separate drug/cosmetic pathway (see Risks).</li></ul>")

# 5 Go-to-market
A("<h2>5. Go-to-Market</h2>")
A("<ul><li><b>Customers:</b> aesthetic/derm physicians &amp; clinics — Korea first, then Hong Kong.</li>"
  "<li><b>Model:</b> place/sell the applicator device, then earn recurring revenue on personalised "
  "kits; CodeLife + outcome data make the relationship sticky.</li>"
  "<li><b>Build:</b> a focused clinical/KOL salesforce in two concentrated markets; physician "
  "advocates and head-to-head efficacy data drive adoption.</li></ul>")

# 6 AI & data-science build plan
A("<h2>6. AI &amp; Data-Science Build Plan &amp; Costs</h2>")
A("<p>How Pillar 1 (the moat) gets built — and what it costs. All AI/data spend below is a "
  "<b>subset of the OpEx “R&amp;D incl. AI” line</b>, not additional.</p>")
A(tbl(["Phase", "Window", "Deliverables"], [
    ["1 — Foundation", "2026", "Data schema + device-side capture pipeline (consented inputs, "
     "settings, images); <b>CodeLife v1</b> configuration engine within the approved envelope; "
     "<b>AI-QA tooling</b> (batch/variant validation, anomaly detection)."],
    ["2 — Data flywheel", "2027–28", "Live outcome capture from clinics; models linking "
     "formulation/device parameters → outcomes; the <b>proprietary dataset</b> compounds; "
     "physician dashboards (beta)."],
    ["3 — Own large model", "2029–30", "Train a proprietary <b>aesthetic-medicine model</b> on "
     "multimodal data (images + formulations + outcomes); ship physician outcome-analytics "
     "products (Pillar 3 upside)."],
]))
A("<h3>6.1 Team &amp; cost (AI/data subset of OpEx, $000s)</h3>")
A(tbl(["Year", "AI/data FTE", "Personnel", "Compute &amp; data ops", "Total AI spend", "(Total OpEx)"], [
    ["2026", "2", "250", "50", "<b>300</b>", "(700)"],
    ["2027", "4", "600", "100", "<b>700</b>", "(2,600)"],
    ["2028", "7", "1,050", "250", "<b>1,300</b>", "(6,000)"],
    ["2029", "10", "1,600", "400", "<b>2,000</b>", "(8,200)"],
    ["2030", "12", "2,000", "600", "<b>2,600</b>", "(10,000)"],
]))
A("<p>Core roles: <b>ML/AI lead</b> (peptide design + model strategy), data/ML engineers, "
  "data-platform/MLOps, clinical-data/annotation, and regulatory-aware ML (SaMD). Recruit the "
  "ML/AI lead and a data engineer first (2026); scale annotation and MLOps as clinic data arrives.</p>")
A("<p><b>Data moat:</b> every CodeLife-configured treatment generates consented inputs, device "
  "parameters and (where permitted) outcome data via the applicator device. More treatments → "
  "better models → peptides that outperform generalised products → more clinics → more data. The "
  "<b>dataset, not the code, is the durable moat</b> — and the line item that turns Synapep from a "
  "medtech story (Lens A) into an AI/data-company story (Lens B). Governance: consent, "
  "de-identification, Korea/HK data-protection compliance, physician in the loop.</p>")

# 7 Financial model
A("<h2>7. Financial Model</h2>")
A("<p>Bottom-up by <b>clinics</b> (~100–125 kits/clinic/month at maturity). Kit unit economics: "
  "COGS = 20%×EXW + $4.50 material = $11.00 at $32.50 → <b>GP $21.50, 66.2%</b>. Device ASP "
  "$3,000 at 40% GM. All figures USD; illustrative.</p>")
A(tbl(["Driver", "2026 prep", "2027", "2028", "2029", "2030"], [
    ["Clinics (cumulative)", "0", "150", "400", "700", "1,000"],
    ["New clinics (devices sold)", "0", "150", "250", "300", "300"],
    ["Treatment kits (000s)", "0", "148", "600", "900", "1,200"],
]))
A("<h3>7.1 P&amp;L ($ thousands)</h3>")
A(tbl(["Line", "2026", "2027", "2028", "2029", "2030"], [
    ["Kit revenue ($32.50)", "0", "4,810", "19,500", "29,250", "39,000"],
    ["Device revenue ($3k ASP)", "0", "450", "750", "900", "900"],
    ["<b>Total revenue</b>", "0", "<b>5,260</b>", "<b>20,250</b>", "<b>30,150</b>", "<b>39,900</b>"],
    ["Kit gross profit (66.2%)", "0", "3,182", "12,900", "19,350", "25,800"],
    ["Device gross profit (40%)", "0", "180", "300", "360", "360"],
    ["<b>Total gross profit</b>", "0", "<b>3,362</b>", "<b>13,200</b>", "<b>19,710</b>", "<b>26,160</b>"],
    ["Blended gross margin", "—", "63.9%", "65.2%", "65.4%", "65.6%"],
    ["OpEx (clinical sales, reg, R&amp;D incl. AI, G&amp;A)", "700", "2,600", "6,000", "8,200", "10,000"],
    ["<b>EBITDA</b>", "(700)", "<b>762</b>", "<b>7,200</b>", "<b>11,510</b>", "<b>16,160</b>"],
]))
A("<h3>7.2 Scenarios (2029)</h3>")
A(tbl(["Scenario", "Clinics", "EXW", "Revenue", "Gross profit"], [
    ["Conservative", "~500", "$30", "~$22M", "~$14M"],
    ["Base", "700", "$32.50", "$30.2M", "$19.7M"],
    ["Upside", "~850", "$35", "~$38M", "~$25M"],
]))
A("<p class='note'>Pillar-3 data monetisation (model/insight licensing, outcome analytics) is "
  "deliberately excluded from the base P&amp;L and treated as upside.</p>")

# 8 Valuation
A("<h2>8. Valuation — Two Lenses</h2>")
A("<p><b>Lens A — device + consumables business (the floor; sets the kickoff price).</b> Recommend "
  "<b>$5–7M pre-money / $6–8M post</b>, $6M midpoint → $1.0M buys ~14.3%. Three methods reconcile: "
  "seed convention for an IP-owning JV ($5–7M); DCF (40% discount, 8× EBITDA exit) ≈ $35M "
  "un-risk-adjusted EV → ~$5–7M risk-adjusted; forward multiple. Recurring medical consumables + "
  "regulatory moat support the upper half and a higher revenue multiple (3–6×).</p>")
A("<p><b>Lens B — AI / data-science company (the prize; attracts institutional AI capital).</b> "
  "With a proprietary model, an AI-QA/analytics suite, and a compounding data flywheel, the "
  "comparables shift from medtech to AI/data platforms — much higher multiples. This does not "
  "change the $1M kickoff price (priced on Lens A) but raises the valuation ceiling and reframes "
  "the <b>2028 Series A as a premium, institutional AI round</b>.</p>")
A("<h3>8.1 Cap table (post-raise, $6.0M pre-money)</h3>")
A(tbl(["Holder", "Contribution", "Founder %", "% post-raise"], [
    ["WBI", "IP (CodeLife.AI/IT-EXO/SynExo) + R&amp;D", "70.0%", "60.0%"],
    ["Eyesel", "Manufacturing (production, fill-finish, QA)", "30.0%", "25.7%"],
    ["Kickoff investor(s)", "$1.0M cash", "—", "14.3%"],
    ["Total", "", "100%", "100%"],
]))
A("<p class='note'>Recommendation: price the kickoff on Lens A ($6M midpoint); pitch Lens B as the "
  "prize and the Series A thesis. Optionally test institutional-AI appetite for a larger round.</p>")

# 9 What a technical investor will challenge
A("<h2>9. What a Technical Investor Will Challenge (and Our Answer)</h2>")
A("<p>A chemical-engineer investor entering aesthetics will press these; pre-empting them:</p>")
A(tbl(["Challenge", "Our answer / action"], [
    ["Cold chain — resolved; substantiate it. Proprietary stabilisation gives an ambient-/2–8 °C "
     "format (no −80 °C) — a distribution/export advantage. COGS is still top-down with no BOM.",
     "Provide the stability/shelf-life dossier confirming the cold-chain-free format, and publish a "
     "bottom-up BOM incl. per-batch QC-release cost; treat early-year margins as lower until scale."],
    ["Personalisation vs “same raw materials” is a contradiction — real personalisation changes "
     "the active and breaks the device fast-path.", "Personalisation lives in a pre-cleared "
     "configuration envelope (delivery, depth, concentration range, option menu) — defended as both "
     "regulatorily clean and clinically differentiating."],
    ["Exosomes are a regulatory/characterisation minefield (Korea ad ban; EU human-exosome ban; "
     "US FDA warnings).", "Lead with non-human (salmon/synthetic) origin; provide "
     "COA/particle/potency/purity/stability/batch data; market on function, not medical claims."],
    ["“$25M exposure” is weasel-phrased — it aggregates affiliated entities.", "Re-present at "
     "entity/product/channel level with reorder data; weight as market signal, not Synapep revenue."],
    ["“Own large model” overreaches for a 2→12 FTE team.", "Reframe as a structured, consented "
     "outcomes dataset + decision-support analytics; moat is data + clinic data-rights clauses."],
    ["Clinic ramp is aggressive (0→150 in year one; plan itself calls 150 ‘upside’).", "Rebuild the "
     "base off anchor-clinic actuals (real kits/clinic/month + reorder cohorts) before scaling capital."],
]))

# 10 International expansion
A("<h2>10. International Expansion (KFDA as an Export Springboard)</h2>")
A("<p>Synapep is <b>not a Korea-only play</b>: a Korean MFDS registration anchors a reliance-led "
  "export strategy (full detail in <i>export-strategy.md</i>). Two-speed thesis — the applicator "
  "<b>device travels widely</b> on the Korean technical file; the peptide/exosome <b>kit is wrapped "
  "per market</b> (cosmetic vs device vs drug), leaning on <b>salmon/synthetic origin</b> and strict "
  "claim discipline.</p>")
A(tbl(["Tier", "Markets &amp; KFDA leverage"], [
    ["Tier 1 — ASEAN + Hong Kong (fastest)", "<b>Hong Kong MDACS</b> recognises Korea MFDS as a "
     "reference regulator (pair Korea + Singapore for the ≥2-reference expedited route); "
     "<b>Vietnam</b> accepts MFDS certifications; <b>Singapore HSA</b> is the gateway; one "
     "<b>ASEAN AMDD/CSDT</b> dossier cascades to Thailand, Malaysia, Indonesia, Philippines."],
    ["Tier 2 — GCC + Greater China", "<b>Saudi SFDA</b> (GCC regional reference) + <b>UAE MOHAP</b>; "
     "<b>Taiwan TFDA</b> accepts Korean data; <b>China NMPA</b> via Hainan/cross-border first."],
]))
A("<p>Precedent: Korean salmon-<b>PDRN</b> boosters (e.g., Rejuran) exported across SEA/Middle "
  "East/Europe off a Korean approval — a near-exact analog. Sequence: Korea anchor → "
  "HK/Vietnam/Singapore (2027–28) → ASEAN + GCC (2028–29) → Taiwan/China (2029–30); each market "
  "needs a local responsible person/distributor. <b>Cold-chain-free advantage:</b> stabilisation "
  "removes the −80 °C dependency, so cross-border distribution is far easier than for typical "
  "exosome products. Effect: the clinic ramp becomes a <b>multi-market TAM</b>, strengthening Lens "
  "A and the Series A.</p>")

# 11 Risks
A("<h2>11. Key Risks</h2><ul>"
  "<li><b>Device-vs-drug classification (#1).</b> An <b>IM injectable</b> peptide is very likely a "
  "<b>drug/biologic</b>, not a device, in Korea and HK. Lead the device fast-path with the "
  "<b>microneedling/topical</b> line + applicator system; run the IM/injectable line on a separate "
  "drug/cosmetic track.</li>"
  "<li><b>“Same raw materials” constraint.</b> Personalise via device parameters within an approved "
  "envelope; changing the active molecule can break the fast path.</li>"
  "<li><b>AI substantiation.</b> The “outperforms generalised products” and data-moat claims need "
  "<b>head-to-head efficacy evidence</b> and a real ML capability/dataset behind the “own large "
  "model.”</li>"
  "<li><b>SaMD exposure.</b> CodeLife may be regulated as Software as a Medical Device; keep the "
  "physician in the loop and operate within a cleared envelope.</li>"
  "<li><b>Incumbents.</b> HA/botox (~$5–6.5B, still growing) are not displaced — position as a new "
  "adjacent category.</li>"
  "<li><b>Capital adequacy.</b> $1M kicks off; multi-market registration + clinical salesforce + AI "
  "team likely need a 2028 Series A.</li></ul>")

# 12 Next steps
A("<h2>12. What Would Make This Investment-Grade</h2><ul>"
  "<li>Confirm the regulatory split: microneedling/topical (device fast-path) vs IM injectable (drug).</li>"
  "<li>Produce head-to-head efficacy data (AI-personalised vs generalised) and define the AI/data "
  "team and dataset plan behind the “own large model.”</li>"
  "<li>Document the IP-contribution scope WBI assigns into the JV.</li>"
  "<li>Confirm device ASP/GM, clinic ramp, and kits/clinic/month; name the core team and an "
  "anchor-clinic pipeline in Korea/HK.</li></ul>")
A("<p class='note'>Sources — medical aesthetics market: MarketsandMarkets, P&amp;S Intelligence, "
  "DataM. Korea MFDS modified-device path: Emergo by UL, ElendiLabs, MedDeviceGuide. Hong Kong "
  "MDACS: mdd.gov.hk, Asia Actual. Botox/HA: Future Market Insights, Allied Market Research, "
  "Grand View Research.</p>")

A("</body></html>")
html = "".join(P)
with open("/home/user/gamification/synexo/Synapep_Business_Plan_and_Valuation.html", "w") as f:
    f.write(html)
print("HTML bytes:", len(html))
