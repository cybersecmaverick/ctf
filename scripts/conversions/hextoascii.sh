#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <hex_values_file.csv>"
    exit 1
fi

while IFS=, read -r hex; do
    printf "\\x${hex:2:2}"
done < "$1" | tr -d '\n'
