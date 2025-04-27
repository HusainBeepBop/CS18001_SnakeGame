# 10

def is_prime_while():
    n = int(input("Enter a number: "))
    if n <= 1:
        print(n, "is not prime")
        return
    i = 2
    while i < n:
        if n % i == 0:
            print(n, "is not prime")
            return
        i = i + 1
    print(n, "is prime")

is_prime_while()