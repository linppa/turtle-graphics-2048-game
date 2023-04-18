import turtle
import random

'''
Linda Quach
CS 5001 - Spring 2023
Final Project - 2048

This program contains the functions used in the 2048 game. Utilizes Python's
Turtle and Random libraries as import.

The game of 2048 is a simple 1-player board game, comprising of a 4x4 grid of
numbers. The player starts with two numbers (2 or 4) on the board, and in each
turn, the player can move the numbers up, down, left, or right. 

If two numbers are of the same value, the numbers merge into one, & the value
of the new number is the sum of the two, essentially "sliding" the numbers
together. The numbers can only slide in a direction to occupy the farthest
cell without jumping over another number. 

The player's goal is to obtain the number 2048 on the board. Game ends when
this is obtained, or the board is full and no more moves can be made. If the
player obtains a win, they may continue playing until the board is full.

Resources & referenced materials:
https://cs111.wellesley.edu/labs/lab02/colors
https://www.geeksforgeeks.org/2048-game-in-python/#
https://www.geeksforgeeks.org/turtle-shape-function-in-python/
https://youtu.be/b4XP2IcI-Bg 
'''
# ---- GLOBAL GAME VARIABLES ----
current_score = 0


# ---- GLOBAL INTERFACE VARIABLES ----
# turtle staff members
screen = turtle.Screen()
screen.tracer(0, 0)
score = turtle.Turtle()
grid = turtle.Turtle()
number = turtle.Turtle()
game_over = turtle.Turtle()
win = turtle.Turtle()
# frequently used fonts
font = ('courier', 12, 'normal')
font2 = ('courier', 20, 'normal')


# ---- GAME WINDOW SETUP FUNCTIONS ----

def start_window(grid_size):
    '''
    start_window() is a helper function that presents window setup -- 
        opening an appropriately sized window, calling functions to draw the
        initial grid, score, & menu options.
    Parameters: 
        grid_size (int), the size of the grid
    Returns: 
        none
    '''
    # open appropriate window based on grid size
    if grid_size == 4:
        screen.setup(650, 750)
    elif grid_size == 5:
        screen.setup(730, 800)
    elif grid_size == 6:
        screen.setup(750, 870)
    # title & background color
    screen.title('CS5001 2048 :)')
    screen.bgcolor('seashell2')


def get_grid_size():
    '''
    get_grid_size() takes input from user to determine size of grid. Input is
        taken through the turtle input window so it does not explicity 
        take in a parameter.
    Parameters: 
        none
    Raises: 
        ValueError if input is not a number from 4-6, prints error message
        to the terminal and prompts user to re-enter input through the turtle
        window. Raises won't terminate the program, but will continue to
        reprompt the user until valid input is entered.
    Returns: 
        grid_size, the size of the grid
    '''
    # initialize turtle input window
    size = turtle.Screen()
    size.setup(450, 450)
    screen.bgcolor('seashell2')
    size.title("Welcome to CS5001 2048 :)")
    # display instructions
    size_turtle = turtle.Turtle()
    size_turtle.hideturtle()
    size_turtle.penup()
    size_turtle.goto(-115, 80)
    size_turtle.color('AntiqueWhite4')
    size_turtle.write(f"Please type in a number from 4-6: \n\n"
                    f"Click 'OK' to begin! \n"
                    f"Click 'X' on your window to exit.", font = font)
    # get input from user, reprompt until valid input of 4-6
    grid_size = 0
    while grid_size < 4:
        try:
            input = int(size.textinput("Game board size?", 
                                    "Enter a number from 4-6:"))
            if input > 6:
                # reprompt if input is greater than 6
                continue
            else:
                # if input is valid, assign to grid_size
                grid_size = input
        except ValueError:
            print("Please enter a number that is either 4, 5, or 6.")
            continue
        except TypeError:
            print("Please enter only numbers.")
            continue
    # clear instructions from input window
    size_turtle.clear()
    return grid_size


