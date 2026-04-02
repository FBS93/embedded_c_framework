See [Embedded C Workbench documentation](doc/ecw.md) for the base template documentation used by this project.


xxxyyy nomes fer referencia a ECW pero en doc de ECW s'ha de fer referencia a ECF

xxxyyy desde ecw fer referencia a development methology + + skills ia que s'ha afegti ultimament pq quedi tot linkat a nivell documental

See [Embedded C Framework documentation](sw/ecf/doc/ecf.md) for project-specific documentation.

@todo Add a concise getting-started guide covering devcontainer setup, build, test, debug, and daily workflow.

@todo Document the practical usage of all CMake presets, including host/target variants and hard_debug behavior.

@todo Document the meaning and effect of build configuration variables such as ECF_TEST, EBF_CORE, EBF_PORT, and ECF_TARGET_PLATFORM.

@todo Document the official VS Code workflow, including tasks, task buttons, launch configurations, and expected extensions.

@todo Document the platform integration pattern based on platform.cmake and ect_add_executable().

@todo Document the CMake test and mock helper functions and the expected way to register tests and generate mocks.

@todo Document the source formatting workflow, including clang-format, asm_format.py, format.sh, and format-on-save behavior.

@todo Document all user-facing devcontainer environment variables, including which ones are required and which workflows depend on them.

@todo Document the exact HiL test runner contract, including expected serial output patterns, timeout behavior, and hardware resource locking.

@todo Document the current lab assumptions and hardware-specific defaults, including J-Link GDB server settings and serial device auto-selection behavior.

@todo Document the expected dual-target usage model and clarify the distinction between host/SiL and target/HiL workflows.

@todo Document that several core workflows depend on a Raspberry Pi gateway and explain when it is required.

@todo Document that this repository assumes a specific reference hardware setup and explain how to adapt it to a different target.

@todo Document the practical day-to-day application of the V-model workflow used by this repository.
