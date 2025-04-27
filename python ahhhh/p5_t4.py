# 4

def binary_to_hex():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    hex_num = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hex_num = str(remainder) + hex_num
        else:
            hex_num = chr(55 + remainder) + hex_num
        decimal = decimal // 16
    print("Hexadecimal representation is", hex_num)

binary_to_hex()