# 4

def check_palindrome():
    word = input("Enter a word: ")
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            print(word, "is not a palindrome")
            return
        i = i + 1
        j = j - 1
    print(word, "is a palindrome")

check_palindrome()