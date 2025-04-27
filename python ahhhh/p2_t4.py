# 4

def greatest_nested():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a > b:
        if a > c:
            print("The greatest number is", a)
        else:
            print("The greatest number is", c)
    else:
        if b > c:
            print("The greatest number is", b)
        else:
            print("The greatest number is", c)

greatest_nested()