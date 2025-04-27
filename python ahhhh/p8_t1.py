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