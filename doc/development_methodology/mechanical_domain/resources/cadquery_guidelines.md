# CadQuery guidelines

## Glossary

| Term | Definition |
|---|---|
| Component | CadQuery source file defining a single geometric component. |

## Code review criteria

### Python coding guidelines
---

All rules defined in the [Python coding guidelines](../../resources/python_coding_guidelines.md) shall apply unless explicitly overridden in this document.

---

### Naming conventions
---

Component file names shall match the component name in lower_snake_case format.

Example: `component_name.py`

---

The component builder function shall be named `build_component`.

---

The preview function shall be named `preview_component`.

---

Export functions shall use lower_snake_case format and start with the prefix `export_`.

Examples: `export_stl`, `export_step`, `export_svg`

---

Exported file names shall use the source file name in lower_snake_case format.

Example: `source_file_name.stl`

---

### File templates
---

Mechanical component files shall:
- Define all component-defining values explicitly in the `CONSTANTS` section and keep them separated from the geometry construction logic.
- Define a component builder function named `build_component`.
- Define one or more export functions named using the `export_` prefix when exported files are required.
- Define a preview function named `preview_component` when direct preview support is needed.

---

Mechanical test files shall:
- Define one or more test functions named with the `test_` prefix.
- Import the component geometry builder or other required project-specific test inputs explicitly.
