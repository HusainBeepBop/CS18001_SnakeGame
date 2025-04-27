# 5

def octal_to_binary():
    octal = input("Enter an octal number: ")
    binary_map = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    binary = ""
    for digit in octal:
        binary = binary + binary_map[digit]
    print("Binary representation is", binary)

octal_to_binary()