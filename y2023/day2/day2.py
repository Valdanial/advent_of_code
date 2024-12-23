from functools import reduce

DAY = "day2"
INPUT_FILE = f"y2023/input/{DAY}"
TEST_INPUT_FILE_1 = f"y2023/input/{DAY}_test_1"
TEST_INPUT_FILE_2 = f"y2023/input/{DAY}_test_1"

def lines_to_games(lines):
    games = []
    for line in lines:
        game_id, game_rounds = line[5:].split(":")
        game = {"id": int(game_id), "rounds": []}
        rounds = game_rounds.split(";")
        for round in rounds:
            game_round = {}
            draws = round.split(",")
            for draw in draws:
                count, color = draw.split()
                game_round[color] = int(count)
            game["rounds"].append(game_round)
        games.append(game)
    return games

def is_valid(game, supply):
    for round in game["rounds"]:
        for color, count in round.items():
            if count > supply[color]:
                return False
    return True

def get_game_minimum(game):
    minimum = {"red": 0, "green": 0, "blue": 0}
    for round in game["rounds"]:
        minimum = {color: max(count, int(color in round) and round[color]) for color, count in minimum.items()}
    return minimum

def get_valid_games_sum(lines, supply):
    sum = 0
    games = lines_to_games(lines)
    for game in games:
        if is_valid(game, supply):
            sum += game["id"]
    return sum

def get_cube_power_sum(lines):
    sum = 0
    games = lines_to_games(lines)
    for game in games:
        minimum = get_game_minimum(game)
        product = reduce(lambda x,y: x*y, minimum.values())
        sum += product
    return sum


# Part 1
PART1_SUPPLY = {"red": 12, "green": 13, "blue": 14}
def part1(input_str):
    part1_sum = get_valid_games_sum(input_str, PART1_SUPPLY)
    return part1_sum

# Part 2
def part2(input_str):
    part2_sum = get_cube_power_sum(input_str)
    return part2_sum


# assert part1(TEST_INPUT_FILE_1) == 8
# print(f"Part 1: sum = {part1(INPUT_FILE)}")

# assert part2(TEST_INPUT_FILE_2) == 2286
# print(f"Part 2: sum = {part2(INPUT_FILE)}")

