# Set stdio library, startup file and linker file for all executables.
set(ECT_GLOBAL_LIBS stdio)
set(ECT_STARTUP_FILES ${CMAKE_CURRENT_LIST_DIR}/../startup/startup.S)
set(ECT_LINKER_FILES ${CMAKE_CURRENT_LIST_DIR}/../linker/linker.ld)

# Set target platform compiler options.
add_compile_options(
    -mcpu=cortex-m3
)

# Set target platform linker options.
add_link_options(
    -mcpu=cortex-m3
)