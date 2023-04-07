import unittest
from functions_2048 import *

class TestFunctions2048(unittest.TestCase):
    # ---- TEST GAME FUNCTIONS ----
    def test_initialize_board(self):
        # initialize board
        test_board = []
        test_board = initialize_board(test_board)
        # board should be 4x4
        # rows
        self.assertEqual(len(test_board), 4)
        # columns
        self.assertEqual(len(test_board[0]), 4)


    def test_add_new_number(self):
        # numbers on board, 2 non-zeros, 14 zeros
        test_board_new = [[2, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        # add a new number to board
        test_board_new = add_new_number(test_board_new)
        zeros = 0
        non_zeros = 0
        for row in test_board_new:
            for number in row:
                if number == 0:
                    zeros += 1
                else:
                    non_zeros += 1
        # should be 13 zeros & 3 non-zeros on the board after new number
        self.assertEqual(zeros, 13)
        self.assertEqual(non_zeros, 3)


    def test_add_new_number_full_board(self):
        # numbers on board, 16 total (either 2 or 4)
        test_board_full = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
        # attempt to add a new number to the board
        add_new_number(test_board_full)
        self.assertFalse(add_new_number(test_board_full))

        

def main():
    unittest.main(verbosity = 3)
    
if __name__ == '__main__':
    main()