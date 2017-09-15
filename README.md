# theaxec.github.com

This is my GitHub user page made with Jekyll and Bootstrap. The website functions as both a blog and a resume.

The website contains an overview of the projects I have made and my academic record. Occasionally I also blog about my experiences as a grad student at KULeuven.

The script `add_static_plugin.sh` is used to copy the generated files from the plugins to the root directory.
This is required since Github does not run these plugins.

## Editing

Adding new content can be done by only changing:
- _data/
- _news/
- _posts/
- _pages/
- _rss/

Publications are added into their respective folder:
- _abstracts/
- _conference/
- _journal/
- _posters/
- _thesis/

Content can be added using:
- _data/awards.yml for any honors and awards
- _data/education.yml for educational achievements
- _data/projects.yml for completed projects
- _data/experience.yml for work or research experience
- _data/publications.yml for publications
- _data/description.yml for any personal information
- _data/references.yml for contact information
- _data/research.yml for research topics
- _rss/atom.xml for the rss feed (automatically takes posts)
- _news/ for any upcoming events
- _posts/ for any blog posts
- _pages/ for any new pages

Other:
- _includes/ for html layouts of specific parts (navigation, footer, head)
- _layout/ for the main layouts
- _plugins/ for ruby scripts
- category/
- tags/
- res/css/
- res/img/
- res/js/
