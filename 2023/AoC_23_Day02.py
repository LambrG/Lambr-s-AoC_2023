# Importing a function named `read_data` from a module named `file_reader`
from file_reader import read_data

# Reading data from a file named "input23_02.txt"
file = "input23_02.txt"
raw_data = read_data(file)
data_games = []

# Parsing the raw data and organizing it into a structured format
for game in raw_data:
    game = game.split(":")
    rounds = game[1]
    rounds = rounds.split(";")
    data_rounds = []  
    for round in rounds:             
        round = round.split(",")
        data_pulls = {}
        for pulls in round:
            pulls = pulls.strip().split(" ")
            data_pulls[pulls[1]] = int(pulls[0])
        data_rounds.append(data_pulls)
    data_games.append(data_rounds)


def game_possible(game, bag):
    """
    Determines if a game is possible to play with the given bag configuration.

    Args:
    - game: A list containing game rounds as dictionaries representing available pulls.
    - bag: A dictionary representing the available counts of different colored items in the bag.

    Returns:
    - Boolean: True if the game is possible with the given bag, False otherwise.
    """
    for round in game:
        keys = round.keys()
        for key in keys:
            if round[key] > bag[key]:
                return False
    return True


def bag_value(game):
    """
    Calculates the total value of the bag after playing a game.

    Args:
    - game: A list containing game rounds as dictionaries representing available pulls.

    Returns:
    - Integer: Total value of the bag after playing the game.
    """
    bag = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in game:
        keys = round.keys()
        for key in keys:
            bag[key] = max(bag[key], round[key])
    total = 1
    keys = bag.keys()
    for key in keys:
        total *= bag[key]
    return total

            
def part_1():
    """
    Solves Part 1 of the problem by calculating the total possible games based on the bag configuration.

    Returns:
    - Integer: Total possible games.
    """
    total = 0
    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for i, game in enumerate(data_games):
        total += (i + 1) * game_possible(game, bag)
    return total

def part_2():
    """
    Solves Part 2 of the problem by calculating the total value of the bag after playing all games.

    Returns:
    - Integer: Total value of the bag after playing all games.
    """
    total = 0
    for game in data_games:
        total += bag_value(game)
    return total


# Prints the results of Part 1 and Part 2 of the problem
print(part_1())
print(part_2())

