# theaxec.github.com

This is my GitHub user page made with Jekyll and Bootstrap. The website functions as both a blog and a resume.

The website contains an overview of the projects I have made and my academic record. Occasionally I also blog about my experiences.

## Editing

Adding new content can be done by only changing:
- _data/data.yml [background information]
- _data/publications.yml [publication list]
- _data/website.yml [website specific data]
- _pages/ [main webpages]
- _projects/ [markdown posts]
- _blog/ [markdown posts]

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
- _layout/ [for the main html layouts (cv, default and posts)]
- assets/ [for css, images and js]
- _scripts/ [for python cv latex generator]

## Starting the server

> bundle exec jekyll serve

## Running the CV Generator

> run generate.py in _scripts