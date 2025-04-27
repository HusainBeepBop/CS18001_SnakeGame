# 7

def decimal_to_binary_bitwise():
    num = int(input("Enter a decimal number: "))
    binary = ""
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        binary = binary + str(bit)
    binary = binary.lstrip("0")  # Remove leading zeros
    print("Binary representation is", binary)

decimal_to_binary_bitwise()