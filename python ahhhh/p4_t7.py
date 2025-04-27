# 7

def divisible_by_5_or_7():
    i = 0
    while i <= 100:
        if i % 5 == 0 or i % 7 == 0:
            print(i)
        i = i + 1

divisible_by_5_or_7()