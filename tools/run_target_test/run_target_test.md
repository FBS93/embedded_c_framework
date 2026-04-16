# Run target test overview

`run_target_test.py` automates remote Hardware-in-the-Loop target execution by flashing a test binary through GDB, enabling remote logging, running the firmware, and translating the observed result into a process exit code suitable for `CTest`.

It works as follows:
- Starting GDB server on a remote Raspberry Pi.
- Flashing firmware via the GDB server.
- Starting a serial-to-TCP bridge.
- Running the target firmware.
- Capturing serial output.
- Reporting PASS/FAIL.

# Glossary

| Term | Definition |
|---|---|
|   |   |

# Usage example

Run one target test binary manually after exporting the required environment variables:

```bash
python tools/run_target_test/run_target_test.py build/target/example_test
```
