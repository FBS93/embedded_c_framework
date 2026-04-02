# mech-architecture

## Purpose

Define mechanical architecture from mechanical requirements.

## Input work products

- Mechanical requirements

## Output work products

- Mechanical architecture
- Mechanical-hardware interface

## Steps

1. Review the mechanical requirements.
2. Identify the mechanical architecture elements required to address the mechanical requirements.
3. Define the mechanical architecture based on the identified mechanical architecture elements.
4. Define traceability between mechanical architecture elements and mechanical requirements.
5. Check the mechanical architecture for completeness, consistency, and correctness.

## Guidelines

### Mechanical architecture work product

The mechanical architecture work product shall follow the [Architecture definition](../../resources/architecture_definition.md), except for:
- The mandatory dynamic views (sequence diagrams) defined in the [Architecture views](../../resources/architecture_definition.md#architecture-views) chapter.
- The architecture designs defined in the [Architecture designs](../../resources/architecture_definition.md#architecture-designs) chapter.

The mechanical architecture shall define the complete mechanical solution that satisfies all the mechanical requirements using architecture components, interfaces, and parameters.
- Each mechanical component shall represent a real part of the final mechanical assembly. 
- Mechanical interfaces shall define the physical couplings and interactions between parts. 
- Mechanical parameters shall define configurable or fixed values affecting the mechanical solution.

### Mechanical-hardware interface work product

The mechanical-hardware interface work product shall define all constraints from the mechanical domain that affect the hardware domain.

This shall include, when applicable:
- PCB outline constraints.
- Component allocation constraints.
- Connector accessibility constraints.
- Mounting constraints.
- Keep-out constraints.
- Thermal interface constraints.

@todo Specify the exact document format, document name and define whether this work product should be part of the mechanical architecture work product or a separate linked work product. All constraints defined here shall be traced from the mechanical architecture. Do the same in the Hardware domain.
