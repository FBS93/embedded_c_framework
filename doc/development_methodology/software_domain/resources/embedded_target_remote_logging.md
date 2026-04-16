# Embedded target remote logging

## Overview

This document describes how embedded target logging is performed remotely using a Raspberry Pi acting as a serial-to-TCP bridge.
A USB-to-serial adapter is connected between the target device and the Raspberry Pi, allowing serial peripheral output to be forwarded over the network.

## Architecture

- Embedded target outputs logs via serial peripheral.
- A USB-to-serial adapter connects the target to the Raspberry Pi.
- The Raspberry Pi runs a serial-to-TCP bridge.
- The host machine connects to the Raspberry Pi TCP port to receive logs.

Target serial interface --> USB-Serial Adapter --> Raspberry Pi --> TCP --> Host

## Logging Setup

Logging is enabled by executing [run_target_logging_server.sh](../../../../.vscode/tasks/run_target_logging_server.sh)

This script:
- Copies the script provided by the [run_target_logging_server tool](../../../../tools/run_target_logging_server/run_target_logging_server.md) to the Raspberry Pi.
- Connects to the Raspberry Pi via SSH.
- Selects the first available serial device.
- Reuses an already healthy running target logging server when available.
- If not, starts the script provided by the [run_target_logging_server tool](../../../../tools/run_target_logging_server/run_target_logging_server.md) on the Raspberry Pi with the selected serial device, configured TCP port and configured baud rate.
- Verifies that the target logging server is running.

The host can then connect to the configured TCP port to receive runtime logs.

## Dependencies

The Raspberry Pi must have Python 3 installed (default in Raspberry Pi OS).

Make sure that the environment variables in [devcontainer.json](../../../../.devcontainer/devcontainer.json) are configured for the logging setup and target environment:

- `RPI_USER` and `RPI_HOST` must match the Raspberry Pi SSH credentials.
- `LOG_PORT` must match the port used for serial logging.
- `LOG_BAUD_RATE` must match the target serial configuration.
- `NETWORK_LATENCY_TIMEOUT_S` defines the maximum wait time used by readiness checks for the logging server.
