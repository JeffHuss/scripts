#!/bin/bash

# Exit if any command fails
set -e

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "✅ Dependencies installed."
else
    echo "⚠️ No requirements.txt found. Please install dependencies manually."
fi

echo "✅ Setup complete. To activate the environment, run: source venv/bin/activate"