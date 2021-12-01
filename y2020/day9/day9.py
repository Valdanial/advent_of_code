from typing import List

from y2020.lib.multiline_input import get_multiline_input
from y2020.lib.get_first_by_sum import get_first_by_sum

def get_first_not_xmas(number_list: List[int], preamble_length):
    if len(number_list) < preamble_length or preamble_length < 2:
        # Not enough
        return None
    preamble = number_list[0:preamble_length]
    remaining_numbers = number_list[preamble_length:-1]
    for number in remaining_numbers:
        if not get_first_by_sum(preamble, number, 2):
            return number
        preamble = preamble[1:]
        preamble.append(number)
    return None

def find_contiguous_items_that_sum_up_to(number_list: List[int], target_sum: int):
    following_idx = 0
    for number in number_list:
        following_idx += 1
        tmp_sum = number
        tmp_list = [number]
        if tmp_sum == target_sum:
            return tmp_list
        for following_number in number_list[following_idx:-1]:
            tmp_sum += following_number
            tmp_list.append(following_number)
            if tmp_sum == target_sum:
                return tmp_list
    return None



input_list = [int(number) for number in get_multiline_input("y2020/input/day9")]

part_1_number = get_first_not_xmas(input_list, 25)
print(f"Part 1: First number not respecting xmas: {part_1_number}")

part_2_list = find_contiguous_items_that_sum_up_to(input_list, part_1_number)
part_2_result = min(part_2_list) + max(part_2_list)

print(f"Part 2: Sum : {part_2_result}")
