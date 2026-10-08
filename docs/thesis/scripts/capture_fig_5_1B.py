#!/usr/bin/env python3
"""Capture skiing-game screenshots at five staged difficulty levels for
Figure 5.1B, then compose them into a single labelled figure panel."""
import time
from playwright.sync_api import sync_playwright

GAME = ("file:///home/user/gamification/docs/thesis/game/"
        "Alpine_Coordination_Game_Stage3_v2.html")
OUT = "/tmp/claude-0/-home-user-gamification/3d8a50e8-9258-51ce-a7d6-194da50f9a04/scratchpad/"
LEVELS = [(1, 0.40), (2, 0.65), (3, 0.90), (4, 1.15), (5, 1.40)]
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path=CHROME)
    page = browser.new_page(viewport={"width": 1000, "height": 900})
    for lvl, diff in LEVELS:
        page.goto(GAME)
        page.fill("#pid", "DEMO")
        page.select_option("#sessno", str(min(lvl, 5)))
        page.select_option("#goal", "400")          # longer run: more time to capture
        page.evaluate("document.getElementById('agentic').checked = false")
        page.click("#startBtn")
        # pin the difficulty and density so the frame shows the staged level
        page.evaluate(
            "d => { setInterval(() => { if (S) { S.diff = d; S.obFactor = 1.0; } }, 50); }",
            diff)
        # let the run build up obstacles appropriate to the level
        time.sleep(4.5 if lvl < 4 else 6.0)
        page.locator("#cv").screenshot(path=f"{OUT}fig51B_level{lvl}.png")
        print(f"captured level {lvl} (diff {diff})")
    browser.close()

# ---------------- compose ----------------
from PIL import Image, ImageDraw, ImageFont

panels = [Image.open(f"{OUT}fig51B_level{l}.png") for l, _ in LEVELS]
w, h = panels[0].size
scale = 0.5
w2, h2 = int(w * scale), int(h * scale)
panels = [p.resize((w2, h2), Image.LANCZOS) for p in panels]
PAD, LABEL_H = 14, 34
cols, rows = 2, 3
W = cols * w2 + (cols + 1) * PAD
H = rows * (h2 + LABEL_H) + (rows + 1) * PAD
canvas = Image.new("RGB", (W, H), "#FFFFFF")
draw = ImageDraw.Draw(canvas)
try:
    font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 17)
    font_s = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", 15)
except Exception:
    font = font_s = ImageFont.load_default()

INK = (34, 48, 43)
for i, (img, (lvl, diff)) in enumerate(zip(panels, LEVELS)):
    r, c = divmod(i, cols)
    x = PAD + c * (w2 + PAD)
    y = PAD + r * (h2 + LABEL_H + PAD)
    draw.text((x + 2, y + 6),
              f"Level {lvl}  ·  difficulty multiplier {diff:.2f}",
              fill=INK, font=font)
    canvas.paste(img, (x, y + LABEL_H))
    draw.rectangle([x, y + LABEL_H, x + w2, y + LABEL_H + h2],
                   outline=(74, 90, 102), width=2)
# legend in the empty sixth cell
x = PAD + 1 * (w2 + PAD)
y = PAD + 2 * (h2 + LABEL_H + PAD) + LABEL_H
draw.rectangle([x, y, x + w2, y + h2], outline=(74, 90, 102), width=2,
               fill=(246, 235, 215))
legend = ("Difficulty rises from Level 1 to Level 5:\n"
          "obstacle spawn rate increases with the\n"
          "multiplier, stones become more frequent\n"
          "relative to trees, and boulder pairs\n"
          "appear from Level 3 upward. The skier is\n"
          "steered by lateral weight shift; coins\n"
          "reward forward play. Captured from the\n"
          "programme's archived game build.")
draw.multiline_text((x + 16, y + 18), legend, fill=INK, font=font_s,
                    spacing=6)
canvas.save(OUT + "fig_5_1B.png")
print("composed fig_5_1B.png", canvas.size)
