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