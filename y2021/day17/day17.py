import math

INPUT_FILE = "y2021/input/day17"

MIN_X = 150
MAX_X = 171
MIN_Y = -129
MAX_Y = -70

MAX_STEPS = 500

def get_part_1_result(ymin, ymax):
    highest_point = -math.inf
    for y in range(ymin, -ymin):
        max_y = 0
        current_y = 0
        n = 0
        while n < MAX_STEPS and current_y >= ymax:
            current_y += y - n
            max_y = max(current_y, max_y)
            n += 1
        if ymin <= current_y <= ymax:
            highest_point = max(highest_point, max_y)
    return highest_point

def get_part_2_result(ymin, ymax, xmin, xmax):
    y_pairs = []
    x_pairs = []
    for y in range(ymin, -ymin):
        current_y = 0
        n = 0
        while n < MAX_STEPS and ymin <= current_y:
            current_y += y - n
            n += 1
            if ymax >= current_y >= ymin:
                y_pairs.append((n, y))
    for x in range(0, MAX_STEPS):
        current_x = 0
        n = 0
        while n < x + 1:
            current_x += x - n
            current_x = 0 if current_x < 0 else current_x
            n += 1
            if xmax >= current_x >= xmin:
                x_pairs.append((n, x))
    valid_entries = []
    for ny, y in y_pairs:
        for x in [x for nx, x in x_pairs if nx == ny or ny > x and (x, x) in x_pairs]:
            valid_entries.append((x, y))
    valid_entries = set(valid_entries)
    return len(valid_entries)

def test_and_execute():
    # Part 1 tests
    test_1_1_result = get_part_1_result(-10, -5)
    assert(test_1_1_result == 45)

    # Part 2 tests
    test_2_1_result = get_part_2_result(-10, -5, 20, 30)
    assert(test_2_1_result == 112)

    # Part 1

    part_1_result = get_part_1_result(MIN_Y, MAX_Y)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    part_2_result = get_part_2_result(MIN_Y, MAX_Y, MIN_X, MAX_X)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()