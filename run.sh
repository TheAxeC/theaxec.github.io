#!/bin/bash
set -euo pipefail

# Always run from the repo root, regardless of where this is invoked from.
cd "$(dirname "$0")"

# Regenerate the CV PDF unless SKIP_CV=1 (handy for fast Jekyll-only restarts).
if [ "${SKIP_CV:-0}" != "1" ]; then
    echo "Generating CV PDF..."
    python _scripts/cv_pdf_generator.py --save --quiet
    echo "CV PDF generated."
fi

# Live reload on by default: the browser refreshes automatically on any change.
# Extra args ($@) pass straight through, e.g. ./run.sh --drafts
echo "Starting Jekyll server (live reload)..."
exec bundle exec jekyll serve --livereload --open-url "$@"
