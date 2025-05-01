# Take input from the user
words = input("Enter a set of words separated by spaces: ")

# Split the input string into a list of words
word_list = words.split()

# Find the longest word
longest_word = max(word_list, key=len)

# Print the result
print(f"The longest word is '{longest_word}' with length {len(longest_word)}.")

# -------------------------------------------------------------------------------

# Take input from the user
words = input("Enter a set of words separated by spaces: ")

# Split the input string into a list of words
word_list = words.split()

# Initialize variables to track the longest word and its length
longest_word = ""
max_length = 0

# Iterate through the list of words
for word in word_list:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

# Print the result
print(f"The longest word is '{longest_word}' with length {max_length}.")