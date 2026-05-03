# KiCad libraries for JLCPCB and LCSC

## Purpose

Define the common KiCad libraries and controlled intake workflow used by the hardware domain when working with [JLCPCB](https://jlcpcb.com/) and [LCSC](https://www.lcsc.com/) providers.

Using these libraries enables:
- PCB fabrication and assembly, or PCB fabrication without assembly, using [JLCPCB](https://jlcpcb.com/).
- Individual component procurement for manual assembly using [LCSC](https://www.lcsc.com/).

## Component selection criteria

Component selection shall follow the criteria below, ordered by priority:
- Complete component information, where applicable, including, for example:
  - Relevant component attributes
  - Datasheet and other documentation
  - Manufacturer part number
- Component availability.
- Price.

## Primary KiCad library

The primary KiCad library [CDFER/JLCPCB-Kicad-Library](https://github.com/CDFER/JLCPCB-Kicad-Library) shall be used by default for all components available in that library. This is a full KiCad library containing matched schematic symbols and PCB footprints, complete with 3D STEP models. In [EW](../../../ew.md), the synchronized library state is available under [tools/kicad_state/3rdparty/](../../../../tools/kicad_state/3rdparty/). This library is focused on components from JLCPCB basic and preferred parts lists, helping avoid extra setup costs.

Component selection shall apply the criteria described in [Component selection criteria](#component-selection-criteria).

The current methodology does not define a dedicated project-specific KiCad library format. Components obtained from [CDFER/JLCPCB-Kicad-Library](https://github.com/CDFER/JLCPCB-Kicad-Library) shall be used in the format provided by that source.

## Fallback KiCad library

When a required component is not available in the primary KiCad library, the fallback source shall be used to generate the corresponding KiCad library elements.

The fallback KiCad library is a custom library created with the [TousstNicolas/JLC2KiCad_lib](https://github.com/TousstNicolas/JLC2KiCad_lib) script. In [EW](../../../ew.md), the fallback library shall be located under [hw/kicad_lib/](../../../../hw/kicad_lib/). This script generates a component library (symbol, footprint and 3D model) for KiCad from the JLCPCB/EasyEDA library. This allows a minimal custom library to be defined for missing components while maintaining compatibility with [JLCPCB](https://jlcpcb.com/) and [LCSC](https://www.lcsc.com/) providers.

When the fallback library is used and the required component is not already available in that library and AI-assisted tooling is used for this work, the following controlled workflow shall be used:
1. AI-assisted tooling shall propose one or more candidate component references from the [JLCPCB parts library](https://jlcpcb.com/parts), including JLCPCB part numbers and links to the corresponding library entries. Component selection shall apply the criteria described in [Component selection criteria](#component-selection-criteria).
2. A human shall review the proposed candidates and select the exact component reference to be used, identified by the JLCPCB part number. The selection is not limited to the proposed candidates and may include any other valid component reference from [JLCPCB parts library](https://jlcpcb.com/parts).
3. After the human confirms the selected component, regardless of whether it was part of the proposed candidates, AI-assisted tooling shall execute the following checks in order, only up to the step needed:
  1. Check whether the selected component is available in the [Primary KiCad library](#primary-kicad-library). If available, use it and stop.
  2. If not available in the primary library, check whether it is already available in the fallback custom library. If available, use it and stop.
  3. If not available in either library, use `JLC2KiCadLib` command to generate and add the new component to the fallback custom library, then use that generated component. Example for component `C1337258`:

     ```bash
     JLC2KiCadLib C1337258 \
       -dir ${WORKSPACE_FOLDER}/hw/kicad_lib \
       -symbol_lib project_symbols \
       -symbol_lib_dir symbols \
       -footprint_lib footprints/project_footprints.pretty \
       -model_dir ../../3dmodels
     ```

The current methodology does not define a dedicated project-specific KiCad library format. Components obtained from [TousstNicolas/JLC2KiCad_lib](https://github.com/TousstNicolas/JLC2KiCad_lib) shall be used in the format provided by that source.
