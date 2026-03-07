#!/usr/bin/env bash
set -e

# Load and validate environment variables
: "${RPI_USER:?Missing RPI_USER}"
: "${RPI_HOST:?Missing RPI_HOST}"

echo "Connecting to ${RPI_USER}@${RPI_HOST}..."

exec ssh -o StrictHostKeyChecking=accept-new "${RPI_USER}@${RPI_HOST}"
