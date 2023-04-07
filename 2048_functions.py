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
score = 0
game_board = []

# -- TURTLE SETUP --
# start window screen with menu options and score displayed
def start_window():
    