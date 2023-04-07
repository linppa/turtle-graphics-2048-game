from functions_2048 import *

# ---- GLOBAL VARIABLES ----
# current_score imported from functions_2048.py
# game_board imported from functions_2048.py

def main():
    start_window()
    current_board = []
    current_board = initialize_board(current_board)
    print("Current board:")
    print_stacked_list(current_board)
    current_board = add_new_number(current_board)
    print("New number added:")
    print_stacked_list(current_board)
    
    
if __name__ == '__main__':
    main()

