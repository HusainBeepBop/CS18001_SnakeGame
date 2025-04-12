import pygame
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Snake Game")
root.attributes('-fullscreen', True)
root.configure(bg="#1f1f1f")

snake = []
snake_body = []
snake1 = []
snake1_body = []
snake2 = []
snake2_body = []
food = None
food1 = None
food2 = None
direction = 'Right'
direction1 = 'Right'
direction2 = 'Right'
global snake_color
snake_color = "black"
colors=["black","blue","green", "purple", "orange", "yellow", "cyan", "magenta"]
speed = 100

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
global score_p1, score_p2
score_p1 = 0
score_p2 = 0

score_counter_p1 = tk.Label(close_game, text=f"Player 1: {score_p1}", font=("Arial", 23), bg="#181818", fg='white')
score_counter_p1.pack(side=tk.LEFT, anchor=tk.W)

def draw_grid():
    grid_size = 40
    canvas_width = sp_game_canvas.winfo_width()
    canvas_height = sp_game_canvas.winfo_height()

    for x in range(0, canvas_width, grid_size):
        sp_game_canvas.create_line(x, 0, x, canvas_height, fill="lightgray")

    for y in range(0, canvas_height, grid_size):
        sp_game_canvas.create_line(0, y, canvas_width, y, fill="lightgray")

def draw_grid1():
    grid_size = 40
    canvas_width1 = dp_game_canvas_left.winfo_width()
    canvas_height1 = dp_game_canvas_left.winfo_height()

    for x in range(0, canvas_width1, grid_size):
        dp_game_canvas_left.create_line(x, 0, x, canvas_height1, fill="lightgray")

    for y in range(0, canvas_height1, grid_size):
        dp_game_canvas_left.create_line(0, y, canvas_width1, y, fill="lightgray")

def draw_grid2():
    grid_size = 40
    canvas_width2 = dp_game_canvas_right.winfo_width()
    canvas_height2 = dp_game_canvas_right.winfo_height()

    for x in range(0, canvas_width2, grid_size):
        dp_game_canvas_right.create_line(x, 0, x, canvas_height2, fill="lightgray")

    for y in range(0, canvas_height2, grid_size):
        dp_game_canvas_right.create_line(0, y, canvas_width2, y, fill="lightgray")

