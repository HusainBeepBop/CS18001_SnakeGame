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

des_section = tk.Frame(root, width=des_width, height=des_height, borderwidth=5, relief="raised")
des_section.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
des_section.configure(bg="#f0f0f0")
des_section.pack_propagate(False)

photoWidth = int(des_width * 0.9)
photoHeight = int(des_height * 0.4)

logo_frame = tk.Frame(des_section, relief="raised")
logo_frame.pack(pady=(10, 5))
logo_image = Image.open("./assets/logo.png")
logo_image = logo_image.resize((photoWidth, photoHeight), Image.Resampling.LANCZOS)

logo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo)
logo_label.pack()

team_frame = tk.Frame(des_section, relief="raised")
team_frame.pack(pady=(5, 10))
team_frame.configure(bg="#181818")
team_frame.pack_propagate(False)
team_frame.configure(width=photoWidth, height=photoHeight)

infoButton = tk.Button(des_section, text="Info", bg="#181818", fg="#f0f0f0", relief="raised")
infoButton.pack(pady=(5, 5), padx=(5, 5), side=tk.BOTTOM)
infoButton.configure(width=photoWidth)

main_area_frame = tk.Frame(root, borderwidth=5, relief="groove")
main_area_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
pygame.init()
