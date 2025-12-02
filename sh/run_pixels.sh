#!/bin/bash

echo "start"

SHELLSCRIPT_PATH=$(realpath "$0")
PROJECT_ROOT=${SHELLSCRIPT_PATH%/*}/..
echo "$PROJECT_ROOT"

source $PROJECT_ROOT/.venv/bin/activate
sudo --preserve-env=PATH,VIRTUAL_ENV python3 $PROJECT_ROOT/app/pixels.py
