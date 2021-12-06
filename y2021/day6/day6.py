from os import stat
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day6"

SPAWN_INTERVAL = 7
NEW_FISH_DELAY = 2

def get_fish_list(fish_input):
    return [int(el) for el in fish_input.split(',')]

def get_fish_day_tracker(fish_list):
    # returns counter of fish per day of spawn from fish list
    return [fish_list.count(i) for i in range(SPAWN_INTERVAL + NEW_FISH_DELAY)]

def pass_day(fish_day_tracker):
    result = fish_day_tracker[1:]
    result.append(fish_day_tracker[0])
    result[SPAWN_INTERVAL - 1] += fish_day_tracker[0]
    return result

def get_part_1_result(fish_list, days_to_pass):
    # The Book Of Us: Lanternfish
    fish_day_tracker = get_fish_day_tracker(fish_list)
    for day in range(days_to_pass):
        fish_day_tracker = pass_day(fish_day_tracker)
    return sum(fish_day_tracker)


# Part 1

input_list = get_multiline_input(INPUT_FILE)

part_1_result = get_part_1_result(get_fish_list(input_list[0]), 80)

print(f"Part 1: result = {part_1_result}")

# Part 2

input_list = get_multiline_input(INPUT_FILE)

part_2_result = get_part_1_result(get_fish_list(input_list[0]), 256)

print(f"Part 2: result = {part_2_result}")
