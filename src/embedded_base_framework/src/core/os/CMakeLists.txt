if((EBF_PORT STREQUAL "EBF_PORT_POSIX_NON_PREEMPTIVE") OR
   (EBF_PORT STREQUAL "EBF_PORT_POSIX_PREEMPTIVE"))
    add_subdirectory(posix)
else()
    message(FATAL_ERROR "Invalid EBF_PORT value: ${EBF_PORT}")
endif()