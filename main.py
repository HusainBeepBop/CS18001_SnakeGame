import pygame
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.attributes('-fullscreen', True)
root.title("Snake Game")
home=tk.Frame(root, height=100)
Gframe=tk.Frame(root)
home.pack()

logo = ImageTk.PhotoImage(Image.open("./assets/logo.png"))
logo_label = Label(home, image=logo)
logo_label.grid(row=0, column=0)

close_button = tk.Button(home, text="Close", bg='Red', font='Chewy 20', command=root.destroy)
close_button.grid(row=0, column=2)
 
single_Player = tk.Button(home, text="Single Player", bg='Orange', font='Chewy 40', height=2)
single_Player.grid(row=5, column=5)

double_Player = tk.Button(home, text="Multi Player", bg='Blue', font='Chewy 40', height=2)
double_Player.grid(row=6, column=5)

root.mainloop()
pygame.init()
