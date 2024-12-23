import importlib
import sys
from lib.multiline_input import get_input, get_test_input

DAY_PREFIX = "day"
INPUT_PATH = './input/'
INPUT_SEPARATOR = "\n"

def run_day(day: int, is_test_run: bool):
    day_str = DAY_PREFIX + str(day)
    day_module = importlib.import_module(day_str + "." + day_str, '.')

    input_separator = day_module.INPUT_SEPARATOR if hasattr(day_module, "INPUT_SEPARATOR") else INPUT_SEPARATOR

    input_get_func = get_test_input if is_test_run else get_input

    if is_test_run:
        print("Running with test input")

    raw_input = input_get_func(INPUT_PATH + day_str, input_separator)


    # PART 1
    result_1 = day_module.part1(raw_input)
    print("PART 1:", result_1)

    # PART 2
    result_2 = day_module.part2(raw_input)
    print("PART 2:", result_2)

if len(sys.argv) > 1:
    input_day = int(sys.argv[1])
    if 1 <= input_day and input_day <= 25:
        is_test = len(sys.argv) > 2 and sys.argv[2] == "test"
        run_day(input_day, is_test)
    else:
        print("Invalid first argument: Needs to be a number between 1 and 25")
else:
    print("Missing argument. First argument should be day number, like '2'")
