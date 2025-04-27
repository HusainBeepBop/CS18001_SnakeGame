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