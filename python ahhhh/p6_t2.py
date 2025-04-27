# 2

def print_vowel_indices():
    string = "Hello World"
    vowels = "aeiouAEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            print("Vowel", string[i], "at index", i)

print_vowel_indices()