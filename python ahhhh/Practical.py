#Practical 1

# 1
a = 10
b = 20
print("Before Swap:", a, b)
c = a
a = b
b = c
print("After Swap:", a, b)

# 2 and 3
def swapOneVariable():
    a = 15
    b = 30
    print("Before Swap:", a, b)
    c = a
    a = b
    b = c
    print("After Swap:", a, b)

swapOneVariable()

# 4
def swapWithArithmetic():
    a = 25
    b = 50
    print("Before Swap:", a, b)
    a = a + b
    b = a - b
    a = a - b
    print("After Swap:", a, b)

swapWithArithmetic()

# 5
def arithmetic():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)

arithmetic()

# 6
def divide():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        print("Division Result:", numerator / denominator)
    else:
        print("Error: Division by zero is not allowed.")

divide()

# 7
def power():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    result = base ** exponent
    print("Result:", result)

power()

# 8
import math

def square():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Square of", a, "is", a * a)
    print("Square of", b, "is", b * b)

def squareRoot():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Square root of", a, "is", math.sqrt(a))
    print("Square root of", b, "is", math.sqrt(b))

square()
squareRoot()

# 9
def cube():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Cube of", a, "is", a * a * a)
    print("Cube of", b, "is", b * b * b)

def cubeRoot():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Cube root of", a, "is", math.pow(a, 1/3))
    print("Cube root of", b, "is", math.pow(b, 1/3))

cube()
cubeRoot()

# 10
def remainder():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if b != 0:
        print("Remainder of", a, "divided by", b, "is", a % b)
    else:
        print("Error: Division by zero is not allowed.")

remainder()

# 11
def increment():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a + 1
    b = b + 1
    print("After incrementing, first number is", a, "and second number is", b)

def decrement():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a = a - 1
    b = b - 1
    print("After decrementing, first number is", a, "and second number is", b)

increment()
decrement()

# 12
def Sinterest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))
    simple_interest = (principal * rate * time) / 100
    print("Simple Interest is", simple_interest)

Sinterest()

# 13
def Cinterest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period in years: "))
    n = int(input("Enter the number of times interest is compounded per year: "))
    compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal
    print("Compound Interest is", compound_interest)

Cinterest()

#Practical 2

# 1

def evenOdd():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print("The number", number, "is even.")
    else:
        print("The number", number, "is odd.")

evenOdd()

# 2

def compare_num():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a > b:
        print("The first number", a, "is greater than the second number", b)
    elif a < b:
        print("The first number", a, "is less than the second number", b)
    else:
        print("The first number", a, "is equal to the second number", b)

compare_num()

# 3

def greatest():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a > b and a > c:
        print("The greatest number is", a)
    elif b > c:
        print("The greatest number is", b)
    else:
        print("The greatest number is", c)

greatest()

# 4

def greatest_nested():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    if a > b:
        if a > c:
            print("The greatest number is", a)
        else:
            print("The greatest number is", c)
    else:
        if b > c:
            print("The greatest number is", b)
        else:
            print("The greatest number is", c)

greatest_nested()

# 5

def grade():
    marks = []
    for i in range(1, 7):
        mark = int(input("Enter the marks for subject " + str(i) + ": "))
        if mark > 100:
            print("Error: Marks cannot exceed 100.")
            return
        marks.append(mark)
    
    average = sum(marks) / 6
    print("Average Marks:", average)
    
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade()

#Practical 3

# 1
def printhelloworld():
    for i in range(5):
        print("Hello World")

printhelloworld()

# 2

def printnumbers():
    for i in range(1, 101):
        print(i)

printnumbers()

# 3

def printoddnumbers():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

printoddnumbers()

# 4

def print_even_or_odd():
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

print_even_or_odd()

# 5

def sum_of_numbers():
    total = 0
    for i in range(1, 101):
        total += i
    print("The sum of all natural numbers from 1 to 100 is", total)

sum_of_numbers()

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

# 7

def divisible_by_5_or_7():
    for i in range(1, 101):
        if i % 5 == 0 or i % 7 == 0:
            print(i)

divisible_by_5_or_7()

# 8

def calculate_factorial():
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is", factorial)

calculate_factorial()

# 9

