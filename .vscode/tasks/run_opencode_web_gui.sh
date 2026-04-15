#!/usr/bin/env bash
set -e

# Validate required command.
if ! command -v opencode >/dev/null 2>&1; then
    echo "❌ Error: opencode not found."
    exit 1
fi

HOSTNAME="0.0.0.0"
PORT="4096"

exec opencode web --hostname "${HOSTNAME}" --port "${PORT}"
