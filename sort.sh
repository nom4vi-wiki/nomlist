#!/bin/bash

set -e -o pipefail

file_path="main.csv"

{
  head -n 1 "$file_path"
  tail -n +2 "$file_path" | LC_COLLATE=vi_VN.UTF-8 sort -f
} | sponge "$file_path"
