# 9

def generate_fibonacci():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    print("Fibonacci series up to", n, "terms:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

generate_fibonacci()