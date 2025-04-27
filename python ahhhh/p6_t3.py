# 3

def print_left_of_vowels():
    string = "Hello World"
    vowels = "aeiouAEIOU"
    for i in range(1, len(string)):
        if string[i] in vowels:
            print("Character to the left of", string[i], "is", string[i - 1])

print_left_of_vowels()