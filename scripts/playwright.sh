#!/bin/bash
set -euo pipefail

# Check if Playwright is installed
if ! command -v playwright &>/dev/null; then
  echo "Error: Playwright is not installed. Please install it before running this script."
  exit 1
fi

echo "Installing Playwright dependencies..."
playwright install-deps

echo "Installing Chromium browser..."
playwright install chromium

echo "Installation complete!"
