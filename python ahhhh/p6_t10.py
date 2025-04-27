# 10

def sort_strings_by_length():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    strings.sort(key=len)
    print("Strings sorted by length:", strings)

sort_strings_by_length()