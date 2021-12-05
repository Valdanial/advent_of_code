import re
from os import stat
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day450v"

class BingoGrid():
    def __init__(self, input_grid, game_master, id):
        self.id = id
        self.grid = {}
        self.size = len(input_grid)
        self.completion_grid = {}
        self.is_winner_grid = False
        
        if self.size > 5:
            print(input_grid)

        for i, subgrid in enumerate(input_grid):
            for j, element in enumerate(subgrid):
                game_master.subscribe((i, j), element, self)
                self.grid[element] = (i, j)
                self.completion_grid[(i, j)] = 0

    def check_number(self, number):
        position = self.grid.get(number)
        if position:
            self.completion_grid[position] = 1
            if self.check_row(position[0]):
                self.is_winner_grid = True
            if self.check_column(position[1]):
                self.is_winner_grid = True

    def check_row(self, i):
        return sum([self.completion_grid[(i, j)] for j in range(self.size)]) == self.size

    def check_column(self, j):
        return sum([self.completion_grid[(i, j)] for i in range(self.size)]) == self.size

class BingoGameMaster():
    def __init__(self):
        self.subscriptions = {} # Stores subscriptions
        self.already_won_grids = [] # List of ids

    def subscribe(self, position, number, grid):
        self.subscriptions[number] = self.subscriptions.get(number, [])
        self.subscriptions[number].append(grid)

    def draw(self, input_draw):
        for number in input_draw:
            winner_grid = None
            for grid in self.subscriptions.get(number, []):
                if grid.id not in self.already_won_grids:
                    grid.check_number(number)
                    if grid.is_winner_grid:
                        winner_grid = grid
                        self.already_won_grids.append(grid.id)
            if winner_grid:
                return winner_grid, number

def create_bingo_grid_from_input(input, game_master, id):
    input_grid = []
    for line in input.split("\n"):
        input_grid.append(re.findall("\d+", line))
    bingo_grid = BingoGrid(input_grid, game_master, id)
    return bingo_grid

def get_part_1_result(input_list):
    draw = input_list[0].split(',')
    game_master = BingoGameMaster()
    for idx, grid_input in enumerate(input_list[1:]):
        create_bingo_grid_from_input(grid_input, game_master, idx)

    # Proceed with draw
    result_grid, final_number = game_master.draw(draw)

    sum = 0

    for number, position in result_grid.grid.items():
        if not result_grid.completion_grid[position]:
            sum += int(number)

    return sum * int(final_number)

def get_part_2_result(input_list):
    draw = input_list[0].split(',')
    game_master = BingoGameMaster()
    for idx, grid_input in enumerate(input_list[1:]):
        create_bingo_grid_from_input(grid_input, game_master, idx)

    # Proceed with draw
    new_result_grid, new_final_number = game_master.draw(draw)
    result_grid = None
    final_number = None
    while(new_result_grid and new_final_number and final_number != draw[-1]):
        result_grid = new_result_grid
        final_number = new_final_number
        new_result_grid, new_final_number = game_master.draw(draw[draw.index(final_number) + 1:]) or (None, None)

    sum = 0

    for number, position in result_grid.grid.items():
        if not result_grid.completion_grid[position] or final_number in draw[draw.index(final_number) + 1:]:
            sum += int(number)

    return sum * int(final_number)


# Part 1

input_list = get_multiline_input(INPUT_FILE, '\n\n') # Separator is two carriage returns


part_1_result = get_part_1_result(input_list)

print(f"Part 1: result = {part_1_result}")

# Part 2

part_2_result = get_part_2_result(input_list)

print(f"Part 2: result = {part_2_result}")

