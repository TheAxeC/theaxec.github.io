#!/bin/bash
# Run the Python script
python _scripts/script.py --save --quiet

# If the Python script succeeds, start the Jekyll server
if [ $? -eq 0 ]; then
    echo "Python script completed successfully. Starting Jekyll server..."
    bundle exec jekyll serve
else
    echo "Python script failed. Jekyll server not started."
    exit 1
fi