from os import stat
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day7"

def get_crab_list(crab_input):
    return [int(el) for el in crab_input.split(',')]

def get_fuel_cost(crab_list, position):
    fuel_cost = 0
    for crab_position in crab_list:
        fuel_cost += abs(crab_position - position)
    return fuel_cost

def get_real_fuel_cost(crab_list, position):
    fuel_cost = 0
    for crab_position in crab_list:
        fuel_cost += sum(range(abs(crab_position - position) + 1))
    return fuel_cost

def get_mean(crab_list):
    return sum(crab_list) / len(crab_list)

def get_median(crab_list):
    sorted_list = [*crab_list]
    sorted_list.sort()
    return sorted_list[int(len(sorted_list) / 2)]

def get_part_1_result(crab_list):
    return get_fuel_cost(crab_list, get_median(crab_list))

def get_part_2_result(crab_list):
    # Get mean, and check around it. Not 100% sure it's mathematically valid 🤷
    mean = round(get_mean(crab_list))
    lesser_fuel_cost = min([get_real_fuel_cost(crab_list, mean + i) for i in range(-1, 2)])
    return lesser_fuel_cost


# Part 1

input_list = get_multiline_input(INPUT_FILE)

part_1_result = get_part_1_result(get_crab_list(input_list[0]))

print(f"Part 1: result = {part_1_result}")

# Part 2

input_list = get_multiline_input(INPUT_FILE)

part_2_result = get_part_2_result(get_crab_list(input_list[0]))

print(f"Part 2: result = {part_2_result}")
