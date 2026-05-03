# hw-architecture

## Purpose

Define hardware architecture from hardware requirements.

## Input work products

- Hardware requirements

## Output work products

- Hardware architecture

## Steps

1. Review the hardware requirements.
2. Identify the hardware architecture elements required to address the hardware requirements.
3. Define the hardware architecture based on the identified hardware architecture elements.
4. Define traceability between hardware architecture elements and hardware requirements.
5. Check the hardware architecture for completeness, consistency and correctness.

## Guidelines

### Hardware architecture work product

The hardware architecture work product shall follow the [Architecture definition](../../resources/architecture_definition.md), except for:
- The mandatory dynamic views (sequence diagrams) defined in the [Architecture views](../../resources/architecture_definition.md#architecture-views) chapter.

The hardware architecture shall define the complete hardware solution that satisfies all the hardware requirements using architecture components, interfaces, parameters and designs.
- Each hardware component shall represent an indivisible functional or logical hardware block of the final hardware solution.
- Hardware interfaces shall define the electrical or logical interactions between hardware components and external elements.
- Hardware parameters shall define values affecting the hardware solution.
- Hardware designs shall define architectural decisions that are not represented as hardware components, hardware interfaces, or hardware parameters.

The mandatory static view using a component diagram shall represent the hardware solution as simple hardware components and their interfaces.

#### Hardware assemblies

Hardware assemblies shall be defined as hardware designs.

The hardware design defining a hardware assembly shall contain:
- A description of the hardware assembly with the following information:
  - A clear and concise description defining the hardware assembly, including its purpose, the functionality it provides and the rationale for its physical grouping.
  - Whether the hardware assembly represents a PCB, an interconnected set of components without a PCB, or any other type of physical grouping.
- Hardware components assigned to the hardware assembly. This shall be defined as a list of Markdown links referencing the corresponding hardware components. 
  - Each hardware component shall be referenced by exactly one hardware assembly.

The following template shall be used for the description of this hardware design:

```md
<Hardware assembly description>.

Hardware components:
- [<HW_ARCH_COMPONENT_X>](#...)
```
