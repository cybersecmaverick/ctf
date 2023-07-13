#!/bin/bash

################################################################################
# Author: CyberSecMaverick
# Date:26-06-2023
#
# Description: Reads hexadecimal values from a CSV file and converts them to ASCII.
# Usage: ./hex2ascii.sh <hex_values_file.csv>
#
# Required Files:
#   - Hex Values File: Specify the hex values file as a command-line argument when running the script.
#     Example: ./hex2ascii.sh hex_values.csv
#
# Output:
#   - The ASCII representation of the hexadecimal values, displayed on stdout.
################################################################################

if [ $# -eq 0 ]; then
    echo "Usage: $0 <hex_values_file.csv>"
    exit 1
fi

# Read each line from the hex values file
while IFS=, read -r hex; do
    # Extract the hexadecimal value and convert it to ASCII
    printf "\\x${hex:2:2}"
done < "$1" | tr -d '\n'
