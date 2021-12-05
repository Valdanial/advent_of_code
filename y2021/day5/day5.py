import re
from os import stat
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day5"

VENTS_MAP_SIZE = 1000

def get_straight_vents_map(vent_list):
    vents_map = [[0] * VENTS_MAP_SIZE for i in range(VENTS_MAP_SIZE)]
    for vent_description in vent_list:
        vent_coordinates = [int(el) for el in re.findall('\d+', vent_description)]
        x1, y1, x2, y2 = vent_coordinates[0], vent_coordinates[1], vent_coordinates[2], vent_coordinates[3]
        # Only straight lines
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                vents_map[i][y1] += 1
        elif x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                vents_map[x1][i] += 1
    return vents_map

def get_direction(a, b):
    if a > b:
        return -1
    return int(b > a)

def get_vents_map(vent_list):
    # Diagon Alley 🧙
    vents_map = [[0] * VENTS_MAP_SIZE for i in range(VENTS_MAP_SIZE)]
    for vent_description in vent_list:
        vent_coordinates = [int(el) for el in re.findall('\d+', vent_description)]
        x1, y1, x2, y2 = vent_coordinates[0], vent_coordinates[1], vent_coordinates[2], vent_coordinates[3]
        xdir = get_direction(x1, x2)
        ydir = get_direction(y1, y2)
        for i in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
            vents_map[x1 + i * xdir][y1 + i * ydir] += 1
    return vents_map

def get_part_1_result(vent_list):
    vents_map = get_straight_vents_map(vent_list)
    result = 0
    for vent_lines in vents_map:
        for vent_position in vent_lines:
            if vent_position > 1:
                result += 1
    return result

def get_part_2_result(vent_list):
    vents_map = get_vents_map(vent_list)
    result = 0
    for vent_lines in vents_map:
        for vent_position in vent_lines:
            if vent_position > 1:
                result += 1
    return result

# Part 1

input_list = get_multiline_input(INPUT_FILE)

part_1_result = get_part_1_result(input_list)

print(f"Part 1: result = {part_1_result}")

# Part 2

part_2_result = get_part_2_result(input_list)

print(f"Part 2: result = {part_2_result}")
