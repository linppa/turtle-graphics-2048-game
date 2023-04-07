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
global_score = 0
global_game_board = []

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


def draw_grid():
    pass


# ---- SCORE FUNCTIONS & DISPLAY TEXTS ----
def get_score():
    global global_score
    return global_score


def update_score(add_points):
    global global_score
    global_score += add_points
    

# display current score
def display_score():
    global global_score
    score = turtle.Turtle()
    score.hideturtle()
    score.penup()
    score.goto(-250, 200)
    score.write(f"score:{global_score}", font = font)

def print_stacked_list(game_board):
    for row in game_board:
        print(row)
    print('')
    

# display options to restart & close game
def display_menu():
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.goto(-250, 230)
    menu.color('AntiqueWhite4')
    menu.write(f"To end game, press 'E'\n"
               f"To restart,  press 'R'", font = font)


def game_over():
    print("Game over!")
    

# ---- KEY BINDINGS ----
# listen for key presses
def key_binding():
    turtle.listen()
    # turtle.onkey(move_up, 'Up')
    # turtle.onkey(move_down, 'Down')
    turtle.onkey(move_left, 'Left')
    # turtle.onkey(move_right, 'Right')
    turtle.onkey(restart_game, 'r')
    turtle.onkey(screen.bye, 'e')
    
def restart_game():
    global global_game_board, global_score
    global_game_board = []
    global_score = 0
    global_game_board = start_board()

    
def move_left():
    global global_game_board
    print("Move Left:")
    for row in global_game_board:
        # combine adjacent matching numbers
        for i in range(GRID_SIZE - 1, 0, -1):
            if row[i] != 0:
                for j in range(i-1, -1, -1):
                    if row[j] != 0:
                        if row[i] == row[j]:
                            row[i], row[j] = (row[i] * 2), 0
                        break
        # shift all non-zero numbers to the left
        # new list containing all non-zero numbers in the current row
        non_zero_numbers = [number for number in row if number != 0]
        # empty spaces in row
        empty_spaces = GRID_SIZE - len(non_zero_numbers)
        # new list of zeroes with length = to number of empty space
        zeroes = [0] * empty_spaces
        new_row = non_zero_numbers + zeroes
        row[:] = new_row
    
    add_new_number()
    print_stacked_list(global_game_board)
    return global_game_board
    
def move_right():
    pass
def move_up():
    pass
def move_down():
    pass
    
# ---- GAME FUNCTIONS ----
# create game board
def initialize_board():
    global global_game_board
    # iterate through 4 rows
    for size in range(GRID_SIZE):
        # create a list of 4 zeros
        global_game_board.append([0] * GRID_SIZE)
    
    # add two numbers to the board
    add_new_number()
    add_new_number()

    return global_game_board

# starting board ready with 2 numbers
def start_board():
    global global_game_board
    global_game_board = initialize_board()
    print_stacked_list(global_game_board)
    return global_game_board


# add a new number to the board
def add_new_number():
    global global_game_board
    print(f"globacl board before add new number: {global_game_board}")
    random_row = 0
    random_column = 0
    
    #if the board is full, return
    if 0 not in [i for row in global_game_board for i in row]:
        game_over()
        return global_game_board
    
    while True:
        # pick a random row and column
        random_row = random.randint(0, GRID_SIZE - 1)
        random_column = random.randint(0, GRID_SIZE - 1)
        # if the cell is empty, add a 2 or 4
        if global_game_board[random_row][random_column] == 0:
            break
    
    global_game_board[random_row][random_column] = random.choice([2, 4])
    # if the cell is not empty, call the function again
    return global_game_board