import pygame
from tkinter as *
import tkinter as tk
from tkinter import ttk

root=tk.Tk
root.geometry('5000x5000')
root.title("Snake Game")
Lframe=Frame(root)
Gframe=Frame(root)
Lframe.pack()

single=Tk.Button(Lframe, Text="Single Player", bg='Orange', font='Chewy 40', height=3)
single.pack()

multi=Tk.Button(Lframe, Text="Multi Player", bg='Blue', font='Chewy 40', height=3)
multi.pack()

root.mainloop()
pygame.init()
