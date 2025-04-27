# 8

def calculate_factorial():
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    factorial = 1
    i = 1
    while i <= number:
        factorial = factorial * i
        i = i + 1
    print("The factorial of", number, "is", factorial)

calculate_factorial()