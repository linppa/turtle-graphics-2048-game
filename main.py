from functions_2048 import *

'''
Linda Quach
CS 5001 - Spring 2023
Final Project - 2048

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

Please refer to README.txt file for more information & controls on the game.
'''

def main():
    '''
    This main() serves as the driver to boot up the 2048 game. This file takes
    imported functions and global variables from functions_2048.py.
    Please run this file to begin the game. Enjoy!
    '''
    # ---- start the 2048 game ----
    new_game()
    turtle.mainloop()
    
    # ---- end game display ----
    print('Thank you for playing 2048! \n')
    
if __name__ == '__main__':
    main()

