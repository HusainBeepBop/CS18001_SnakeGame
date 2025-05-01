# Take input from the user
n = int(input("Enter a number: "))

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of the number
        if num % i == 0:
            return False
    return True

# Find all prime numbers less than n
prime_numbers = []
for i in range(2, n):
    if is_prime(i):
        prime_numbers.append(i)

# Print the result
print(f"Prime numbers less than {n}: {prime_numbers}")