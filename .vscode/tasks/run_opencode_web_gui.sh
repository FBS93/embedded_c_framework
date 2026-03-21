#!/usr/bin/env bash
set -e

HOSTNAME="0.0.0.0"
PORT="4096"

exec opencode web --hostname "${HOSTNAME}" --port "${PORT}"