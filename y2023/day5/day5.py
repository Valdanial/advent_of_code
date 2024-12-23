import re
from itertools import accumulate

INPUT_SEPARATOR = "\n\n"
NUM_REGEX = r"\d+"

def get_maps_and_seed_ranges(input_str: list[str], is_seed_range: bool = False)->tuple[list[int], dict]:
    seed_numbers = list(map(int, re.findall(NUM_REGEX, input_str[0])))
    seed_ranges = map(lambda a, b: [a, b], seed_numbers[::2], seed_numbers[1::2]) if is_seed_range else map(lambda a: [a, 1], seed_numbers)
    maps = {}
    for map_str in input_str[1:]:
        split_map_str = map_str.splitlines()
        map_name = split_map_str[0][0:-5]
        maps[map_name] = [tuple(map(int, re.findall(NUM_REGEX, map_line))) for map_line in split_map_str[1:]]
    return seed_ranges, maps

def process_range(r: tuple[int], m: tuple[int])->tuple[tuple[int], list[tuple[int]]]:
    res, rem = [], []
    start = max(r[0], m[1])
    end = min(r[0] + r[1], m[1] + m[2])
    if start >= end: # no intersection
        rem.append(r)
    else:
        res.append((m[0] + start - m[1], end - start)) #  intersection
        if start > r[0]: # remaining on the left
            rem.append((r[0], start - r[0]))
        if end < r[0] + r[1]: # remaining on the right
            rem.append((end, r[1] - end + start))
    return res, rem

def process_with_maps(seed_ranges: list[tuple[int, int]], maps: dict)->list[int]:
    result_ranges = [*seed_ranges]
    for map_type in maps.values():
        current = [*result_ranges]
        result_ranges = []
        for m in map_type:
            remaining = []
            for seed_range in current:
                res, rem = process_range(seed_range, m)
                result_ranges += res
                remaining += rem
            current = [*remaining]
        result_ranges += remaining
    
    return result_ranges


# Part 1
def part1(input_str: list[str])->str:
    seed_ranges, maps = get_maps_and_seed_ranges(input_str)
    processed_seeds = process_with_maps(seed_ranges, maps)
    return min(processed_seeds)[0]

# Part 2
def part2(input_str: list[str])->str:
    seed_ranges, maps = get_maps_and_seed_ranges(input_str, True)
    processed_seeds = process_with_maps(seed_ranges, maps)
    return min(processed_seeds)[0]
