# 6

def remove_repeated_characters():
    word = input("Enter a word: ")
    result = ""
    for char in word:
        if char not in result:
            result = result + char
    print("String after removing repeated characters:", result)

remove_repeated_characters()