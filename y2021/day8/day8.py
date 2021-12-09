import re
from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day8"

EASY_DIGITS_SEGMENT_COUNT = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

REGEX_1 = r"\w{2}"
REGEX_4 = r"\w{4}"
REGEX_7 = r"\w{3}"
REGEX_8 = r"\w{7}"

LINE_MAP = {
    "a": 1 << 6,
    "b": 1 << 5,
    "c": 1 << 4,
    "d": 1 << 3,
    "e": 1 << 2,
    "f": 1 << 1,
    "g": 1 << 0
}

# Default association between binary value and digit
DIGIT_MAP = {
    int('1110111', 2): 0,
    int('0010100', 2): 1,
    int('1011101', 2): 2,
    int('1011011', 2): 3,
    int('0111010', 2): 4,
    int('1101011', 2): 5,
    int('1101111', 2): 6,
    int('1010010', 2): 7,
    int('1111111', 2): 8,
    int('1111011', 2): 9
}

def format_input(input):
    return input.split(" | ")

def get_association_map(input):
    association_map = {}
    length_to_str_map = {i:[] for i in range(2, 8)}
    for string in input:
        length_to_str_map[len(string)].append(sum([LINE_MAP[c]for c in string]))

    a = length_to_str_map[3][0] - length_to_str_map[2][0]
    bd = length_to_str_map[4][0] - length_to_str_map[2][0]
    abfg = reduce(lambda x, y: x & y, length_to_str_map[6])
    b = abfg & bd
    d = bd - b
    f = abfg & length_to_str_map[2][0]
    g = abfg - a - b - f
    c = length_to_str_map[2][0] - f
    e = (1 << 7) - 1 - a - b - c - d - f - g

    association_map = {
        a + b + c + e + f + g: 0,
        c + f: 1,
        a + c + d + e + g: 2,
        a + c + d + f + g: 3,
        b + c + d + f: 4,
        a + b + d + f + g: 5,
        a + b + d + e + f + g: 6,
        a + c + f: 7,
        a + b + c + d + e + f + g: 8,
        a + b + c + d + f + g: 9
    }
    return association_map

def get_easy_digits_count(signal):
    return {digit: len(re.findall(rf"\b(\w{{{segment_count}}})\b", signal)) for (digit, segment_count) in EASY_DIGITS_SEGMENT_COUNT.items()}

def get_part_1_result(input_l):
    return sum([sum(get_easy_digits_count(format_input(input_line)[1]).values()) for input_line in input_l])

def get_part_2_result(input_l):
    result = 0
    for input_line in input_l:
        formatted_input = format_input(input_line)
        formatted_input = [el.split(' ') for el in formatted_input]
        formatted_line = [*(formatted_input[0]), *(formatted_input[1])]
        association_map = get_association_map(formatted_line)
        formatted_output = [sum([LINE_MAP[c] for c in el]) for el in formatted_input[1]]
        output_digits = [association_map[el] for el in formatted_output]
        output_value = reduce(lambda x, y: str(x) + str(y), output_digits)
        result += int(output_value)
    return result

def check_all_lengths_are_in_input(lines):
    # Check all lengths are in the input. It doesn't have to be executed to get a result
    for line in lines:
        formatted_line = format_input(line)
        formatted_line = [*(formatted_line[0].split(' ')), *(formatted_line[1].split(' '))]
        lengths = [len(el) for el in formatted_line]
        for i in range(2, 7):
            if i not in lengths:
                print(lengths)
                print(f"{i} not in line")
                break

# Part 1

input_list = get_multiline_input(INPUT_FILE)

part_1_result = get_part_1_result(input_list)

print(f"Part 1: result = {part_1_result}")

# Part 2

input_list = get_multiline_input(INPUT_FILE)

part_2_result = get_part_2_result(input_list)

print(f"Part 2: result = {part_2_result}")