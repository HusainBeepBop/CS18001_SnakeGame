# 13

def sort_numbers_by_length():
    n = int(input("Enter the number of strings: "))
    numbers = []
    for i in range(n):
        numbers.append(input("Enter number " + str(i + 1) + ": "))
    numbers.sort(key=len)
    print("Numbers sorted by length:", numbers)

sort_numbers_by_length()