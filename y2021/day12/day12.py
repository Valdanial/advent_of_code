import re
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day12"
TEST_FILE_1 = "y2021/input/day12_test1"
TEST_FILE_2 = "y2021/input/day12_test2"
TEST_FILE_3 = "y2021/input/day12_test3"

STARTING_NODE = 'start'
ENDING_NODE = 'end'

def is_visitable_part1(node_name, visit_count):
    return node_name < 'a' or visit_count.get(node_name, 0) < 1

def is_visitable_part2(node_name, visit_count):
    if node_name in [STARTING_NODE, ENDING_NODE]:
        return visit_count.get(node_name, 0) < 1
    return node_name < 'a' or visit_count.get(node_name, 0) < 1 + int(not any([nn > 'a' and c >= 2 for nn, c in visit_count.items()]))

def generate_graph(input):
    # generates graph as dict from input
    graph = {}
    for line in input:
        start, end = tuple(line.split('-'))
        graph[start] = [*graph.get(start, []), end]
        graph[end] = [*graph.get(end, []), start]
    return graph

def list_paths(graph, start, end, visit_count=None, visitable_func=is_visitable_part2):
    current_visit_count = {**visit_count} if visit_count else {}
    current_visit_count[start] = current_visit_count.get(start, 0) + 1
    paths = []
    # get adjacent nodes
    adjacent_nodes = graph.get(start, [])
    for adjacent_node in adjacent_nodes:
        if visitable_func(adjacent_node, current_visit_count):
            # for each adjacent node, list paths from them to end and add start to each of them
            adjacent_paths = list_paths(graph, adjacent_node, end, current_visit_count, visitable_func)
            paths += [[start, *adjacent_path] for adjacent_path in adjacent_paths]
            if adjacent_node == end:
                paths.append([start])
    return paths


def get_part_1_result(input):
    graph = generate_graph(input)
    return len(list_paths(graph, STARTING_NODE, ENDING_NODE, visitable_func=is_visitable_part1))

def get_part_2_result(input):
    graph = generate_graph(input)
    return len(list_paths(graph, STARTING_NODE, ENDING_NODE, visitable_func=is_visitable_part2))

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1)
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 10)
    test_list_2 = get_multiline_input(TEST_FILE_2)
    test_1_2_result = get_part_1_result(test_list_2)
    assert(test_1_2_result == 19)
    test_list_3 = get_multiline_input(TEST_FILE_3)
    test_1_3_result = get_part_1_result(test_list_3)
    assert(test_1_3_result == 226)

    # Part 2 tests
    test_2_1_result = get_part_2_result(test_list_1)
    assert(test_2_1_result == 36)
    test_2_2_result = get_part_2_result(test_list_2)
    assert(test_2_2_result == 103)
    test_2_3_result = get_part_2_result(test_list_3)
    assert(test_2_3_result == 3509)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()