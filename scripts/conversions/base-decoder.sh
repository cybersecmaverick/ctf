#!/bin/bash

################################################################################
# Date: 21-06-2023
# Author: CyberSecMaverick
#
# Description:
# This bash script takes an input from the user and attempts to decode it using Base32, Base64, and Base58 encoding schemes.
# These encoding schemes are commonly used in various CTF challenges.
#
# Usage:
# 0. Ensure you have the tools installed for base32, base64, base58 (coreutils, basez, base58 on Debian)
# 1. Make sure the script is executable by running: chmod +x base-decoder.sh
# 2. Run the script using: ./base-decoder.sh
# 3. Enter the encoded string when prompted.
################################################################################

# Check if the required binaries are available
check_binaries() {
  local missing_binaries=()
  for binary in base32 base58 base64; do
    if ! command -v "$binary" >/dev/null 2>&1; then
      missing_binaries+=("$binary")
    fi
  done

  if [[ ${#missing_binaries[@]} -gt 0 ]]; then
	echo
    echo "WARNING! The following required tools are missing: ${missing_binaries[*]}"
	echo
  fi
}

# Read input string from the command prompt
read -p "Enter the encoded string: " encoded_string

# Display the original string
echo
echo "Original String: $encoded_string"
echo

# Check if the required binaries are available
check_binaries

# Decode using base32
decoded_base32=$(echo "$encoded_string" | base32 -d)
if [[ -n "$decoded_base32" ]]; then
  echo "Decoded (Base32): $decoded_base32"
fi

echo

# Decode using base58
decoded_base58=$(echo "$encoded_string" | base58 -d)
if [[ -n "$decoded_base58" ]]; then
  echo "Decoded (Base58): $decoded_base58"
fi


echo

# Decode using base64
decoded_base64=$(echo "$encoded_string" | base64 -d)
if [[ -n "$decoded_base64" ]]; then
  echo "Decoded (Base64): $decoded_base64"
fi

echo
