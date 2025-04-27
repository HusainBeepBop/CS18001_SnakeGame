# 10
def remainder():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if b != 0:
        print("Remainder of", a, "divided by", b, "is", a % b)
    else:
        print("Error: Division by zero is not allowed.")

remainder()