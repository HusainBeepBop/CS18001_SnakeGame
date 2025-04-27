# 8

def binary_to_decimal_for():
    binary = input("Enter a binary number: ")
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal * 2 + int(binary[i])
    print("Decimal representation is", decimal)

binary_to_decimal_for()