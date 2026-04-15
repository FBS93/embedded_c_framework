#!/usr/bin/env python3

# ==============================================================================
# @brief Capture the current KiCad user state into the repository.
#
# This script saves the minimal KiCad user state into:
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
import sys
from pathlib import Path

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
from kicad_state_common import replace_dir
from kicad_state_common import remove_path

# ==============================================================================
# CONSTANTS
# ==============================================================================

EXTERNAL_LIBRARY_SUFFIXES = (
  ".kicad_sym",
  ".pretty",
  ".3dshapes",
  ".step",
  ".stp",
  ".wrl",
)

# ==============================================================================
# CLASSES
# ==============================================================================

# ==============================================================================
# FUNCTIONS
# ==============================================================================


##
# @brief Return the repository root.
#
# @return Absolute workspace root path.
##
def get_workspace_root():
  return Path(__file__).resolve().parents[2]


##
# @brief Detect the active KiCad version from the config directory.
#
# @return Version string such as `10.0`, or None when detection fails.
##
def detect_kicad_version():
  versions = get_detected_versions()
  if not versions:
    return None

  return versions[-1]


##
# @brief Create or remove `.gitkeep` depending on directory emptiness.
#
# @param[in] directory Directory to normalize.
##
def ensure_gitkeep_if_empty(directory):
  directory.mkdir(parents=True, exist_ok=True)
  gitkeep_path = directory / ".gitkeep"
  entries = [path for path in directory.iterdir() if path.name != ".gitkeep"]

  if entries:
    if gitkeep_path.exists():
      gitkeep_path.unlink()
  else:
    gitkeep_path.touch()


##
# @brief Copy one optional KiCad state directory into the repository.
#
# @param[in] source_dir Directory in the user profile.
# @param[in] state_dir Destination directory in the repository state.
##
def sync_dir(source_dir, state_dir):
  if source_dir.is_dir():
    replace_dir(source_dir, state_dir)
  else:
    remove_path(state_dir)
    state_dir.mkdir(parents=True, exist_ok=True)

  ensure_gitkeep_if_empty(state_dir)


##
# @brief Return absolute paths referenced from one KiCad table file.
#
# @param[in] table_file KiCad table file path.
# @return List of absolute path strings found in the file.
##
def extract_absolute_paths(table_file):
  if not table_file.is_file():
    return []

  return re.findall(r'"(/[^\"]+)"', table_file.read_text(encoding="utf-8"))


##
# @brief Warn when KiCad tables reference custom libraries outside the repo.
#
# @param[in] state_custom_libs_dir Repo-managed custom library directory.
# @param[in] table_files KiCad table files to inspect.
##
def warn_for_external_custom_libraries(state_custom_libs_dir, table_files):
  workspace_root = get_workspace_root().resolve()
  custom_libs_root = state_custom_libs_dir.resolve()
  detected_paths = []

  for table_file in table_files:
    for raw_path in extract_absolute_paths(table_file):
      if not any(
        raw_path.endswith(suffix) for suffix in EXTERNAL_LIBRARY_SUFFIXES
      ):
        continue

      resolved_path = Path(raw_path).resolve()
      if (
        workspace_root in resolved_path.parents
        or resolved_path == workspace_root
      ):
        continue
      if (
        custom_libs_root in resolved_path.parents
        or resolved_path == custom_libs_root
      ):
        continue
      detected_paths.append(raw_path)

  if not detected_paths:
    return

  print(
    "Warning: external KiCad libraries were detected outside the repository."
  )
  print(
    "Move or copy them into tools/kicad_state/state/<version>/custom-libraries and update the KiCad tables to point to repo-managed paths."
  )
  for detected_path in sorted(set(detected_paths)):
    print(f"  - {detected_path}")


##
# @brief Capture the current KiCad state into the repository.
##
def main():
  kicad_version = detect_kicad_version()
  if kicad_version is None:
    print(f"KiCad version could not be detected in {get_config_root()}.")
    return 1

  source_config_dir = get_config_root() / kicad_version
  source_share_dir = get_share_root() / kicad_version
  state_dir = get_state_root_dir() / kicad_version
  state_config_dir = state_dir / "config"
  state_plugins_dir = state_dir / "data" / "plugins"
  state_template_dir = state_dir / "data" / "template"
  state_custom_libs_dir = state_dir / "custom-libraries"

  state_config_dir.mkdir(parents=True, exist_ok=True)
  state_plugins_dir.mkdir(parents=True, exist_ok=True)
  state_template_dir.mkdir(parents=True, exist_ok=True)
  state_custom_libs_dir.mkdir(parents=True, exist_ok=True)

  for file_name in CONFIG_FILE_NAMES:
    copy_optional_file(
      source_config_dir / file_name, state_config_dir / file_name
    )

  sync_dir(source_config_dir / "colors", state_config_dir / "colors")
  sync_dir(source_share_dir / "plugins", state_plugins_dir)
  sync_dir(source_share_dir / "template", state_template_dir)
  ensure_gitkeep_if_empty(state_custom_libs_dir)
  ensure_gitkeep_if_empty(get_state_root_dir())

  warn_for_external_custom_libraries(
    state_custom_libs_dir,
    [
      source_config_dir / "sym-lib-table",
      source_config_dir / "fp-lib-table",
      source_config_dir / "design-block-lib-table",
    ],
  )

  print(f"KiCad state saved for version {kicad_version}.")
  return 0


# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
  sys.exit(main())
