#!/usr/bin/env python3

# ==============================================================================
# @brief Common helpers for KiCad state save/restore scripts.
#
# Shared logic used by the KiCad state tools located in:
# tools/kicad_state/
#
# Full tool documentation is defined in:
# tools/kicad_state/kicad_state.md
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
import shutil
from pathlib import Path

# ------------------------------------------------------------------------------
# External library imports
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# Project-specific imports
# ------------------------------------------------------------------------------

# ==============================================================================
# CONSTANTS
# ==============================================================================

CONFIG_FILE_NAMES = [
  "kicad_common.json",
  "sym-lib-table",
  "fp-lib-table",
  "user.hotkeys",
  "design-block-lib-table",
]

# ==============================================================================
# CLASSES
# ==============================================================================

# ==============================================================================
# FUNCTIONS
# ==============================================================================


##
# @brief Return the workspace-local KiCad state root.
#
# @return Absolute path to `tools/kicad_state/state`.
##
def get_state_root_dir():
  return Path(__file__).resolve().parent / "state"


##
# @brief Return the KiCad config root in the current user home.
#
# @return Absolute config root path.
##
def get_config_root():
  return Path.home() / ".config" / "kicad"


##
# @brief Return the KiCad share root in the current user home.
#
# @return Absolute share root path.
##
def get_share_root():
  return Path.home() / ".local" / "share" / "kicad"


##
# @brief Return detected KiCad versions from the config root.
#
# @return Sorted list of version strings.
##
def get_detected_versions():
  config_root = get_config_root()
  if not config_root.exists():
    return []

  return sorted(
    [path.name for path in config_root.iterdir() if path.is_dir()],
    key=parse_version_key,
  )


##
# @brief Convert a dotted version string into a sortable tuple.
#
# @param[in] version Version string.
# @return Tuple of integers for sorting.
##
def parse_version_key(version):
  return tuple(int(part) for part in version.split("."))


##
# @brief Remove a file or directory path when it exists.
#
# @param[in] path Path to remove.
##
def remove_path(path):
  if path.is_dir() and not path.is_symlink():
    shutil.rmtree(path)
  elif path.exists() or path.is_symlink():
    path.unlink()


##
# @brief Copy one optional file and remove the destination when absent.
#
# @param[in] source_file Source file path.
# @param[in] destination_file Destination file path.
##
def copy_optional_file(source_file, destination_file):
  if source_file.is_file():
    destination_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_file, destination_file)
  else:
    remove_path(destination_file)


##
# @brief Replace one directory tree from a source directory.
#
# @param[in] source_dir Source directory path.
# @param[in] destination_dir Destination directory path.
##
def replace_dir(source_dir, destination_dir):
  if destination_dir.exists():
    shutil.rmtree(destination_dir)

  shutil.copytree(
    source_dir,
    destination_dir,
    ignore=shutil.ignore_patterns(".gitkeep"),
  )
