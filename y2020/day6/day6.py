from typing import List

from y2020.lib.multiline_input import get_multiline_input

def get_occurrences(input_data):
    input_lines = input_data.split("\n")
    occurrences = set()
    for input_line in input_lines:
        occurrences |= set(input_line)
    return occurrences

def get_unanimous_answers(input_data):
    input_lines = input_data.split("\n")
    unanimous_answers = list(input_lines[0])
    for input_line in input_lines:
        unanimous_answers = [answer for answer in unanimous_answers if answer in list(input_line)]
    return unanimous_answers

input_data_list = get_multiline_input("y2020/input/day6", "\n\n")


counter = 0
unanimous_answers_counter = 0
for input_data in input_data_list:
    counter += len(get_occurrences(input_data))
    unanimous_answers_counter += len(get_unanimous_answers(input_data))

print(f"Part 1: count = {counter}")

print(f"Part 2: count = {unanimous_answers_counter}")

