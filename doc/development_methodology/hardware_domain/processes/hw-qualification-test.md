# hw-qualification-test

## Purpose

Define and implement hardware qualification tests against hardware requirements to validate that the hardware architecture and hardware implementation correctly realize them.

## Input work products

- Hardware requirements
- Hardware architecture
- Hardware implementation
- Tools

## Output work products

- Hardware qualification test

## Steps

1. Review the hardware requirements.
2. Review available tools required to implement and execute hardware qualification tests.
3. Identify hardware requirements requiring validation.
4. Define and implement the hardware qualification tests.
5. Define traceability between hardware qualification tests and the corresponding hardware requirements.
6. Check the hardware qualification tests for completeness, consistency, and correctness.

## Guidelines

### Hardware qualification test work product

The hardware qualification test work product shall follow the [Hardware test definition](../resources/hardware_test_definition.md).

In addition to the [Hardware test definition](../resources/hardware_test_definition.md), the hardware qualification tests shall:
- Be derived from the hardware requirements to validate that the hardware architecture and hardware implementation correctly realize them.
- Use the hardware architecture as complementary input only to understand how the hardware solution is defined and to support test implementation.
- Use the hardware implementation only as the element under test.
- Define at least one qualification test for each hardware requirement, ensuring full coverage of all hardware requirements.
- Have a unique and well-defined objective. Multiple tests may be defined when required to validate different aspects of the same hardware requirement.
- Validate the hardware solution from an external perspective, without relying on internal implementation details.

At the end of the hardware qualification test process, it shall be ensured that all hardware requirements are validated by at least one hardware qualification test and that the complete hardware solution is as specified.
