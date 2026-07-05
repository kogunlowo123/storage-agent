#!/bin/bash
set -euo pipefail
echo "Setting up Storage Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