def generate_fibonacci():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    print("Fibonacci series up to", n, "terms:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

generate_fibonacci()

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

#Practical 4

# 1

def print_hello_world():
    i = 0
    while i < 5:
        print("Hello World")
        i = i + 1

print_hello_world()

# 2

def print_numbers():
    i = 1
    while i <= 100:
        print(i)
        i = i + 1

print_numbers()

# 3 

def print_odd_numbers():
    i = 1
    while i < 100:
        if i % 2 != 0:
            print(i)
        i = i + 1

print_odd_numbers()

# 4

def print_even_or_odd():
    i = 0
    while i <= 100:
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
        i = i + 1

print_even_or_odd()


# 5

def sum_of_numbers():
    i = 0
    total = 0
    while i <= 100:
        total = total + i
        i = i + 1
    print("The sum of all natural numbers from 0 to 100 is", total)

sum_of_numbers()


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


# 7

def divisible_by_5_or_7():
    i = 0
    while i <= 100:
        if i % 5 == 0 or i % 7 == 0:
            print(i)
        i = i + 1

divisible_by_5_or_7()


# 8

def calculate_factorial():
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    factorial = 1
    i = 1
    while i <= number:
        factorial = factorial * i
        i = i + 1
    print("The factorial of", number, "is", factorial)

calculate_factorial()


# 9

def generate_fibonacci():
    n = int(input("Enter the number of terms: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    i = 0
    print("Fibonacci series up to", n, "terms:")
    while i < n:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        i = i + 1
    print()

generate_fibonacci()


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

#Practical 5

# 1

def decimal_to_binary():
    num = int(input("Enter a decimal number: "))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print("Binary representation is", binary)

decimal_to_binary()


# 2

def binary_to_decimal():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    print("Decimal representation is", decimal)

binary_to_decimal()


# 3

def hex_to_binary():
    hex_num = input("Enter a hexadecimal number: ")
    binary = ""
    i = 0
    while i < len(hex_num):
        digit = hex_num[i]
        binary = binary + bin(int(digit, 16))[2:].zfill(4)
        i = i + 1
    print("Binary representation is", binary)

hex_to_binary()


# 4

def binary_to_hex():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    hex_num = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hex_num = str(remainder) + hex_num
        else:
            hex_num = chr(55 + remainder) + hex_num
        decimal = decimal // 16
    print("Hexadecimal representation is", hex_num)

binary_to_hex()


# 5

def octal_to_binary():
    octal = input("Enter an octal number: ")
    binary_map = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    binary = ""
    for digit in octal:
        binary = binary + binary_map[digit]
    print("Binary representation is", binary)

octal_to_binary()


# 6

def binary_to_octal():
    binary = input("Enter a binary number: ")
    decimal = 0
    i = 0
    while i < len(binary):
        decimal = decimal * 2 + int(binary[i])
        i = i + 1
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    print("Octal representation is", octal)

binary_to_octal()


# 7

def decimal_to_binary_bitwise():
    num = int(input("Enter a decimal number: "))
    binary = ""
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        binary = binary + str(bit)
    binary = binary.lstrip("0")  # Remove leading zeros
    print("Binary representation is", binary)

decimal_to_binary_bitwise()


# 8

def binary_to_decimal_for():
    binary = input("Enter a binary number: ")
    decimal = 0
    for i in range(len(binary)):
        decimal = decimal * 2 + int(binary[i])
    print("Decimal representation is", decimal)

binary_to_decimal_for()


# 9

def hex_to_binary_for():
    hex_num = input("Enter a hexadecimal number: ")
    binary_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary = ""
    for digit in hex_num:
        binary = binary + binary_map[digit.upper()]
    print("Binary representation is", binary)

hex_to_binary_for()


# 10

def binary_to_hex_for():
    binary = input("Enter a binary number: ")
    binary = binary.zfill((len(binary) + 3) // 4 * 4)  # Ensure proper padding
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex_num = ""
    for i in range(0, len(binary), 4):
        hex_num = hex_num + hex_map[binary[i:i+4]]
    print("Hexadecimal representation is", hex_num)

binary_to_hex_for()


# 11

def octal_to_binary_for():
    octal = input("Enter an octal number: ")
    binary_map = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111'
    }
    binary = ""
    for digit in octal:
        binary = binary + binary_map[digit]
    print("Binary representation is", binary)

octal_to_binary_for()


# 12

def binary_to_octal_for():
    binary = input("Enter a binary number: ")
    binary = binary.zfill((len(binary) + 2) // 3 * 3)  # Ensure proper padding
    octal_map = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'
    }
    octal = ""
    for i in range(0, len(binary), 3):
        octal = octal + octal_map[binary[i:i+3]]
    print("Octal representation is", octal)

binary_to_octal_for()


#Practical 6

# 1

def print_characters():
    string = "Hello World"
    for char in string:
        print(char)

print_characters()


# 2

def print_vowel_indices():
    string = "Hello World"
    vowels = "aeiouAEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            print("Vowel", string[i], "at index", i)

print_vowel_indices()


# 3

def print_left_of_vowels():
    string = "Hello World"
    vowels = "aeiouAEIOU"
    for i in range(1, len(string)):
        if string[i] in vowels:
            print("Character to the left of", string[i], "is", string[i - 1])

print_left_of_vowels()


# 4

def check_palindrome():
    word = input("Enter a word: ")
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            print(word, "is not a palindrome")
            return
        i = i + 1
        j = j - 1
    print(word, "is a palindrome")

check_palindrome()


# 5

def check_anagrams():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    if len(word1) != len(word2):
        print("The words are of different lengths, so they cannot be anagrams.")
        return
    if sorted(word1) == sorted(word2):
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")

check_anagrams()


# 6

def remove_repeated_characters():
    word = input("Enter a word: ")
    result = ""
    for char in word:
        if char not in result:
            result = result + char
    print("String after removing repeated characters:", result)

remove_repeated_characters()


# 7

def print_substrings():
    word = input("Enter a word: ")
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            print(word[i:j])

print_substrings()


# 8

def print_substrings_length_3():
    word = input("Enter a word: ")
    for i in range(len(word) - 2):
        print(word[i:i+3])

print_substrings_length_3()


# 9

def print_long_strings():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    for string in strings:
        if len(string) >= 3:
            print(string)

print_long_strings()


# 10

def sort_strings_by_length():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    strings.sort(key=len)
    print("Strings sorted by length:", strings)

sort_strings_by_length()


# 11

def print_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix row by row:")
    for i in range(3):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
        matrix.append(row)

    print("Row-wise elements:")
    for row in matrix:
        print(row)

    print("Column-wise elements:")
    for j in range(3):
        for i in range(3):
            print(matrix[i][j], end=" ")
        print()

print_matrix()


# 12

def is_identity_matrix():
    matrix = []
    print("Enter the elements of the 3x3 matrix row by row:")
    for i in range(3):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
        matrix.append(row)

    for i in range(3):
        for j in range(3):
            if i == j and matrix[i][j] != 1:
                print("False")
                return
            elif i != j and matrix[i][j] != 0:
                print("False")
                return
    print("True")

is_identity_matrix()


# 13

def sort_numbers_by_length():
    n = int(input("Enter the number of strings: "))
    numbers = []
    for i in range(n):
        numbers.append(input("Enter number " + str(i + 1) + ": "))
    numbers.sort(key=len)
    print("Numbers sorted by length:", numbers)

sort_numbers_by_length()


# 14

def search_element():
    n = int(input("Enter the number of strings: "))
    strings = []
    for i in range(n):
        strings.append(input("Enter string " + str(i + 1) + ": "))
    element = input("Enter the element to search for: ")
    if element in strings:
        print("Element found at index", strings.index(element))
    else:
        print("Element not found in the list.")

search_element()


#Practical 7

# 1

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_vehicle(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print("Battery Capacity:", self.battery_capacity, "kWh")

class Car(Vehicle, Electric):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        Electric.__init__(self, battery_capacity)

    def display_car(self):
        self.display_vehicle()
        self.display_battery()


car = Car("Tesla", "Model S", 2022, 100)
car.display_car()


# 2

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self._model = model  
        self.__year = year  

    def get_year(self):
        return self.__year  

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

class Car(Vehicle, Electric):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        Electric.__init__(self, battery_capacity)

    def display_attributes(self):
        print("Brand (Public):", self.brand)
        print("Model (Protected):", self._model)
        print("Year (Private):", self.get_year())
        print("Battery Capacity:", self.battery_capacity)


car = Car("Tesla", "Model 3", 2021, 75)
car.display_attributes()


# 3

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand  
        self._model = model  
        self.__year = year  

    def get_year(self):
        return self.__year  
    
class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

class Car(Vehicle, Electric):
    def __init__(self, brand, model, year, battery_capacity):
        Vehicle.__init__(self, brand, model, year)
        Electric.__init__(self, battery_capacity)

    def display_attributes(self):
        print("Brand (Public):", self.brand)
        print("Model (Protected):", self._model)
        print("Year (Private):", self.get_year())
        print("Battery Capacity:", self.battery_capacity)


car = Car("Tesla", "Model 3", 2021, 75)
car.display_attributes()


#Practical 8

# 1

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Train" and password == "123":
        login_window.destroy()
        open_calculator()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_calculator():
    calc_window = tk.Tk()
    calc_window.title("Calculator")
    calc_window.geometry("300x400")
    tk.Label(calc_window, text="Calculator", font=("Arial", 16)).pack()
    calc_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack()

login_window.mainloop()


# 2

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Train" and password == "123":
        login_window.destroy()
        open_calculator()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_calculator():
    def click_button(value):
        current = display_label.cget("text")
        display_label.config(text=current + value)

    def calculate():
        try:
            result = eval(display_label.cget("text"))
            display_label.config(text=str(result))
        except Exception as e:
            display_label.config(text="Error")

    calc_window = tk.Tk()
    calc_window.title("Calculator")
    calc_window.geometry("300x400")

    display_label = tk.Label(calc_window, text="", font=("Arial", 16), bg="white", anchor="e")
    display_label.pack(fill="both", padx=10, pady=10)

    buttons = [
        ('7', '8', '9', '+'),
        ('4', '5', '6', ''),
        ('1', '2', '3', ''),
        ('0', '=', '', '')
    ]

    for row in buttons:
        frame = tk.Frame(calc_window)
        frame.pack(expand=True, fill="both")
        for button in row:
            if button:
                tk.Button(frame, text=button, font=("Arial", 14), command=lambda b=button: click_button(b) if b != '=' else calculate()).pack(side="left", expand=True, fill="both")

    calc_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack()

login_window.mainloop()


# 3

import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "Train" and password == "123":
        login_window.destroy()
        open_calculator()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_calculator():
    def click_button(value):
        current = display_label.cget("text")
        display_label.config(text=current + value)

    def calculate():
        try:
            result = eval(display_label.cget("text"))
            display_label.config(text=str(result))
        except Exception as e:
            display_label.config(text="Error")

    calc_window = tk.Tk()
    calc_window.title("Calculator")
    calc_window.geometry("300x400")


    display_label = tk.Label(calc_window, text="", font=("Arial", 16), bg="white", anchor="e")
    display_label.pack(fill="both", padx=10, pady=10)


    buttons = [
        ('7', '8', '9', '+'),
        ('4', '5', '6', '-'),
        ('1', '2', '3', '*'),
        ('0', '=', '/', 'C')
    ]

    for row in buttons:
        frame = tk.Frame(calc_window, bg="lightgray")
        frame.pack(expand=True, fill="both")
        for button in row:
            if button == "C":
                tk.Button(frame, text=button, font=("Arial", 14), bg="red", fg="white",
                          command=lambda: display_label.config(text="")).pack(side="left", expand=True, fill="both")
            elif button == "=":
                tk.Button(frame, text=button, font=("Arial", 14), bg="green", fg="white",
                          command=calculate).pack(side="left", expand=True, fill="both")
            else:
                tk.Button(frame, text=button, font=("Arial", 14),
                          command=lambda b=button: click_button(b)).pack(side="left", expand=True, fill="both")

    calc_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")


tk.Label(login_window, text="Username:", font=("Arial", 12)).pack(pady=5)
username_entry = tk.Entry(login_window, font=("Arial", 12))
username_entry.pack(pady=5)


tk.Label(login_window, text="Password:", font=("Arial", 12)).pack(pady=5)
password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
password_entry.pack(pady=5)


tk.Button(login_window, text="Login", font=("Arial", 12), bg="blue", fg="white", command=login).pack(pady=10)

login_window.mainloop()