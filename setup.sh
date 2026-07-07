#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

echo "🚀 Starting project setup..."

# Ensure you are using the right Python from pyenv
PYTHON_VERSION="3.11.7"
echo "🔍 Checking Python version..."
if ! pyenv versions --bare | grep -q "$PYTHON_VERSION"; then
    echo "⚠️ Python $PYTHON_VERSION not found in pyenv. Installing..."
    pyenv install "$PYTHON_VERSION"
fi

echo "🐍 Using Python $PYTHON_VERSION"
#pyenv shell "$PYTHON_VERSION"
alias python='PYENV_VERSION=$PYTHON_VERSION python'

# Remove existing venv if exists (optional: safety check)
if [ -d "venv" ]; then
    echo "🧹 Removing existing venv..."
    rm -rf venv
fi

# Create a fresh virtual environment
echo "📦 Creating new virtual environment..."
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip and wheel
echo "⬆️ Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Install main requirements
if [ -f "requirements.txt" ]; then
    echo "📦 Installing main requirements..."
    pip install --force-reinstall -r requirements.txt
fi

# Install dev requirements
if [ -f "requirements-dev.txt" ]; then
    echo "🛠️ Installing development requirements..."
    pip install --force-reinstall -r requirements-dev.txt
fi

echo "🧪 Verifying test environment..."
which pytest
pytest --version || echo "⚠️ Pytest not installed correctly!"

echo "🎉 Setup complete! Virtual environment is ready."
echo "👉 To activate your environment, run: source venv/bin/activate"
echo "👉 To run tests, use: pytest"
echo "👉 To run pre-commit manually, use: pre-commit run --all-files"

