import math

from typing import List

from y2020.lib.multiline_input import get_multiline_input

def get_differences_list_and_count(number_list: List[int], max_difference: int):
    differences_count = [0 for i in range(max_difference + 1)]
    differences_list = []
    number_list.sort()
    number_list.append(number_list[-1] + max_difference)
    differences_count[number_list[0]] += 1
    for idx in range(len(number_list) - 1):
        difference = number_list[idx + 1] - number_list[idx]
        if difference > max_difference:
            raise Exception(f"Can't reach end of list with max difference of {max_difference}")
        differences_count[difference] += 1
        differences_list.append(difference)
    return differences_list, differences_count

def get_possibilities(intervals_list: List[int], max_interval: int):
    # Assuming max interval is 3 because finding a generic solution was a bit time-consuming
    print(intervals_list)
    interesting_segments: List[List[int]] = []
    current_streak = []
    previous_interval = max_interval
    # get interesting segments: streaks of 3 or more intervals for which sum of two consecutive intervals is lower than max_interval
    for interval in intervals_list:
        if interval + previous_interval > max_interval:
            if len(current_streak) > 1:
                interesting_segments.append(current_streak)
            current_streak = [interval] if interval <= max_interval else []
        else:
            current_streak.append(interval)
        previous_interval = interval
    for interesting_segment in interesting_segments:
        get_segment_possibilities(interesting_segment, max_interval)
    return interesting_segments

def get_segment_deletion_possibilities(segment: List[int], max_item: int):
    segment_sum = sum(segment)
    affected_items = len(segment) - 1
    max_deletions = affected_items - int(math.floor((segment_sum - 1) / max_item))
    possibilities = 0
    for i in range(max_deletions + 1):
        possibilities += int(math.factorial(affected_items) / (math.factorial(i) * math.factorial(affected_items - i)))
    return possibilities

def get_segment_possibilities(segment: List[int], max_item: int):
    deletion_possibilities = get_segment_deletion_possibilities(segment, max_item)
    possibilities = deletion_possibilities

    for i in range(len(segment) - 1):
        
    print(deletion_possibilities)



input_list = [int(number) for number in get_multiline_input("y2020/day10/input")]
diff_list, diff_count = get_differences_list_and_count(input_list, 3)

part_1_result = diff_count[1] * diff_count[3]
print(f"Part 1 result = {part_1_result}")

print(get_possibilities(diff_list, 3))

print(get_possibilities([3, 1, 2, 2, 1, 3], 3))

print(get_possibilities([3, 1, 1, 1, 1, 1, 3], 3))