def draw_grid(grid_size, board):
    '''
    draw_grid() creates blocks from square turtles, & stamps them on the game
        board. Numbers are written on top of the blocks, if they are not 0.
    Parameters:
        grid_size (int), the size of the grid
        board (list), the game board
    Returns: none
    '''
    # clear grid & numbers each time function called
    grid.hideturtle()
    grid.clear()
    number.clear()
    grid.speed(0)
    grid.penup()
    # create square turtle & stretch it
    grid.shape('square')
    grid.shapesize(4, 4, 10)
    # dictionary of colors for each number
    color_dictionary = {0: 'AntiqueWhite4', 2: 'AntiqueWhite3', 4: 'wheat3', 
                        8: 'goldenrod3', 16: 'DarkGoldenrod2', 
                        32: 'goldenrod1', 64: 'sienna3', 128: 'sienna2', 
                        256: 'sienna4', 512: 'DarkSeaGreen4', 
                        1024: 'DarkSeaGreen3', 2048: 'CadetBlue3', 
                        4096: 'CadetBlue4', 8192: 'DarkSlateGray4'}
    # stamp grid at coordinates
    y_coordinate = 125
    for row in range(grid_size):
        x_coordinate = -90
        for column in range(grid_size):
            grid.goto(x_coordinate - 120, y_coordinate + 10)
            # if a number on the board is in the dictionary, add colors
            if board[row][column] in color_dictionary:
                grid.color(color_dictionary[board[row][column]])
            else:
                grid.color('AntiqueWhite4')
            grid.stamp()
            # if the number is not 0, write it on the block
            if board[row][column] != 0:
                number.hideturtle()
                number.color('white')
                number.penup()
                number.goto(x_coordinate - 120, y_coordinate - 5)
                number.write(str(board[row][column]), 
                            align = 'center', 
                            font=("courier", 25, "bold"))
            x_coordinate += 96
        y_coordinate -= 96


# ---- SCORE FUNCTIONS & DISPLAY TEXTS ----

def update_score(add_points: int):
    '''
    update_score() takes in the number of points to add to current score, &
        returns the updated score. It also updates the global variable.
    Parameters:
        add_points (int), the number of points to add to current score
    Returns:
        current_score (int), the updated score
    '''
    global current_score
    #add points to current score
    current_score += add_points
    return current_score


def display_score():
    '''
    display_score() displays the current score on game board using turtle.
        It refreshes the score every time it is called using the turtle.
    Parameters: 
        none
    Returns: 
        current_score (int), the current score
    '''
    global current_score
    # clear previous score
    score.clear()
    score.hideturtle()
    score.penup()
    score.goto(-280, 270)
    score.color('sienna')
    # write current score
    score.write(f"Score:{current_score}", font = font)
    return current_score


def print_stacked_list(game_board):
    '''
    print_stacked_list() is a helper function that prints game board to the
        terminal in a grid format to make it easier to visualize. 
    Parameters:
        game_board (list), the game board
    Returns:
        none, prints game board to terminal
    '''
    for row in game_board:
        print(row)
    print('')
    
    
def display_menu():
    '''
    display_menu() displays the menu options on the turtle screen
        to the user. It is visible at all times during the game aside from 
        when user is inputting a grid size.
    Parameters:
        none
    Returns:
        none
    '''
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.goto(-280, 300)
    menu.color('AntiqueWhite4')
    menu.write(f"To end game, press 'e'\n"
            f"To restart,  press 'r'", font = font)


def display_game_over():
    '''
    display_game_over() displays the game over text on the turtle screen. It
        is visible when check_game_over() confirms that the game is over.
    Parameters:
        none
    Returns:
        none
    '''
    game_over.hideturtle()
    win.clear()
    game_over.clear()
    game_over.penup()
    game_over.goto(-280, 200)
    game_over.color('firebrick2')
    game_over.write(f"GAME OVER!\n", font = font2)


def display_win():
    '''
    display_win() displays the win text on the turtle screen. It
        is visible when check_win() confirms that the user has won the game.
        The user can continue to play after winning.
    Parameters:
        none
    Returns:
        none
    '''
    win.hideturtle()
    win.clear()
    win.penup()
    win.goto(-280, 200)
    win.color('PaleGreen4')
    win.write(f"YOU WIN!\n", font = font2)
    # thank you message in terminal & on game window :)
    print('Thank you for playing 2048! \n& for helping us learn \n'
        'throughout the semester, \n'
        'to make this game possible! :)\n')
    win.goto(10, 260)
    win.color('PaleGreen4')
    win.write(f'Thank you for playing 2048! \n& for helping us learn \n'
                    'throughout the semester, \n'
                    'to make this game possible! :)', font = font)


# ---- KEY BINDINGS ----

