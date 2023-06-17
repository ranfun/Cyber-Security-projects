import sys

# Decryption function using Vigenere Cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = ''
    key_len = len(key)
    key_idx = 0
    for word in ciphertext.split():
        for letter in word:
            shift = ord(key[key_idx]) - ord('a')
            plaintext += chr((ord(letter) - shift - ord('a')) % 26 + ord('a'))
            key_idx = (key_idx + 1) % key_len
        plaintext += ' '
    return plaintext.strip()

# Check if correct number of command line arguments is passed
if len(sys.argv) != 4:
    print("Usage: python vdecrypt.py ciphertext_file plaintext_file key")
    sys.exit()
    
# Read key from command line argument
key = sys.argv[3]

# Read plaintext from input file
ciphertext_file = sys.argv[1]
with open(ciphertext_file, 'r') as f:
    ciphertext = f.read()

# Decrypt ciphertext using Vigenere Cipher
decrypted_plaintext = vigenere_decrypt(ciphertext, key)

# Write ciphertext to output file
decrypted_text_file = sys.argv[2]
with open(decrypted_text_file, 'w') as f:
    f.write(decrypted_plaintext)