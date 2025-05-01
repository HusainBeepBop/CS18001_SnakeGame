digits = 1
num = 120
while (num >= 10):
    num = num / 10
    digits = digits + 1

print(digits, end=" ")