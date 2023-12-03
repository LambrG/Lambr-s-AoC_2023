from file_reader import read_data

file = "input23_02.txt"
raw_data = read_data(file)
data_games = []


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
    for round in game:
        keys = round.keys()
        for key in keys:
            if round[key] > bag[key]:
                return False
    return True


def bag_value(game):
    bag = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
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
    total = 0
    bag = {
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }
    for i, game in enumerate(data_games):
        total += (i+1) * game_possible(game, bag)
    return total

def part_2():
    total = 0
    for game in data_games:
        total += bag_value(game)
    return total


print(part_1())
print(part_2())


