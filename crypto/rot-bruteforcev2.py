# Date: 26-06-2023
# Author: CyberSecMaverick
#
# Description:
# =============
# This is a ROT-1 to ROT-25 (plus ROT-47) brute force script.
# If an argument is given, the first commandline argument should be a filename with the cipher text.The script will output all potential results in every ROT scheme to output.txt
# If no argument is given, the script will rpompt you to enter a string or a short ciper text tobe decoded.
#
# Usage:
# =======
# $ python3 ./rot-bruteforce.py
# $ python3 ./rot-bruteforce.py encryptedtext.txt

import sys


def rot_decode(cipher_text):
    if len(sys.argv) > 1:
        # If a file name is specified as a command line argument
        # Open the output file
        with open("output.txt", "w") as output_file:
            # Loop over all possible ROT values (1 to 25)
            for rot in range(1, 26):
                decoded_text = ""
                # Loop over each character in the cipher text
                for c in cipher_text:
                    # Check if the character is a letter
                    if c.isalpha():
                        # Determine the ASCII offset based on whether the letter is uppercase or lowercase
                        if c.isupper():
                            ascii_offset = 65
                        else:
                            ascii_offset = 97
                        # Convert the character to its ASCII code
                        c_code = ord(c)
                        # Determine the new ASCII code by applying the ROT value
                        new_c_code = (c_code - ascii_offset + rot) % 26 + ascii_offset
                        # Convert the new ASCII code back to a character
                        new_c = chr(new_c_code)
                        decoded_text += new_c
                    else:
                        # If the character is not a letter, add it to the decoded text as is
                        decoded_text += c
                # Write the decoded text for the current ROT value to the output file
                output_file.write(f"# ROT {rot:02d}\n{decoded_text}\n\n")

            # Apply ROT47
            decoded_text = ""
            for c in cipher_text:
                if 33 <= ord(c) <= 126:
                    new_c_code = (ord(c) - 33 + 47) % 94 + 33
                    new_c = chr(new_c_code)
                    decoded_text += new_c
                else:
                    decoded_text += c
            # Write the decoded text for ROT47 to the output file
            output_file.write(f"# ROT 47\n{decoded_text}\n")
    else:
        # Prompt the user to enter a word or sentence
        # Loop over all possible ROT values (1 to 25)
        for rot in range(1, 26):
            decoded_text = ""
            # Loop over each character in the cipher text
            for c in cipher_text:
                # Check if the character is a letter
                if c.isalpha():
                    # Determine the ASCII offset based on whether the letter is uppercase or lowercase
                    if c.isupper():
                        ascii_offset = 65
                    else:
                        ascii_offset = 97
                    # Convert the character to its ASCII code
                    c_code = ord(c)
                    # Determine the new ASCII code by applying the ROT value
                    new_c_code = (c_code - ascii_offset + rot) % 26 + ascii_offset
                    # Convert the new ASCII code back to a character
                    new_c = chr(new_c_code)
                    decoded_text += new_c
                else:
                    # If the character is not a letter, add it to the decoded text as is
                    decoded_text += c
            # Print the decoded text for the current ROT value
            print(f"ROT{rot:02d}   : {decoded_text}")

        # Add support for ROT47. A popular scheme used to support special characters.
        decoded_text = ""
        for c in cipher_text:
            if 33 <= ord(c) <= 126:
                new_c_code = (ord(c) - 33 + 47) % 94 + 33
                new_c = chr(new_c_code)
                decoded_text += new_c
            else:
                decoded_text += c
        # Print the decoded text for ROT47
        print(f"ROT47   : {decoded_text}")


if len(sys.argv) > 1:
    # If a file name is specified as a command line argument
    file_name = sys.argv[1]
    with open(file_name, "r") as input_file:
        cipher_text = input_file.read().strip()
        rot_decode(cipher_text)
else:
    # Prompt the user to enter a word or sentence
    cipher_text = input("Enter the cipher text: ").strip()
    rot_decode(cipher_text)
