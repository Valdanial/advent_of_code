import re

from typing import List

from y2020.lib.multiline_input import get_multiline_input

BOARDING_PASS_REGEX = re.compile(r"^([BF]+)([LR]+)$")

def get_seat_id(seat_spec: str):
    row_spec, column_spec = BOARDING_PASS_REGEX.match(seat_spec).groups()
    row_binary = row_spec.replace("F", "0")
    row_binary = row_binary.replace("B", "1")
    column_binary = column_spec.replace("L", "0")
    column_binary = column_binary.replace("R", "1")

    row = int(row_binary, 2)
    column = int(column_binary, 2)
    return row * 8 + column

def check_missing_seat(seat_id_list: List[str]):
    for seat_id in seat_id_list:
        if seat_id + 1 not in seat_id_list and seat_id + 2 in seat_id_list:
            return seat_id + 1
    return None

seat_spec_list = get_multiline_input("y2020/input/day5")

seat_ids = []
for seat_spec in seat_spec_list:
    seat_ids.append(get_seat_id(seat_spec))

max_id = max(seat_ids)

print(f"Part 1: max seat id = {max_id}")

missing_seat = check_missing_seat(seat_ids)

print(f"Part 2: missing_seat = {missing_seat}")
