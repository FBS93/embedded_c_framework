# Sigrok remote client overview

`sigrok_remote_client.py` provides a minimal Python wrapper that runs `sigrok-cli` on the Raspberry Pi and stores fetched capture artifacts under the configured local logic analyzer artifacts directory.

It works as follows:
- Loading the Raspberry Pi SSH settings and logic analyzer configuration from the environment variables.
- Running `sigrok-cli` on the Raspberry Pi with the configured `LOGIC_ANALYZER_DEVICE` selector.
- Fetching one or more remote capture artifacts into `LOGIC_ANALYZER_ARTIFACTS_DIR/<capture_name>/`.

# Glossary

| Term | Definition |
|---|---|
| `.sr` capture | Sigrok session file that stores one logic analyzer capture. |
| `sigrok-cli` | Command-line tool used to control capture and export operations of the logic analyzer. |
| PulseView | Sigrok graphical viewer used to inspect `.sr` captures interactively. |

# Usage example

Run one remote capture and fetch the resulting `.sr` file into the configured local artifacts directory:

```python
from tools.sigrok_remote_client import SigrokRemoteClient

client = SigrokRemoteClient()
remote_capture = "/tmp/example_test.sr"

client.run(
  "--config", "<config>",
  "--output-file", remote_capture,
)

local_capture = client.fetch_artifact(
  "example_test",
  remote_capture,
)

print(local_capture)
```
