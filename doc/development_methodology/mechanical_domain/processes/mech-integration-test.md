# mech-integration-test

## Purpose

Define and implement mechanical integration tests against mechanical architecture to validate that the mechanical implementation correctly realizes it.

## Input work products

- Mechanical architecture
- Mechanical implementation
- Tools

## Output work products

- Mechanical integration test

## Steps

1. Review the mechanical architecture.
2. Review available tools required to implement and execute mechanical integration tests.
3. Identify mechanical architecture elements requiring validation.
4. Define and implement the mechanical integration tests.
5. Define traceability between mechanical integration tests and the corresponding mechanical architecture elements.
6. Check the mechanical integration tests for completeness, consistency, and correctness.

## Guidelines

### Mechanical integration test work product

The mechanical integration test work product shall follow the [Mechanical test definition](../resources/mechanical_test_definition.md).

In addition to the [Mechanical test definition](../resources/mechanical_test_definition.md), the mechanical integration tests shall:
- Be derived from the mechanical architecture to validate that the mechanical implementation correctly realizes it.
- Use the mechanical implementation only as the element under test.
- Define integration tests for individual mechanical components when this is useful to validate relevant component properties.
- Define integration tests for mechanical architecture interfaces between mechanical components when needed to ensure that all relevant assembly points are validated.
- Have a unique and well-defined objective. Multiple tests may be defined when required to validate the same mechanical architecture element.

At the end of the mechanical integration test process, it shall be ensured that all defined mechanical architecture elements are as specified and that the complete mechanical solution can be assembled consistently.
