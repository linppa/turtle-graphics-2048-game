from functions_2048 import *

# ---- GLOBAL VARIABLES ----
# current_score imported from functions_2048.py
# global_game_board imported from functions_2048.py

def main():
    get_grid_size()
    global global_game_board
    global_game_board = start_board()

    start_window()
    print("current board:")
    print_stacked_list(global_game_board)


    
if __name__ == '__main__':
    main()

