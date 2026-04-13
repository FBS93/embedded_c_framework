# Repository sync workflow

## Overview

This document describes the GitHub Actions workflow that automates third-party repository synchronization.

The workflow definition is implemented in [../../.github/workflows/repo_sync.yml](../../.github/workflows/repo_sync.yml). The underlying synchronization script is documented in [../../tools/repo_sync/repo_sync.md](../../tools/repo_sync/repo_sync.md).

## Prerequisites

The `repo_sync.yml` workflow creates branches and pull requests automatically. To allow this behavior, apply the following settings in the GitHub repository:

- `Settings > Actions > General > Workflow permissions > Read and write permissions`
- `Settings > Actions > General > Workflow permissions > Allow GitHub Actions to create and approve pull requests`
