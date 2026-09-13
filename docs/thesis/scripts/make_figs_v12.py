#!/usr/bin/env python3
"""Regenerate Figure 6.1 and Figure 6.3 on the rebuilt register denominators
(38 / 41 / 41), in the same visual style as the other regenerated diagrams."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.size"] = 10

INK = "#22302B"; EDGE = "#4A5A66"
GREEN_D = "#7FB99A"; CORAL_D = "#DE9A85"; BLUE_D = "#8FB4D4"; SAND_D = "#DCC08A"

bands = ["25–44\n(n = 38)", "45–64\n(n = 41)", "65–80\n(n = 41)"]
x = np.arange(3)

# ---------- Figure 6.1: retention and observed non-return by band ----------
retention = [100.0, 95.1, 85.4]
nonreturn = [0.0, 4.9, 14.6]
f, ax = plt.subplots(figsize=(8.2, 4.4), dpi=200)
w = 0.36
b1 = ax.bar(x - w/2, retention, w, color=GREEN_D, edgecolor=EDGE, lw=1.2,
            label="Retention at end of study window")
b2 = ax.bar(x + w/2, nonreturn, w, color=CORAL_D, edgecolor=EDGE, lw=1.2,
            label="Observed non-return")
for b in list(b1) + list(b2):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1.5,
            f"{b.get_height():.1f}%", ha="center", va="bottom",
            fontsize=9, color=INK)
ax.set_xticks(x); ax.set_xticklabels(bands, color=INK)
ax.set_ylim(0, 112)
ax.set_ylabel("Per cent of band", color=INK)
ax.set_title("Stage-3 retention and observed non-return by age band (N = 120)",
             fontsize=11, color=INK)
ax.legend(frameon=False, loc="center right", fontsize=9)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(EDGE)
ax.tick_params(colors=EDGE)
f.savefig("figure_6_1_v12.png", bbox_inches="tight", facecolor="white")
plt.close(f); print("saved figure_6_1_v12.png")

# ---------- Figure 6.3: retention vs regular-use intention by band ----------
intention = [65.8, 68.3, 56.1]
f, ax = plt.subplots(figsize=(8.2, 4.4), dpi=200)
b1 = ax.bar(x - w/2, retention, w, color=BLUE_D, edgecolor=EDGE, lw=1.2,
            label="Observed session retention")
b2 = ax.bar(x + w/2, intention, w, color=SAND_D, edgecolor=EDGE, lw=1.2,
            label="Stated regular-use intention")
for b in list(b1) + list(b2):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1.5,
            f"{b.get_height():.1f}%", ha="center", va="bottom",
            fontsize=9, color=INK)
# bracket for the 29.3-pp commitment gap in the 65-80 band
gx = 2
y_hi, y_lo = retention[2], intention[2]
bx = gx + w/2 + 0.28
ax.plot([bx, bx + 0.07, bx + 0.07, bx], [y_hi, y_hi, y_lo, y_lo],
        color=INK, lw=1.2)
ax.text(bx + 0.11, (y_hi + y_lo)/2, "29.3 pp\ncommitment gap",
        va="center", ha="left", fontsize=9, color=INK)
ax.set_xticks(x); ax.set_xticklabels(bands, color=INK)
ax.set_xlim(-0.6, 3.1)
ax.set_ylim(0, 112)
ax.set_ylabel("Per cent of band", color=INK)
ax.set_title("Stage-3 session retention versus stated regular-use intention by age band",
             fontsize=11, color=INK)
ax.legend(frameon=False, loc="lower left", fontsize=9)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(EDGE)
ax.tick_params(colors=EDGE)
f.savefig("figure_6_3_v12.png", bbox_inches="tight", facecolor="white")
plt.close(f); print("saved figure_6_3_v12.png")
