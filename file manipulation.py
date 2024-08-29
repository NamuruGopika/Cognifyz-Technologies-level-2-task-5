from collections import Counter
import re

def count_words_in_file(filename):
    # Open and read the file
    with open(filename, 'r') as file:
        text = file.read()
    
    # Use regular expressions to remove punctuation and make all words lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the occurrences of each word
    word_count = Counter(words)
    
    # Sort the words alphabetically and display the count
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

# Specify the filename
filename = 'python.txt'

# Call the function
count_words_in_file(filename)