def key_binding(grid_size, board):
    '''
    key_binding() binds the arrow keys to the move functions, & the 'r' key
        to the new_game() function. It also binds the 'e' key to the exit
        function to close the game window with turtle.
    Parameters:
        grid_size (int), the size of the game board
        board (list), the game board
    Returns:
        none
    '''
    # bind arrow keys to move functions, 'r' to new_game(), 'e' to exit
    turtle.listen()
    turtle.onkey(lambda: move_up(grid_size, board), 'Up')
    turtle.onkey(lambda: move_down(grid_size, board), 'Down')
    turtle.onkey(lambda: move_left(grid_size, board), 'Left')
    turtle.onkey(lambda: move_right(grid_size, board), 'Right')
    turtle.onkey(new_game, 'r')
    turtle.onkey(new_game, 'R')
    turtle.onkey(screen.bye, 'e')
    turtle.onkey(screen.bye, 'E')
    # bind error function to all other 'invalid' keys
    for key in ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', '0', 'space',
                'Escape', 'BackSpace', 'Tab', 'Caps_Lock',
                'Control_L', 'Control_R',
                'Alt_L', 'Alt_R', 'Pause', 'Scroll_Lock', 'Home',
                'Insert', 'Delete', 'End', 'Page_Up', 'Page_Down',
                'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                'F9', 'F10', 'F11', 'F12', '<', '>', '?', '/',
                ':', ';', '"', "'", '[', ']', '{', '}', '|',
                '+', '-', '*', '=', '_', '(', ')', '&', '^',
                '%', '$', '#', '@', '!', '~', '`', 'comma', 'period']:
        turtle.onkey(key_error, key)
    
    
def key_error():
    '''
    key_error() is a helper function that displays an error message on the
        turtle screen when the user inputs an invalid key. The error message
        is brielfy visible on the screen for a second before it is cleared.
    Parameters:
        none
    Returns:
        none
    '''
    # print error message in terminal
    print('Invalid key!')
    key_error = turtle.Turtle()
    key_error.hideturtle()
    key_error.penup()
    key_error.goto(10, 200)
    key_error.color('firebrick2')
    # display error message on turtle screen
    key_error.write(f"Invalid key! Try again.", font = font)
    # clear error message after a second
    turtle.ontimer(key_error.clear, 500)


# ---- CORE GAME FUNCTIONS ----

def new_game():
    '''
    new_game() is a helper function that brings together all the functions
    that allow the game to run. Can be called to start the game, or restart
    the game.
    Notably, it starts by clearing the turtle screen, board, scores, & begins
    the game with the keybinding used for the controls of the game. 
    Parameters: 
        None
    Returns: 
        board (list): the new game board
        current_score (int): the new score
    '''
    # reset variables
    global current_score
    board = []
    current_score = 0
    # turtle clean up crew
    grid.clear()
    number.clear()
    game_over.clear()
    win.clear()
    # reboot game, new board
    grid_size = get_grid_size()
    board = initialize_board(grid_size, board)
    # add two numbers to board
    add_new_number(grid_size, board)
    add_new_number(grid_size, board)
    #print board to terminal
    print_stacked_list(board)
    # open turtle window, with key bindings
    start_window(grid_size)
    key_binding(grid_size, board)
    # display board, score, & menu
    draw_grid(grid_size, board)
    display_score()
    display_menu()
    return board, current_score


def move_left(grid_size, board):
    '''
    move_left() moves all the numbers on the board to the left, combining
        adjacent matching numbers, & adding a new number to the board. After
        a move is made, the board draws to the turtle screen, the score is
        updated, and the game is checked for a win or loss.
    Parameters:
        grid_size (int), the size of the game board
        board (list), the game board
    Returns:
        board (list), the updated game board
    '''
    print('left:')
    # initiate check for valid moves
    valid_move = False
    for row in board:
        # combine adjacent matching numbers 'i' & 'j'
        for i in range(0, grid_size - 1,):
            if row[i] != 0:
                for j in range(i+1, grid_size):
                    if row[j] != 0:
                        # combine numbers into 'i' & make zero 'j' if match
                        if row[i] == row[j]:
                            row[i], row[j] = (row[i] * 2), 0
                            # update score
                            update_score((row[i]))
                            # valid move was made
                            valid_move = True
                        break
        # shift non-zero numbers to left by counting empty spaces in row
        non_zero_numbers = [number for number in row if number != 0]
        empty_spaces = grid_size - len(non_zero_numbers)
        # for each empty space, add a zero
        zeroes = [0] * empty_spaces
        new_row = non_zero_numbers + zeroes
        # if new row is different, valid move was made
        if row != new_row:
            valid_move = True
        # update row
        row[:] = new_row
    # if valid move was made, add new number to board
    if valid_move == True:
        add_new_number(grid_size, board)
        display_score()
    else:
        print("Invalid move!")
    # check for win/loss, draw board, print to terminal
    check_game_over(grid_size, board)
    check_win(board)
    draw_grid(grid_size, board)
    print_stacked_list(board)
    return board


