import unittest
from functions_2048 import initialize_board, add_new_number, check_game_over, check_win, update_score, move_left, move_right, move_up, move_down


class TestFunctions2048(unittest.TestCase):
    ''' TestFunctions2048() serves as a test class for functions_2048.py
        We will be testing functions with core game functionality, such as
        initialize_board(), add_new_number(), check_game_over(), check_win(),
        update_score(), move_left(), move_right(), move_up(), and move_down().
        Functions that heavily rely on turtle will not be tested due to
        crashing unittests.
    '''
    
    # ---- TEST CORE GAME FUNCTIONS ----
    def test_initialize_board(self):
        '''
        test_initialize_board() serves as a test function for
        initialize_board() which creates an empty game board & adds two random
        numbers, then returns the updated board.
        '''
        # ---- TESTING BOARDS ----
        blank_board = []
        actual_4x4_board = initialize_board(4, blank_board)
        blank_board = []
        actual_5x5_board = initialize_board(5, blank_board)
        blank_board = []
        actual_6x6_board = initialize_board(6, blank_board)
        blank_board = []
        # ---- TEST CASES ----
        # TEST CASE 1: 4x4 board should be a list
        self.assertIsInstance(actual_4x4_board, list)
        # TEST CASE 2: length of main list (columns) should be 4
        self.assertEqual(len(actual_4x4_board), 4)
        # TEST CASE 3: length of nested list (rows) should be 4
        for row in actual_4x4_board:
            self.assertEqual(len(row), 4)
        # TEST CASE 4: sum of all numbers is zero
        total = 0
        for row in actual_4x4_board:
            for num in row:
                total += num
        self.assertEqual(total, 0)
        # TEST CASE 5: 5x5 board should be a list
        self.assertIsInstance(actual_5x5_board, list)
        # TEST CASE 6: length of main list (columns) should be 5
        self.assertEqual(len(actual_5x5_board), 5)
        # TEST CASE 7: length of nested list (rows) should be 5
        for row in actual_5x5_board:
            self.assertEqual(len(row), 5)
        # TEST CASE 8: sum of all numbers is zero
        total = 0
        for row in actual_5x5_board:
            for num in row:
                total += num
        self.assertEqual(total, 0)
        # TEST CASE 9: 6x6 board should be a list
        self.assertIsInstance(actual_6x6_board, list)
        # TEST CASE 10: length of main list (columns) should be 6
        self.assertEqual(len(actual_6x6_board), 6)
        # TEST CASE 11: length of nested list (rows) should be 6
        for row in actual_6x6_board:
            self.assertEqual(len(row), 6)
        # TEST CASE 12: sum of all numbers is zero
        total = 0
        for row in actual_6x6_board:
            for num in row:
                total += num
        self.assertEqual(total, 0)
        

    def test_check_game_over(self):
        '''
        test_check_game_over() serves as a test function for check_game_over()
        which checks if game is over, and returns True if game over, or False
        if valid moves remain.
        '''
        # ---- TESTING BOARDS ----
        blank_board = ([[0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0]])
        false_lose = check_game_over(4, blank_board)
        full_board = ([[2, 4, 2, 4],
                       [4, 2, 4, 2],
                       [2, 4, 2, 4],
                       [4, 2, 4, 2]]) 
        true_lose = check_game_over(4, full_board)
        full_board2 = ([[8, 8, 8, 4],
                       [4, 8, 8, 2],
                       [8, 8, 2, 4],
                       [4, 2, 4, 8]])
        false_lose2 = check_game_over(4, full_board2)
        
        # ---- TEST CASES ----
        # TEST CASE 1: if board is empty, game not over
        self.assertFalse(false_lose)
        # TEST CASE 2: if board is full, game over
        self.assertTrue(true_lose)
        # TEST CASE 3: if board is full, but move is possible, game not over
        self.assertFalse(false_lose2)

   
    def test_check_win(self):
        '''
        test_check_win() serves as a test function for check_win() which checks
        if the player has won the game, and returns True if player has won, or
        False if player has not won.
        '''
        # ---- TESTING BOARDS ----
        blank_board = ([[0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0]])
        false_win = check_win(blank_board)
        win_board = ([[2, 4, 2, 4],
                      [4, 2, 4, 2],
                      [2, 4, 2, 4],
                      [4, 2, 4, 2048]])
        true_win = check_win(win_board)
        
        # ---- TEST CASES ----
        # TEST CASE 1: if board doesn't contain 2048, no win
        self.assertFalse(false_win)
        # TEST CASE 2: if board contains 2048, win
        self.assertTrue(true_win)


    def test_update_score(self):
        '''
        test_update_score() serves as a test function for update_score() which
        adds the score to the current score, then returns the updated score.
        '''
        # ---- TESTING SCORES ----
        global current_score
        current_score = 0
        actual_score_add2 = update_score(2)
        actual_score_add40 = update_score(40)
        actual_score_add100 = update_score(100)
        actual_score_add0 = update_score(0)
        current_score = 0
        
        # ---- TEST CASES ----
        # TEST CASE 1: score should change
        self.assertNotEqual(current_score, actual_score_add2)
        # TEST CASE 2: add 2 to current score of 0 = 2
        self.assertEqual(actual_score_add2, 2)
        # TEST CASE 3: add 40 to current score of 2 = 42
        self.assertEqual(actual_score_add40, 42)
        # TEST CASE 4: add 100 to current score of 42 = 142
        self.assertEqual(actual_score_add100, 142)
        # TEST CASE 5: add zero to current score = 142
        self.assertEqual(actual_score_add0, 142)


    def test_move_left(self):
        '''
        test_move_left() serves as a test function for move_left() which
        moves all numbers to the left, then returns the updated board.
        '''
        # ---- TESTING BOARDS ----
        test_board = ([[0, 8, 0, 0],
                       [0, 0, 0, 2],
                       [0, 0, 4, 2],
                       [16, 0, 8, 0]])
        actual_board = move_left(4, test_board)
        test_board = ([[0, 8, 0, 0],
                       [0, 0, 0, 2],
                       [0, 0, 4, 2],
                       [16, 0, 8, 0]])
        test_board2 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [8, 8, 0, 2],
                       [0, 0, 0, 0]])
        actual_board2 = move_left(4, test_board)
        test_board2 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [8, 8, 0, 2],
                       [0, 0, 0, 0]])
        test_board3 = ([[0, 0, 0, 0],
                       [8, 0, 0, 0],
                       [4, 0, 0, 0],
                       [2, 0, 0, 0]])
        actual_board3 = move_left(4, test_board3)
        test_board3 = ([[0, 0, 0, 0],
                       [8, 0, 0, 0],
                       [4, 0, 0, 0],
                       [2, 0, 0, 0]])
        
        # ---- TEST CASES ----
        # TEST CASE 1: numbers should move to the left, & add new number
        self.assertNotEqual(test_board, actual_board)
        # TEST CASE 2: numbers should move to the left, & merge same numbers
        self.assertNotEqual(test_board2, actual_board2)
        # TEST CASE 3: merged number should now be a 16
        for row in actual_board2:
            for num in row:
                if num == 16:
                    self.assertEqual(num, 16)
        # TEST CASE 4: board should remain original grid size
        self.assertEqual(len(actual_board), 4)
        # TEST CASE 5: cannot move left if no numbers to merge/move
        self.assertEqual(test_board3, actual_board3)


    def test_move_right(self):
        '''
        test_move_right() serves as a test function for move_right() which
        moves all numbers to the right, then returns the updated board. 
        '''
        # ---- TESTING BOARDS ----
        test_board_right = ([[2, 8, 0, 0],
                       [2, 0, 0, 0],
                       [4, 0, 8, 16],
                       [0, 2, 8, 0]])
        actual_board = move_right(4, test_board_right)
        test_board_right = ([[2, 8, 0, 0],
                       [2, 0, 0, 0],
                       [4, 0, 8, 16],
                       [0, 2, 8, 0]])
        test_board2 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [16, 16, 0, 2],
                       [0, 4, 0, 0]])
        actual_board2 = move_right(4, test_board_right)
        test_board2 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [16, 16, 0, 2],
                       [0, 4, 0, 0]])
        test_board3 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [0, 0, 0, 8],
                       [0, 0, 0, 4]])
        actual_board3 = move_right(4, test_board3)
        test_board3 = ([[0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [0, 0, 0, 8],
                       [0, 0, 0, 4]])
        
        # ---- TEST CASES ----
        # TEST CASE 1: numbers should move to the right, & add new number
        self.assertNotEqual(test_board_right, actual_board)
        # TEST CASE 2: numbers should move to the right, & merge same numbers
        self.assertNotEqual(test_board2, actual_board2)
        # TEST CASE 3: merged number should now be a 32
        for row in actual_board2:
            for num in row:
                if num == 32:
                    self.assertEqual(num, 32)
        # TEST CASE 4: board should remain original grid size
        self.assertEqual(len(actual_board), 4)
        # TEST CASE 5: cannot move right if no numbers to merge/move
        self.assertEqual(test_board3, actual_board3)


    def test_add_new_number(self):
        '''
        test_add_new_number() serves as a test function for add_new_number()
        which adds a new number (2 or 4) to the board, then returns the updated
        board.
        '''
        # ---- TESTING BOARDS ----
        blank_board = ([[0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0]])
        actual_board = add_new_number(4, blank_board)
        blank_board = ([[0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0], 
                       [0, 0, 0, 0]])
        full_board = ([[2, 4, 2, 4],
                       [4, 2, 4, 2],
                       [2, 4, 2, 2],
                       [4, 2, 4, 2]])

        # ---- TEST CASES ----
        # TEST CASE 1: numbers added should be 2 or 4
        for row in actual_board:
            for num in row:
                self.assertIn(num, [0, 2, 4])
        # TEST CASE 2: board should be changed with new added number
        for row in actual_board:
            for num in row:
                self.assertNotEqual(blank_board, actual_board)
        # TEST CASE 3: sum of all numbers is even
        total = 0
        for row in actual_board:
            for num in row:
                total += num
            self.assertEqual(total % 2, 0)
        # TEST CASE 4: board should remain original grid size
        self.assertEqual(len(actual_board), 4)


    def test_move_up(self):
        '''
        test_move_up() serves as a test function for move_up() which moves all
        numbers up, then returns the updated board.
        '''
        # ---- TESTING BOARDS ----
        test_board_up = ([[2, 0, 8, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [16, 4, 0, 0]])
        actual_board = move_up(4, test_board_up)
        test_board_up = ([[2, 0, 8, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 2],
                       [16, 4, 0, 0]])
        test_board2 = ([[32, 0, 0, 0],
                       [0, 0, 0, 2],
                       [32, 8, 0, 2],
                       [0, 4, 0, 0]])
        actual_board2 = move_up(4, test_board_up)
        test_board2 = ([[32, 0, 0, 0],
                       [0, 0, 0, 2],
                       [32, 8, 0, 2],
                       [0, 4, 0, 0]])
        test_board3 = ([[0, 8, 2, 4],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]])
        actual_board3 = move_up(4, test_board3)
        test_board3 = ([[0, 8, 2, 4],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0]])
        
        # ---- TEST CASES ----
        # TEST CASE 1: numbers should move up, & add new number
        self.assertNotEqual(test_board_up, actual_board)
        # TEST CASE 2: numbers should move up, & merge same numbers
        self.assertNotEqual(test_board2, actual_board2)
        # TEST CASE 3: merged number should now be a 64
        for row in actual_board2:
            for num in row:
                if num == 64:
                    self.assertEqual(num, 64)
        # TEST CASE 4: board should remain original grid size
        self.assertEqual(len(actual_board), 4)
        # TEST CASE 5: cannot move up if no numbers to merge/move
        self.assertEqual(test_board3, actual_board3)
        
        
    def test_move_down(self):
        '''
        test_move_down() serves as a test function for move_down() which moves
        all numbers down, then returns the updated board.
        '''
        # ---- TESTING BOARDS ----
        test_board_down = ([[8, 32, 0, 0],
                       [0, 0, 0, 0],
                       [2, 0, 16, 2],
                       [0, 4, 0, 0]])
        actual_board = move_down(4, test_board_down)
        test_board_down = ([[8, 32, 0, 0],
                       [0, 0, 0, 0],
                       [2, 0, 16, 2],
                       [0, 4, 0, 0]])
        test_board2 = ([[64, 0, 0, 0],
                       [0, 0, 0, 2],
                       [64, 8, 0, 2],
                       [0, 4, 0, 0]])
        actual_board2 = move_down(4, test_board_down)
        test_board2 = ([[64, 0, 0, 0],
                       [0, 0, 0, 2],
                       [64, 8, 0, 2],
                       [0, 4, 0, 0]])
        test_board3 = ([[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 4, 8, 2]])
        actual_board3 = move_down(4, test_board3)
        test_board3 = ([[0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 0, 0, 0],
                       [0, 4, 8, 2]])
        
        # ---- TEST CASES ----
        # TEST CASE 1: numbers should move down, and add new number
        self.assertNotEqual(test_board_down, actual_board)
        # TEST CASE 2: numbers should move down, and merge same numbers
        self.assertNotEqual(test_board2, actual_board2)
        # TEST CASE 3: merged number should now be a 128
        for row in actual_board2:
            for num in row:
                if num == 128:
                    self.assertEqual(num, 128)
        # TEST CASE 4: board should remain original grid size
        self.assertEqual(len(actual_board), 4)
        # TEST CASE 5: cannot move down if no numbers to merge/move
        self.assertEqual(test_board3, actual_board3)


def main():
    ''' main() serves as the test driver for the program, utilizing
        unittest.main() to run all test cases.
    '''
    unittest.main(verbosity = 2)

if __name__ == '__main__':
    main()