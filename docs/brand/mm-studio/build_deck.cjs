// MM Studio — UK investor brief v3 generator (v2 plus the Seoul immersion memo of 5 Oct 2026).
// Run: node build_deck.js [outfile]   (needs pptxgenjs, react, react-dom, react-icons, sharp)
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const SKILL = process.env.PPTX_SKILL_DIR || "/root/.claude/skills/synced/36b83d80-6c88-4b1f-9f14-ce26657dad9e_62282606-1d66-4bbb-8992-2f9c9ff867bd/pptx";
const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));

const OUT = process.argv[2] || path.join(__dirname, "MM_Studio_Investor_Brief_EN_v3.pptx");
const ASSETS = path.join(__dirname, "assets");
const NOTES_V1 = process.env.NOTES_V1 ? JSON.parse(fs.readFileSync(process.env.NOTES_V1, "utf8")) : {};

const THEME = {
  name: "MM Studio",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: { dk1: "1B2233", lt1: "FFFFFF", dk2: "5C6270", lt2: "F4F2ED", accent1: "B08D57", accent2: "C9CEDA",
    accent3: "7A8CA8", accent4: "8C4A4A", accent5: "3E6B5A", accent6: "2A3550", hlink: "2A3550", folHlink: "5C6270" },
};
const HEX = { ink: "1B2233", grey: "5C6270", mist: "C9CEDA", cream: "F4F2ED", gold: "B08D57", white: "FFFFFF" };

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "MM Studio — Investor Brief (UK programme)";
pres.author = "MM Studio";
const C = pres.SchemeColor;
const W = 13.333, M = 0.6, CW = W - 2 * M;

pres.defineSlideMaster({
  title: "LIGHT",
  objects: [
    { text: { text: "MM Studio  ·  Investor brief  ·  UK programme  ·  Discussion draft  ·  October 2026",
        options: { x: M, y: 7.0, w: 9, h: 0.3, fontSize: 11, color: C.text2, margin: 0, isTextBox: true } } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 0.4, w: CW, h: 1.0, fontSize: 28, bold: true,
        color: C.text1, valign: "top", align: "left", margin: 0 }, text: "" } },
  ],
  slideNumber: { x: W - M - 0.6, y: 7.0, w: 0.6, h: 0.3, fontSize: 11, color: C.text2, align: "right" },
});
pres.defineSlideMaster({ title: "DARK", background: { color: HEX.ink }, objects: [] });

// ---------- helpers ----------
const png = async (Icon, color, size = 256) => {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Icon, { color: "#" + color, size: String(size) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
};
const crop = async (file, wIn, hIn, pos = "attention") => {
  const buf = await sharp(path.join(ASSETS, file)).resize(Math.round(wIn * 200), Math.round(hIn * 200), { fit: "cover", position: pos }).jpeg({ quality: 88 }).toBuffer();
  return "image/jpeg;base64," + buf.toString("base64");
};
const asset = (f) => path.join(ASSETS, f);
const card = (s, x, y, w, h, name, fill = C.background2) =>
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h, fill: { color: fill }, line: { color: fill, width: 0 }, rectRadius: 0.08, objectName: name });
const txt = (s, text, x, y, w, h, o = {}) =>
  s.addText(text, Object.assign({ x, y, w, h, fontSize: 14, color: C.text1, margin: 0, valign: "top", isTextBox: true }, o));
async function badge(s, Icon, x, y, d, name, bg = C.text1, fg = "FFFFFF") {
  s.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color: bg }, line: { color: bg, width: 0 }, objectName: name + " circle" });
  s.addImage({ data: await png(Icon, fg), x: x + d * 0.25, y: y + d * 0.25, w: d * 0.5, h: d * 0.5, objectName: name + " icon", altText: name });
}
const notes = (s, extra, v1) => s.addNotes([extra, v1 ? NOTES_V1[v1] : ""].filter(Boolean).join("\n\n"));
const light = (title, section) => { const s = pres.addSlide({ masterName: "LIGHT", sectionTitle: section }); s.addText(title, { placeholder: "title" }); return s; };

