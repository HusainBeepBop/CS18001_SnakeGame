# 6

def sum_even_and_odd():
    sum_even = 0
    sum_odd = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print("The sum of all even numbers from 1 to 100 is", sum_even)
    print("The sum of all odd numbers from 1 to 100 is", sum_odd)

sum_even_and_odd()