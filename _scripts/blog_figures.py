"""Writes the SVG figures of the research blog posts to assets/images/<post>/.

Each figure is written twice, as <name>-light.svg and <name>-dark.svg, with the site's theme colours.
Run from the repository root: python3 _scripts/blog_figures.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "images"
POST = {"early-timeline": "what-early-means", "early-design": "what-early-means", "proof-average-box": "proof-of-interpretability", "wall-objects": "what-crosses-the-hospital-wall"}
THEMES = {
    "light": {"paper": "#F0F3F1", "surface": "#FFFFFF", "ink": "#121C19", "muted": "#566761", "line": "#DAE3DF", "soft": "#E5EDE9", "accent": "#0C594E"},
    "dark": {"paper": "#0B1311", "surface": "#11201C", "ink": "#E6EFEB", "muted": "#8BA39B", "line": "#213029", "soft": "#152420", "accent": "#37C3AC"},
}
INK, MUTED, LINE, ACCENT, SURFACE = "var(--ink)", "var(--muted)", "var(--line)", "var(--accent)", "var(--surface)"
W = 560


def text(x, y, s, fill=INK, size=13, anchor="start", weight=400):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-size="{round(size * 1.16, 1)}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'


def line(x1, y1, x2, y2, stroke=LINE, width=1, dash=None, extra=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round"{d}{extra}/>'


def dot(x, y, tip, fill=ACCENT, stroke=SURFACE, r=6, width=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"><title>{escape(tip)}</title></circle>'


def write(name, height, title, desc, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" role="img" font-family="Helvetica, Arial, sans-serif">'
        f"<title>{escape(title)}</title><desc>{escape(desc)}</desc>" + "".join(body) + "</svg>\n"
    )
    folder = OUT / POST[name]
    folder.mkdir(parents=True, exist_ok=True)
    for theme, colours in THEMES.items():
        out = svg
        for token, value in colours.items():
            out = out.replace(f"var(--{token})", value)
        (folder / f"{name}-{theme}.svg").write_text(out)


def early_timeline():
    stops = [(170, "Disease starts"), (320, "Clinician acts"), (420, "Diagnosis"), (530, "Death")]
    body = []
    for x, label in stops:
        body += [text(x, 18, label, MUTED, 12, "middle"), line(x, 28, x, 270, LINE, 1, "3 4")]
    lanes = [
        ("Future event", "compared with age and known facts", 20, 170),
        ("Hidden disease", "compared with the reading of the same exam", 170, 320),
        ("Acute alert", "compared with the clinician", 270, 320),
        ("Screening gain", "compared with the same patients unscreened", 230, 420),
    ]
    y = 62
    for name, comp, x1, x2 in lanes:
        body.append(f'<text x="20" y="{y - 10}" font-size="15" fill="{INK}" style="paint-order:stroke;stroke:var(--paper);stroke-width:4px"><tspan font-weight="600">{name}</tspan><tspan fill="{MUTED}"> {comp}</tspan></text>')
        if name == "Screening gain":
            body += [line(x2 - 8, y + 2, x1 + 10, y + 2, ACCENT, 2.5), f'<path d="M{x1} {y + 2} l11 -6 v12 z" fill="{ACCENT}"/>', dot(x2, y + 2, "Usual date of diagnosis", SURFACE, ACCENT, 5, 2.5), text(x1, y + 24, "Diagnosis moves earlier. Death may not move.", MUTED, 12)]
        else:
            body.append(f'<rect x="{x1}" y="{y - 2}" width="{x2 - x1}" height="8" rx="4" fill="{ACCENT}"><title>{name}: when the model has to speak</title></rect>')
        y += 56
    write("early-timeline", 276, "The four claims of early detection on one patient timeline",
          "Schematic. A future event claim scores an exam before disease starts. A hidden disease claim scores an exam between disease start and the clinician acting. An acute alert speaks shortly before the clinician acts. A screening gain moves the diagnosis earlier and may leave the date of death unchanged.", body)


def early_dumbbell():
    x0, x1, lo, hi = 24, 470, 0.4, 0.9
    X = lambda v: round(x0 + (v - lo) / (hi - lo) * (x1 - x0), 1)
    top, step = 62, 52
    rows = [
        ("Sepsis: exclude predictions after recognition", 0.62, 0.47, "-0.15"),
        ("Sepsis: exclude predictions after onset", 0.80, 0.63, "-0.17"),
        ("Pancreatic cancer: exclude last 3 months", 0.879, 0.843, "-0.036"),
        ("Pancreatic cancer above age 50: exclude last 3 months", 0.753, 0.674, "-0.079"),
        ("Pancreatic cancer: all ages to above age 50", 0.879, 0.753, "-0.126"),
    ]
    bottom = top + step * (len(rows) + 1) - 18
    body = [
        dot(30, 16, "Before", SURFACE, MUTED, 5, 2), text(42, 20, "Before the change", MUTED, 12),
        dot(170, 16, "After", ACCENT, SURFACE, 6), text(182, 20, "After the change", MUTED, 12),
        text(W - 8, 20, "Change", MUTED, 12, "end"),
    ]
    for t in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9):
        body += [line(X(t), 40, X(t), bottom, LINE), text(X(t), bottom + 16, f"{t:.1f}", MUTED, 12, "middle")]
    body.append(text(X(0.5) + 5, 50, "coin toss", MUTED, 12))
    y = top
    for label, a, b, change in rows:
        body += [text(x0, y + 4, label, INK, 12.5), line(X(b), y + 20, X(a), y + 20, MUTED, 2),
                 dot(X(a), y + 20, f"{label}: before {a}", SURFACE, MUTED, 5, 2),
                 dot(X(b), y + 20, f"{label}: after {b}", ACCENT, SURFACE, 6), text(W - 8, y + 24, change, INK, 12.5, "end")]
        y += step
    body += [text(x0, y + 4, "Mammography, 7 sites: exclude cancers within 6 months (C-index)", INK, 12.5),
             line(X(0.75), y + 15, X(0.84), y + 15, MUTED, 4), line(X(0.69), y + 24, X(0.78), y + 24, ACCENT, 4),
             text(W - 8, y + 24, "-0.03 to -0.10", INK, 12.5, "end")]
    write("early-design", bottom + 24, "Scores of one model before and after a change of design",
          "Dumbbell chart of the six rows of the table above. Every score falls. The mammography row shows the range across sites before and after.", body)


def proof_dots():
    x0, x1 = 214, 540
    X = lambda v: round(x0 + v / 0.7 * (x1 - x0), 1)
    rows = [
        ("RetinaNet", "a detection network", 0.59, MUTED),
        ("XRAI", "highest saliency method", 0.52, MUTED),
        ("Average box", "same box for every patient", 0.47, ACCENT),
        ("SIG", "lowest saliency method", 0.16, MUTED),
    ]
    top, step = 26, 46
    bottom = top + step * len(rows) - 8
    body = [f'<rect x="{X(0.16)}" y="{top + step - 16}" width="{X(0.52) - X(0.16)}" height="{step * 3 - 12}" rx="4" fill="var(--soft)"/>',
            text((X(0.16) + X(0.52)) / 2, 18, "range of the saliency methods", MUTED, 12, "middle")]
    for t in (0, 0.2, 0.4, 0.6):
        body += [line(X(t), top - 2, X(t), bottom, LINE), text(X(t), bottom + 16, f"{t:.1f}", MUTED, 12, "middle")]
    y = top + 16
    for name, note, v, colour in rows:
        body += [text(8, y, name, INK, 13, weight=600), text(8, y + 15, note, MUTED, 12), line(x0, y + 4, X(v), y + 4, colour, 2),
                 dot(X(v), y + 4, f"{name}: {v}", colour), text(X(v) + 11, y + 8, f"{v:.2f}", INK, 12.5)]
        y += step
    write("proof-average-box", bottom + 24, "Mean AUPRC on pneumonia for the average box and three models or methods",
          "Dot plot. RetinaNet 0.59, XRAI 0.52, average box 0.47, SIG 0.16.", body)


def wall_objects():
    wall, rows = 170, ["Gradient", "Model weights", "Sum under secure aggregation", "Part of a model", "Summary in a few components", "Score for each patient"]
    top, step = 62, 30
    bottom = top + step * len(rows) - 10
    body = [
        f'<rect x="8" y="{top - 22}" width="{wall - 40}" height="{bottom - top + 28}" rx="8" fill="var(--soft)"/>',
        text((8 + wall - 32) / 2, top + 58, "Hospital", INK, 14, "middle", 600), text((8 + wall - 32) / 2, top + 76, "patient records", MUTED, 12, "middle"), text((8 + wall - 32) / 2, top + 92, "stay here", MUTED, 12, "middle"),
        line(wall, 28, wall, bottom + 12, ACCENT, 3),
        dot(wall + 26, 16, "Published attack found", ACCENT, SURFACE, 6), text(wall + 38, 20, "attack found", MUTED, 12),
        dot(wall + 142, 16, "No attack found", SURFACE, MUTED, 5, 2), text(wall + 154, 20, "none found", MUTED, 12),
    ]
    y = top
    for row in rows:
        attacked = row != "Part of a model"
        body += [line(wall - 26, y, wall + 26, y, MUTED, 1.5), f'<path d="M{wall + 34} {y} l-9 -5 v10 z" fill="{MUTED}"/>',
                 dot(wall + 50, y, f"{row}: published attack found" if attacked else f"{row}: no attack found", ACCENT if attacked else SURFACE, SURFACE if attacked else MUTED, 6 if attacked else 5, 2),
                 text(wall + 66, y + 4, row)]
        y += step
    write("wall-objects", bottom + 22, "The six objects that can leave a hospital in federated learning",
          "Six arrows cross the hospital boundary: gradient, model weights, sum under secure aggregation, part of a model, summary in a few components and score for each patient. A published attack was found on all but part of a model.", body)


for make in (early_timeline, early_dumbbell, proof_dots, wall_objects):
    make()
