import re
from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day13"
TEST_FILE_1 = "y2021/input/day13_test1"

def get_dots_list(dots_list_str):
    dots_list = []
    for line in dots_list_str.split('\n'):
        coordinates = line.split(',')
        dots_list.append(tuple([int(coordinate) for coordinate in coordinates]))
    return set(dots_list)

def get_fold_instructions(fold_instructions_str):
    fold_instructions = []
    for fold_instruction in fold_instructions_str.split('\n'):
        axis = fold_instruction[11]
        coordinate = int(fold_instruction[13:])
        fold_instructions.append((int(axis == 'x') and coordinate, int(axis == 'y' and coordinate)))
    return fold_instructions

def fold(dots_list, fold_instruction):
    result_dots_list = []
    for dot in dots_list:
        new_coordinates = []
        for coordinate, fold_coordinate in zip(dot, fold_instruction):
            new_coordinates.append(coordinate if not fold_coordinate or fold_coordinate >= coordinate else 2 * fold_coordinate - coordinate)
        result_dots_list.append(tuple(new_coordinates))
    return set(result_dots_list)

def generate_code_output(dots_list, fold_instructions):
    max_x, max_y = (min([x for x,_ in fold_instructions if x > 0]), min([y for _,y in fold_instructions if y > 0]))
    code_output_list = [list('.' * max_x) for i in range(max_y + 1)]
    for x, y in dots_list:
        code_output_list[y][x] = '#'
    code_output = '\n'.join([reduce(lambda a, b: a + b, el) for el in code_output_list])
    return code_output

def get_part_1_result(input):
    dots_list_str, fold_instructions_str = tuple(input)
    dots_list = get_dots_list(dots_list_str)
    fold_instructions = get_fold_instructions(fold_instructions_str)
    result_dots_list = fold(dots_list, fold_instructions[0])
    return len(result_dots_list)

def get_part_2_result(input):
    dots_list_str, fold_instructions_str = tuple(input)
    dots_list = get_dots_list(dots_list_str)
    fold_instructions = get_fold_instructions(fold_instructions_str)
    current_dot_list = dots_list
    for fold_instruction in fold_instructions:
        for el in current_dot_list:
            break
        current_dot_list = fold(current_dot_list, fold_instruction)
    return generate_code_output(current_dot_list, fold_instructions)

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1, '\n\n')
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 17)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE, '\n\n')
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE, '\n\n')
    part_2_result = get_part_2_result(input_list)
    # Result will be visible in the terminal
    # Alternatively, one could also whip up some code for letter recognition, but who's got time for that, really?
    print(f"Part 2: result = \n{part_2_result}")

test_and_execute()