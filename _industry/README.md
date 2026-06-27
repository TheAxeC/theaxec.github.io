# `_industry`, industry-focused CV + cover letter

A sibling to `_scripts/` (the academic CV pipeline). Same Awesome-CV engine and
`src/ -> _tmp/ -> xelatex` flow, but it renders an **industry**-tailored one/two-page
CV plus a matching cover letter, driven by a single data file with a profile switch.

## Build

```bash
cd _industry
python3 cv_pdf_generator.py --profile analyst --save   # Senior Data Analyst (Guerrilla Games)
python3 cv_pdf_generator.py --profile pharma  --save   # Biomedical / health data science
```

`--save` copies the PDFs to the repo root as `cv-industry-<profile>.pdf` and
`coverletter-<profile>.pdf`. Add `--templates` to render `.tex` without compiling,
`--quiet` to suppress LaTeX logs.

### One-page variant (`--compact`)

```bash
python3 cv_pdf_generator.py --profile analyst --compact --save
```

Produces a tightened single-page CV saved as `cv-industry-<profile>-onepage.pdf`
(the full CV and the cover letter are left untouched). Compact mode:

- drops any `skills` / `projects` / `awards` item marked `compact: false`;
- uses `about_compact` instead of `about` for an experience entry when present;
- uses `summary.text_compact` instead of `text` when present;
- tightens section / header vertical spacing.

So the one-pager is curated, not auto-truncated, choose what to drop by tagging
items in `industry.yml`.

## Where the content lives

All text is in **`../_data/industry.yml`**:

- `shared.personal`, name, photo, contact links (common to every profile).
- `profiles.<name>`, one block per target. Each supplies its own `titles`,
  `summary`, `skills`, `experience`, `projects`, `education`, `awards`, and a
  `letter` (recipient, date, title, opening, body, closing).

To add a new target (e.g. another studio or company), copy a profile block,
rename it, edit the text, and run with `--profile <name>`. Keep everything
**true to `data.yml`**, these go to real employers.

## Files

- `cv_pdf_generator.py`, reuses the `Template` engine from `../_scripts/`, selects
  the profile, builds the context, compiles CV (+ cover letter if the profile has one).
- `src/cv.tex.template` + `src/cv/*.template`, resume layout (summary, skills,
  experience, projects, education, awards).
- `src/coverletter.tex.template`, cover letter (Awesome-CV header + manual letter body).
- `src/awesome-cv.cls`, copy of the class, with a small `cvparagraph` environment
  added for the summary.
- `src/fonts/`, Roboto + FontAwesome (copied from `_scripts/src/fonts`).