def move_right(grid_size, board):
    '''
    move_right() moves all the numbers on the board to the right, combining
        adjacent matching numbers, & adding a new number to the board. After
        a move is made, the board draws to the turtle screen, the score is
        updated, and the game is checked for a win or loss.
    Parameters:
        grid_size (int), the size of the game board
        board (list), the game board
    Returns:
        board (list), the updated game board
    '''
    print('right:')
    # initiate check for valid moves
    valid_move = False
    for row in board:
        # combine adjacent matching numbers 'i' & 'j'
        for i in range(grid_size - 1, 0, -1):
            if row[i] != 0:
                for j in range(i-1, -1, -1):
                    if row[j] != 0:
                        # combine numbers into 'i' & make zero 'j' if match
                        if row[i] == row[j]:
                            row[i], row[j] = (row[i] * 2), 0
                            # update score
                            update_score((row[i]))
                            # valid move was made
                            valid_move = True
                        break
        # shift non-zero numbers to left by counting empty spaces in row
        non_zero_numbers = [number for number in row if number != 0]
        empty_spaces = grid_size - len(non_zero_numbers)
        # for each empty space, add a zero
        zeroes = [0] * empty_spaces
        new_row = zeroes + non_zero_numbers
        # if new row is different, valid move was made
        if row != new_row:
            valid_move = True
        # update row
        row[:] = new_row
    # if valid move was made, add new number to board
    if valid_move == True:
        add_new_number(grid_size, board)
        display_score()
    else:
        print("Invalid move!")
    # check for win/loss, draw board, print to terminal
    check_game_over(grid_size, board)
    check_win(board)
    draw_grid(grid_size, board)
    print_stacked_list(board)
    return board


def move_up(grid_size, board):
    '''
    move_up() moves all the numbers on the board up, combining
        adjacent matching numbers, & adding a new number to the board. After
        a move is made, the board draws to the turtle screen, the score is
        updated, and the game is checked for a win or loss.
    Parameters:
        grid_size (int), the size of the game board
        board (list), the game board
    Returns:
        board (list), the updated game board
    '''
    print('up:')
    # initiate check for valid moves
    valid_move = False
    for column in range(grid_size):
        # combine above/below matching numbers 'i' & 'j'
        for i in range(grid_size - 1):
            if board[i][column] != 0:
                for j in range(i+1, grid_size):
                    if board[j][column] != 0:
                        # combine numbers into 'i' & make zero 'j' if match
                        if board[i][column] == board[j][column]:
                            board[i][column], board[j][column] = (board[i]
                                                                [column] 
                                                                * 2), 0
                            # update score
                            update_score((board[i][column]))
                            # valid move was made
                            valid_move = True
                        break
        # shift non-zero numbers up by counting empty spaces in column
        non_zero_numbers = [number for number in [row[column] for 
                                                row in board] if number != 0]
        empty_spaces = grid_size - len(non_zero_numbers)
        # for each empty space, add a zero
        zeroes = [0] * empty_spaces
        new_column = non_zero_numbers + zeroes
        # if new column is different, valid move was made
        if [row[column] for row in board] != new_column:
            valid_move = True
        # update columns
        for i in range(grid_size):
            board[i][column] = new_column[i]
    # if valid move was made, add new number to board
    if valid_move == True:
        add_new_number(grid_size, board)
        display_score()
    else:
        print("Invalid move!")
    # check for win/loss, draw board, print to terminal
    check_game_over(grid_size, board)
    check_win(board)
    draw_grid(grid_size, board)
    print_stacked_list(board)
    return board


