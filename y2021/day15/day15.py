import heapq
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day15"
TEST_FILE_1 = "y2021/input/day15_test1"

NEIGHBOUR_VECTORS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

class NodeWithScore():
    def __init__(self, coordinates, score):
        self.coordinates = coordinates
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

def get_neighbours(grid, point):
    neighbours = []
    for neighbour_vector in NEIGHBOUR_VECTORS:
        neighbour_coordinates = []
        for c, nc in zip(point, neighbour_vector):
            neighbour_coordinates.append(c + nc)
        if grid.get(tuple(neighbour_coordinates)):
            neighbours.append(tuple(neighbour_coordinates))
    return neighbours

def get_grid(input, offset=0, xoffset=0, yoffset=0):
    grid = {}
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            grid[(x + xoffset, y + yoffset)] = ((int(c) - 1 + offset) % 9) + 1
    return grid

def get_theorical_min_dist(a, b):
    dist = 0
    for ac, bc in zip(a, b):
        dist += abs(bc - ac)
    return dist

def get_shortest_path(start, finish, grid):
    distance_map = {start: 0} # starting position cost is always zero
    nodes_to_consider = [NodeWithScore(start, 0)]
    while nodes_to_consider:
        point_to_consider = heapq.heappop(nodes_to_consider).coordinates
        neighbours = get_neighbours(grid, point_to_consider)
        for neighbour in neighbours:
            neighbour_distance = distance_map.get(point_to_consider) + grid.get(neighbour)
            if neighbour not in distance_map.keys() or distance_map[neighbour] > neighbour_distance:
                heapq.heappush(nodes_to_consider, NodeWithScore(neighbour, neighbour_distance + get_theorical_min_dist(neighbour, finish)))
                distance_map[neighbour] = neighbour_distance
    return distance_map[finish]

def get_part_1_result(input):
    grid = get_grid(input)
    return get_shortest_path((0, 0), (len(input[0]) - 1, len(input) - 1), grid)

def get_part_2_result(input):
    PART_2_MULTIPLICATOR = 5
    xlen = len(input[0])
    ylen = len(input)
    grid = {}
    for y in range(PART_2_MULTIPLICATOR):
        yoffset = y * ylen
        for x in range(PART_2_MULTIPLICATOR):
            xoffset = x * xlen
            grid.update(get_grid(input, x + y, xoffset, yoffset))
    return get_shortest_path((0, 0), (len(input[0]) * PART_2_MULTIPLICATOR - 1, len(input) * PART_2_MULTIPLICATOR - 1), grid)

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1)
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 40)

    # Part 2 tests
    test_2_1_result = get_part_2_result(test_list_1)
    assert(test_2_1_result == 315)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()