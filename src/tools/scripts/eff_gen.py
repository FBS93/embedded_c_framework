# ==============================================================================
# @brief Fake functions generator for Embedded Fake Framework.
#
# Usage:
#   python3 eff_gen.py -i <input_path> -o <output_path>
#
# Parameters:
#   -i Path to input header file or directory containing headers.
#   -o Path to output directory where generated files are stored.
#
# @copyright
# Copyright (c) 2026 FBS93.
# See the LICENSE file of this project for license details.
# This notice shall be retained in all copies or substantial portions
# of the software.
#
# @note
# This file is a derivative work based on:
# fff-mock-gen (c) Amcolex.
#
# @warning
# This software is provided "as is", without any express or implied warranty.
# The user assumes all responsibility for its use and any consequences.
# ==============================================================================
 
# ==============================================================================
# IMPORTS
# ==============================================================================

# ------------------------------------------------------------------------------
# External imports
# ------------------------------------------------------------------------------
import glob
import argparse
import re
from pathlib import Path
import shutil

# ------------------------------------------------------------------------------
# Project-specific imports
# ------------------------------------------------------------------------------

# ==============================================================================
# CONSTANTS
# ==============================================================================

# ==============================================================================
# CLASSES
# ==============================================================================

# ==============================================================================
# FUNCTIONS
# ==============================================================================

