# mech-implementation

## Purpose

Implement the mechanical design from mechanical requirements and mechanical architecture.

## Input work products

- Mechanical requirements
- Mechanical architecture
- Tools

## Output work products

- Mechanical implementation
- Mechanical-hardware interface

## Steps

1. Review the mechanical requirements and mechanical architecture.
2. Review available tools required for the implementation.
3. Implement each mechanical component according to its mechanical architecture definition.
4. Ensure consistency between the implementation and the mechanical architecture and mechanical requirements.
5. Check the mechanical implementation for completeness, consistency, and correctness.
6. Define the mechanical-hardware interface according to the mechanical architecture and mechanical implementation.
7. Ensure consistency between mechanical-hardware interface, mechanical architecture and mechanical implementation.
8. Check the mechanical-hardware interface for completeness, consistency, and correctness.

## Guidelines

### Mechanical implementation work product

Each mechanical component shall be implemented strictly according to its mechanical architecture definition and shall not introduce additional constraints.

Mechanical requirements shall be used only as complementary input when the mechanical architecture does not fully define the mechanical component.

The implementation of each mechanical component shall:
- Be written in Python using [CadQuery](https://cadquery.readthedocs.io/).
- Follow the rules defined in [cadquery_guidelines.md](../resources/cadquery_guidelines.md).
- Be implemented in a single Python source file whose name matches the mechanical component name defined in the architecture, using lower_snake_case. This establishes an implicit 1:1 relationship between the mechanical component and its implementation.
- Realize the referenced mechanical interfaces and mechanical parameters only through the corresponding mechanical component implementation to which they are linked in the mechanical architecture.
- Generate all required exported files from the source files and never edit exported files manually.
- Use the mechanical component source file to generate the required CAD exchange files (`.step`), mesh export files (`.stl`), and 2D projection files (`.svg`) when applicable.

### Mechanical-hardware interface work product

The mechanical-hardware interface work product shall follow the [Cross-domain interface definition](../../resources/cross_domain_interface_definition.md).

The mechanical-hardware interface work product shall be defined using as input the traceable elements of the mechanical architecture and mechanical implementation that are relevant to the hardware domain.

The mechanical-hardware interface work product may include, for example, when applicable:
- PCB outline constraints.
- Component allocation constraints.
- Connector accessibility constraints.
- Thermal interface constraints.
