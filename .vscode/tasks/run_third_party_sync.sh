#!/usr/bin/env bash
set -e

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 [WORKSPACE_ROOT]"
    exit 1
fi

workspace_root="$1"

cd "${workspace_root}"

echo "🔄 Synchronizing third-party repositories ..."
python "tools/third_party_sync/third_party_sync.py" --workspace "."
echo "✅ Third-party repositories synchronization completed."
