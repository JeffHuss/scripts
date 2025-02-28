#!/bin/bash

# Exit on errors
set -e

# Ensure project name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <project-name>"
    exit 1
fi

PROJECT_NAME=$1
PROJECT_DIR=~/github_repos/scripts/python_labs/current_assignments  # Ensure new projects go here
TEMPLATE_DIR=~/github_repos/scripts/templates  # Path to setup.sh template

# Ensure the target directory exists
mkdir -p "$PROJECT_DIR"

# Create the new project inside the correct directory
mkdir "$PROJECT_DIR/$PROJECT_NAME"
cd "$PROJECT_DIR/$PROJECT_NAME"

# Copy setup.sh
cp "$TEMPLATE_DIR/setup.sh" .

# Create an empty requirements.txt
touch requirements.txt

echo "✅ Project '$PROJECT_NAME' created in $PROJECT_DIR/$PROJECT_NAME with setup.sh and requirements.txt."