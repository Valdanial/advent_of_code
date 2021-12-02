from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day2"

MOVING_INSTRUCTION_SEPARATOR = " "
ORIGIN = (0, 0, 0) # (x, y, aim)

def move_from_vector(moving_vector):
    def move(initial_position, step):
        return tuple(current_coordinate + step * direction_coordinate for current_coordinate, direction_coordinate in zip(initial_position, moving_vector))
    return move

def forward(initial_position, step):
    x, y, aim = initial_position
    return (x + step, y + step * aim, aim)

PART_1_INSTRUCTION_MAP = {
    "forward": move_from_vector((1, 0)),
    "up": move_from_vector((0, -1)),
    "down": move_from_vector((0, 1))
}

INSTRUCTION_MAP = {
    "forward": forward,
    "up": move_from_vector((0, 0, -1)),
    "down": move_from_vector((0, 0, 1))
}

def move_from_moving_instructions(moving_instructions, instruction_map, initial_position=None):
    current_position = initial_position or ORIGIN
    for moving_instruction in moving_instructions:
        instruction, instruction_value = tuple(moving_instruction.split(MOVING_INSTRUCTION_SEPARATOR))
        instruction_value = int(instruction_value)
        current_position = instruction_map[instruction](current_position, instruction_value)
    return current_position

# Part 1

input_list = get_multiline_input(INPUT_FILE)
submarine_position = move_from_moving_instructions(input_list, PART_1_INSTRUCTION_MAP)

part_1_result = submarine_position[0] * submarine_position[1]

print(f"Part 1: result = {part_1_result}")

# Part 2

submarine_position = move_from_moving_instructions(input_list, INSTRUCTION_MAP)

part_2_result = submarine_position[0] * submarine_position[1]

print(f"Part 2: result = {part_2_result}")
