# 10

def binary_to_hex_for():
    binary = input("Enter a binary number: ")
    binary = binary.zfill((len(binary) + 3) // 4 * 4)  # Ensure proper padding
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex_num = ""
    for i in range(0, len(binary), 4):
        hex_num = hex_num + hex_map[binary[i:i+4]]
    print("Hexadecimal representation is", hex_num)

binary_to_hex_for()