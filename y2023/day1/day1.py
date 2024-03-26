import re

from y2023.lib.multiline_input import get_multiline_input

DAY = "day1"
INPUT_FILE = f"y2023/input/{DAY}"
TEST_INPUT_FILE_1 = f"y2023/input/{DAY}_test_1"
TEST_INPUT_FILE_2 = f"y2023/input/{DAY}_test_2"

str_num_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def parse_first_last_digit(line):
    first = '0'
    last = ''
    for character in line:
        if character.isnumeric():
            first = character
            break
    for character in line[::-1]:
        if character.isnumeric():
            last = character
            break
    return int(first + last)

first_regex = r"\w*?(\d|one|two|three|four|five|six|seven|eight|nine)\w*"
last_regex = r"\w*(\d|one|two|three|four|five|six|seven|eight|nine)\w*?"

def parse_numbers(line):
    match_first = re.findall(first_regex, line)
    match_last = re.findall(last_regex, line)
    first, last = match_first[0], match_last[0]
    return int(((first.isnumeric() and first) or str_num_to_digit[first]) + ((last.isnumeric() and last) or str_num_to_digit[last]))



def get_sum(lines, parse_function):
    result_sum = 0
    for line in lines:
        result = parse_function(line)
        result_sum += result
    return result_sum


# Part 1
def part1(input_file):
    input = get_multiline_input(input_file)
    part1_sum = get_sum(input, parse_first_last_digit)
    return part1_sum

# Part 2
def part2(input_file):
    input = get_multiline_input(input_file)
    part2_sum = get_sum(input, parse_numbers)
    return part2_sum


assert part1(TEST_INPUT_FILE_1) == 142
print(f"Part 1: sum = {part1(INPUT_FILE)}")

assert part2(TEST_INPUT_FILE_2) == 281
print(f"Part 2: sum = {part2(INPUT_FILE)}")

