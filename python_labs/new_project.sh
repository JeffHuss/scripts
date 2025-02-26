#!/bin/bash

# Exit on errors
set -e

# Ensure project name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <project-name>"
    exit 1
fi

PROJECT_NAME=$1
TEMPLATE_DIR=~/github_repos/scripts/templates  # Change this if needed

# Create project directory
mkdir "python_labs/$PROJECT_NAME" && cd "python_labs/$PROJECT_NAME"

# Copy setup.sh
cp "$TEMPLATE_DIR/setup.sh" .

# Create an empty requirements.txt
touch requirements.txt

echo "✅ Project '$PROJECT_NAME' created with setup.sh and requirements.txt."