(async () => {
  // ===== 1 Cover =====
  pres.addSection({ title: "Opening" });
  let s = pres.addSlide({ masterName: "DARK", sectionTitle: "Opening" });
  s.addImage({ data: await crop("london-opening.jpg", 4.9, 7.5, "north"), x: W - 4.9, y: 0, w: 4.9, h: 7.5, objectName: "London opening photo", altText: "MM Studio London grand opening team" });
  txt(s, "MM STUDIO", M + 0.2, 0.7, 6, 0.4, { fontSize: 16, bold: true, color: C.accent1, charSpacing: 6 });
  txt(s, "Digital cosmetics,\npersonalised for the world.", M + 0.2, 1.9, 7.4, 2.4, { fontSize: 46, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  txt(s, "Korean R&D and 30+ years of product design, a UK training hub, and an AI-ready client ecosystem.", M + 0.2, 4.55, 6.9, 1.0, { fontSize: 20, color: C.background2 });
  txt(s, "Investor brief  ·  UK programme  ·  Discussion draft  ·  October 2026", M + 0.2, 6.6, 7.2, 0.35, { fontSize: 13, color: C.accent2 });
  notes(s, "Positioning headline reflects the owner's goal (digital cosmetics) and mission (personalised solutions as the deliverable to the world), 4 Oct 2026. Photo: London opening, from the v1 deck.");

  // ===== 2 Vision, mission, values =====
  pres.addSection({ title: "Why MM Studio" });
  s = light("Digital cosmetics: where MM Studio is going", "Why MM Studio");
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 1.65, w: 5.0, h: 5.05, fill: { color: C.text1 }, line: { color: C.text1, width: 0 }, rectRadius: 0.08, objectName: "Goal and mission panel" });
  txt(s, "OUR GOAL", M + 0.4, 2.0, 4.2, 0.3, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 4 });
  txt(s, "Digital cosmetics", M + 0.4, 2.35, 4.2, 0.7, { fontSize: 30, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  txt(s, "Cosmetic care that is measured, personalised and tracked over time, so every product and protocol is chosen from data about the individual.", M + 0.4, 3.1, 4.2, 1.5, { fontSize: 15, color: C.background2 });
  txt(s, "OUR MISSION", M + 0.4, 4.75, 4.2, 0.3, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 4 });
  txt(s, "Deliver personalised solutions to the world.", M + 0.4, 5.1, 4.2, 1.3, { fontSize: 22, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  const vals = [
    [fa.FaUserCheck, "Personal, not generic", "Every plan starts from the individual's own scan, goals and history."],
    [fa.FaFlask, "Science with discipline", "We explain mechanisms and keep evidence separate from marketing claims."],
    [fa.FaHandsHelping, "Craft guided by data", "Trained professional hands, supported by AI-assisted imaging, never replaced by it."],
    [fa.FaLayerGroup, "One shared standard", "A single method, product range and training path across every studio."],
  ];
  const vx = M + 5.35, vw = (CW - 5.35 - 0.25) / 2;
  for (let i = 0; i < 4; i++) {
    const x = vx + (i % 2) * (vw + 0.25), y = 1.65 + Math.floor(i / 2) * 2.65;
    card(s, x, y, vw, 2.4, "Value card " + (i + 1));
    await badge(s, vals[i][0], x + 0.3, y + 0.3, 0.6, "Value " + (i + 1));
    txt(s, vals[i][1], x + 0.3, y + 0.95, vw - 0.6, 0.65, { fontSize: 16, bold: true });
    txt(s, vals[i][2], x + 0.3, y + 1.55, vw - 0.6, 0.8, { fontSize: 13, color: C.text2 });
  }
  notes(s, "Goal and mission are the owner's wording (key-elements archive, items 2 and 3). The four values are drafted from the brand book's stated approach and need owner confirmation.");

  // ===== 3 Leadership =====
  s = light("A leadership bench no single-discipline rival can match", "Why MM Studio");
  const lead = [
    [fa.FaMicroscope, "Scientists", "Formulation and vesicle research behind IT-EXO and SynExo.", "Dr. Keith Kwong, Chief Scientist\nDavid Shim, VP R&D"],
    [fa.FaUserMd, "Physicians", "Clinical judgement and evidence from physician shareholders.", "K-Doctor network"],
    [fa.FaRocket, "Entrepreneurs", "Built a trading business into an R&D-led biotech group.", "Theresa Jang, CEO"],
    [fa.FaBriefcase, "Corporate executives", "Technology, finance and brand leadership for global markets.", "Dr. Sidney Tam, CTO\nSylvia Wong, CMO"],
    [fa.FaIndustry, "Engineering experts", "Production and development, from formula to tested product.", "Kwongjae Park, CEO, WellBester (GMP and QC)"],
  ];
  const lw = (CW - 4 * 0.25) / 5;
  for (let i = 0; i < 5; i++) {
    const x = M + i * (lw + 0.25);
    card(s, x, 1.65, lw, 3.75, "Leader card " + (i + 1));
    await badge(s, lead[i][0], x + 0.25, 1.85, 0.65, lead[i][1]);
    txt(s, lead[i][1], x + 0.25, 2.65, lw - 0.5, 0.6, { fontSize: 15, bold: true });
    txt(s, lead[i][2], x + 0.25, 3.3, lw - 0.5, 1.15, { fontSize: 12, color: C.text2 });
    txt(s, lead[i][3], x + 0.25, 4.5, lw - 0.5, 0.85, { fontSize: 12, bold: true });
  }
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.6, w: CW, h: 1.15, fill: { color: C.text1 }, line: { color: C.text1, width: 0 }, rectRadius: 0.08, objectName: "Leadership takeaway" });
  txt(s, "Why it matters", M + 0.4, 5.78, 2.6, 0.3, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 3 });
  txt(s, "One cross-border team (Seoul, Hong Kong, London) covers invention, safe delivery, scale-up and capital discipline, so no link in the chain depends on an outside party.", M + 0.4, 6.08, CW - 0.8, 0.6, { fontSize: 15, color: "FFFFFF" });
  notes(s, "Leadership disciplines are the owner's wording (key-elements archive, item 1). Named leaders and titles come from WBI_Investor_Deck_2026.pptx (team slide). Mapping each person to one of the five disciplines is an inference from title and must be confirmed; the K-Doctor network is described there as physician shareholders and partner clinics. Add one proof point per person before circulation.");

  // ===== 4 Innovation =====
  pres.addSection({ title: "Innovation" });
  s = light("IT-EXO and SynExo: our baseline for resilient, regenerative care", "Innovation");
  const plat = [
    ["01", "IT-EXO®", "Exosome research and formulation for professional aesthetic products, including licensed human-derived exosome technology for hair and skin.", "Baseline platform for resilience."],
    ["02", "SynExo", "Synthetic exosome with HLA-G immune shielding and EGF/bFGF cargo. Korean patent registered 2026; manuscript under peer review.", "Baseline platform for regenerative biotech."],
    ["03", "RetroEV ExoShot", "Needle-free device platform with compatible EXO DERMA and EXO HAIR formulations and care protocols.", "Makes the science a repeatable studio service."],
  ];
  const pw = (CW - 2 * 0.25) / 3;
  for (let i = 0; i < 3; i++) {
    const x = M + i * (pw + 0.25);
    card(s, x, 1.65, pw, 3.3, "Platform card " + (i + 1));
    txt(s, plat[i][0], x + 0.3, 1.85, 0.8, 0.3, { fontSize: 13, bold: true, color: C.accent1 });
    txt(s, plat[i][1], x + 0.3, 2.15, pw - 0.6, 0.45, { fontSize: 22, bold: true, fontFace: "Cambria" });
    txt(s, plat[i][2], x + 0.3, 2.7, i === 2 ? pw - 0.6 : pw - 0.6, 1.4, { fontSize: 13 });
    txt(s, plat[i][3], x + 0.3, 4.2, i === 2 ? pw - 1.9 : pw - 0.6, 0.6, { fontSize: 13, italic: true, color: C.text2 });
    if (i === 2) {
      s.addImage({ path: asset("exo-derma.png"), x: x + pw - 1.55, y: 3.85, w: 0.62, h: 0.93, objectName: "EXO DERMA vial", altText: "RetroEV EXO DERMA vial" });
      s.addImage({ path: asset("exo-hair.png"), x: x + pw - 0.9, y: 3.85, w: 0.62, h: 0.93, objectName: "EXO HAIR vial", altText: "RetroEV EXO HAIR vial" });
    }
  }
  const ev = [[">95%", "cell viability, 0 to 15 µg/mL"], ["24-36 h", "peak EGF/bFGF expression"], ["4 of 4", "pro-inflammatory cytokines lowered"], ["2.2-2.9×", "target-cell proliferation"]];
  const ew = (CW - 3 * 0.2) / 4;
  txt(s, "SynExo in-vitro results (submitted manuscript)", M, 5.12, 6, 0.28, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 2 });
  ev.forEach((e, i) => {
    const x = M + i * (ew + 0.2);
    txt(s, e[0], x, 5.42, ew, 0.5, { fontSize: 26, bold: true, fontFace: "Cambria" });
    txt(s, e[1], x, 5.95, ew, 0.3, { fontSize: 12, color: C.text2 });
  });
  txt(s, "Laboratory (in vitro) data only. Mechanisms and clinical outcomes need separate evidence; product documentation defines intended use.", M, 6.5, CW, 0.3, { fontSize: 12, color: C.text2 });
  notes(s, "IT-EXO and SynExo as baseline innovations for resilience and regenerative biotech is the owner's wording (item 4). SynExo details (HLA-G, EGF/bFGF cargo, Korean patent 2026, manuscript under review at Biomolecules MDPI) and the in-vitro figures come from WBI_Investor_Deck_2026.pptx slides 6 and 8. These are cell-based results from a submitted manuscript, not clinical results. The WBI deck cites the human-derived exosomes as licensed technology; confirm that IT-EXO is that platform. Exosome-based items in any Seoul clinic programme offered through the immersion are clinic protocols, not evidence; this slide's in-vitro caveat applies to them.", 3);

  // ===== 5 Unique design =====
  s = light("Why our design is different: 30+ years from supply chain to studio", "Innovation");
  const flow = ["Design", "Formulate", "Manufacture", "Train", "Serve"];
  const fw = (7.9 - 4 * 0.12) / 5;
  flow.forEach((f, i) => {
    const x = M + i * (fw + 0.12);
    s.addShape(pres.ShapeType.homePlate, { x, y: 1.7, w: fw + 0.1, h: 0.75, fill: { color: i === 4 ? C.accent1 : C.text1 }, line: { color: C.background1, width: 0 }, objectName: "Flow step " + f });
    txt(s, f, x + 0.12, 1.7, fw - 0.2, 0.75, { fontSize: 12, bold: true, color: "FFFFFF", valign: "middle", align: "center" });
  });
  const dz = [
    [fa.FaHistory, "30+ years of product design", "Decades of product design experience through Korean supply chains means formats, packaging and ranges are engineered with manufacturing in mind."],
    [fa.FaCubes, "Designed as a system", "Formulations, device and care protocol are developed together, so a studio service is a repeatable method, not a loose set of products."],
    [fa.FaIndustry, "Own GMP/ISO manufacturing", "In-house production and QC labs (WellBester) with batch release and stability testing. 53 registrations across 20 export markets."],
  ];
  for (let i = 0; i < 3; i++) {
    const y = 2.75 + i * 1.35;
    await badge(s, dz[i][0], M, y + 0.1, 0.6, dz[i][1]);
    txt(s, dz[i][1], M + 0.85, y, 7.0, 0.35, { fontSize: 17, bold: true });
    txt(s, dz[i][2], M + 0.85, y + 0.4, 7.0, 0.85, { fontSize: 14, color: C.text2 });
  }
  card(s, 8.95, 1.7, W - M - 8.95, 4.95, "Product shelf");
  const imgs = [["remirae-cleanser.png", 0.95, 1.7], ["remirae-cream.png", 0.95, 1.45], ["exo-derma.png", 0.95, 1.4], ["exo-hair.png", 0.95, 1.4]];
  const px = [9.2, 10.55, 9.2, 10.55], py = [1.95, 1.95, 4.15, 4.15];
  imgs.forEach((im, i) => s.addImage({ path: asset(im[0]), x: px[i] + 0.1, y: py[i], w: 0.95 * 1.2, h: 1.9, sizing: { type: "contain", w: 1.14, h: 1.9 }, objectName: "Product " + im[0], altText: im[0].replace(".png", "") }));
  txt(s, "re'mirae  ·  MORIMANA  ·  RetroEV", 9.2, 6.2, 3.3, 0.3, { fontSize: 12, color: C.text2, align: "center" });
  notes(s, "30+ years of product design through Korean supply chains is the owner's wording (item 5). Product forms come from the supply price table in the v1 notes. Owner to confirm which entities and factories the 30 years refer to. GMP/ISO production, QC labs and the 53 registrations in 20 markets come from WBI_Investor_Deck_2026.pptx (slides 4 and 15); certificates and capacity should sit in the data room.", 6);

  // ===== 5b Technology whitespace =====
  s = light("Against named exosome players, SynExo owns the whitespace", "Innovation");
  const ch = (t) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color: HEX.ink }, fontSize: 13, valign: "middle" } });
  const cc = (t, b, hi) => ({ text: t, options: { fontSize: 13, bold: !!b, color: HEX.ink, valign: "middle", fill: { color: hi ? "EADFC9" : (b ? HEX.cream : HEX.white) } } });
  s.addTable([
    [ch("Player"), ch("Approach"), ch("Constraint"), ch("Positioning")],
    [cc("ExoCoBio", 1), cc("Human-derived (ASC exosomes); category leader"), cc("Donor-dependent batches; no engineered immune tolerance"), cc("Premium clinic channel, about 2× WBI supply price")],
    [cc("Prostemics", 1), cc("Human-derived; clinic-channel pioneer"), cc("Same biology constraints; no owned consumer channel"), cc("Clinic and derma channel, about 2× price tier")],
    [cc("BioFD&C, GFC", 1), cc("Plant-derived exosomes"), cc("Lower target-cell delivery than regeneration-grade claims"), cc("Functional-cosmetic pricing, mass retail")],
    [cc("WBI SynExo", 1, 1), cc("Synthetic, designed; patented HLA-G immune tolerance", 0, 1), cc("In cell tests, efficacy similar to human-derived (in vitro)", 0, 1), cc("Mid price, plus own GMP plant and owned studio channel", 0, 1)],
  ], { x: M, y: 1.65, w: CW, colW: [1.9, 3.5, 3.5, 3.23], rowH: [0.5, 0.8, 0.8, 0.8, 0.9], border: { type: "solid", color: HEX.mist, pt: 0.75 }, objectName: "Exosome competitor table" });
  txt(s, "No marketed competitor we have found combines engineered immune tolerance, synthetic batch consistency, an owned plant and an owned studio channel. Korean aesthetic-exosome market: ₩35bn (2024), ₩55bn (2025), ₩75bn (2026E).", M, 5.8, CW, 0.7, { fontSize: 13, bold: true });
  txt(s, "Competitor positioning: public price lists and disclosures 2025-26, as compiled by WBI. Market size: Grand View Research, KoBIA. A head start, not an absence of rivals.", M, 6.6, CW, 0.3, { fontSize: 11, color: C.text2 });
  notes(s, "Source: WBI_Investor_Deck_2026.pptx slide 7 (named competitors, price tiers, market size) and slide 16 (moat). The 'about 2×' price comparison and the 'no competitor combines' statement are WBI management claims; verify against current public price lists before circulation. Cell-test equivalence is in vitro only.");

  // ===== 6 Ecosystem =====
  pres.addSection({ title: "Ecosystem" });
  s = light("One managed client journey, not a one-off treatment", "Ecosystem");
  s.addImage({ data: await crop("care.jpg", 3.7, 5.05, "center"), x: M, y: 1.65, w: 3.7, h: 5.05, objectName: "Care photo", altText: "Head spa care in a MM Studio" });
  const steps = [
    [fa.FaCamera, "1  Imaging assessment", "AI-assisted scans record skin and scalp condition."],
    [fa.FaComments, "2  Personalised consultation", "A care plan built around the individual's needs and goals."],
    [fa.FaSpa, "3  Professional care", "Korean head spa, needle-free care and facials."],
    [fa.FaSyncAlt, "4  Follow-up and homecare", "Compare follow-up images; membership and homecare."],
  ];
  const sx = M + 3.95, sw = (CW - 3.95 - 0.25) / 2;
  for (let i = 0; i < 4; i++) {
    const x = sx + (i % 2) * (sw + 0.25), y = 1.65 + Math.floor(i / 2) * 1.75;
    card(s, x, y, sw, 1.55, "Step card " + (i + 1));
    await badge(s, steps[i][0], x + 0.25, y + 0.25, 0.6, "Step " + (i + 1));
    txt(s, steps[i][1], x + 1.05, y + 0.15, sw - 1.25, 0.55, { fontSize: 14, bold: true });
    txt(s, steps[i][2], x + 1.05, y + 0.75, sw - 1.25, 0.8, { fontSize: 12, color: C.text2 });
  }
  s.addShape(pres.ShapeType.roundRect, { x: sx, y: 5.2, w: CW - 3.95, h: 1.5, fill: { color: C.text1 }, line: { color: C.text1, width: 0 }, rectRadius: 0.08, objectName: "Ecosystem takeaway" });
  txt(s, "What makes the ecosystem unique", sx + 0.35, 5.38, 6, 0.3, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 3 });
  txt(s, "The loop closes: each follow-up scan tests the plan, refines the next visit and informs product development in Korea. Studios, the K-Doctor physician network, partners and R&D share one consented client record.", sx + 0.35, 5.7, CW - 3.95 - 0.7, 0.95, { fontSize: 13, color: "FFFFFF" });
  notes(s, "The Mirae Method steps summarise the brand materials. AI analysis is not a medical diagnosis; medical diagnosis, prescriptions and procedures remain with qualified medical professionals. Ecosystem framing (closed loop across studios, clinics, partners and R&D) is the owner's request to articulate why the client-management ecosystem is unique.", 4);

  // ===== 7 Competitive advantage =====
  s = light("Where MM Studio is different from the alternatives", "Ecosystem");
  const hdr = (t, first) => ({ text: t, options: { bold: true, color: first ? HEX.white : HEX.white, fill: { color: first ? HEX.gold : HEX.ink }, fontSize: 13, align: first ? "left" : "center", valign: "middle" } });
  const lv = (t) => ({ text: t, options: { align: "center", valign: "middle", fontSize: 13, bold: t === "Core", color: t === "Core" ? HEX.ink : HEX.grey, fill: { color: t === "Core" ? "EADFC9" : HEX.white } } });
  const lab = (t) => ({ text: t, options: { bold: true, fontSize: 13, color: HEX.ink, valign: "middle", fill: { color: HEX.cream } } });
  const rows = [
    ["Personalised plan from an individual scan", "Core", "Partial", "Rarely", "Partial"],
    ["Own formulation and manufacturing chain", "Core", "Rarely", "Partial", "Rarely"],
    ["Professional training and shared standards", "Core", "Partial", "Rarely", "Partial"],
    ["Follow-up comparison and data continuity", "Core", "Rarely", "Rarely", "Partial"],
    ["Homecare linked to the care plan", "Core", "Partial", "Core", "Rarely"],
    ["Medical oversight where needed", "Via clinic format", "Rarely", "Rarely", "Core"],
    ["Global distribution and partner network", "Core", "Rarely", "Partial", "Rarely"],
  ];
  const tbl = [[hdr("Capability", true), hdr("MM Studio"), hdr("Typical salon or spa"), hdr("Product-only brand"), hdr("Clinic-only")]];
  rows.forEach((r) => tbl.push([lab(r[0]), ...r.slice(1).map(lv)]));
  s.addTable(tbl, { x: M, y: 1.65, w: CW, colW: [4.4, 2.0, 1.9, 1.9, 1.93], rowH: [0.62, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], border: { type: "solid", color: HEX.mist, pt: 0.75 }, fontFace: "Calibri", objectName: "Competitive comparison" });
  txt(s, "No single competitor type combines all seven. MM Studio's advantage is the combination, held together by one trained method and one client record.", M, 6.0, CW, 0.55, { fontSize: 14, bold: true });
  txt(s, "Illustrative management view of typical market formats, not a market study. Named competitors and evidence to be added.", M, 6.6, CW, 0.3, { fontSize: 12, color: C.text2 });
  notes(s, "Qualitative positioning table prepared to meet the 'no competitive advantages' feedback. It generalises about formats and should be validated with named competitor examples and customer evidence before circulation.");

  // ===== 8 UK hub =====
  pres.addSection({ title: "UK and reach" });
  s = light("The UK: global centre of hair care and our training hub", "UK and reach");
  s.addImage({ data: await crop("team.jpg", 4.6, 3.3, "center"), x: W - M - 4.6, y: 1.65, w: 4.6, h: 3.3, objectName: "Team photo", altText: "MM Studio London team" });
  const big = [["Global centre of hair care", "The UK sets the standard that the world's hair and scalp professionals look to."], ["World leader as coach and trainer", "UK educators train professionals globally, which is the skill our partner model needs."]];
  for (let i = 0; i < 2; i++) {
    const y = 1.65 + i * 1.75;
    card(s, M, y, 7.0, 1.55, "UK strength " + (i + 1));
    txt(s, big[i][0], M + 0.35, y + 0.22, 6.3, 0.5, { fontSize: 22, bold: true, fontFace: "Cambria" });
    txt(s, big[i][1], M + 0.35, y + 0.8, 6.3, 0.65, { fontSize: 14, color: C.text2 });
  }
  const chain = [["Seoul", "R&D, GMP/ISO manufacturing, Seongsu studio"], ["London", "Knightsbridge flagship, academy-trained therapists"], ["Global network", "OEM/ODM contracts in 20 countries; HK Central and LA mapped next"]];
  const cw3 = (CW - 2 * 0.5) / 3;
  chain.forEach((c, i) => {
    const x = M + i * (cw3 + 0.5);
    s.addShape(pres.ShapeType.roundRect, { x, y: 5.05, w: cw3, h: 1.2, fill: { color: i === 1 ? C.accent1 : C.text1 }, line: { color: C.background1, width: 0 }, rectRadius: 0.08, objectName: "Chain " + c[0] });
    txt(s, c[0], x + 0.25, 5.15, cw3 - 0.5, 0.4, { fontSize: 18, bold: true, color: i === 1 ? C.text1 : "FFFFFF", fontFace: "Cambria" });
    txt(s, c[1], x + 0.25, 5.6, cw3 - 0.5, 0.6, { fontSize: 12, color: i === 1 ? C.text1 : C.background2 });
  });
  txt(s, "Our global sales network carries the method outward: London trains, Seoul supplies, partners sell and serve. UK sales use the cosmetic route already secured (16 SCPN registrations).", M, 6.4, CW, 0.5, { fontSize: 13, bold: true });
  notes(s, "UK as global hair-care centre and world leader as coach and trainer, and the global sales network, are the owner's wording (items 6 and 7). Network facts (20 export countries, 53 registrations, SCPN 16, London Knightsbridge and Seoul Seongsu studios, HK Central and LA Century City mapped) come from WBI_Investor_Deck_2026.pptx slides 3, 4, 6, 10 and 15. Still needed: UK industry evidence for the trainer claim. The proposed UK certificate course is not confirmed: certification body, accreditation, internship roles and terms remain open.", 2);

  // ===== 9 AI & data =====
  pres.addSection({ title: "Future" });
  s = light("Next: AI and data that make care measurably personal", "Future");
  const streams = [
    [fa.FaCamera, "Scanner data", "Standardised skin and scalp images at every visit."],
    [fa.FaClipboardList, "Service data", "Which protocol, products and frequency were used."],
    [fa.FaHeart, "Client experience", "Goals, feedback, comfort and homecare habits."],
  ];
  const sw3 = (CW - 2 * 0.25) / 3;
  for (let i = 0; i < 3; i++) {
    const x = M + i * (sw3 + 0.25);
    card(s, x, 1.65, sw3, 1.35, "Data stream " + (i + 1));
    await badge(s, streams[i][0], x + 0.25, 1.95, 0.6, streams[i][1]);
    txt(s, streams[i][1], x + 1.05, 1.85, sw3 - 1.25, 0.35, { fontSize: 16, bold: true });
    txt(s, streams[i][2], x + 1.05, 2.25, sw3 - 1.25, 0.7, { fontSize: 13, color: C.text2 });
  }
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 3.15, w: CW, h: 0.5, fill: { color: C.text1 }, line: { color: C.text1, width: 0 }, rectRadius: 0.08, objectName: "Data platform bar" });
  txt(s, "One consented client record, shared across studios, clinics and R&D (proposed data platform)", M, 3.15, CW, 0.5, { fontSize: 14, bold: true, color: "FFFFFF", align: "center", valign: "middle" });
  const hz = [
    ["TODAY", "In place", ["AI-assisted imaging at assessment", "Follow-up image comparison", "Membership and homecare reorders"]],
    ["NEXT", "Proposed", ["Client AI app: scan, protocol, homecare, rebooking", "Common data model across studios", "Anonymised protocol benchmarking"]],
    ["LATER", "Proposed", ["Recommendations matching protocol and formula to profile", "AI-designed peptides in the formulation pipeline", "Made-to-measure digital cosmetic products"]],
  ];
  for (let i = 0; i < 3; i++) {
    const x = M + i * (sw3 + 0.25);
    card(s, x, 3.85, sw3, 2.45, "Horizon " + hz[i][0]);
    txt(s, hz[i][0], x + 0.3, 4.0, 1.4, 0.3, { fontSize: 13, bold: true, color: C.accent1, charSpacing: 3 });
    txt(s, hz[i][1], x + sw3 - 1.6, 4.0, 1.3, 0.3, { fontSize: 12, italic: true, color: C.text2, align: "right" });
    txt(s, hz[i][2].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 2, paraSpaceAfter: 4 } })), x + 0.3, 4.35, sw3 - 0.6, 1.9, { fontSize: 13 });
  }
  txt(s, "WBI plan: 25,000 engaged, consented users across the studio network within two years. Built on explicit consent and UK GDPR; AI supports professionals and does not diagnose.", M, 6.42, CW, 0.5, { fontSize: 12, bold: true });
  notes(s, "Addresses the missing future-development gap: AI and data from the scanner, services and client experience. 'Today' reflects AI-assisted scanning and follow-up comparison described in the brand materials; 'Next' and 'Later' are proposed development, not shipped features. The client AI app (scan, protocol, homecare compliance, rebooking), the Engage-Capture-Learn-Compound loop, AI peptide design and the 25,000-user target are from WBI_Investor_Deck_2026.pptx slides 6 and 11; the app is described there as funded by WBI's own round, so confirm its timing for MM Studio UK. Skin and scalp images are personal data (possibly special-category); a consent, retention and DPIA plan is needed. Owner to confirm the current scanner hardware and what data it stores. If the Seoul immersion involves participants' health information, consultation records or images, that is special-category data under UK GDPR (explicit consent, a privacy notice naming the controllers, minimisation, retention limits, a DPIA); transfers to Korea rely on the UK's 2022 adequacy regulations for the Republic of Korea.");

  // ===== 10 Business models =====
  pres.addSection({ title: "Commercial" });
  s = light("Three operating formats share one brand and product standard", "Commercial");
  const bh = (t) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color: HEX.ink }, fontSize: 14, valign: "middle" } });
  const bc = (t, b) => ({ text: t, options: { fontSize: 14, bold: !!b, color: HEX.ink, valign: "middle", fill: { color: b ? HEX.cream : HEX.white } } });
  s.addTable([
    [bh("Format"), bh("Operating model"), bh("Revenue sources")],
    [bc("Flagship Studio", 1), bc("Demonstration studios in Seoul and London"), bc("Care services, memberships and product sales")],
    [bc("Studio in a Clinic", 1), bc("Agreed responsibilities with doctors and healthcare providers"), bc("Care packages and product sales")],
    [bc("Partner Studio / Distribution", 1), bc("Training, brand standards and product supply support"), bc("Startup packages and reorders, plus agreed service fees")],
  ], { x: M, y: 1.65, w: CW, colW: [3.3, 4.7, 4.13], rowH: 0.85, border: { type: "solid", color: HEX.mist, pt: 0.75 }, objectName: "Business model table" });
  const rec = [[fa.FaRedo, "Recurring by design", "Ongoing care, membership and homecare support repeat business."], [fa.FaGraduationCap, "Training builds loyalty", "Partners complete training, follow shared standards and reorder as needed."], [fa.FaCoins, "US$3,800 a year", "Estimated annual spend per engaged client."]];
  for (let i = 0; i < 3; i++) {
    const x = M + i * (sw3 + 0.25);
    card(s, x, 5.25, sw3, 1.5, "Model benefit " + (i + 1));
    await badge(s, rec[i][0], x + 0.25, 5.5, 0.55, rec[i][1]);
    txt(s, rec[i][1], x + 1.0, 5.4, sw3 - 1.2, 0.35, { fontSize: 14, bold: true });
    txt(s, rec[i][2], x + 1.0, 5.78, sw3 - 1.2, 0.95, { fontSize: 12, color: C.text2 });
  }
  notes(s, "Per-client spend (about US$3,800: skin programme $1,800, hair/scalp programme $1,200, homecare $800) is a management estimate from WBI_Investor_Deck_2026.pptx slide 9. WBI's 15% supplier capture is WBI revenue, not a return to MM Studio UK unit holders. The Seoul immersion memo asks WBI for 'diverse and flexible routes' into the ecosystem and a 'lightest and fastest' entry option; the three formats here and the UK unit are the documented routes, and none is ranked by speed or ease.", 5);

  // ===== 11 Who does what =====
  s = light("Who does what: Korean R&D, UK operations and investors", "Commercial");
  const who = [
    [fa.FaFlask, "WBI Korea technical team", ["CEO Theresa Jang", "Product development, manufacturing and supply", "Seoul immersion: hosting and content (to be confirmed)"]],
    [fa.FaUniversity, "NeuNova UK team", ["London operations and course planning", "Support for studio partners", "Seoul immersion: programme planning (proposed)"]],
    [fa.FaSpa, "MM Studio service team", ["Client consultation and professional care", "Ongoing service management", "Seongsu studio walk-through (to be confirmed)"]],
    [fa.FaHandHoldingUsd, "Private investors", ["Programme funding through units", "Agreed MM Studio equity allocation", "Study visit: Seoul immersion (proposed)"]],
  ];
  const ww = (CW - 3 * 0.25) / 4;
  for (let i = 0; i < 4; i++) {
    const x = M + i * (ww + 0.25);
    card(s, x, 1.65, ww, 4.2, "Role card " + (i + 1));
    await badge(s, who[i][0], x + 0.3, 1.95, 0.7, who[i][1]);
    txt(s, who[i][1], x + 0.3, 2.9, ww - 0.6, 0.8, { fontSize: 18, bold: true });
    txt(s, who[i][2].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < who[i][2].length - 1, paraSpaceAfter: 6 } })), x + 0.3, 3.7, ww - 0.6, 2.1, { fontSize: 12.5, color: C.text2 });
  }
  txt(s, "Clear responsibilities let each partner do what it does best, while the client sees one MM Studio.", M, 6.1, CW, 0.5, { fontSize: 15, bold: true });
  notes(s, "Seoul immersion roles follow the planning memo received 5 Oct 2026 (author Rocky Chi, addressed to Theresa Jang and Sidney Tam). The memo asks WBI to confirm academy speakers, R&D and manufacturing access, the treatment programme and route options, and asks for a Seongsu walk-through; those bullets are labelled 'to be confirmed'. The memo does not state which entity runs or sells the programme; the planning role sits on the NeuNova card as 'proposed' because NeuNova already carries course planning and the memo's costing sheet names NeuNova as a party. Owner to confirm: who runs and sells the immersion, who contracts with the investor for each unit component, and who attends the trip. Commercial arrangements between the parties are not deck content.", 2);

  // ===== 12 Financials =====
  pres.addSection({ title: "Financials" });
  s = light("Illustrative London studio model: EBITDA positive from Year 2", "Financials");
  const yrs = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"];
  s.addChart(pres.charts.BAR, [
    { name: "Revenue (GBP)", labels: yrs, values: [148104, 188496, 228888, 269280, 282744] },
    { name: "EBITDA (GBP)", labels: yrs, values: [-13743, 20342, 52987, 85632, 94593] },
  ], { x: M, y: 1.6, w: 8.1, h: 4.35, barDir: "col", barGrouping: "clustered", chartColors: [HEX.ink, HEX.gold], showTitle: true, title: "London pilot: revenue and EBITDA (GBP)", titleFontSize: 14, titleColor: HEX.ink, titleFontFace: "+mn-lt",
    showValue: true, dataLabelFormatCode: "#,##0", dataLabelFontSize: 10, dataLabelColor: HEX.ink, dataLabelFontFace: "+mn-lt", dataLabelPosition: "outEnd",
    catAxisLabelColor: HEX.grey, catAxisLabelFontSize: 12, catAxisLabelFontFace: "+mn-lt", valAxisLabelColor: HEX.grey, valAxisLabelFontSize: 11, valAxisLabelFontFace: "+mn-lt", valAxisLabelFormatCode: "#,##0",
    valGridLine: { color: "E4E6EC", size: 0.75 }, catGridLine: { style: "none" }, showLegend: true, legendPos: "b", legendFontSize: 12, legendColor: HEX.grey, legendFontFace: "+mn-lt", objectName: "Revenue and EBITDA chart" });
  const kp = [["£50,000", "Initial London investment"], ["£46,000", "First-year sales revenue"], ["₩16.4bn", "WBI group FY2025 revenue, about US$11.7M"]];
  kp.forEach((k, i) => {
    const y = 1.65 + i * 1.25;
    card(s, M + 8.4, y, CW - 8.4, 1.1, "KPI " + (i + 1));
    txt(s, k[0], M + 8.65, y + 0.1, CW - 8.9, 0.55, { fontSize: 28, bold: true, fontFace: "Cambria" });
    txt(s, k[1], M + 8.65, y + 0.68, CW - 8.9, 0.4, { fontSize: 12, color: C.text2 });
  });
  txt(s, "Management data, unaudited. London first-year period and profitability to be confirmed. Single-studio illustration; excludes UK head-office costs and the proposed internship budget. Capacity needs review: 56 monthly visits projected against capacity for 44 treatments.", M + 8.4, 5.5, CW - 8.4, 1.2, { fontSize: 11, color: C.text2 });
  txt(s, "EBITDA = earnings before interest, tax, depreciation and amortisation. Sales alone do not establish an investment return; full P&L and cash balances are pending.", M, 6.15, 8.1, 0.6, { fontSize: 12, color: C.text2 });
  notes(s, "WBI group FY2025 combined revenue of ₩16.4bn (about US$11.7M) is from WBI_Investor_Deck_2026.pptx slide 13 (management data, with net income ₩291M, 5.1% margin). It describes the supplier group, not MM Studio UK. WBI's separate US$2.0M-for-10% round and its franchise forecasts are deliberately not part of this UK programme.", 7);

  // ===== 13 Funding =====
  s = light("Funding programme: each unit combines training and MM Studio equity", "Financials");
  const fh = (t, al) => ({ text: t, options: { bold: true, color: HEX.white, fill: { color: HEX.ink }, fontSize: 14, valign: "middle", align: al || "left" } });
  const fc = (t, al, b) => ({ text: t, options: { fontSize: 14, color: HEX.ink, bold: !!b, valign: "middle", align: al || "left", fill: { color: b ? HEX.cream : HEX.white } } });
  s.addTable([
    [fh("Use of funds per unit"), fh("Amount (GBP)", "right")],
    [fc("Study visits, training and practical sessions (proposed: the four-day Seoul immersion)"), fc("£15,000", "right")],
    [fc("12-month professional certificate course"), fc("From £25,000", "right")],
    [fc("12-month internship and work programme"), fc("£XXXX", "right")],
    [fc("MM Studio equity allocation", "left", 1), fc("£50,000", "right", 1)],
  ], { x: M, y: 1.65, w: 7.4, colW: [5.2, 2.2], rowH: [0.62, 0.8, 0.62, 0.62, 0.62], border: { type: "solid", color: HEX.mist, pt: 0.75 }, objectName: "Use of funds table" });
  const fk = [["£XXX", "Per funding unit"], ["N units × £XXX", "Total funding target; unit count to be confirmed"], ["£90,000+", "Indicative minimum, plus internship and work budget"]];
  fk.forEach((k, i) => {
    const y = 1.65 + i * 1.28;
    card(s, M + 7.7, y, CW - 7.7, 1.12, "Funding KPI " + (i + 1));
    txt(s, k[0], M + 7.95, y + 0.12, CW - 8.2, 0.5, { fontSize: 24, bold: true, fontFace: "Cambria" });
    txt(s, k[1], M + 7.95, y + 0.65, CW - 8.2, 0.4, { fontSize: 12, color: C.text2 });
  });
  txt(s, "£15,000 excludes travel, hotel and transport; the Seoul immersion's price and inclusions are being confirmed with WBI. MM Studio's 2026 baseline value: £XXXX. Final ownership percentage to be confirmed. The equity budget provisionally assumes an equal cash subscription.", M, 5.2, 7.4, 0.9, { fontSize: 12, color: C.text2 });
  txt(s, "Certification, internship and work terms, timing, share issuer and shareholder rights require confirmation. No recognised qualification, job, visa, immigration outcome or investment return is guaranteed.", M, 6.1, CW, 0.7, { fontSize: 12, color: C.text2 });
  notes(s, "Seoul immersion. The planning memo received 5 Oct 2026 (author Rocky Chi, addressed to Theresa Jang and Sidney Tam; internal source file sources/seoul-immersion-memo.md, not for circulation) describes a four-day Seoul programme. This deck proposes it as the study-visit component of each unit; the memo itself does not mention the UK unit programme, so the link is an owner decision and is labelled 'proposed'. The memo's working price is in USD, on the earlier three-day basis, covers treatments, academy sessions and meals, and asks WBI for a four-day total including hotel nights; the deck's £15,000 is in GBP and excludes travel, hotel and transport. These are different numbers with different inclusions, so no memo figure is shown or converted here. Owner decisions: (1) whether the £15,000 component is the Seoul immersion alone or the immersion plus UK practical sessions; (2) the GBP price and inclusions of the four-day version; (3) who attends (the investor, a nominated trainee, or both) and whether the trip precedes or follows the unit subscription; (4) whether a stand-alone trip fee is credited against a later unit. Day 4 involves business and investment conversations with prospective participants: take advice on UK financial-promotion rules before those sessions. Internal costing detail from the memo is not deck content.", 8);


  // ===== 13b Seoul immersion =====
  pres.addSection({ title: "Programme" });
  s = light("Four days in Seoul: from the treatment room to the boardroom", "Programme");
  txt(s, "Proposed as the study-visit component of each funding unit: experience, science, business, opportunity.", M, 1.5, CW, 0.3, { fontSize: 13, color: C.text2 });
  s.addImage({ data: await crop("seongsu-consultation.jpg", 2.3, 4.13, "north"), x: M, y: 1.95, w: 2.3, h: 4.13, objectName: "Seongsu consultation photo", altText: "Consultation at MM Studio Seongsu, Seoul" });
  const days = [
    ["DAYS 1-2", "Experience the treatments", "A personalised treatment programme in Seoul, subject to clinical suitability. Treatments may be substituted within a fixed programme fee (policy proposed)."],
    ["DAY 3", "Discover the science, understand the business", "Presentations and site visits: the science and products behind the treatments; regenerative aesthetics and biotech; exosomes, peptides and protocols; product development; treatment and homecare economics; consumer insights; scaling a consumer business."],
    ["DAY 4", "Explore the opportunity", "Presentations, one-to-one conversations and Q&A on routes into the ecosystem: the operating formats and the UK unit programme (options to be confirmed)."],
  ];
  const dx = M + 2.5, dwid = 6.2, dh = [1.24, 1.5, 1.24];
  let dy = 1.95;
  days.forEach((d, i) => {
    const y = dy;
    card(s, dx, y, dwid, dh[i], "Day card " + (i + 1));
    txt(s, d[0], dx + 0.25, y + 0.12, 2, 0.22, { fontSize: 10.5, bold: true, color: C.accent1, charSpacing: 2 });
    txt(s, d[1], dx + 0.25, y + 0.34, dwid - 0.5, 0.3, { fontSize: 13.5, bold: true });
    txt(s, d[2], dx + 0.25, y + 0.68, dwid - 0.5, dh[i] - 0.72, { fontSize: 11, color: C.text2 });
    dy += dh[i] + 0.075;
  });
  const pxx = dx + dwid + 0.25, pw2 = W - M - pxx;
  s.addShape(pres.ShapeType.roundRect, { x: pxx, y: 1.95, w: pw2, h: 4.13, fill: { color: C.background1 }, line: { color: HEX.mist, width: 1, dashType: "dash" }, rectRadius: 0.08, objectName: "Access panel" });
  txt(s, "Access being arranged (to be confirmed)", pxx + 0.25, 2.15, pw2 - 0.5, 0.5, { fontSize: 12, bold: true });
  txt(s, ["R&D and manufacturing facility visit", "Meet the scientists and product team", "Formulation-to-protocol demonstration", "MM Studio Seongsu walk-through", "Academy speakers and their bios"].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 4, paraSpaceAfter: 5 } })), pxx + 0.25, 2.7, pw2 - 0.5, 3.1, { fontSize: 11.5, color: C.text2 });
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 6.16, w: CW, h: 0.42, fill: { color: C.text1 }, line: { color: C.text1, width: 0 }, rectRadius: 0.08, objectName: "Seoul takeaway" });
  txt(s, "Why it matters: participants see for themselves what this brief describes: the treatments, the science behind them and how a studio operates.", M + 0.35, 6.16, CW - 0.7, 0.42, { fontSize: 11.5, bold: true, color: "FFFFFF", valign: "middle" });
  txt(s, "Programme in planning: content, site access, price and inclusions to be confirmed with WBI. Proposed as the study-visit component of each unit, not the certificate course; no qualification conferred. Treatments are given in Korea, subject to clinical suitability; no outcome is claimed; exosome evidence is in vitro only.", M, 6.62, CW, 0.36, { fontSize: 9.5, color: C.text2 });
  notes(s, "Source: planning memo 'Seoul K-Beauty Ecosystem Immersion: From the Treatment Room to the Boardroom', author Rocky Chi, addressed to Theresa Jang and Sidney Tam, received 5 Oct 2026 (internal file sources/seoul-immersion-memo.md, not for circulation). Set out in the memo and shown as such: the programme name and tagline; the four-step narrative (experience the treatments, discover the science, understand the business, explore the opportunity); the four-day structure, extended from three days to weight Days 3 and 4 towards academy and business content; the Day 3 topic list, delivered by presentation and site visits; Day 4 as presentations and one-to-one conversations with business and investment Q&A. The memo's own framing: it is not primarily selling a beauty holiday, a two-day academy, a corporate investment seminar or a package of individual medical treatments, but access to the full journey behind Korean beauty, from personal experience and clinical innovation to business creation and international growth. Requested from WBI on 5 Oct 2026 and not yet answered: everything in the dashed panel, confirmation of the treatment programme and its supporting price list, the substitution policy and matrix, the four-day price and inclusions (hotel nights, meals, transport, dinners), pre- and post-trip extensions, the routes WBI will present on Day 4, WBI highlights, Seoul photography and a CEO welcome note for the brochure. Replace the dashed panel with confirmed wording, or remove it, before external circulation; name speakers and print dates only once confirmed; use 'exclusive' only if WBI confirms the access is not offered to other groups. Presenter guidance: do not name any treatment, product or medicine and do not use outcome words; the clinic sets the programme at consultation, and UK-originated material must not promote prescription-only medicines. Substitution wording proposed in the memo for the booking pack: 'The programme fee remains fixed. Individual treatments may be substituted based on personal preference and clinical suitability, subject to the available treatment programme.' The memo's costing sheet is on a seven-participant, three-day basis and predates the four-day extension; its figures and internal arrangements are not deck content. Photo: MM Studio Seongsu consultation, from WBI's investor deck. The link between the immersion and the £15,000 study-visit component is this deck's proposal, not a statement in the memo; see the Funding programme notes for the owner decisions.");

  // ===== 14 Closing =====
  pres.addSection({ title: "Closing" });
  s = pres.addSlide({ masterName: "DARK", sectionTitle: "Closing" });
  txt(s, "Why invest, and what happens next", M, 0.6, CW, 0.9, { fontSize: 36, bold: true, color: "FFFFFF", fontFace: "Cambria" });
  const why = [[fa.FaUsers, "A team no rival has", "Named scientists, physicians, entrepreneurs, executives and engineers."], [fa.FaDna, "Defensible innovation", "IT-EXO and a patented SynExo, backed by 30+ years of Korean product design and GMP/ISO manufacturing."], [fa.FaProjectDiagram, "A client ecosystem", "One method and one client record from scan to homecare."], [fa.FaGlobe, "Reach from the UK", "A global training hub and sales network."]];
  const dw = (CW - 3 * 0.25) / 4;
  for (let i = 0; i < 4; i++) {
    const x = M + i * (dw + 0.25);
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.8, w: dw, h: 2.85, fill: { color: C.accent6 }, line: { color: C.accent6, width: 0 }, rectRadius: 0.08, objectName: "Why card " + (i + 1) });
    await badge(s, why[i][0], x + 0.3, 2.05, 0.65, why[i][1], C.accent1, HEX.ink);
    txt(s, why[i][1], x + 0.3, 2.85, dw - 0.6, 0.6, { fontSize: 15, bold: true, color: "FFFFFF" });
    txt(s, why[i][2], x + 0.3, 3.5, dw - 0.6, 1.0, { fontSize: 12, color: C.accent2 });
  }
  txt(s, "NEXT STEPS", M, 5.0, 4, 0.3, { fontSize: 12, bold: true, color: C.accent1, charSpacing: 4 });
  txt(s, [
    { text: "Confirm unit price, unit count and 2026 baseline value", options: { bullet: true, breakLine: true, paraSpaceAfter: 4 } },
    { text: "Share leadership profiles and AI and data governance plan", options: { bullet: true, breakLine: true, paraSpaceAfter: 4 } },
    { text: "Arrange visits to the London studio and, once the programme is confirmed, the four-day Seoul immersion", options: { bullet: true } },
  ], M, 5.4, CW, 1.3, { fontSize: 16, color: "FFFFFF" });
  txt(s, "MM Studio  ·  Discussion draft  ·  October 2026", M, 6.95, 8, 0.3, { fontSize: 11, color: C.accent2 });
  notes(s, "Closing summary of the four owner-supplied differentiators and the open items listed in the key-elements archive. Seoul immersion dates are not printed until WBI confirms the programme. Open asks to WBI from the planning memo of 5 Oct 2026, kept here so next steps and the memo stay aligned: WBI highlights for the cohort (cross-check against the sourced facts on the Leadership, Innovation, Design, whitespace and UK hub slides); Seoul photography assets and a CEO welcome note for the brochure; academy speakers and bios; R&D and manufacturing access; meeting the scientists and product team; a formulation-to-protocol demonstration; the Seongsu walk-through; confirmation and price list for the treatment programme; the substitution policy and matrix; the four-day price and inclusions; the policy on pre- and post-trip extensions; the route options for joining the ecosystem. The memo's guest-to-guest referral benefit is kept out of the deck pending advice on UK financial-promotion rules, because a referred guest may subscribe for a unit that includes equity. Keep 'golden opportunity', 'fast-growing' and 'franchisee' off slides.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
