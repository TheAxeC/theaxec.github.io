# theaxec.github.com

This is my GitHub user page made with Jekyll and Bootstrap. The website functions as both a blog and a resume.

The website contains an overview of the projects I have made and my academic record. Occasionally I also blog about my experiences.

## Editing

Adding new content can be done by only changing:
- _data/data.yml [background information]
- _data/publications.yml [publication list]
- _data/website.yml [website specific data]
- _pages/ [main webpages]
- _blog/ [markdown posts]

(Projects shown on the site are generated from the `projects:` section of
`_data/data.yml`, not a `_projects/` collection.)

Publications are added into their respective folder:
- publications/abstracts/
- publications/conference/
- publications/journal/
- publications/other/
- publications/posters/
- publications/preprint/
- publications/thesis/

Other:
- _includes/ [for html includes (widgets) or general components (navbar and footer)
- _layouts/ [for the main html layouts (cv, default and posts)]
- assets/ [for css, images and js]
- _scripts/ [for python cv latex generator]

## Starting the server

`./run.sh` regenerates the CV PDF and then starts Jekyll. Extra args pass straight
through (e.g. `./run.sh --livereload --drafts`). Set `SKIP_CV=1` to skip the CV
step, or run Jekyll directly:

> bundle exec jekyll serve

## Running the CV Generator

> python _scripts/cv_pdf_generator.py --save --quiet

Flags: `--all` (default, full pipeline) / `--templates` / `--compile`; `--save`
copies the PDF to the home folder; `--quiet` suppresses LaTeX logs.