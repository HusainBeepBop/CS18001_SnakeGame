# 8
import math

def square():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Square of", a, "is", a * a)
    print("Square of", b, "is", b * b)

def squareRoot():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Square root of", a, "is", math.sqrt(a))
    print("Square root of", b, "is", math.sqrt(b))

square()
squareRoot()