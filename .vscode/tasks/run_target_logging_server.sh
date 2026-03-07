#!/usr/bin/env bash
set -e

# -----------------------------------------------------------------------------
# This script automatically selects the FIRST device found in:
#   /dev/serial/by-id/
#
# If multiple USB/serial adapters are connected to the Raspberry Pi, this may
# select the wrong one. In that case, manual filtering must be added.
# -----------------------------------------------------------------------------

# Load and validate environment variables
: "${RPI_USER:?Missing RPI_USER}"
: "${RPI_HOST:?Missing RPI_HOST}"
: "${LOG_PORT:?Missing LOG_PORT}"
: "${LOG_BAUD_RATE:?Missing LOG_BAUD_RATE}"
: "${NETWORK_LATENCY_TIMEOUT:?Missing NETWORK_LATENCY_TIMEOUT}"
: "${WORKSPACE_FOLDER:?Missing WORKSPACE_FOLDER}"

# Local and remote file paths used to deploy and run the logging server.
LOCAL_SCRIPT="${WORKSPACE_FOLDER}/tools/scripts/run_target_logging_server.py"
REMOTE_SCRIPT="/tmp/run_target_logging_server.py"
REMOTE_LOG="/tmp/run_target_logging_server.log"

if [ ! -f "${LOCAL_SCRIPT}" ]; then
  echo "❌ Missing local script: ${LOCAL_SCRIPT}"
  exit 1
fi

# Copy target logging server script to Raspberry Pi (overwrite if exists).
scp -o StrictHostKeyChecking=accept-new "${LOCAL_SCRIPT}" "${RPI_USER}@${RPI_HOST}:${REMOTE_SCRIPT}" >/dev/null

ssh -o StrictHostKeyChecking=accept-new "${RPI_USER}@${RPI_HOST}" bash << EOF
set -e

# Find serial device.
SERIAL_NAME=\$(ls -1 /dev/serial/by-id/ 2>/dev/null | head -n1)
if [ -z "\$SERIAL_NAME" ]; then
    echo "❌ No USB serial device found."
    exit 1
fi

SERIAL_DEV="/dev/serial/by-id/\$SERIAL_NAME"
echo "USB serial device found: \$SERIAL_DEV."

# Reuse existing logging server when healthy and matching device/port.
if /usr/bin/ss -ltn | /usr/bin/grep -q ":$LOG_PORT" && \
   /usr/bin/pgrep -f "python3 ${REMOTE_SCRIPT} \${SERIAL_DEV} ${LOG_PORT} ${LOG_BAUD_RATE}" >/dev/null; then
    if bash -c "exec 9<>/dev/tcp/127.0.0.1/$LOG_PORT" 2>/dev/null; then
        exec 9>&-
        exec 9<&-
        echo "✅ Logging server already listening on port $LOG_PORT."
        exit 0
    fi
fi

# Stop stale instances before starting a fresh one.
if /usr/bin/ss -ltn | /usr/bin/grep -q ":$LOG_PORT"; then
    /usr/bin/fuser -k ${LOG_PORT}/tcp 2>/dev/null || true
fi
/usr/bin/pkill -f "python3 ${REMOTE_SCRIPT}" 2>/dev/null || true

# Start logging server.
nohup python3 "${REMOTE_SCRIPT}" "\${SERIAL_DEV}" "${LOG_PORT}" "${LOG_BAUD_RATE}" \
    > "${REMOTE_LOG}" 2>&1 &

# Wait for TCP port.
TIMEOUT_MS=\$(awk 'BEGIN { print int(${NETWORK_LATENCY_TIMEOUT} * 1000) }')
while true; do
    if /usr/bin/ss -ltn | /usr/bin/grep -q ":$LOG_PORT"; then
        echo "✅ Logging server ready on port $LOG_PORT."
        exit 0
    fi
    if [ "\$TIMEOUT_MS" -le 0 ]; then
        break
    fi
    /usr/bin/sleep 0.2
    TIMEOUT_MS=\$((TIMEOUT_MS - 200))
done

echo "❌ Logging server failed."
/usr/bin/tail -n 40 "${REMOTE_LOG}" || true
exit 1
EOF
