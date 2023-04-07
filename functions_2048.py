import turtle
import random

'''
Linda Quach
CS 5001 - Spring 2023
Project - 2048

This program contains the functions used in the 2048 game. It utilizes Python's
Turtle and Random libraries.

The game of 2048 is
a simple 1-player board game, comprising of a 4x4 grid of numbers. The player
starts with two numbers (2 or 4) on the board, and in each turn, the player can
move the numbers up, down, left, or right. If two numbers are of the same value,
the numbers merge into one, and the value of the new number is the sum of the
two, essentially "sliding" the numbers together. The numbers can only slide in a
direction to occupy the farthest blank cell without jumping over another number.

The player's goal is to obtain the number 2048 on the board. The game ends when
this is obtained, or the board is full and no more moves can be made.
'''
# -- GLOBAL VARIABLES --
current_score = 0
game_board = []
font = ('courier', 12, 'normal')
screen = turtle.Screen()
GRID_SIZE = 4

# ---- TURTLE SETUP ----
# start window screen with menu options and score displayed
def start_window():
    screen.setup(600, 600)
    screen.title('CS5001 2048 :D')
    screen.bgcolor('AntiqueWhite')
    
    # text & score
    display_score()
    display_menu()
    
    # key bindings
    key_binding()
    
    turtle.mainloop()


# ---- SCORE FUNCTIONS & TEXTS ----
def update_score():
    pass

# display current score
def display_score():
    global current_score
    score = turtle.Turtle()
    score.hideturtle()
    score.penup()
    score.goto(-250, 200)
    score.write(f"score:{current_score}", font = font)

# display options to restart & close game
def display_menu():
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.goto(-250, 230)
    menu.color('AntiqueWhite4')
    menu.write(f"To end game, press 'E'\n"
               f"To restart,  press 'R'", font = font)
    

# ---- KEY BINDINGS ----
# listen for key presses
def key_binding():
    turtle.listen()
    # turtle.onkey(move_up, 'Up')
    # turtle.onkey(move_down, 'Down')
    # turtle.onkey(move_left, 'Left')
    # turtle.onkey(move_right, 'Right')
    # turtle.onkey(restart, 'r')
    turtle.onkey(screen.bye, 'e')
    
def restart_game():
    global game_board, current_score
    
def move_left():
    pass
def move_right():
    pass
def move_up():
    pass
def move_down():
    pass
    
# ---- GAME FUNCTIONS ----
# create game board
def initialize_board():
    global game_board
    # iterate through 4 rows
    for i in range(GRID_SIZE):
        game_board.append([0] * GRID_SIZE)
    add_new_number()
    add_new_number()
    print(game_board)
    return game_board

# add a new number to the board
def add_new_number():
    global game_board
    #if the board is full, return
    if 0 not in game_board:
        print("Game over!")
        return game_board
    # pick a random row and column
    row = random.randint(0, GRID_SIZE - 1)
    col = random.randint(0, GRID_SIZE - 1)
    # if the cell is empty, add a 2 or 4
    if game_board[row][col] == 0:
        game_board[row][col] = random.choice([2, 4])
    # if the cell is not empty, call the function again
    else:
        add_new_number()
        
def game_over():
    pass