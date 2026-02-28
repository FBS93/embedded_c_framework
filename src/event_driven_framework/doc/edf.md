# Event Driven Framework (EDF) overview

EDF is a lightweight, multi-platform base framework designed to run on both embedded systems and host environments. Its purpose is to provide:
- A structured event-driven architecture.
- Active Objects implemented as event consumers using Hierarchical State Machines (HSM) for scalable and maintainable application logic.
- A unified event management and dispatching mechanism based on a publish-subscribe model.
- Static event pools for deterministic and efficient memory management of mutable events.
- Deterministic real-time scheduling kernels.
- Configurable framework parametrization to adapt to resource-constrained systems.

All configuration options of this library are documented in the "EDF default configuration" section of [CMakeLists.txt](../../../CMakeLists.txt).

This framework is a derivative work based on:
- QP/C (c) Quantum Leaps, LLC.

# Glossary

| Term | Definition |
|------|------------|
| Active Object | Event-driven software component encapsulating behavior implemented as a HSM.|
| HSM | Hierarchical State Machine. |
| Publish-subscribe | Event distribution mechanism decoupling event producers from event consumers. |
| Event Pool | Section of static memory used for deterministic and safe sharing of mutable events. |
| Immutable Event | Read-only event instance that cannot be changed at runtime and can be safely shared without memory management. |
| Mutable Event | Event instance created at runtime whose payload is filled dynamically and managed through static event pools. |

# Usage example

@todo