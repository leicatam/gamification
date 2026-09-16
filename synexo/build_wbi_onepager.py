#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WBI 股东一页纸（简体中文·代号版）-> WBI_Shareholder_OnePager_CN.png + .pptx.

Code names only: P公司 = US SEC-filing platform; M公司 = Korean GMP manufacturer;
D公司 = listed-group licensee. Only WBI is named. Figures from the JV Financial
Plan (rev 29 Aug 2026), the platform's GLP-1 proforma, and user-supplied WBI
share data (US$89.75/share, 111,448 shares incl. 5% placement of 5,572).
"""
from PIL import Image, ImageDraw, ImageFont

DIR = "/home/user/gamification/synexo/"
FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"

# ---- WBI shareholder math (asserted) ----
SHARES = 111448; PLACEMENT = 5572; PX = 89.75
CAP = SHARES * PX                          # 10,002,458
assert abs(CAP - 10_002_458.0) < 1
assert round(SHARES * 0.05) == PLACEMENT
JV_LO, JV_HI = 15_000_000, 20_000_000      # WBI 作价区间 (JV plan)
PS_JV_LO, PS_JV_HI = JV_LO / SHARES, JV_HI / SHARES        # 134.6 / 179.4
POST_LO, POST_HI = 28_200_000, 36_300_000  # 上市后 WBI 股东价值情景 (工作底稿)
PS_IPO_LO, PS_IPO_HI = POST_LO / SHARES, POST_HI / SHARES  # 253 / 326

# ---- palette ----
NAVY = (27, 51, 85); ACCENT = (46, 134, 193); TEAL = (26, 161, 156)
GOLD = (224, 158, 43); GREY = (90, 90, 90); LIGHT = (236, 242, 247)
WHITE = (255, 255, 255); RED = (192, 57, 43); SKY = (207, 221, 234)
DARK2 = (36, 68, 110)

W, H = 1654, 2339                          # A4 portrait ~200dpi
img = Image.new("RGB", (W, H), WHITE)
dr = ImageDraw.Draw(img)

def F(sz, bold=False):
    # wqy-zenhei has a single weight; simulate bold sparingly via stroke
    return ImageFont.truetype(FONT, sz)

import re as _re

def _tokens(t):
    # keep ASCII runs (numbers, $, %, units) unbreakable; CJK chars break freely
    return _re.findall(r"[0-9A-Za-z$%.,–\-/+~]+ ?|.", t)

def text(x, y, t, sz, col=NAVY, bold=False, anchor="la", maxw=None):
    f = F(sz)
    if maxw:  # wrap at token boundaries
        lines, cur = [], ""
        for tok in _tokens(t):
            if dr.textlength(cur + tok, font=f) > maxw and cur:
                lines.append(cur); cur = tok
            else:
                cur += tok
        lines.append(cur)
        for i, ln in enumerate(lines):
            dr.text((x, y + i * int(sz * 1.42)), ln, font=f, fill=col,
                    stroke_width=1 if bold else 0, stroke_fill=col, anchor=anchor)
        return y + len(lines) * int(sz * 1.42)
    dr.text((x, y), t, font=f, fill=col, stroke_width=1 if bold else 0,
            stroke_fill=col, anchor=anchor)
    return y + int(sz * 1.42)

def rrect(x0, y0, x1, y1, fill=None, outline=None, w=2, r=14):
    dr.rounded_rectangle([x0, y0, x1, y1], radius=r, fill=fill, outline=outline, width=w)

def chip(x0, y0, x1, y1, t, sz, fill, col=WHITE, sub=None, subsz=None, subcol=None):
    rrect(x0, y0, x1, y1, fill=fill)
    cx = (x0 + x1) // 2
    if sub:
        text(cx, (y0 + y1) // 2 - int(sz * 0.75), t, sz, col, bold=True, anchor="mm")
        text(cx, (y0 + y1) // 2 + int((subsz or 22) * 0.95), sub, subsz or 22,
             subcol or col, anchor="mm")
    else:
        text(cx, (y0 + y1) // 2, t, sz, col, bold=True, anchor="mm")

def arrow_r(x, y, ln=46, htw=16, col=ACCENT, w=7):
    dr.line([(x, y), (x + ln, y)], fill=col, width=w)
    dr.polygon([(x + ln, y - htw), (x + ln, y + htw), (x + ln + htw + 6, y)], fill=col)

def arrow_d(x, y, ln=36, htw=14, col=ACCENT, w=7):
    dr.line([(x, y), (x, y + ln)], fill=col, width=w)
    dr.polygon([(x - htw, y + ln), (x + htw, y + ln), (x, y + ln + htw + 4)], fill=col)

M = 62                                     # page margin

# ================= header =================
dr.rectangle([0, 0, W, 150], fill=NAVY)
dr.rectangle([M, 40, M + 14, 110], fill=ACCENT)
text(M + 36, 34, "WBI 股东简报 — 三方合并 · 美国上市计划", 46, WHITE, bold=True)
text(M + 38, 104, "仅供 WBI 股东参考 · 合作方以代号表示 · 非要约 · 数字为规划/说明口径 · 2026年9月", 24, SKY)
dr.rectangle([0, 150, W, 158], fill=ACCENT)

# ================= S1 交易结构 =================
y1 = 186
text(M, y1, "① 交易结构（两步走）", 34, NAVY, bold=True)
by = y1 + 62                               # diagram top
bh = 92
# step1 boxes
chip(M, by, M + 300, by + bh, "WBI", 34, ACCENT, sub="股东持股 49%", subsz=24)
chip(M, by + bh + 26, M + 300, by + 2 * bh + 26, "M公司", 34, TEAL, sub="韩国GMP制造 · 51%", subsz=24)
# arrows to holdco
midy = by + bh + 13
arrow_r(M + 310, by + bh // 2, 40)
arrow_r(M + 310, by + bh + 26 + bh // 2, 40)
chip(M + 412, by + 18, M + 760, by + 2 * bh + 8, "合资控股公司", 34, NAVY,
     sub="开曼 · 技术团队股权池5–10%", subsz=22, subcol=SKY)
arrow_r(M + 770, midy + 4, 40)
chip(M + 872, by + 18, M + 1150, by + 2 * bh + 8, "韩国子公司", 32, DARK2,
     sub="100% 收购两家公司", subsz=22, subcol=SKY)
# step2: merge with P
arrow_r(M + 1160, midy + 4, 40, col=GOLD)
chip(M + 1262, by + 18, W - M, by + 2 * bh + 8, "P公司", 34, GOLD,
     sub="美国合并对象·按核实价值(备选)", subsz=20)
# footnote row
yf = by + 2 * bh + 44
text(M, yf, "换股合并（第二步·备选）：合资公司股东按持股比例、以整体进入 P公司；P公司现有股东占比按独立核实价值＋公平性意见厘定（若核实值≈$0–2M，其占比预计仅为低个位数）。",
     23, GREY, maxw=W - 2 * M)
# timeline
ty = yf + 74
dr.line([(M + 10, ty + 26), (W - M - 10, ty + 26)], fill=SKY, width=6)
steps = [("2026 Q4", "启动PCAOB审计（关键路径）", ACCENT), ("2027 Q1–Q2", "完成两家公司换股", TEAL),
         ("2027 底", "递交美国上市申报", GOLD), ("2028", "目标完成上市", NAVY)]
seg = (W - 2 * M - 20) / 3
for i, (tt, dd, col) in enumerate(steps):
    cx = int(M + 10 + i * seg)
    dr.ellipse([cx - 13, ty + 13, cx + 13, ty + 39], fill=col)
    anchor = "ma" if 0 < i < 3 else ("la" if i == 0 else "ra")
    ax = cx if 0 < i < 3 else (M if i == 0 else W - M)
    text(ax, ty + 52, tt, 26, col, bold=True, anchor=anchor)
    text(ax, ty + 88, dd, 22, GREY, anchor=anchor)

# ================= S2 关键数字 =================
y2 = ty + 150
text(M, y2, "② 关键数字（美元）", 34, NAVY, bold=True)
cy = y2 + 60
# left: revenue bars
ch_x, ch_y, ch_w, ch_h = M, cy + 10, 760, 330
years = ["2026", "2027", "2028", "2029", "2030"]
vals = [16.39, 25.31, 31.70, 43.82, 58.91]
maxv = 60.0
bw = 92; gap = (ch_w - 5 * bw) / 4
for i, (yy, v) in enumerate(zip(years, vals)):
    x0 = ch_x + int(i * (bw + gap)); hpx = int(v / maxv * (ch_h - 70))
    y0 = ch_y + ch_h - 40 - hpx
    dr.rectangle([x0, y0, x0 + bw, ch_y + ch_h - 40], fill=ACCENT if i < 4 else NAVY)
    text(x0 + bw // 2, y0 - 30, "%.1f" % v, 24, NAVY, bold=True, anchor="ma")
    text(x0 + bw // 2, ch_y + ch_h - 30, yy, 24, GREY, anchor="ma")
text(ch_x, ch_y + ch_h + 8, "集团收入规划（合并前口径，百万美元）；P公司 GLP-1 数字为其计划值、未经核实，不计入本集团规划",
     22, GREY, maxw=760)
# right: stat chips
sx = M + 820; sw = W - M - sx
chip(sx, cy + 10, W - M, cy + 112, "$30–40M", 42, NAVY, sub="合资公司合并估值区间（技术授权价值另有 $5–10M 情景）", subsz=21, subcol=SKY)
chip(sx, cy + 132, sx + (sw - 20) // 2, cy + 234, "≈$0–2M", 40, TEAL, sub="P公司尽调后核实价值区间", subsz=20)
chip(sx + (sw - 20) // 2 + 20, cy + 132, W - M, cy + 234, "2028", 40, GOLD, sub="目标上市年份", subsz=21)
chip(sx, cy + 254, W - M, cy + 356, "₩104.6亿", 40, ACCENT, sub="M公司FY2025法定营收（已核实·净利₩20.5亿）", subsz=20, subcol=SKY)

# ================= S3 WBI 每股价值路径 =================
y3 = cy + 430
text(M, y3, "③ WBI 每股价值路径（说明性）", 34, NAVY, bold=True)
py = y3 + 60
# three-stage bars
stages = [("现值", PX, PX, ACCENT, "已发行 111,448 股（含5%增发 5,572 股）≈ 总值 $1,000万"),
          ("合资作价隐含", PS_JV_LO, PS_JV_HI, TEAL, "WBI 作价区间 $15–20M ÷ 111,448 股"),
          ("上市情景", PS_IPO_LO, PS_IPO_HI, GOLD, "上市后WBI股东价值情景 $28.2M–$36.3M（工作底稿）")]
pmax = 340.0; pw = 300; pg = (W - 2 * M - 3 * pw) // 2; ph_area = 290
for i, (lab, lo, hi, col, note) in enumerate(stages):
    x0 = M + i * (pw + pg)
    hpx_hi = int(hi / pmax * ph_area); hpx_lo = int(lo / pmax * ph_area)
    base = py + ph_area + 10
    dr.rectangle([x0 + 60, base - hpx_hi, x0 + pw - 60, base], fill=tuple(min(255, c + 70) for c in col))
    dr.rectangle([x0 + 60, base - hpx_lo, x0 + pw - 60, base], fill=col)
    if hi > lo:
        text(x0 + pw // 2, base - hpx_hi - 34, "$%.0f–%.0f" % (lo, hi), 30, col, bold=True, anchor="ma")
    else:
        text(x0 + pw // 2, base - hpx_hi - 34, "$%.2f" % lo, 30, col, bold=True, anchor="ma")
    text(x0 + pw // 2, base + 10, lab, 28, NAVY, bold=True, anchor="ma")
    text(x0 + pw // 2, base + 48, note, 20, GREY, anchor="ma", maxw=pw + 40)
    if i < 2:
        arrow_r(x0 + pw - 26, base - 120, 44, col=GREY)
text(M, py + ph_area + 128,
     "以上为规划/说明性区间，非承诺；实际取决于独立估值、公平性意见、审计与市场条件。全体 WBI 股东按持股比例同步参与。",
     22, RED, maxw=W - 2 * M)

# ================= S4 优势 vs 风险 =================
y4 = py + ph_area + 196
text(M, y4, "④ 优势 与 风险管理", 34, NAVY, bold=True)
colw = (W - 2 * M - 40) // 2
ly = y4 + 58
rrect(M, ly, M + colw, ly + 500, outline=ACCENT, w=3)
rrect(M + colw + 40, ly, W - M, ly + 500, outline=RED, w=3)
text(M + 24, ly + 16, "优势", 30, ACCENT, bold=True)
text(M + colw + 64, ly + 16, "风险 → 管理措施", 30, RED, bold=True)
pros = [
    "自主赴美上市（默认路径）与韩国上市（备选）双轨并行；集团有经核实的盈利基础（M公司FY2025净利₩20.5亿）",
    "若P公司GLP-1计划经独立核实（1-K年报＋运营数据），其渠道或可与本集团品类协同（目前仅为计划）",
    "M公司 GMP 产能与现有收入并表，集团2030规划收入 $58.9M",
    "D公司（某上市集团附属）正评估技术授权；若达成将佐证AI肽平台$5–10M价值并增特许权收入（前提：权属链完成）",
]
risks = [
    "P公司尽调：仅Reg A+众筹备案、暂无营收（待1-K确认）→ 仅按核实价值、取消期权池后才考虑合并；否则不采用",
    "个人先持的过渡安排 → 书面代持声明、限期同价转入控股公司、韩国税务书面意见；最终全体股东按比例整体进入",
    "M公司FY2025报表已核实：较$8.0M基准偏差-6.6%（@₩1,400），在15%带内，51:49维持；日后偏差>15%仍强制调整",
    "合并本身不募集资金 → 另行制定融资方案；上市后再行增发补充资本",
]
for i, p in enumerate(pros):
    yy = ly + 70 + i * 106
    dr.ellipse([M + 24, yy + 6, M + 46, yy + 28], fill=ACCENT)
    text(M + 40 - 5, yy + 4, str(i + 1), 20, WHITE, bold=True, anchor="ma")
    text(M + 62, yy, p, 23, NAVY, maxw=colw - 90)
for i, p in enumerate(risks):
    yy = ly + 70 + i * 106
    dr.ellipse([M + colw + 64, yy + 6, M + colw + 86, yy + 28], fill=RED)
    text(M + colw + 80 - 5, yy + 4, str(i + 1), 20, WHITE, bold=True, anchor="ma")
    text(M + colw + 102, yy, p, 23, NAVY, maxw=colw - 90)

# ================= footer =================
dr.rectangle([0, H - 74, W, H], fill=NAVY)
text(W // 2, H - 52, "机密 · 仅供 WBI 股东参考 · 非投资建议 · 所有交易须待尽职调查、独立估值、审计与最终协议", 21, SKY, anchor="ma")

img.save(DIR + "WBI_Shareholder_OnePager_CN.png")
print("Saved WBI_Shareholder_OnePager_CN.png  (%dx%d)" % (W, H))
print("per-share: now $%.2f | JV $%.1f-%.1f | IPO $%.1f-%.1f | cap $%s"
      % (PX, PS_JV_LO, PS_JV_HI, PS_IPO_LO, PS_IPO_HI, format(int(CAP), ",")))

# ================= pptx mirror (editable) =================
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

C = lambda t: RGBColor(*t)
prs = Presentation()
prs.slide_width = Inches(8.27); prs.slide_height = Inches(11.69)   # A4 portrait
s = prs.slides.add_slide(prs.slide_layouts[6])
SC = 8.27 / W                                                       # px -> inch

def prect(x0, y0, x1, y1, fill=None, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    sp = s.shapes.add_shape(shape, Inches(x0 * SC), Inches(y0 * SC),
                            Inches((x1 - x0) * SC), Inches((y1 - y0) * SC))
    if fill is None: sp.fill.background()
    else: sp.fill.solid(); sp.fill.fore_color.rgb = C(fill)
    if line is None: sp.line.fill.background()
    else: sp.line.color.rgb = C(line); sp.line.width = Pt(1.5)
    sp.shadow.inherit = False
    return sp

def ptext(x, y, w, t, sz, col=NAVY, bold=False, align=PP_ALIGN.LEFT):
    tb = s.shapes.add_textbox(Inches(x * SC), Inches(y * SC), Inches(w * SC), Inches(0.35))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = t
    r.font.size = Pt(sz * SC * 72 / 1.0 * 0.95); r.font.bold = bold
    r.font.color.rgb = C(col); r.font.name = "微软雅黑"
    return tb

prect(0, 0, W, 150, fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
ptext(M, 30, W - 2 * M, "WBI 股东简报 — 三方合并 · 美国上市计划", 46, WHITE, True)
ptext(M, 100, W - 2 * M, "仅供 WBI 股东参考 · 合作方以代号表示 · 非要约 · 数字为规划/说明口径 · 2026年9月", 24, SKY)
pic = s.shapes.add_picture(DIR + "WBI_Shareholder_OnePager_CN.png", 0, 0,
                           Inches(8.27), Inches(11.69))
# put the picture behind is unnecessary; instead we ship the PNG as the page and
# keep a text layer above for editing convenience — simplest robust mirror:
# remove overlay text boxes (picture already contains everything)
for sh in list(s.shapes):
    if sh.shape_type != 13:  # keep only the picture
        sh._element.getparent().remove(sh._element)
prs.save(DIR + "WBI_Shareholder_OnePager_CN.pptx")
print("Saved WBI_Shareholder_OnePager_CN.pptx (A4 portrait, image page)")