def spawn_food():
    import random
    global food

    canvs_width = sp_game_canvas.winfo_width()
    canvs_height = sp_game_canvas.winfo_height()

    foodx = random.randint(1, (canvs_width // 40)) * 40
    foody = random.randint(1, (canvs_height // 40)) * 40

    food = sp_game_canvas.create_oval(foodx, foody, foodx + 40, foody + 40, fill="red")

def spawn_food1():
    import random
    global food1

    canvs_width1 = dp_game_canvas_left.winfo_width()
    canvs_height1 = dp_game_canvas_left.winfo_height()

    foodx = random.randint(1, (canvs_width1 // 40)) * 40
    foody = random.randint(1, (canvs_height1 // 40)) * 40

    food1 = dp_game_canvas_left.create_oval(foodx, foody, foodx + 40, foody + 40, fill="red")

def spawn_food2():
    import random
    global food2

    canvs_width2 = dp_game_canvas_right.winfo_width()
    canvs_height2 = dp_game_canvas_right.winfo_height()

    foodx = random.randint(1, (canvs_width2 // 40)) * 40
    foody = random.randint(1, (canvs_height2 // 40)) * 40

    food2 = dp_game_canvas_right.create_oval(foodx, foody, foodx + 40, foody + 40, fill="red")

def snake_move():
    global snake, snake_body, direction, score_p1, food, sp_game_canvas, snake_color

    canvas_width = sp_game_canvas.winfo_width()
    canvas_height = sp_game_canvas.winfo_height()

    head_x, head_y = snake[0]
    if direction == "Right":
        head_x += 40
    elif direction == "Left":
        head_x -= 40
    elif direction == "Up":
        head_y -= 40
    elif direction == "Down":
        head_y += 40
        
    if head_x<0 or head_x>=canvas_width or head_y<0 or head_y>=canvas_height:
        messagebox.showinfo("Game Over", f"You crashed into the wall! Your Score: {score_p1}")
        sp_game_canvas.destroy()
        sp_game_canvas=None
        snake.clear()
        snake_body.clear()
        score_p1=0
        score_counter_p1.config(text=f"Player 1: {score_p1}")
    
    if (head_x, head_y) in snake:
        messagebox.showinfo("Game Over", f"You bit yourself! Your Score: {score_p1}")
        sp_game_canvas.destroy()
        sp_game_canvas=None
        snake.clear()
        snake_body.clear()
        score_p1=0
        score_counter_p1.config(text=f"Player 1: {score_p1}")
        

    new_head = (head_x, head_y)
    snake.insert(0, new_head)
    new_block = sp_game_canvas.create_rectangle(head_x, head_y, head_x + 40, head_y + 40, fill=snake_color)
    snake_body.insert(0, new_block)

    if food is not None:
        coords = sp_game_canvas.coords(food)
        food_x, food_y = int(coords[0]), int(coords[1])
    
        if head_x == food_x and head_y == food_y:
            score_p1 += 1
            score_counter_p1.config(text=f"Player 1: {score_p1}")
            sp_game_canvas.delete(food)
            spawn_food()
            snake_color=random.choice(colors)
            

    tail = snake.pop()
    sp_game_canvas.delete(snake_body.pop())
    sp_game_canvas.after(100, snake_move)


def snake_move1():
    global snake1, snake1_body, direction1, score_p1, food1, dp_game_canvas_left, snake_color

    canvas_width = dp_game_canvas_left.winfo_width()
    canvas_height = dp_game_canvas_left.winfo_height()

    head_x, head_y = snake1[0]
    if direction1 == "Right":
        head_x += 40
    elif direction1 == "Left":
        head_x -= 40
    elif direction1 == "Up":
        head_y -= 40
    elif direction1 == "Down":
        head_y += 40
        
    if head_x<0 or head_x>=canvas_width or head_y<0 or head_y>=canvas_height:
        messagebox.showinfo("Game Over", f"You crashed into the wall! Your Score: {score_p1}")
        dp_game_canvas_left.destroy()
        dp_game_canvas_left=None
        snake1.clear()
        snake1_body.clear()
        score_p1=0
        score_counter_p1.config(text=f"Player 1: {score_p1}")

    if (head_x, head_y) in snake1:
        messagebox.showinfo("Game Over", f"You bit yourself! Your Score: {score_p1}")
        dp_game_canvas_left.destroy()
        dp_game_canvas_left=None
        snake1.clear()
        snake1_body.clear()
        score_p1=0
        score_counter_p1.config(text=f"Player 1: {score_p1}")
    

    new_head = (head_x, head_y)
    snake1.insert(0, new_head)
    new_block1 = dp_game_canvas_left.create_rectangle(head_x, head_y, head_x + 40, head_y + 40, fill=snake_color)
    snake1_body.insert(0, new_block1)

    if food1 is not None:
        coords = dp_game_canvas_left.coords(food1)
        foodx, foody = int(coords[0]), int(coords[1])

        if head_x == foodx and head_y == foody:
            score_p1 += 1
            score_counter_p1.config(text=f"Player 1: {score_p1}")
            dp_game_canvas_left.delete(food1)
            spawn_food1()
            snake_color=random.choice(colors)
       
    tail = snake1.pop()
    dp_game_canvas_left.delete(snake1_body.pop())
    dp_game_canvas_left.after(100, snake_move1)

def snake_move2():
    global snake2, snake2_body, direction2, score_p2, food2, dp_game_canvas_right, snake_color

    canvas_width = dp_game_canvas_right.winfo_width()
    canvas_height = dp_game_canvas_right.winfo_height()

    head_x, head_y = snake2[0]
    if direction2 == "Right":
        head_x += 40
    elif direction2 == "Left":
        head_x -= 40
    elif direction2 == "Up":
        head_y -= 40
    elif direction2 == "Down":
        head_y += 40
        
    if head_x<0 or head_x>=canvas_width or head_y<0 or head_y>=canvas_height:
        messagebox.showinfo("Game Over", f"You crashed into the wall! Your Score: {score_p2}")
        dp_game_canvas_right.destroy()
        dp_game_canvas_right=None
        snake2.clear()
        snake2_body.clear()
        score_p2=0
        score_counter_p2.config(text=f"Player 2: {score_p2}")

    if (head_x, head_y) in snake2:
        messagebox.showinfo("Game Over", f"You bit yourself! Your Score: {score_p2}")
        dp_game_canvas_right.destroy()
        dp_game_canvas_right=None
        snake2.clear()
        snake2_body.clear()
        score_p2=0
        score_counter_p1.config(text=f"Player 2: {score_p2}")
    

    new_head = (head_x, head_y)
    snake2.insert(0, new_head)
    new_block2 = dp_game_canvas_right.create_rectangle(head_x, head_y, head_x + 40, head_y + 40, fill=snake_color)
    snake2_body.insert(0, new_block2)

    if food2 is not None:
        coords = dp_game_canvas_right.coords(food2)
        foodx, foody = int(coords[0]), int(coords[1])

        if head_x == foodx and head_y == foody:
            score_p2 += 1
            score_counter_p2.config(text=f"Player 2: {score_p2}")
            dp_game_canvas_right.delete(food2)
            spawn_food2()
            snake_color=random.choice(colors)

    tail = snake2.pop()
    dp_game_canvas_right.delete(snake2_body.pop())
    dp_game_canvas_right.after(100, snake_move2)
 
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

def handle_keypress(event):
    
    global direction1, direction2

    key = event.keysym

    if key in ("w", "W") and direction1 != "Down":
        direction1 = "Up"
    elif key in ("s", "S") and direction1 != "Up":
        direction1 = "Down"
    elif key in ("a", "A") and direction1 != "Right":
        direction1 = "Left"
    elif key in ("d", "D") and direction1 != "Left":
        direction1 = "Right"

    if key == "Up" and direction2 != "Down":
        direction2 = "Up"
    elif key == "Down" and direction2 != "Up":
        direction2 = "Down"
    elif key == "Left" and direction2 != "Right":
        direction2 = "Left"
    elif key == "Right" and direction2 != "Left":
        direction2 = "Right"


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

    snake = [(40, 40), (0, 40)]
    snake_body = []
    for x, y in snake:
        snake_body.append(sp_game_canvas.create_rectangle(x, y, x+40, y+40, fill="black"))

    direction = "Right"

    sp_game_canvas.focus_set()
    sp_game_canvas.bind("<KeyPress>", change_direction)

    sp_game_canvas.after(50, draw_grid)
    sp_game_canvas.after(100, spawn_food)

    sp_game_canvas.after(200, snake_move)

   

def dp():
    global dp_game_canvas_left, dp_game_canvas_right, sp_game_canvas
    global score_counter_p2, score_p2
    global snake1, snake1_body, direction1
    global snake2, snake2_body, direction2

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

    snake1 = [(40, 40), (0, 40)]
    snake2 = [(40, 40), (0, 40)]
    snake1_body = []
    snake2_body = []

    for x, y in snake1:
        snake1_body.append(dp_game_canvas_left.create_rectangle(x, y, x + 40, y + 40, fill="white"))

    for x, y in snake2:
        snake2_body.append(dp_game_canvas_right.create_rectangle(x, y, x + 40, y + 40, fill="white"))

    direction1 = "Right"
    direction2 = "Right"

    dp_game_canvas_left.focus_set()
    dp_game_canvas_left.bind("<KeyPress>", handle_keypress)
    dp_game_canvas_right.focus_set()
    dp_game_canvas_right.bind("<KeyPress>", handle_keypress)

    dp_game_canvas_left.after(50, draw_grid1)
    dp_game_canvas_right.after(50, draw_grid2)
    dp_game_canvas_left.after(100, spawn_food1)
    dp_game_canvas_right.after(100, spawn_food2)
    dp_game_canvas_left.after(300, snake_move1)
    dp_game_canvas_right.after(300, snake_move2)


single_player = tk.Button(start_game, text="Single Player", bg="#181818", fg="#f0f0f0", relief="raised", command=sp)
single_player.pack(side='left', pady=(0, 5), fill=tk.BOTH, expand=True)

dual_player = tk.Button(start_game, text="Dual Player", bg="#181818", fg="#f0f0f0", relief="raised", command=dp)
dual_player.pack(side='right', pady=(0, 5), fill=tk.BOTH, expand=True)

root.mainloop()
pygame.init()
