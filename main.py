import pygame
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

max_frame_width = int(screen_width * 0.9)  
max_frame_height = int(screen_height * 0.9)

root.attributes('-fullscreen', True)
root.title("Snake Game")

max_screen_width = 1366
max_screen_height = 768

frame_width = min(max_frame_width, max_screen_width)
frame_height = min(max_frame_height, max_screen_height)

home = tk.Frame(root, height=frame_height, width=frame_width)
Gframe=tk.Frame(root)
home.grid()

description = tk.Frame(home, bg='black', height=max_frame_height*0.9, width=max_frame_width*0.3)
description.grid(row=0, column=1)


logo = ImageTk.PhotoImage(file="./assets/logo.png")
logo_label = Label(description, image=logo, width=300, height=300)
logo_label.grid(row=0, column=0)

close_button = tk.Button(root, text="Close", bg='Red', font='Chewy 20', command=root.destroy)
close_button.grid(row=0, column=2)
 
single_Player = tk.Button(home, text="Single Player", bg='Orange', font='Chewy 40', height=2)
single_Player.grid(row=5, column=5)

double_Player = tk.Button(home, text="Multi Player", bg='Blue', font='Chewy 40', height=2)
double_Player.grid(row=6, column=5)

root.mainloop()
pygame.init()
