import re

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

FIRST_REGEX = r"\w*?(\d|one|two|three|four|five|six|seven|eight|nine)\w*"
LAST_REGEX = r"\w*(\d|one|two|three|four|five|six|seven|eight|nine)\w*?"

def parse_numbers(line):
    match_first = re.findall(FIRST_REGEX, line)
    match_last = re.findall(LAST_REGEX, line)
    first, last = match_first[0], match_last[0]
    return int(((first.isnumeric() and first) or str_num_to_digit[first]) + ((last.isnumeric() and last) or str_num_to_digit[last]))



def get_sum(lines, parse_function):
    result_sum = 0
    for line in lines:
        result = parse_function(line)
        result_sum += result
    return result_sum


# Part 1
def part1(input_str: list[str]):
    part1_sum = get_sum(input_str, parse_first_last_digit)
    return part1_sum

# Part 2
def part2(input_str: list[str]):
    part2_sum = get_sum(input_str, parse_numbers)
    return part2_sum
