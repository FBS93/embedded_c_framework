# SKiDL guidelines

## Glossary

| Term | Definition |
|---|---|
| Component | SKiDL source file defining a single hardware component or circuit block. |
| Assembly | SKiDL source file defining the top-level hardware assembly interconnection of one or multiple components. |

## Code review criteria

### Python coding guidelines
---

All rules defined in the [Python coding guidelines](../../resources/python_coding_guidelines.md) shall apply unless explicitly overridden in this document.

All project-specific KiCad library work shall follow the [KiCad libraries for JLCPCB and LCSC](kicad_libraries_for_jlcpcb_lcsc.md).

---

### Naming conventions
---

Assembly file names shall match the assembly name in lower_snake_case format.

Example: `assembly_name.py`

---

Component file names shall match the component name in lower_snake_case format.

Example: `component_name.py`

---

The component builder function shall be named `build_component`.

---

Netlist export functions shall use lower_snake_case format and start with the prefix `export_`.

Examples: `export_netlist`, `export_svg`

---

Generated output file names shall use the source file name in lower_snake_case format.

Example: `source_file_name.net`

---

### File templates
---

Hardware assembly files shall:
- Define the top-level circuit definition for the assembly.
- Be the only entry point used to build the complete circuit.
- Import the component modules.
- Instantiate each component.
- Interconnect the exposed interfaces returned by each component.
- Define all inter-component connections explicitly.
- Not define component internal implementation details.

---

Hardware component files shall:
- Define all component-defining values explicitly in the `CONSTANTS` section.
- Define a component builder function named `build_component`.
- Define internal components and connectivity.
- Encapsulate internal implementation details.
- Expose only the external interfaces required for interconnection.
- Return a structured representation of external interfaces from `build_component` (for example, a dictionary of named nets or connection points).
- Not directly import and connect to other components.

---

Hardware test files shall:
- Define one or more test functions named with the `test_` prefix.
- Import the SKiDL circuit builder, simulation setup, or other required project-specific test inputs explicitly.
