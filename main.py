import pygame
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("Snake Game")
root.attributes('-fullscreen', True)
root.configure(bg="#1f1f1f")

vpWidth = root.winfo_screenwidth()
vpheight = root.winfo_screenheight()

desWidth = int(vpWidth * 0.25)    
desHeight = int(vpheight * 0.9)

des_section = tk.Frame(root, width=desWidth, height=desHeight, borderwidth=5, relief="raised")
des_section.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
des_section.configure(bg="#f0f0f0")
des_section.pack_propagate(False)

photoWidth = int(desWidth * 0.9)
photoHeight = int(desHeight * 0.4)

logo_frame = tk.Frame(des_section, relief="raised")
logo_frame.pack(pady=(5, 5))
logo_image = Image.open("./assets/logo.png")
logo_image = logo_image.resize((photoWidth, photoHeight), Image.Resampling.LANCZOS)

logo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo)
logo_label.image=logo
logo_label.pack()

team_frame = tk.Frame(des_section, relief="raised")
team_frame.pack(pady=(0, 5))
team_frame.configure(bg="#f0f0f0")
team_frame.pack_propagate(False)
team_frame.configure(width=photoWidth, height=photoHeight)

def info():
    messagebox.showinfo("Info about Game", "Enter Info here")

infoButton = tk.Button(des_section, text="Info", bg="#181818", fg="#f0f0f0", relief="raised", command=info)
infoButton.pack(pady=(5, 5), padx=(5, 5), side=tk.BOTTOM)
infoButton.configure(width=photoWidth)

content_section = tk.Frame(root, borderwidth=5, relief="raised")
content_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(0,5), pady=5)
content_section.configure(bg="#1f1f1f")

close_game = tk.Frame(content_section)
close_game.pack(side=tk.TOP, anchor=tk.NE)
close_game.configure(width=content_section.winfo_width(), height=content_section.winfo_height() * 0.06)


close_button = tk.Button(close_game, text="X", font=('Arial',16), bg="#181818", fg="#f0f0f0", relief="raised", command=root.destroy)
close_button.pack(side=tk.LEFT, anchor=tk.NE)
close_button.pack_propagate(False)

main_area = tk.Frame(content_section)
main_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

start_game = tk.Frame(main_area)
start_game.configure( height=100)
start_game.pack(side= 'bottom', fill=tk.X)
start_game.pack_propagate(False)

def sp():
    game_canvas= Canvas(main_area, width=200, height=100, bg="green").pack(anchor=tk.CENTER,expand=True)

single_player = tk.Button(start_game, width=85, height=100, text="Single Player", bg="#181818", fg="#f0f0f0", relief="raised", command=sp)
single_player.pack(side='left', pady=(0, 5), fill=tk.X)

dual_player = tk.Button(start_game, width=100, height=100, text="Dual Player", bg="#181818", fg="#f0f0f0", relief="raised")
dual_player.pack(side='right', pady=(0, 5), fill=tk.X)

root.mainloop()
pygame.init()