import re
import sys

def find_repeating_word(words):
    max_repeats = 0
    max_word = None

    for word in words:
        letter_count = {}
        repeats = 0

        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
                if letter_count[letter] == 2:
                    repeats += 1
            else:
                letter_count[letter] = 1

        if repeats > max_repeats:
            max_repeats = repeats
            max_word = word

    return max_word

    
# Function to find the key from a hint word and ciphertext
def crack_vigenere(ciphertext, hint_word):
    # Convert the hint word to lowercase
    hint_word = hint_word.lower()

    # Use regular expressions to extract all words from the ciphertext
    words = re.findall(r'\b[a-zA-Z]+\b', ciphertext)

    # Find the positions of words in the ciphertext that have the same length as the hint word
    word_positions = [i for i in range(len(words)) if len(words[i]) == len(hint_word)]
    global keys
    keys=[]
    # Loop over the positions of words in the ciphertext that have the same length as the hint word
    for i in word_positions:
        # Loop over the characters of the hint word and the corresponding characters of the ciphertext
        key = []
        for j in range(len(hint_word)):
            # Find the shift between the hint word character and the corresponding ciphertext character
            shift = ord(words[i][j]) - ord(hint_word[j])

            # Append the key character that corresponds to this shift
            key.append(chr((shift % 26) + ord('a')))
        
        # Try to decrypt the ciphertext using the key
        decrypted_text = decrypt_vigenere(ciphertext, ''.join(key))
        keys.append(''.join(key))

# Function to decrypt a Vigenere ciphertext using a key
def decrypt_vigenere(ciphertext, key):
    # Convert the key to lowercase
    key = key.lower()

    # Use regular expressions to extract all words from the ciphertext
    words = re.findall(r'\b[a-zA-Z]+\b', ciphertext)

    # Loop over the words in the ciphertext
    decrypted_words = []
    for i in range(len(words)):
        # Loop over the characters in the word and the corresponding characters in the key
        decrypted_word = []
        for j in range(len(words[i])):
            # Find the shift between the ciphertext character and the corresponding key character
            shift = ord(words[i][j]) - ord(key[j % len(key)])

            # Append the decrypted character that corresponds to this shift
            decrypted_word.append(chr((shift % 26) + ord('a')))

        # Append the decrypted word to the list of decrypted words
        decrypted_words.append(''.join(decrypted_word))

    # Join the decrypted words into a string and return it
    return ' '.join(decrypted_words)

# Parse command-line arguments
if len(sys.argv) != 3:
    print('Usage: python vcrack.py <ciphertext_file> <hint_word>')
    sys.exit(1)
ciphertext_file = sys.argv[1]
hint_word = sys.argv[2]

# Read the ciphertext from the file
with open(ciphertext_file, 'r') as f:
    ciphertext = f.read().strip()

# Crack the Vigenere cipher and print the key
crack_vigenere(ciphertext, hint_word)
answer=find_repeating_word(keys)
print("Possible keys are: {}".format(keys))
print("The key is most likely: {}".format(answer))