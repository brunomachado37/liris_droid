#!/bin/bash

# activate conda
source ~/miniconda3/bin/activate
conda activate polymetis

# run user command
exec "$@"
