import re

from y2020.lib.multiline_input import get_multiline_input

def count_rule_check(rule_password: str):
    split_rule_password = rule_password.split()
    count_rule = split_rule_password[0]
    character_rule = split_rule_password[1][0]
    password = split_rule_password[2]

    count_rule = count_rule.replace("-", ",")
    count_rule_regex = "{" + count_rule + "}"

    rule_regex = re.compile(f"^(?:[^{character_rule}]*{character_rule}){count_rule_regex}[^{character_rule}]*$")

    match = re.match(rule_regex, password)
    return match

def position_rule_check(rule_password: str):
    split_rule_password = rule_password.split()
    position_rule = split_rule_password[0]
    split_position_rule = position_rule.split("-")
    position1 = int(split_position_rule[0]) - 1
    position2 = int(split_position_rule[1]) - 1
    character_rule = split_rule_password[1][0]
    password = split_rule_password[2]

    return (password[position1] == character_rule) ^ (password[position2] == character_rule)

INPUT_FILE = "y2020/input/day2_input"

input_list = get_multiline_input(INPUT_FILE)
count_matches = 0
position_matches = 0

for in_str in input_list:
    if count_rule_check(in_str):
        count_matches += 1
    if position_rule_check(in_str):
        position_matches += 1

print(f"Part 1: count = {count_matches}")
print(f"Part 2: count = {position_matches}")
