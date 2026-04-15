# kicad_state overview

`save_kicad_state.py` captures the minimal KiCad user state into `tools/kicad_state/state/<version>/`, and `setup_kicad_state.py` restores that versioned state into the devcontainer user profile.

# Glossary

| Term | Definition |
|---|---|
| | |

# Usage example

Restore the stored KiCad state into the devcontainer user profile:

```bash
python tools/kicad_state/setup_kicad_state.py
```

Capture the current KiCad state back into the repository:

```bash
python tools/kicad_state/save_kicad_state.py
```

Versioned state layout:

```text
tools/kicad_state/state/<version>/
├── config/
│   ├── kicad_common.json
│   ├── sym-lib-table
│   ├── fp-lib-table
│   ├── user.hotkeys
│   ├── design-block-lib-table
│   └── colors/
├── data/
│   ├── plugins/
│   └── template/
└── custom-libraries/
```

Behavior rules:

- `setup_kicad_state.py` restores only the versioned state already present under `tools/kicad_state/state/<version>/`.
- `save_kicad_state.py` captures only the minimal KiCad state intentionally tracked by the repository.
- `colors/`, `plugins/`, `template/`, and `custom-libraries/` contain `.gitkeep` only when otherwise empty.
- Caches, logs, backups, and temporary KiCad files are not versioned.
- `save_kicad_state.py` warns when KiCad library tables still reference custom libraries outside the repository.
