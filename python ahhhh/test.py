import tkinter as tk

def submit_action():
    message_label.config(text="Submitted Successfully!", fg="green")  # Change label text & color


root = tk.Tk()
root.title("Test Window")
root.geometry("300x200")

login= tk.Frame(root)
login.pack()

tk.Label(login, text="This is a test label").pack()
name_Entry = tk.Entry(login)
name_Entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_action)
submit_button.pack(pady=20)

message_label = tk.Label(root, text="", font=("Arial", 12))  # Empty label
message_label.pack(pady=10)

root.mainloop()