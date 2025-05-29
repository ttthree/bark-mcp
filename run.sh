#!/bin/bash
# Run bark-mcp using the conda environment

# Path to conda environment Python
PYTHON_BIN="/Users/jietong/miniconda3/envs/bark/bin/python"

# Run the module
$PYTHON_BIN -m bark_mcp.cli "$@"
