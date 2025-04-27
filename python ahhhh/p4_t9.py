# 9

def generate_fibonacci():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    i = 0
    print("Fibonacci series up to", n, "terms:")
    while i < n:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        i = i + 1
    print()

generate_fibonacci()