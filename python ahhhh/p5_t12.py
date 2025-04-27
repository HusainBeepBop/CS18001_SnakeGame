# 12

def binary_to_octal_for():
    binary = input("Enter a binary number: ")
    binary = binary.zfill((len(binary) + 2) // 3 * 3)  # Ensure proper padding
    octal_map = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'
    }
    octal = ""
    for i in range(0, len(binary), 3):
        octal = octal + octal_map[binary[i:i+3]]
    print("Octal representation is", octal)

binary_to_octal_for()