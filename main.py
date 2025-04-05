import pygame
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Snake Game")
root.attributes('-fullscreen', True)
root.configure(bg="#181818")

des_section = tk.Frame(root, borderwidth=2, relief="groove")
des_section.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
des_section.configure(bg="#1f1f1f")
des_section.pack_propagate(False)

logo_frame = tk.Frame(des_section)
logo_frame.pack(pady=(10, 5))
logo = tk.PhotoImage(file="./assets/logo.png") 
logo_label = tk.Label(logo_frame, image=logo, bg="white")  
logo_label.pack()

root.mainloop()
pygame.init()
