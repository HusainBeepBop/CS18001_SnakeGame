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

root.mainloop()
pygame.init()
