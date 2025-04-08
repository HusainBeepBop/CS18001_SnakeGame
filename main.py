import pygame
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

root = tk.Tk()
root.title("Snake Game")
root.attributes('-fullscreen', True)
root.configure(bg="#1f1f1f")

snake = []
snake_body = []
food = None
food1 = None
food2 = None
direction = 'Right'
speed = 100
test = None
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
close_button.pack(side=tk.RIGHT, anchor=tk.NE)
close_button.pack_propagate(False)

main_area = tk.Frame(content_section)
main_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
main_area.pack_propagate(False)

start_game = tk.Frame(main_area)
start_game.configure( height=80)
start_game.pack(side='bottom', fill=tk.X)
start_game.pack_propagate(False)

sp_game_canvas = None  
dp_game_canvas_left = None
dp_game_canvas_right = None
score_p1 = 0
score_p2 = 0

score_counter_p1 = tk.Label(close_game, text=f"Player 1: {score_p1}", font=("Arial", 23), bg="#181818", fg='white')
score_counter_p1.pack(side=tk.LEFT, anchor=tk.W)

def draw_grid():
    grid_size = 20
    canvas_width = sp_game_canvas.winfo_width()
    canvas_height = sp_game_canvas.winfo_height()

    for x in range(0, canvas_width, grid_size):
        sp_game_canvas.create_line(x, 0, x, canvas_height, fill="lightgray")

    for y in range(0, canvas_height, grid_size):
        sp_game_canvas.create_line(0, y, canvas_width, y, fill="lightgray")

def draw_grid1():
    grid_size = 20
    canvas_width = dp_game_canvas_left.winfo_width()
    canvas_height = dp_game_canvas_left.winfo_height()

    for x in range(0, canvas_width, grid_size):
        dp_game_canvas_left.create_line(x, 0, x, canvas_height, fill="lightgray")

    for y in range(0, canvas_height, grid_size):
        dp_game_canvas_left.create_line(0, y, canvas_width, y, fill="lightgray")

def draw_grid2():
    grid_size = 20
    canvas_width = dp_game_canvas_right.winfo_width()
    canvas_height = dp_game_canvas_right.winfo_height()

    for x in range(0, canvas_width, grid_size):
        dp_game_canvas_right.create_line(x, 0, x, canvas_height, fill="lightgray")

    for y in range(0, canvas_height, grid_size):
        dp_game_canvas_right.create_line(0, y, canvas_width, y, fill="lightgray")

