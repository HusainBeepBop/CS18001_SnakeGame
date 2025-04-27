# 8

def print_substrings_length_3():
    word = input("Enter a word: ")
    for i in range(len(word) - 2):
        print(word[i:i+3])
    
print_substrings_length_3()