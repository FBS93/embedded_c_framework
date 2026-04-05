# mech-implementation

## Purpose

Implement the mechanical design from mechanical requirements and mechanical architecture.

## Input work products

- Mechanical requirements
- Mechanical architecture

## Output work products

- Mechanical implementation

## Steps

1. Review the mechanical requirements and mechanical architecture.
2. Implement each mechanical component according to its mechanical architecture definition.
3. Ensure consistency between the implementation and the mechanical architecture and mechanical requirements.
4. Check the mechanical implementation for completeness, consistency, and correctness.

## Guidelines

### Mechanical implementation work product

Each mechanical component shall be implemented strictly according to its mechanical architecture definition and shall not introduce additional constraints.

Mechanical requirements shall be used only as complementary input when the mechanical architecture does not fully define the mechanical component.

The implementation of each mechanical component shall:
- Be written in Python using [CadQuery](https://cadquery.readthedocs.io/).
- Follow the rules defined in [cadquery_guidelines.md](../resources/cadquery_guidelines.md).
- Be implemented in a single Python source file whose name matches the mechanical component name defined in the architecture, using lower_snake_case. This establishes an implicit 1:1 relationship between the mechanical component and its implementation.
- Realize the referenced mechanical interfaces and mechanical parameters only through the corresponding mechanical component to which they are linked in the mechanical architecture.
- Define all component-defining values explicitly in the `CONSTANTS` section and keep them separated from the geometry construction logic.
- Build geometry deterministically so that the same inputs always generate the same model and exports.
- Generate all required exported files from the source model instead of editing generated files manually.
- Generate the required CAD exchange files (`.step`), mesh export files (`.stl`), and 2D projection files (`.svg`) when applicable.
