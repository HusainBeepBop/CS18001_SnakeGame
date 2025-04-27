# 6

def sum_even_and_odd():
    i = 0
    sum_even = 0
    sum_odd = 0
    while i <= 100:
        if i % 2 == 0:
            sum_even = sum_even + i
        else:
            sum_odd = sum_odd + i
        i = i + 1
    print("The sum of all even numbers from 0 to 100 is", sum_even)
    print("The sum of all odd numbers from 0 to 100 is", sum_odd)

sum_even_and_odd()