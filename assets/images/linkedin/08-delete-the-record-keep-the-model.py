"""Graphic for the LinkedIn post 08-delete-the-record-keep-the-model.

Two panels, one claim. Left: a patient record is removed from the database, so its
row is an empty slot. Right: the model that trained on that record keeps a trace of
it, spread over the weights, and nothing says which weights to touch.

Nothing here is measured. It is a schematic of an open problem, so the right panel
is drawn from a seeded random spread on purpose: the point is that the location is
unknown, and a figure that marked specific cells would claim the opposite.

Colours are categorical slots 1 and 2 of the house palette, validated for
colour-vision deficiency separation (worst adjacent protan dE 24.7, floor 8).

Run: python 08-delete-the-record-keep-the-model.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

OUT = "08-delete-the-record-keep-the-model.png"

BLUE = "#2a78d6"    # slot 1: the patient record
ORANGE = "#eb6834"  # slot 2: the trace left in the model
SURFACE = "#fcfcfb"
INK = "#1a1a19"
INK_2 = "#5c5b55"
GRID = "#e4e3de"

N_ROWS = 6          # records in the left panel
GONE = 3            # which one was deleted
N_COLS_W = 13       # weight grid
N_ROWS_W = 10
SEED = 11


def _font():
    """Prefer Helvetica Neue, fall back to whatever the system has."""
    have = {f.name for f in font_manager.fontManager.ttflist}
    for name in ("Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"):
        if name in have:
            return name
    return "sans-serif"


def _records(ax):
    """Six rows of a table with one row emptied out."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    pad = 0.035
    h = (1.0 - pad * (N_ROWS - 1)) / N_ROWS
    for i in range(N_ROWS):
        y = 1.0 - (i + 1) * h - i * pad
        if i == GONE:
            box = FancyBboxPatch(
                (0.0, y), 1.0, h,
                boxstyle="round,pad=0,rounding_size=0.02",
                facecolor=SURFACE, edgecolor=BLUE, linewidth=2.6,
                linestyle=(0, (4, 3)),
            )
            ax.add_patch(box)
        else:
            box = FancyBboxPatch(
                (0.0, y), 1.0, h,
                boxstyle="round,pad=0,rounding_size=0.02",
                facecolor=GRID, edgecolor="none",
            )
            ax.add_patch(box)
            # Two blocks per row, so it reads as a record and not as a bar chart.
            ax.add_patch(Rectangle((0.05, y + h * 0.36), 0.30, h * 0.28,
                                   facecolor="#cfceca", edgecolor="none"))
            ax.add_patch(Rectangle((0.42, y + h * 0.36), 0.46, h * 0.28,
                                   facecolor="#cfceca", edgecolor="none"))


def _weights(ax):
    """A weight grid tinted everywhere, brighter in a few cells, none of them named."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rng = np.random.default_rng(SEED)
    tint = rng.random((N_ROWS_W, N_COLS_W)) ** 2.6

    gap = 0.012
    w = (1.0 - gap * (N_COLS_W - 1)) / N_COLS_W
    h = (1.0 - gap * (N_ROWS_W - 1)) / N_ROWS_W
    for r in range(N_ROWS_W):
        for c in range(N_COLS_W):
            x = c * (w + gap)
            y = 1.0 - (r + 1) * h - r * gap
            ax.add_patch(Rectangle((x, y), w, h, facecolor=GRID, edgecolor="none"))
            ax.add_patch(Rectangle((x, y), w, h, facecolor=ORANGE, edgecolor="none",
                                   alpha=0.06 + 0.72 * tint[r, c]))


def main():
    plt.rcParams["font.family"] = _font()

    fig = plt.figure(figsize=(10, 10), dpi=120, facecolor=SURFACE)

    ax_l = fig.add_axes([0.105, 0.285, 0.335, 0.395])
    ax_r = fig.add_axes([0.570, 0.285, 0.335, 0.395])
    ax_l.set_facecolor(SURFACE)
    ax_r.set_facecolor(SURFACE)
    _records(ax_l)
    _weights(ax_r)

    fig.text(0.105, 0.955, "Removing a patient from", fontsize=42,
             fontweight="bold", color=INK, va="top")
    fig.text(0.105, 0.890, "a model does not stick", fontsize=42,
             fontweight="bold", color=INK, va="top")
    fig.text(0.105, 0.818,
             "A patient can have their hospital record destroyed. The model that\n"
             "was trained on it keeps whatever it learned.",
             fontsize=19.5, color=INK_2, va="top", linespacing=1.5)

    fig.text(0.105, 0.715, "THE RECORD", fontsize=15, fontweight="bold",
             color=BLUE, va="bottom")
    fig.text(0.570, 0.715, "THE MODEL", fontsize=15, fontweight="bold",
             color=ORANGE, va="bottom")

    # The training step, drawn in the gutter between the two panels.
    fig.text(0.5055, 0.508, "trained on", fontsize=13.5, color=INK_2,
             ha="center", va="bottom")
    fig.add_artist(FancyArrowPatch(
        (0.451, 0.483), (0.560, 0.483), transform=fig.transFigure,
        arrowstyle="-|>", mutation_scale=18, color=INK_2, linewidth=1.8,
        shrinkA=0, shrinkB=0))

    fig.text(0.105, 0.225,
             "Deleted on request.\nThree months, no reason needed.",
             fontsize=17, color=INK, va="top", linespacing=1.5)
    fig.text(0.570, 0.225,
             "Whatever it learned from that record\nis still in these numbers.",
             fontsize=17, color=INK, va="top", linespacing=1.5)

    fig.text(0.105, 0.042,
             "Axel Faes, UTwente",
             fontsize=14, color=INK_2)

    fig.savefig(OUT, facecolor=SURFACE)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
