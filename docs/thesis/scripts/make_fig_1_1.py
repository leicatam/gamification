#!/usr/bin/env python3
"""Figure 1.1 — the intellectual structure of the thesis, in the house style."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 10

INK = "#22302B"; BLUE = "#DCE9F5"; GREEN = "#DFF0E4"; SAND = "#F6EBD7"
CORAL = "#F6DCD3"; GREY = "#EDEDE8"; EDGE = "#4A5A66"

f, ax = plt.subplots(figsize=(8.6, 7.2), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

def box(x, y, w, h, text, fc, fs=9.5, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle="round,pad=0.6,rounding_size=1.4",
                 fc=fc, ec=EDGE, lw=1.4))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=fs, color=INK, fontweight="bold" if bold else "normal")

def down(x, y1, y2):
    ax.add_patch(FancyArrowPatch((x, y1), (x, y2), arrowstyle="-|>",
                 mutation_scale=16, color=EDGE, lw=1.8))

def tag(y, text):
    ax.text(88, y, text, ha="left", va="center", fontsize=9,
            color=EDGE, style="italic")

X, W, H = 8, 76, 12.5
ys = [86, 67, 48, 29, 10]

box(X, ys[0], W, H,
    "1 · INDUSTRIAL PROBLEM\nA clinically validated FRA station that elderly users\ntry once and abandon",
    SAND, bold=False)
box(X, ys[1], W, H,
    "2 · OBSERVED BEHAVIOURAL PHENOMENON\nFIAS — failure-induced abandonment:\nwhy users disengage after early failure",
    CORAL)
box(X, ys[2], W, H,
    "3 · ENGINEERING DESIGN PRINCIPLES\nThe adaptive-learning framework:\nidentity disentanglement · trajectory installation · adaptive calibration",
    BLUE)
box(X, ys[3], W, H,
    "4 · SYSTEM IMPLEMENTATION\nDynamic game-state engine with AI support:\nreal-time state monitoring and non-terminal state selection",
    GREEN)
box(X, ys[4], W, H,
    "5 · INDUSTRIAL OUTCOME\nSustained engagement and return; continuous improvement\nat the individual level; clinical validity preserved",
    GREY)

for i in range(4):
    down(X + W/2, ys[i], ys[i+1] + H)

tag(ys[1] + H/2, "the phenomenon\n(why)")
tag(ys[2] + H/2, "the principles\n(how)")
tag(ys[3] + H/2, "the engine\n(real time)")

f.savefig("fig_1_1.png", bbox_inches="tight", facecolor="white")
plt.close(f)
print("saved fig_1_1.png")
