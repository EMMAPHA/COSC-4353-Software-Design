import random
from enum import Enum
from collections import Counter

class Colors(Enum):
    YELLOW = 'yellow'
    RED = 'red'
    GREEN = 'green'
    ORANGE = 'orange'
    LIME = 'lime'
    PINK = 'pink'
    VIOLET = 'violet'
    BLUE = 'blue'
    CYAN = 'cyan'
    MAROON = 'maroon'

class Match(Enum):
    EXACT = 'Exact Match'  
    INCORRECT_POSITION = 'Non Positional Match'
    NO_MATCH = "No Match"

class GameStatus(Enum):
    IN_PROGRESS = 'In Progress'
    WON = 'Won'
    LOST = 'Lost'

MAX_ATTEMPTS = 20
NUM_COLORS = 6

def guess(user_provided_colors, selected_colors):
    def match_for_position(position):
        candidate_color = user_provided_colors[position]

        if candidate_color == selected_colors[position]:
            return Match.EXACT
        elif candidate_color in selected_colors:
            if selected_colors.count(candidate_color) > 0 and user_provided_colors[position] != selected_colors[position]:
                return Match.INCORRECT_POSITION
        return Match.NO_MATCH


    matches = Counter(map(match_for_position, range(len(selected_colors))))


    return {
        Match.EXACT: matches[Match.EXACT],
        Match.INCORRECT_POSITION: matches[Match.INCORRECT_POSITION],
        Match.NO_MATCH: matches[Match.NO_MATCH]
    }

def play(selected_colors, user_provided_colors, number_of_attempts):
    if number_of_attempts >= MAX_ATTEMPTS:
        raise ValueError("No more attempts allowed. The maximum number of attempts is 20.")
    
    guess_result = guess(user_provided_colors, selected_colors)
    attempts = number_of_attempts + 1

    if guess_result[Match.EXACT] == len(selected_colors):
        return (guess_result, attempts, GameStatus.WON)
    
    if attempts >= MAX_ATTEMPTS:
        return (guess_result, attempts, GameStatus.LOST)

    return (guess_result, attempts, GameStatus.IN_PROGRESS)

def select_colors(random_seed=1001):
    random.seed(random_seed)
    return random.sample(list(Colors), NUM_COLORS)
