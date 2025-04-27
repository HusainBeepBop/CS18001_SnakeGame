# 2

def compare_num():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a > b:
        print("The first number", a, "is greater than the second number", b)
    elif a < b:
        print("The first number", a, "is less than the second number", b)
    else:
        print("The first number", a, "is equal to the second number", b)

compare_num()