##
# @brief Fake functions generator.
#
# Parses command-line arguments, scans header files, and generates
# corresponding mock source and header files.
##
def main():
  # get arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', dest='headers_path', required=True)
  parser.add_argument('-o', dest='output_directory', required=True)
  args = parser.parse_args()

  # create full paths
  input_path = Path(args.headers_path).resolve()
  output_path = Path(args.output_directory).resolve()
  print('Input path:', input_path)
  print('Output path:', output_path)

  # find all .h files
  if input_path.is_file():
      header_files = [str(input_path)]
  elif input_path.is_dir():
      header_files = glob.glob(f'{input_path}/*.h')
  else:
      print(f'Input path {input_path} is not valid.')
      exit(1)
  print(f'Found {len(header_files)} header files')

  # if files list is empty return error
  if not header_files:
    print('No files found')
    exit(1)

  # delete output directory if it exists
  if output_path.exists():
    shutil.rmtree(output_path)

  # create output directory with all parent directories
  output_path.mkdir(parents=True)

  # create inc and src directories
  inc_path = output_path / 'inc'
  src_path = output_path / 'src'
  inc_path.mkdir()
  src_path.mkdir()

  # open each header file
  for file in header_files:
    f = open(file)

    # find all function prototypes
    function_prototypes = re.findall(r'''
        ^\s*                           # start of line, optional spaces
        ([\w\s\*\d_]+?)                # return type (group 1)
        \s+                            # at least one space
        (\w+)                          # function name (group 2)
        \s*                            # optional spaces
        \(                             # literal '('
            \s*                        # optional spaces
            ([^)]*)                    # arguments (group 3)
            \s*                        # optional spaces
        \)                             # literal ')'
        \s*;                           # semicolon
        ''', f.read(), re.MULTILINE | re.VERBOSE)

    # remove if contains 'typedef'
    function_prototypes = [x for x in function_prototypes if 'typedef' not in x[0]]

    print('Generating mocks for: ' + file)

    # extract return type, function name, and arguments from each function prototype using regex
    functions = []
    for function in function_prototypes:
      # extract return type
      return_type = function[0].strip()

      # extract function name
      function_name = function[1]

      # extract arguments
      arguments = function[2]
      # split arguments into list of tuples
      arguments = arguments.split(',')

      # Extract argument types, converting array declarations to pointers
      argument_types = []
      for argument in arguments:
        arg = argument.strip()
        if arg == '' or arg == 'void':
          argument_types.append('void')
        else:
          # Match: (base type) + (variable name) + (optional array brackets)
          match = re.match(r'(.+?)\s+([\w\d_]+)(\s*(\[[^\]]*\]\s*)*)$', arg)
          if match:
            base_type = match.group(1).strip()     # e.g., "float" or "const char *"
            brackets = match.group(3)              # e.g., "[3]" or "[2][4]", or empty
            if brackets:
              # Convert array to pointer: float arr[3] → float*
              pointer_type = base_type + ' *'
              argument_types.append(pointer_type.strip())
            else:
              # Not an array → just use the base type
              argument_types.append(base_type)
          else:
            # Fallback: try to remove the last word (variable name)
            parts = arg.split()
            if len(parts) >= 2:
              type_part = ' '.join(parts[:-1])
              argument_types.append(type_part)
            else:
              # Unusual case: use the whole argument string
              argument_types.append(arg)
    
      functions.append({'return_type': return_type, 'function_name': function_name, 'argument_types': argument_types})


    # create mock file .c and .h in inc and src
    mock_file_c = open(f'{output_path}/src/{Path(file).stem}_mock.c', 'w')
    mock_file_h = open(f'{output_path}/inc/{Path(file).stem}_mock.h', 'w')

    # write header to mock file .h
    mock_file_h.write('#pragma once\n')
    mock_file_h.write(f'#define FFF_GCC_FUNCTION_ATTRIBUTES __attribute__((weak))\n')
    mock_file_h.write(f'#include "{Path(file).name}"\n')
    mock_file_h.write(f'#include "eff.h"\n\n')
    # write mock function prototypes to mock file .h
    for function in functions:
      # if function returns void
      if function['return_type'] == 'void':
        # DECLARE_FAKE_VOID_FUNC(function_name)
        if function['argument_types'][0] == 'void':
          mock_file_h.write(f'DECLARE_FAKE_VOID_FUNC({function["function_name"]});\
          \n')
        else:
          mock_file_h.write(f'DECLARE_FAKE_VOID_FUNC({function["function_name"]}, {", ".join(function["argument_types"])});\
          \n')
      else:
        # DECLARE_FAKE_VALUE_FUNC(return_type, function_name, argument_types);
        # if function argument is void
        if function['argument_types'][0] == 'void':
          mock_file_h.write(f'DECLARE_FAKE_VALUE_FUNC({function["return_type"]}, {function["function_name"]});\
          \n')
        else:
          mock_file_h.write(f'DECLARE_FAKE_VALUE_FUNC({function["return_type"]}, {function["function_name"]}, {", ".join(function["argument_types"])});\
          \n')

    # write header to mock file .c
    mock_file_c.write(f'#include "{Path(file).stem}_mock.h"\n\n')

    # write mock function definitions to mock file .c
    for function in functions:
      # if function returns void
      if function['return_type'] == 'void':
        if function['argument_types'][0] == 'void':
          # DEFINE_FAKE_VOID_FUNC(function_name)
          mock_file_c.write(f'DEFINE_FAKE_VOID_FUNC({function["function_name"]});\
          \n')
        else:
          # DEFINE_FAKE_VOID_FUNC(function_name, argument_types)
          mock_file_c.write(f'DEFINE_FAKE_VOID_FUNC({function["function_name"]}, {", ".join(function["argument_types"])});\
          \n')

      else:                
        if function['argument_types'][0] == 'void':
          mock_file_c.write(f'DEFINE_FAKE_VALUE_FUNC({function["return_type"]}, {function["function_name"]});\
          \n')
        else:
          # DEFINE_FAKE_VALUE_FUNC(return_type, function_name, argument_types);
          mock_file_c.write(f'DEFINE_FAKE_VALUE_FUNC({function["return_type"]}, {function["function_name"]}, {", ".join(function["argument_types"])});\
          \n')

    
    # Convert snake_case module name to lowerCamelCase
    parts = Path(file).stem.split('_')
    module_name = parts[0] + ''.join(word.capitalize() for word in parts[1:])

    # Write resetAll function prototype
    mock_file_h.write(f'\nvoid EFF_{module_name}_ResetAll(void);\n')

    # Write resetAll function implementation
    mock_file_c.write(f'\nvoid EFF_{module_name}_ResetAll(void) {{\n')
    for function in functions:
        mock_file_c.write(f'  RESET_FAKE({function["function_name"]});\n')
    mock_file_c.write('}\n')

    # close mock file .c and .h
    mock_file_c.close()
    mock_file_h.close()

# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    main()
