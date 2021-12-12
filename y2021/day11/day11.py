import re
from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day11"
TEST_FILE = "y2021/input/day11_test"

MAX_ENERGY_LEVEL = 9

NEIGHBOURS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def iterate(grid, stop_condition):
    # Wanted to do the treatment in one function, ideally this should be split in mutliple functions to avoid losing half the screen due to tabulations
    current_grid = [[*line] for line in grid]
    iterations = 0
    flashes = 0
    grid_height = len(current_grid)
    grid_length = grid_height and len(current_grid[0])
    while not stop_condition(current_grid, iterations):
        iterations += 1
        already_flashed = []
        for y, line in enumerate(current_grid):
            for x, value in enumerate(line):
                points_to_increment = [(y, x)]
                while points_to_increment:
                    y_to_increment, x_to_increment = points_to_increment.pop()
                    if (y_to_increment, x_to_increment) not in already_flashed:
                        current_grid[y_to_increment][x_to_increment] += 1
                        if current_grid[y_to_increment][x_to_increment] > MAX_ENERGY_LEVEL:
                            # https://en.wikipedia.org/wiki/Pandemic_(board_game)
                            points_to_increment += [(y_to_increment + ny, x_to_increment + nx) for ny,nx in NEIGHBOURS if 0 <= y_to_increment + ny < grid_height and 0 <= x_to_increment + nx < grid_length]
                            already_flashed.append((y_to_increment, x_to_increment))
                            flashes += 1
        for y_to_reset, x_to_reset in already_flashed:
            current_grid[y_to_reset][x_to_reset] = 0
    return current_grid, iterations, flashes

def get_grid(input):
    return [[int(c) for c in line] for line in input]

def get_part_1_result(input):
    result_grid, iterations, flashes = iterate(get_grid(input), lambda _, iterations: iterations >= 100)
    return flashes

def get_part_2_result(input):
    result_grid, iterations, flashes = iterate(get_grid(input), lambda grid, _: not sum([sum(line) for line in grid]))
    return iterations

def test_and_execute():
    test_list = get_multiline_input(TEST_FILE)
    test_1_result = get_part_1_result(test_list)
    assert(test_1_result == 1656)
    test_2_result = get_part_2_result(test_list)
    assert(test_2_result == 195)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()