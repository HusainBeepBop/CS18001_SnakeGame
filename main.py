import pygame
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Snake Game")
root.attributes('-fullscreen', True)
root.configure(bg="#181818")

vp_width = root.winfo_screenwidth()
vp_height = root.winfo_screenheight()

des_width = int(vp_width * 0.25)    
des_height = int(vp_height * 0.9)

des_section = tk.Frame(root, width=des_width, height=des_height, borderwidth=2, relief="groove")
des_section.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
des_section.configure(bg="#1f1f1f")
des_section.pack_propagate(False)

logo_frame = tk.Frame(des_section)
logo_frame.pack(pady=(10, 5))
logo = tk.PhotoImage(file="./assets/logo.png") 
logo_label = tk.Label(logo_frame, image=logo)  
logo_label.configure(width=des_width * 0.9, height=des_height * 0.4)
logo_label.pack()

root.mainloop()
pygame.init()
