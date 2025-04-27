# 10

def is_prime():
    n = int(input("Enter a number: "))
    if n <= 1:
        print(n, "is not prime")
        return
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime")
            return
    print(n, "is prime")

is_prime()