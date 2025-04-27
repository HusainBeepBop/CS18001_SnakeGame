# 9

def print_long_strings():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    for string in strings:
        if len(string) >= 3:
            print(string)

print_long_strings()