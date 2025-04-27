# 1

def decimal_to_binary():
    num = int(input("Enter a decimal number: "))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print("Binary representation is", binary)

decimal_to_binary()