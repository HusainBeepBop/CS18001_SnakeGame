import math
# 9
def cube():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Cube of", a, "is", a * a * a)
    print("Cube of", b, "is", b * b * b)

def cubeRoot():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Cube root of", a, "is", math.pow(a, 1/3))
    print("Cube root of", b, "is", math.pow(b, 1/3))

cube()
cubeRoot()