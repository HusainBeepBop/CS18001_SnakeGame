# 11
def increment():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a + 1
    b = b + 1
    print("After incrementing, first number is", a, "and second number is", b)

def decrement():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a - 1
    b = b - 1
    print("After decrementing, first number is", a, "and second number is", b)

increment()
decrement()