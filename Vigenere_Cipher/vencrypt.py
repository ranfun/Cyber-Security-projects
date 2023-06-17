import sys
import re

# Encryption function using Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_len = len(key)
    key_idx = 0
    for word in re.findall(r'\b[a-z]+\b', plaintext):
        for letter in word:
            shift = ord(key[key_idx]) - ord('a')
            ciphertext += chr((ord(letter) + shift - ord('a')) % 26 + ord('a'))
            key_idx = (key_idx + 1) % key_len
        ciphertext += ' '
    return ciphertext.strip()

# Check if correct number of command line arguments is passed
if len(sys.argv) != 4:
    print("Usage: python vencrypt.py plaintext_file ciphertext_file key")
    sys.exit()

# Read plaintext from input file
plaintext_file = sys.argv[1]
with open(plaintext_file, 'r') as f:
    plaintext = f.read()

# Read key from command line argument
key = sys.argv[3]

# Encrypt plaintext using Vigenere Cipher
ciphertext = vigenere_encrypt(plaintext, key)

# Write ciphertext to output file
ciphertext_file = sys.argv[2]
with open(ciphertext_file, 'w') as f:
    f.write(ciphertext)