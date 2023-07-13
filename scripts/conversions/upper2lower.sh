#!/bin/bash

################################################################################
# Author: CyberSecMaverick
# Date: 11-07-2023
#
# Description: Converts the content of a file to all lowercase and displays it on stdout.
# Usage: ./upper2lower.sh <input file>
#
# Required Files:
#   - Input File: Specify the input file as a command-line argument when running the script.
#     Example: ./upper2lower.sh input.txt
#
# Output:
#   - The content of the input file converted to lowercase, displayed on stdout.
################################################################################

# Check if the input file is specified
if [ $# -eq 0 ]; then
  echo "Error: Input file not specified."
  echo "Usage: ./upper2lower.sh <input file>"
  exit 1
fi

input_file=$1

# Check if the input file exists
if [ ! -f "$input_file" ]; then
  echo "Error: Input file '$input_file' not found."
  exit 1
fi

# Convert the content to lowercase and display on stdout
tr '[:upper:]' '[:lower:]' < "$input_file"
