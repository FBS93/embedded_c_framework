# Embedded Fake Framework (EFF) overview

EFF is a lightweight, platform-agnostic fake functions framework designed to run on both embedded systems and host environments. Its purpose is to provide:
- Macro-based creation of fake functions for testing and validation.
- Fake functions autogeneration script.

The ECF framework provides CMake functions that encapsulate the usage of the autogeneration script. See [ECF cmake functions](../../tools/cmake/functions/ecf_mock.cmake)

This framework is a derivative work based on:
- fff (c) Meekrosoft.
- fff-mock-gen (c) Amcolex.

# Glossary

| Term | Definition |
|------|------------|
| Fake Function | Lightweight function replacement used to isolate code under test, control external dependencies, and monitor interactions. Used synonymously with Mock Function in the context of this library. |
| Mock Function | Lightweight function replacement used to isolate code under test, control external dependencies, and monitor interactions. Used synonymously with Fake Function in the context of this library. |

# Usage example

@todo