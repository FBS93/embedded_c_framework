#!/usr/bin/env bash
set -e

# Parse command-line arguments.
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 [WORKSPACE_ROOT]"
    exit 1
fi

workspace_root="$1"

# Validate workspace input.
if [ ! -d "${workspace_root}" ]; then
    echo "❌ Error: workspace directory not found: ${workspace_root}"
    exit 1
fi

# Validate required command.
if ! command -v python >/dev/null 2>&1; then
    echo "❌ Error: python not found."
    exit 1
fi

cd "${workspace_root}"

echo "💾 Saving KiCad state ..."
python3 "tools/kicad_state/save_kicad_state.py"
echo "✅ KiCad state saved."