def spawn_food():
    import random

    canvs_width = sp_game_canvas.winfo_width()
    canvs_height = sp_game_canvas.winfo_height()

    foodx = random.randint(1, (canvs_width // 20)- 1) * 20
    foody = random.randint(1, (canvs_height // 20)- 1) * 20

    food = sp_game_canvas.create_oval(foodx, foody, foodx + 20, foody + 20, fill="red")

def spawn_food1():
    import random

    canvs_width = dp_game_canvas_left.winfo_width()
    canvs_height = dp_game_canvas_left.winfo_height()

    foodx = random.randint(1, (canvs_width // 20)- 1) * 20
    foody = random.randint(1, (canvs_height // 20)- 1) * 20

    food1 = dp_game_canvas_left.create_oval(foodx, foody, foodx + 20, foody + 20, fill="red")

def spawn_food2():
    import random

    canvs_width = dp_game_canvas_right.winfo_width()
    canvs_height = dp_game_canvas_right.winfo_height()

    foodx = random.randint(1, (canvs_width // 20)- 1) * 20
    foody = random.randint(1, (canvs_height // 20)- 1) * 20

    food2 = dp_game_canvas_right.create_oval(foodx, foody, foodx + 20, foody + 20, fill="red")

def snake_move():

    global snake, snake_body, direction

    head_x, head_y = snake[0]
    if direction == "Right":
        head_x += 20
    elif direction == "Left":
        head_x -= 20
    elif direction == "Up":
        head_y -= 20
    elif direction == "Down":
        head_y += 20

    snake.insert(0, (head_x, head_y))
    new_part = sp_game_canvas.create_rectangle(head_x, head_y, head_x + 20, head_y + 20, fill="black")
    snake_body.insert(0, new_part)

    tail = snake.pop()
    sp_game_canvas.delete(snake_body.pop())
    sp_game_canvas.after(100, snake_move)  

def change_direction(event):
    
    global direction

    key = event.keysym
    if key in ("Up", "w") and direction != "Down":
        direction = "Up"
    elif key in ("Down", "s") and direction != "Up":
        direction = "Down"
    elif key in ("Left", "a") and direction != "Right":
        direction = "Left"
    elif key in ("Right", "d") and direction != "Left":
        direction = "Right"

def sp():
    
    global sp_game_canvas  
    global dp_game_canvas_right, dp_game_canvas_left, score_counter_p2, score_p2
    global snake, snake_body, direction

    if dp_game_canvas_left is not None:
        dp_game_canvas_left.destroy()
    if dp_game_canvas_right is not None:
        dp_game_canvas_right.destroy()
    if score_counter_p2 is not None:
        score_counter_p2.destroy()
    try:
        sp_game_canvas.destroy()
    except:
        pass

    sp_game_canvas= Canvas(main_area, bg="green")
    sp_game_canvas.pack(fill=tk.BOTH, expand=True)

    snake = [(100,100),(80,100)]
    snake_body = []
    for x, y in snake:
        snake_body.append(sp_game_canvas.create_rectangle(x, y, x+20, y+20, fill="black"))

    direction = "Right"

    sp_game_canvas.focus_set()
    sp_game_canvas.bind("<KeyPress>", change_direction)

    sp_game_canvas.after(50, draw_grid)
    sp_game_canvas.after(100, spawn_food)

    snake_move()

   

def dp():
    global dp_game_canvas_left, dp_game_canvas_right, sp_game_canvas, score_counter_p2, score_p2

    if sp_game_canvas is not None:
        sp_game_canvas.destroy()  
    try:
        dp_game_canvas_left.destroy()
        dp_game_canvas_right.destroy()
        score_counter_p2.destroy()
    except:
        pass
    
    dp_game_canvas_left = tk.Canvas(main_area, bg="blue")
    dp_game_canvas_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    dp_game_canvas_right = tk.Canvas(main_area, bg="purple")
    dp_game_canvas_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    score_counter_p2 = tk.Label(close_game, text=f"Player 2: {score_p2}", font=("Arial", 23), bg="#181818", fg='white')
    score_counter_p2.pack(side=tk.LEFT, anchor=tk.W)

    snake1 = [(100, 100),  (80, 100)]  
    snake2 = [(100, 100), (80, 100)]  
    snake1_body = []
    snake2_body = []

    for x, y in snake1:
        snake1_body.append(dp_game_canvas_left.create_rectangle(x, y, x + 20, y + 20, fill="white"))

    for x, y in snake2:
        snake2_body.append(dp_game_canvas_right.create_rectangle(x, y, x + 20, y + 20, fill="white"))

    direction1 = "Right"
    direction2 = "Right"

    dp_game_canvas_left.after(50, draw_grid1)
    dp_game_canvas_right.after(50, draw_grid2)
    dp_game_canvas_left.after(100, spawn_food1)
    dp_game_canvas_right.after(100, spawn_food2)

single_player = tk.Button(start_game, text="Single Player", bg="#181818", fg="#f0f0f0", relief="raised", command=sp)
single_player.pack(side='left', pady=(0, 5), fill=tk.BOTH, expand=True)

dual_player = tk.Button(start_game, text="Dual Player", bg="#181818", fg="#f0f0f0", relief="raised", command=dp)
dual_player.pack(side='right', pady=(0, 5), fill=tk.BOTH, expand=True)

root.mainloop()
pygame.init()