def move_down(grid_size, board):
    '''
    move_down() moves all the numbers on the board down, combining
        adjacent matching numbers, & adding a new number to board. After
        a move is made, the board draws to the turtle screen, the score is
        updated, and the game is checked for a win or loss.
    Parameters:
        grid_size (int), the size of the game board
        board (list), the game board
    Returns:
        board (list), the updated game board
    '''
    print('down:')
    # initiate check for valid moves
    valid_move = False
    for column in range(grid_size):
        # combine above/below matching numbers 'i' & 'j'
        for i in range(grid_size - 1, 0, -1):
            if board[i][column] != 0:
                for j in range(i-1, -1, -1):
                    if board[j][column] != 0:
                        # combine numbers into 'i' & make zero 'j' if match
                        if board[i][column] == board[j][column]:
                            board[i][column], board[j][column] = (board[i]
                                                                [column] 
                                                                * 2), 0
                            # update score
                            update_score((board[i][column]))
                            # valid move was made
                            valid_move = True
                        break
        # shift non-zero numbers down by counting empty spaces in column
        non_zero_numbers = [number for number in [row[column] for 
                                                row in board] if number != 0]
        empty_spaces = grid_size - len(non_zero_numbers)
        # for each empty space, add a zero
        zeroes = [0] * empty_spaces
        new_column = zeroes + non_zero_numbers
        # if new column is different, valid move was made
        if [row[column] for row in board] != new_column:
            valid_move = True
        # update columns
        for i in range(grid_size):
            board[i][column] = new_column[i]
    # if valid move was made, add new number to board
    if valid_move == True:
        add_new_number(grid_size, board)
        display_score()
    else:
        print("Invalid move!")
    # check for win/loss, draw board, print to terminal
    check_game_over(grid_size, board)
    check_win(board)
    draw_grid(grid_size, board)
    print_stacked_list(board)
    return board


def initialize_board(grid_size, board):
    '''
    initialize_board() takes an empty list and creates a nested list of zeros
        depending on the grid size, thus creating the game board.
    Parameters:
        grid_size (int): the size of the game board, as an integer
        board (list): the global game board, as a nested list
    Pre-conditions:
        board (list) must be an empty list, for example: board = []
    Returns:
        board (list): the game board, as a nested list of zeros, created from
        the given empty list
    '''
    # iterate through grid_size rows
    for size in range(grid_size):
        # create a nested list of zeros
        board.append([0] * grid_size)
    return board


def add_new_number(grid_size, board):
    '''
    add_new_number() adds a new number to the game board. The new number
        is either 2 or 4, & is added to a random empty spot on the
        board. An empty spot is defined as a 0 on the board.
    Parameters:
        grid_size (int): the size of the game board, as an integer
        board (list): the global game board, as a nested list
    Pre-conditions:
        board () must be a nested list, with an "empty" spot on the board,
        meaning there must be a 0 in the list
    Returns:
        board (list): the updated game board, as a nested list, with the
            new number added to a random empty spot on the board.
    '''
    # check for empty spot
    while True:
        # pick random row & column with appropriate grid size
        random_row = random.randint(0, grid_size - 1)
        random_column = random.randint(0, grid_size - 1)
        # if spot on grid is empty, break out of check loop
        if board[random_row][random_column] == 0:
            break
    # update the board with either 2 or 4
    board[random_row][random_column] = random.choice([2, 4])
    print('number added.')
    return board


def check_game_over(grid_size, board):
    '''
    check_game_over() checks if the game is over. Game is over if the board
        is full & there are no adjacent matching numbers. If game is over,
        the function displays a game over message.
    Parameters:
        grid_size (int): the size of the game board, as an integer
        board (list): the game board, as a nested list
    Returns:
        True (boolean): if the game is over, prints a game over 
            message to the user.
    '''
    # check each row for 0, meaning board not full
    for row in board:
        for number in row:
            if number == 0:
                return False
    # check for any left/right matching numbers, meaning moves possible
    for row in board:
        for i in range(grid_size - 1):
            if row[i] == row[i+1]:
                return False
    # check for any up/down matching numbers, meaning moves possible
    for i in range(grid_size):
        for j in range(grid_size - 1):
            if board[j][i] == board[j+1][i]:
                return False
    # if no 0s & no matching numbers, display turtle GAME OVER
    display_game_over()
    print('GAME OVER!')
    return True


def check_win(board):
    '''
    check_win() checks if the user has won the game. User wins if they have
        2048 on the board. If there is a win, function calls display_win()
        turtle to display winning message. User may continue to play after
        winning.
    Parameters:
        board (list): the game board, as a nested list, to check for win
    Pre-conditions:
        board (list) must be a nested list, with 2048 on the board to win,
        otherwise the game will continue
    Returns:
        True (boolean): user has won, prints a winning message to the screen
        False (boolean): user has not won, game continues
    '''
    # check each row for 2048, meaning win
    for row in board:
        for number in row:
            if number == 2048:
                display_win()
                print('YOU WIN!')
                return True
    # otherwise no win
    return False