import unittest
from functions_2048 import *

class TestFunctions2048(unittest.TestCase):
    # ---- TEST GAME FUNCTIONS ----
    def test_initialize_board(self):
        # initialize board
        global global_game_board
        global_game_board = []
        global_game_board = initialize_board()
        # board should be 4x4
        # rows
        self.assertEqual(len(global_game_board), 4)
        # columns
        self.assertEqual(len(global_game_board[0]), 4)

        

def main():
    unittest.main(verbosity = 3)
    
if __name__ == '__main__':
    main()