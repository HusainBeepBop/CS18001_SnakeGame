# 12
def Sinterest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest is", simple_interest)

Sinterest()