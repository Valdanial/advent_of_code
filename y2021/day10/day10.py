import re
from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day10"
TEST_FILE = "y2021/input/day10_test"

ILLEGAL_CLOSING_CHARACTER_VALUE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETION_CHARACTER_VALUE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

class ParseError(Exception):
    def __init__(self, illegal_character):
        super().__init__()
        self.illegal_character = illegal_character

def opening_character(stack, character):
    stack.append(character)

def closing_character(opening_character):
    def closing_character_core(stack, character):
        if not stack or stack[-1] != opening_character:
            raise ParseError(character)
        stack.pop()
    return closing_character_core

def init_characters_map(characters_pairs):
    result_map = {}
    for oc, cc in characters_pairs:
        result_map[oc] = opening_character
        result_map[cc] = closing_character(oc)
    return result_map

CHARACTER_PAIRS = [('<', '>'), ('(', ')'), ('[', ']'), ('{', '}')]

CHARACTERS_MAP = init_characters_map(CHARACTER_PAIRS)

def parse(line):
    if not line:
        return
    stack = []
    for c in line:
        if not c in CHARACTERS_MAP.keys():
            raise Exception(f'Character {c} not expected')
        CHARACTERS_MAP[c](stack, c)
    return stack

def get_illegal_characters(lines):
    illegal_characters = []
    for line in lines:
        try:
            parse(line)
        except ParseError as e:
            illegal_characters.append(e.illegal_character)
    return illegal_characters

def get_counterpart_character(char):
    for oc, cc in CHARACTER_PAIRS:
        if char == oc:
            return cc
        if char == cc:
            return oc

def get_completion(stack):
    result = ''
    while stack:
        c = stack.pop()
        result += get_counterpart_character(c)
    return result

def get_part_1_result(input):
    illegal_characters = get_illegal_characters(input)
    return sum([ILLEGAL_CLOSING_CHARACTER_VALUE[ic] for ic in illegal_characters])

def get_part_2_result(input):
    completions = []
    for line in input:
        try:
            stack = parse(line) # parse and correct when necessary
            completions.append(get_completion(stack))
        except ParseError as e:
            # Do nothing
            pass
    scores = [reduce(lambda a, b: a * 5 + COMPLETION_CHARACTER_VALUE[b], [0, *completion]) for completion in completions]
    scores.sort()
    return scores[int((len(scores) - 1) / 2)]

def test_and_execute():
    test_list = get_multiline_input(TEST_FILE)
    test_1_result = get_part_1_result(test_list)
    assert(test_1_result == 26397)
    test_2_result = get_part_2_result(test_list)
    assert(test_2_result == 288957)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()