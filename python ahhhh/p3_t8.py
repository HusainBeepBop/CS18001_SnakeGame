# 8

def calculate_factorial():
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)

calculate_factorial()