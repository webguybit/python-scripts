#!/bin/bash
# Launcher script for Interactive PDF Splitter
# This script activates the virtual environment and runs the interactive splitter

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

echo "🚀 Starting Interactive PDF Splitter..."
echo "   Project: $PROJECT_ROOT"
echo ""

# Activate virtual environment
if [ -d "$PROJECT_ROOT/env" ]; then
    source "$PROJECT_ROOT/env/bin/activate"
    echo "✅ Virtual environment activated"
else
    echo "❌ Virtual environment not found at $PROJECT_ROOT/env"
    exit 1
fi

# Run the interactive splitter
cd "$SCRIPT_DIR"
python interactive_splitter.py

# Deactivate when done
deactivate

