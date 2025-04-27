# 7

def print_substrings():
    word = input("Enter a word: ")
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            print(word[i:j])

print_substrings()