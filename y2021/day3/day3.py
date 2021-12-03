from os import stat
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day3"

def list_sum(l1, l2):
    return [int(l1_el) + int(l2_el) for l1_el, l2_el in zip(l1, l2)]

def get_gamma_and_epsilon(status_report):
    status_report_length = len(status_report)
    line_length = len(status_report[0])
    sum_result = [0] * status_report_length
    for report_line in status_report:
        sum_result = list_sum(sum_result, report_line)
    gamma = sum([int(sum_el > status_report_length / 2) << (line_length - 1 - idx) for idx, sum_el in enumerate(sum_result)])
    epsilon = (1 << line_length) - 1 - gamma
    return gamma, epsilon

def filter_list(l, operator):
    cursor = 0
    line_length = len(l[0])
    list_length = len(l)
    list_to_filter = l
    while(cursor < line_length and list_length > 1):
        number_to_keep = int(operator(sum([int(line[cursor]) for line in list_to_filter]), list_length / 2))
        list_to_filter = list(filter(lambda el: int(el[cursor]) == number_to_keep, list_to_filter))
        list_length = len(list_to_filter)
        cursor += 1
    return list_to_filter[0] # return first element all the time

def bin_string_to_int(bin_string):
    return sum([int(c) << (len(bin_string) - 1 - idx) for idx, c in enumerate(bin_string)])

def get_life_support_rating(status_report):
    ox_gen_rating = bin_string_to_int(filter_list(status_report, lambda a, b: a >= b))
    co2_scrub_rating = bin_string_to_int(filter_list(status_report, lambda a, b: a < b))
    return ox_gen_rating * co2_scrub_rating


# Part 1

input_list = get_multiline_input(INPUT_FILE)
gamma, epsilon = get_gamma_and_epsilon(input_list)

part_1_result = gamma * epsilon

print(f"Part 1: result = {part_1_result}")

# Part 2

input_list = get_multiline_input(INPUT_FILE)

part_2_result = get_life_support_rating(input_list)

print(f"Part 2: result = {part_2_result}")

