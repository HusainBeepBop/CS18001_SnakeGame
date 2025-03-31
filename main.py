import pygame
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root=tk.Tk()
root.geometry('500x500')
root.title("Snake Game")
Lframe=tk.Frame(root, height=100)
Gframe=tk.Frame(root)
Lframe.pack()

im1=ImageTk.PhotoImage(Image.open("C:\Users\Lenovo\Downloads\HD-wallpaper-classic-snake-adventures-snake-game.jpg"))
im1_label = Label(Lframe, image=im1)
im1_label.pack()
 
single=tk.Button(Lframe, text="Single Player", bg='Orange', font='Chewy 40', height=2)
single.grid(row=5, column=5)

multi=tk.Button(Lframe, text="Multi Player", bg='Blue', font='Chewy 40', height=2)
multi.grid(row=6, column=5)

root.mainloop()
pygame.init()
