---
name: hw-integration-test
description: >
  Define and implement hardware integration tests against hardware architecture to validate that the hardware implementation correctly realizes it.
  Trigger: When hardware implementation is completed and hardware integration tests shall be defined and implemented.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## When to Use

- After hardware implementation is completed.
- When any hardware integration test activity is required.

## Critical Patterns

- Shall strictly follow the provided resources and recursively review all referenced documents required to understand the current process, inputs, outputs, rules and directly referenced work products.
- Shall align with hardware architecture (no inconsistencies).
- Shall ensure all hardware integration tests are derived from hardware architecture by adding explicit traceability between them.
- Shall define and implement the hardware integration tests against the hardware architecture to validate that the hardware implementation correctly realizes it.
- Shall use PySpice only when simulation-based validation is appropriate according to the defined process.
- Shall keep documentation DRY (Don't Repeat Yourself) by adding references instead of duplicating content.
- Shall ask for approval on key hardware integration test decisions.
- Shall request final validation before closing the hardware integration test to ensure no further iterations are needed.

## Resources

- **Documentation**: See [references/docs.md](references/docs.md) for resources needed to perform this skill.
