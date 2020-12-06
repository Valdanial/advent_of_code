from typing import List

from y2020.lib.multiline_input import get_multiline_input

class Slope():
    def __init__(self, length, height):
        self.length = length
        self.height = height

class Position():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def get_trees_on_way(pattern: List[str], slope: Slope, position: Position):
    pattern_height = len(pattern)
    pattern_length = len(pattern[position.y]) # if pattern not empty

    tree_on_way = 1 if pattern[position.y][position.x % pattern_length] == '#' else 0
    if position.y + slope.height >= pattern_height:
        return tree_on_way
    new_position = Position(position.x + slope.length, position.y + slope.height)
    return tree_on_way + get_trees_on_way(pattern, slope, new_position)

input_pattern = get_multiline_input("y2020/input/day3_input")

INPUT_SLOPE = Slope(3, 1)

trees_on_way = get_trees_on_way(input_pattern, INPUT_SLOPE, Position())
print(f"Part 1 trees on way = {trees_on_way}")

# Part 2
slopes_collection = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

product = 1

for input_slope in slopes_collection:
    product *= get_trees_on_way(input_pattern, input_slope, Position())

print(f"Part 2 product = {product}")