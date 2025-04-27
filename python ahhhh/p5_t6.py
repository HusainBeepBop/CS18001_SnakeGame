# 6

def binary_to_octal():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    print("Octal representation is", octal)

binary_to_octal()