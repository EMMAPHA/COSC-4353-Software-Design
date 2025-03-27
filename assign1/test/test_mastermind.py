import unittest
from src.mastermind import guess, Match, Colors, play, GameStatus, MAX_ATTEMPTS, select_colors

EXACT = Match.EXACT
NO_MATCH = Match.NO_MATCH
INCORRECT_POSITION = Match.INCORRECT_POSITION

WON = GameStatus.WON
IN_PROGRESS = GameStatus.IN_PROGRESS
LOST = GameStatus.LOST

class MasterMindTests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_guess_with_all_colors_in_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = selected_colors  

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response[EXACT], 6)

    def test_guess_with_all_colors_mismatch(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.GREEN, Colors.CYAN, Colors.PINK]  

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response[NO_MATCH], 6)

    def test_guess_with_all_colors_match_out_of_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.YELLOW, Colors.LIME, Colors.BLUE, Colors.RED, Colors.MAROON, Colors.VIOLET]  

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response[INCORRECT_POSITION], 6)

    def test_guess_with_first_four_colors_match_in_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.CYAN, Colors.ORANGE]

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response, {EXACT: 4, INCORRECT_POSITION: 0, NO_MATCH: 2})

    def test_guess_with_last_four_colors_match_in_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response, {EXACT: 4, INCORRECT_POSITION: 0, NO_MATCH: 2})

    def test_guess_with_first_three_match_in_position_and_last_three_out_of_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.LIME, Colors.VIOLET, Colors.YELLOW]

        response = guess(selected_colors, user_provided_colors)

        self.assertEqual(response, {EXACT: 3, INCORRECT_POSITION: 3, NO_MATCH: 0})

    def test_guess_with_first_and_third_mismatch_second_in_position_and_others_out_of_position(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.GREEN, Colors.BLUE, Colors.CYAN, Colors.RED, Colors.LIME, Colors.YELLOW]

        response = guess(selected_colors, user_provided_colors)
        
        self.assertEqual(response, {EXACT: 1, INCORRECT_POSITION: 3, NO_MATCH: 2})
    
    def test_guess_with_first_color_repeated_five_times(self):
        selected_colors = [Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.LIME]
        user_provided_colors = [Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.BLUE]

        response = guess(selected_colors, user_provided_colors)
        
        self.assertEqual(response, {EXACT: 5, INCORRECT_POSITION: 0, NO_MATCH: 1})
    
    def test_guess_with_last_color_repeated(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.GREEN, Colors.YELLOW]
        user_provided_colors = [Colors.GREEN, Colors.YELLOW, Colors.YELLOW, Colors.BLUE, Colors.MAROON, Colors.VIOLET]

        response = guess(selected_colors, user_provided_colors)
        
        self.assertEqual(response, {EXACT: 0, INCORRECT_POSITION: 5, NO_MATCH: 1})
        
    def test_guess_with_first_color_repeated_from_two_to_six(self):
        selected_colors = [Colors.RED, Colors.GREEN, Colors.VIOLET, Colors.RED, Colors.MAROON, Colors.BLUE]
        user_provided_colors = [Colors.GREEN, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED]

        response = guess(selected_colors, user_provided_colors)
        
        self.assertEqual(response, {EXACT: 1, INCORRECT_POSITION: 2, NO_MATCH: 3})
    
    def test_guess_with_first_color_repeated_and_no_match_first_position(self):
        selected_colors = [Colors.RED, Colors.PINK, Colors.VIOLET, Colors.RED, Colors.MAROON, Colors.BLUE]
        user_provided_colors = [Colors.GREEN, Colors.RED, Colors.RED, Colors.RED, Colors.RED, Colors.RED]

        response = guess(selected_colors, user_provided_colors)
        
        self.assertEqual(response, {EXACT: 1, INCORRECT_POSITION: 1, NO_MATCH: 4}) 
    
    def test_play_first_attempt_exact_match(self):
        selected_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PINK, Colors.ORANGE]
        user_provided_colors = selected_colors  

        guess_result, attempts, status = play(selected_colors, user_provided_colors, 0)

        expected_guess_result = {
            EXACT: 6,
            INCORRECT_POSITION: 0,
            NO_MATCH: 0
        }

        self.assertEqual(guess_result, expected_guess_result)
        self.assertEqual(status, WON)  
        self.assertEqual(attempts, 1) 
    
    def test_play_first_attempt_no_match(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.GREEN, Colors.CYAN, Colors.PINK] 

        guess_result, attempts, status = play(selected_colors, user_provided_colors, 0)

        expected_guess_result = {
            EXACT: 0,
            INCORRECT_POSITION: 0,
            NO_MATCH: 6
        }

        self.assertEqual(guess_result, expected_guess_result)
        self.assertEqual(status, IN_PROGRESS) 
        self.assertEqual(attempts, 1)  
    
    def test_play_first_attempt_some_exact_nonexact_matches(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.RED, Colors.LIME, Colors.BLUE, Colors.VIOLET, Colors.YELLOW, Colors.ORANGE]
    
        guess_result, attempts, status = play(selected_colors, user_provided_colors, 0)

        expected_guess_result = {
            EXACT: 3,
            INCORRECT_POSITION: 2,
            NO_MATCH: 1
        }

        self.assertEqual(guess_result, expected_guess_result)  
        self.assertEqual(status, IN_PROGRESS)  
        self.assertEqual(attempts, 1) 

    def test_play_second_attempt_exact_match(self):
        selected_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PINK, Colors.ORANGE]
        user_provided_colors = selected_colors 
        
        guess_result, attempts, status = play(selected_colors, user_provided_colors, 1)

        expected_guess_result = {
            EXACT: 6,
            INCORRECT_POSITION: 0,
            NO_MATCH: 0
        }
        
        self.assertEqual(guess_result, expected_guess_result)   
        self.assertEqual(status, WON)  
        self.assertEqual(attempts, 2) 

    def test_play_second_attempt_no_match(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.GREEN, Colors.CYAN, Colors.PINK]

        guess_result, attempts, status = play(selected_colors, user_provided_colors, 1)

        expected_guess_result = {
            EXACT: 0,
            INCORRECT_POSITION: 0,
            NO_MATCH: 6
        }

        self.assertEqual(guess_result, expected_guess_result)   
        self.assertEqual(status, IN_PROGRESS)  
        self.assertEqual(attempts, 2) 
    
    def test_play_20th_attempt_exact_match(self):
        selected_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PINK, Colors.ORANGE]
        user_provided_colors = selected_colors  
        
        guess_result, attempts, status = play(selected_colors, user_provided_colors, 19)

        expected_guess_result = {
            EXACT: 6,
            INCORRECT_POSITION: 0,
            NO_MATCH: 0
        }

        self.assertEqual(guess_result, expected_guess_result)  
        self.assertEqual(status, WON)  
        self.assertEqual(attempts, 20) 

    def test_play_20th_attempt_no_match(self):
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.GREEN, Colors.CYAN, Colors.PINK] 

        guess_result, attempts, status = play(selected_colors, user_provided_colors, 19)

        expected_guess_result = {
            EXACT: 0,
            INCORRECT_POSITION: 0,
            NO_MATCH: 6
        }

        self.assertEqual(guess_result, expected_guess_result)  
        self.assertEqual(status, LOST) 
        self.assertEqual(attempts, 20)

    def test_play_21st_attempt_exact_match(self):
        attempts = 20
        selected_colors = [Colors.RED, Colors.GREEN, Colors.BLUE, Colors.YELLOW, Colors.PINK, Colors.ORANGE]
        user_provided_colors = selected_colors 

        self.assertRaisesRegex(
            ValueError, "No more attempts allowed. The maximum number of attempts is 20.", 
            play, selected_colors, user_provided_colors, attempts
        )

    def test_play_21st_attempt_no_match(self):
        attempts = 20
        selected_colors = [Colors.RED, Colors.BLUE, Colors.MAROON, Colors.VIOLET, Colors.YELLOW, Colors.LIME]
        user_provided_colors = [Colors.CYAN, Colors.ORANGE, Colors.PINK, Colors.GREEN, Colors.CYAN, Colors.PINK]  

        self.assertRaisesRegex(
            ValueError, "No more attempts allowed. The maximum number of attempts is 20.", 
            play, selected_colors, user_provided_colors, attempts
        )

    def test_randomize_selected_colors(self): 
        selected_colors = select_colors()

        self.assertEqual(len(selected_colors), 6)
        self.assertTrue(all(color in Colors for color in selected_colors))
        
    def test_randomize_selected_colors_is_different_when_called_twice(self):
        selected_colors_first_call = select_colors(1001)  
        selected_colors_second_call = select_colors(1002)

        self.assertNotEqual(selected_colors_first_call, selected_colors_second_call)

if __name__ == '__main__':
    unittest.main()
