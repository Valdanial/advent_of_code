import re
from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day9"

WALL_HEIGHT = 9

class Vector():
    def __init__(self, *position):
        self.position = position

    def __add__(self, other):
        return Vector(*[a + b for a, b in zip(self.position, other.position)])

    def __eq__(self, other):
        return all([a == b for a, b in zip(self.position, other.position)])

    def lower(self, other):
        return self.position[0] >= other.position[0]

    def after(self, other):
        return self.position[1] >= other.position[1]

    def in_bounds(self, v1, v2, v3, v4):
        return self.after(v1) and self.lower(v1) and v2.after(self) and v2.lower(self) and self.lower(v3) and v3.after(self) and v4.lower(self) and self.after(v4)

class Grid():
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def height(self):
        return len(self.matrix)

    @property
    def length(self):
        return len(self.matrix[0])

    def get(self, vector):
        return self.matrix[vector.position[0]][vector.position[1]]

    def get_neighbours(self, vector):
        bounds_vectors = [Vector(0, 0), Vector(self.height - 1, self.length - 1), Vector(0, self.length - 1), Vector(self.height - 1, 0)]
        neighbours = []
        for neighbour_vector in NEIGHBOUR_VECTORS:
            neighbour_position_vector = vector + neighbour_vector
            if neighbour_position_vector.in_bounds(*bounds_vectors):
                neighbours.append(neighbour_position_vector)
        return neighbours


NEIGHBOUR_VECTORS = [Vector(0, 1), Vector(1, 0), Vector(0, -1), Vector(-1, 0)] # 🐴

def input_to_grid(input):
    return Grid([[int(point) for point in line] for line in input])

def get_low_points(grid):
    low_points = []
    for y, h_line in enumerate(grid.matrix):
        for x, value in enumerate(h_line):
            vector = Vector(y, x)
            if all([value < neighbour_value for neighbour_value in [grid.get(neighbour) for neighbour in grid.get_neighbours(vector)]]):
                low_points.append(vector)
    return low_points

def get_higher_connected_points(grid, vector):
    connected_points = [vector]
    vectors_to_consider = [vector]
    while vectors_to_consider:
        vector_to_consider = vectors_to_consider.pop()
        neighbours = grid.get_neighbours(vector_to_consider)
        for neighbour in neighbours:
            if WALL_HEIGHT > grid.get(neighbour) >= grid.get(vector_to_consider) and neighbour not in connected_points:
                connected_points.append(neighbour)
                vectors_to_consider.append(neighbour)
    return connected_points

def get_basin_list(grid):
    low_points = get_low_points(grid)
    basin_list = []
    # For each low point, get basin
    for low_point in low_points:
        basin_list.append(get_higher_connected_points(grid, low_point))
    return basin_list


def get_part_1_result(input):
    grid = input_to_grid(input)
    low_points = [grid.get(low_point) for low_point in get_low_points(grid)]
    return sum(low_points) + len(low_points)

def get_part_2_result(input):
    grid = input_to_grid(input)
    basin_list = get_basin_list(grid)
    sorted_basin_size_list = [len(basin) for basin in basin_list]
    sorted_basin_size_list.sort(reverse=True)
    return reduce(lambda a, b: a * b, sorted_basin_size_list[0:3])

# Part 1

input_list = get_multiline_input(INPUT_FILE)

part_1_result = get_part_1_result(input_list)

print(f"Part 1: result = {part_1_result}")

# Part 2

input_list = get_multiline_input(INPUT_FILE)

part_2_result = get_part_2_result(input_list)

print(f"Part 2: result = {part_2_result}")