import re
import math

SYMBOL_REGEX = r"[^\d\.]"
NUMBER_REGEX = r"\d+"
GEAR_REGEX = r"\*"
NEIGHBOURS = [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,-1),(1,1),(-1,1)]

def get_symbols(input_str: list[str], regex = SYMBOL_REGEX):
    symbols: dict = {}
    for y, line in enumerate(input_str):
        for m in re.finditer(regex, line):
            symbols[y,m.start()] = []
    return symbols

def get_part_numbers(input_str: list[str], symbols: dict):
    part_numbers = []
    for y, line in enumerate(input_str):
        for m in re.finditer(NUMBER_REGEX, line):
            if any([(j, i) in symbols.keys() for j in range(y-1, y+2) for i in range(m.start() - 1 , m.end() + 1)]):
                part_numbers.append(int(m.group(0)))
    return part_numbers

def get_gear_numbers(input_str: list[str], symbols: dict):
    for y, line in enumerate(input_str):
        for m in re.finditer(NUMBER_REGEX, line):
            for j in range(y-1, y+2):
                for i in range(m.start() - 1, m.end() + 1):
                    if (j,i) in symbols.keys():
                        symbols[(j,i)].append(int(m.group(0)))

# Part 1
def part1(input_str: list[str])->str:
    symbols = get_symbols(input_str)
    return sum(get_part_numbers(input_str, symbols))

# Part 2
def part2(input_str: list[str])->str:
    gears = get_symbols(input_str, GEAR_REGEX)
    get_gear_numbers(input_str, gears)
    res = 0
    for associated_numbers in gears.values():
        if len(associated_numbers) == 2:
            res += math.prod(associated_numbers)
    return res
