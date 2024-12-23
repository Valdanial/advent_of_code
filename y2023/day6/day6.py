import re
from operator import mul
from functools import reduce

NUM_REGEX = r"\d+"

def is_winning(race: tuple[int], hold_time: int):
    return (race[0] - hold_time) * hold_time > race[1]

def get_min_max_for_race(race: tuple[int]):
    t, _ = race
    starting_check_value = half_time = t // 2
    while not is_winning(race, starting_check_value):
        starting_check_value -= half_time // 10 # Check smaller value
        if is_winning(race, t - starting_check_value): # Also check symmetrical value from half time
            starting_check_value = t - starting_check_value
            break

    # Reduce search range by half for both max_min and min_max for each iteration
    # Once they are both found, exit and return the results
    min_min, max_max = 1, t
    max_min = min_max = starting_check_value
    while min_min != max_min and min_max != max_max:
        if min_min != max_min:
            min_to_assess = min_min + (max_min - min_min) // 2
            if not is_winning(race, min_to_assess) or min_to_assess == max_min:
                min_min = min_to_assess
            else:
                max_min = min_to_assess
        if min_max != max_max:
            max_to_assess = min_max + (max_max - min_max) // 2
            if not is_winning(race, max_to_assess) or max_to_assess == min_max:
                max_max = max_to_assess
            else:
                min_max = max_to_assess
    return max_min, min_max

# Part 1
def part1(input_str: list[str])->str:
    races = zip(map(int, re.findall(NUM_REGEX, input_str[0])), map(int, re.findall(NUM_REGEX, input_str[1])))
    min_and_max_hold_times = [get_min_max_for_race(race) for race in races]
    result = reduce(mul, map(lambda t: t[1] - t[0] + 1, min_and_max_hold_times))
    return result

# Part 2
def part2(input_str: list[str])->str:
    race = tuple([int("".join(re.findall(NUM_REGEX, line))) for line in input_str])
    min_t, max_t = get_min_max_for_race(race)
    return max_t - min_t + 1
