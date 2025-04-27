# 3

def hex_to_binary():
    hex_num = input("Enter a hexadecimal number: ")
    binary = ""
    i = 0
    while i < len(hex_num):
        digit = hex_num[i]
        binary = binary + bin(int(digit, 16))[2:].zfill(4)
        i = i + 1
    print("Binary representation is", binary)

hex_to_binary()