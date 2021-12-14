import re
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day14"
TEST_FILE_1 = "y2021/input/day14_test1"

def grow(digram_count_list, insertion_rules, letter_count):
    result_digram_count_list = {}
    for digram, count in digram_count_list.items():
        a, b = tuple(digram)
        result_letter = insertion_rules[digram]
        result_digram_count_list[a + result_letter] = result_digram_count_list.get(a + result_letter, 0) + count
        result_digram_count_list[result_letter + b] = result_digram_count_list.get(result_letter + b, 0) + count
        letter_count[result_letter] = letter_count.get(result_letter, 0) + count
    return result_digram_count_list

def get_insertion_rules(rules_str):
    rules_map = {}
    for rule in rules_str.split('\n'):
        pair, result = rule.split(' -> ')
        rules_map[pair] = result
    return rules_map

def get_digram_count_list(polymer_template_str):
    digram_count_list = {}
    for i in range(len(polymer_template_str) - 1):
        a = polymer_template_str[i]
        b = polymer_template_str[i + 1]
        digram_count_list[a + b] = digram_count_list.get(a + b, 0) + 1
    return digram_count_list

def get_letter_count(polymer_template_str):
    letter_count = {}
    for c in polymer_template_str:
        letter_count[c] = letter_count.get(c, 0) + 1
    return letter_count

def get_day_result(input, steps):
    # Now optimized for part 2!
    polymer_template_str, rules_str = input
    insertion_rules = get_insertion_rules(rules_str)
    digram_count_list = get_digram_count_list(polymer_template_str)
    letter_count = get_letter_count(polymer_template_str)
    for i in range(steps):
        digram_count_list = grow(digram_count_list, insertion_rules, letter_count)
    return max(letter_count.values()) - min(letter_count.values())

def get_part_1_result(input):
    return get_day_result(input, 10)

def get_part_2_result(input):
    return get_day_result(input, 40)

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1, '\n\n')
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 1588)

    # Part 2 tests
    test_2_1_result = get_part_2_result(test_list_1)
    assert(test_2_1_result == 2188189693529)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE, '\n\n')
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE, '\n\n')
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()