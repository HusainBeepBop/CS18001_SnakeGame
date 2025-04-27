# 13
def Cinterest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))
    n = int(input("Enter the number of times interest is compounded per year: "))
    compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal
    print("Compound Interest is", compound_interest)

Cinterest()