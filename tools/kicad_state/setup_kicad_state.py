#!/usr/bin/env python3

# ==============================================================================
# @brief Restore versioned KiCad state into the devcontainer user profile.
#
# This script restores the minimal KiCad user state stored in:
# tools/kicad_state/state/<version>/
#
# @copyright
# Copyright (c) 2026 FBS93.
# See the LICENSE file of this project for license details.
# This notice shall be retained in all copies or substantial portions
# of the software.
#
# @warning
# This software is provided "as is", without any express or implied warranty.
# The user assumes all responsibility for its use and any consequences.
# ==============================================================================

# ==============================================================================
# IMPORTS
# ==============================================================================

# ------------------------------------------------------------------------------
# Standard library imports
# ------------------------------------------------------------------------------
import re
import subprocess
import sys

# ------------------------------------------------------------------------------
# External library imports
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Project-specific imports
# ------------------------------------------------------------------------------
from kicad_state_common import CONFIG_FILE_NAMES
from kicad_state_common import copy_optional_file
from kicad_state_common import get_config_root
from kicad_state_common import get_detected_versions
from kicad_state_common import get_share_root
from kicad_state_common import get_state_root_dir
from kicad_state_common import remove_path
from kicad_state_common import replace_dir

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
# @brief Detect the active KiCad major.minor version.
#
# @return Version string such as `10.0`, or None when detection fails.
##
def detect_kicad_version():
  versions = get_detected_versions()
  if versions:
    return versions[-1]

  try:
    result = subprocess.run(
      ["kicad", "--version"],
      check=True,
      capture_output=True,
      text=True,
    )
  except (OSError, subprocess.CalledProcessError):
    return None

  match = re.search(r"(\d+\.\d+)", result.stdout)
  if match is None:
    return None

  return match.group(1)


##
# @brief Copy one optional state directory into the KiCad profile.
#
# @param[in] source_dir Directory in the versioned state.
# @param[in] target_dir Destination directory in the user profile.
##
def restore_dir(source_dir, target_dir):
  if source_dir.is_dir():
    target_dir.parent.mkdir(parents=True, exist_ok=True)
    replace_dir(source_dir, target_dir)
  else:
    remove_path(target_dir)


##
# @brief Restore the versioned KiCad state when available.
##
def main():
  kicad_version = detect_kicad_version()
  if kicad_version is None:
    print("KiCad version could not be detected. Skipping KiCad state restore.")
    return 0

  state_dir = get_state_root_dir() / kicad_version
  if not state_dir.is_dir():
    print(
      f"No KiCad state stored for version {kicad_version}. Skipping KiCad state restore."
    )
    return 0

  target_config_dir = get_config_root() / kicad_version
  target_share_dir = get_share_root() / kicad_version
  state_config_dir = state_dir / "config"
  state_plugins_dir = state_dir / "data" / "plugins"
  state_template_dir = state_dir / "data" / "template"

  target_config_dir.mkdir(parents=True, exist_ok=True)
  target_share_dir.mkdir(parents=True, exist_ok=True)

  for file_name in CONFIG_FILE_NAMES:
    copy_optional_file(
      state_config_dir / file_name, target_config_dir / file_name
    )

  restore_dir(state_config_dir / "colors", target_config_dir / "colors")
  restore_dir(state_plugins_dir, target_share_dir / "plugins")
  restore_dir(state_template_dir, target_share_dir / "template")

  print(f"KiCad state restored for version {kicad_version}.")
  return 0


# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
  sys.exit(main())
