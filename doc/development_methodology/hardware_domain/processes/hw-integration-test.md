# hw-integration-test

## Purpose

Define and implement hardware integration tests against hardware architecture to validate that the hardware implementation correctly realizes it.

## Input work products

- Hardware architecture
- Hardware implementation
- Tools

## Output work products

- Hardware integration test

## Steps

1. Review the hardware architecture.
2. Review available tools required to implement and execute hardware integration tests.
3. Identify hardware architecture elements requiring validation.
4. Define and implement the hardware integration tests.
5. Define traceability between hardware integration tests and the corresponding hardware architecture elements.
6. Check the hardware integration tests for completeness, consistency and correctness.

## Guidelines

### Hardware integration test work product

The hardware integration test work product shall follow the [Hardware test definition](../resources/hardware_test_definition.md).

In addition to the [Hardware test definition](../resources/hardware_test_definition.md), the hardware integration tests shall:
- Be derived from the hardware architecture to validate that the hardware implementation correctly realizes it.
- Use the hardware implementation only as the element under test.
- Define integration tests for individual hardware components when this is useful to validate relevant component properties.
- Define integration tests for hardware architecture interfaces between hardware components when needed to ensure that all relevant interconnections are validated, including interfaces within the same hardware assembly and between different hardware assemblies.
- Have a unique and well-defined objective. Multiple tests may be defined when required to validate the same hardware architecture element.

At the end of the hardware integration test process, it shall be ensured that all defined hardware architecture elements are as specified and that the complete hardware solution can be integrated consistently.
