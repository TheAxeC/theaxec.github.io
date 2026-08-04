"""Graphic for the LinkedIn post 07-transparent-and-robust.

One picture of the paper's finding: under increasing muscle-noise contamination the
best ECG foundation model collapses while the transparent named-feature model holds.

Numbers are the CODE-15 cohort AUROCs, copied from the paper's own result file
projects/manuscripts/glassbox-decision-pipelines/results/robustness_code15.json
(keys accuracy.named and accuracy.ecg_jepa, conditions clean / emg_noise_1..3).
That JSON is regenerated from raw by code/hpc/run_all.sh in the project repo.

Colours are categorical slots 1 and 2 of the house palette, validated for
colour-vision deficiency separation (worst adjacent protan dE 24.7, floor 8).

Run: python 07-transparent-and-robust.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = "07-transparent-and-robust.png"

# CODE-15, 1-year all-cause mortality, AUROC at rising EMG (muscle) noise severity.
SEVERITY = ["clean", "mild", "moderate", "severe"]
NAMED = [0.8043, 0.7938, 0.7727, 0.7540]
JEPA = [0.8124, 0.7544, 0.6448, 0.6139]

BLUE = "#2a78d6"    # slot 1: the transparent model
ORANGE = "#eb6834"  # slot 2: the foundation model
SURFACE = "#fcfcfb"
INK = "#1a1a19"
INK_2 = "#5c5b55"
GRID = "#e4e3de"


def _font():
    """Prefer Helvetica Neue, fall back to whatever the system has."""
    have = {f.name for f in font_manager.fontManager.ttflist}
    for name in ("Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"):
        if name in have:
            return name
    return "sans-serif"


def main():
    plt.rcParams["font.family"] = _font()

    fig = plt.figure(figsize=(10, 10), dpi=120, facecolor=SURFACE)
    ax = fig.add_axes([0.105, 0.155, 0.855, 0.575])
    ax.set_facecolor(SURFACE)

    x = range(len(SEVERITY))

    # Recessive grid, only where it helps read a value off the y axis.
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color=GRID, linewidth=1.0)
    ax.xaxis.grid(False)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.spines["bottom"].set_linewidth(1.0)
    ax.tick_params(length=0, colors=INK_2, labelsize=15)

    ax.plot(x, NAMED, color=BLUE, linewidth=3.0, marker="o", markersize=10,
            markeredgecolor=SURFACE, markeredgewidth=2.0, zorder=3)
    ax.plot(x, JEPA, color=ORANGE, linewidth=3.0, marker="o", markersize=10,
            markeredgecolor=SURFACE, markeredgewidth=2.0, zorder=3)

    # Direct labels carry series identity, so colour is never the only cue. They sit
    # inside the plot at the right, where each line has clear air around it.
    ax.text(2.96, 0.792, "Transparent model\n165 named ECG features + age",
            color=BLUE, fontsize=17, fontweight="bold", va="bottom", ha="right",
            linespacing=1.4)
    ax.text(2.96, 0.744, "0.754", color=BLUE, fontsize=19, fontweight="bold",
            va="top", ha="right")
    ax.text(2.96, 0.636, "Best foundation model\nECG-JEPA",
            color=ORANGE, fontsize=17, fontweight="bold", va="bottom", ha="right",
            linespacing=1.4)
    ax.text(2.96, 0.604, "0.614", color=ORANGE, fontsize=19, fontweight="bold",
            va="top", ha="right")

    # One note for the shared starting point, instead of two colliding tick labels.
    ax.text(-0.22, 0.828, "clean signal: 0.804 vs 0.812, a tie",
            color=INK_2, fontsize=15.5, va="bottom", ha="left")

    ax.set_xticks(list(x))
    ax.set_xticklabels(SEVERITY, fontsize=16)
    ax.set_xlim(-0.25, 3.06)
    ax.set_ylim(0.578, 0.858)
    ax.set_yticks([0.60, 0.65, 0.70, 0.75, 0.80])
    ax.set_yticklabels(["0.60", "0.65", "0.70", "0.75", "0.80"])
    ax.set_xlabel("muscle-noise contamination of the ECG", fontsize=16.5,
                  color=INK_2, labelpad=10)
    ax.set_ylabel("AUROC, 1-year mortality", fontsize=16.5, color=INK_2, labelpad=10)

    fig.text(0.105, 0.955, "The black box breaks first", fontsize=44,
             fontweight="bold", color=INK, va="top")
    fig.text(0.105, 0.877,
             "Both models predict 1-year mortality from one 12-lead ECG.\n"
             "They tie on a clean signal. Then the recording gets noisy.",
             fontsize=19.5, color=INK_2, va="top", linespacing=1.5)
    fig.text(0.105, 0.042,
             "CODE-15 external cohort, n = 65,000. Faes, XAI-EADM at IEEE CBI/EDOC 2026.",
             fontsize=14, color=INK_2)

    fig.savefig(OUT, facecolor=SURFACE)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
