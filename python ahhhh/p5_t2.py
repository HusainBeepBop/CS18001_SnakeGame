# 2

def binary_to_decimal():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    print("Decimal representation is", decimal)

binary_to_decimal()