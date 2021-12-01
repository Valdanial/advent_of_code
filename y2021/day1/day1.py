import re

from y2021.lib.multiline_input import get_multiline_integers

INPUT_FILE = "y2021/input/day1"

def get_grouped_sum(list, group_size):
    result_list = []
    if len(list) >= group_size:
        for i in range(0, len(list) - group_size + 1):
            s = 0
            for j in range(0, group_size):
                s += list[i + j]
            result_list.append(s)
    return result_list

def get_list_diff(list):
    result_list = []
    if len(list) > 1:
        for i in range(0, len(list) - 1):
            result_list.append(list[i + 1] - list[i])
    return result_list

def get_diff_count(in_list):
    return len(list(filter(lambda el: el > 0, in_list)))

# Part 1

input_list = get_multiline_integers(INPUT_FILE)
diff_list = get_list_diff(input_list)
diff_count = get_diff_count(diff_list)

# Part 2

sum_list = get_grouped_sum(input_list, 3)
sum_diff_list = get_list_diff(sum_list)
sum_diff_count = get_diff_count(sum_diff_list)


print(f"Part 1: count = {diff_count}")
print(f"Part 2: count = {sum_diff_count}")
