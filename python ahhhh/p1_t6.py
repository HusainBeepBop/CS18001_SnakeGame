# 6
def divide():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        print("Division Result:", numerator / denominator)
    else:
        print("Error: Division by zero is not allowed.")

divide()