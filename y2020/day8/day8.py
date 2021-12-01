from typing import List

from y2020.lib.multiline_input import get_multiline_input

def acc(state: dict, argument: str):
    if not argument:
        return state
    state["acc"] += int(argument)
    return state

def jmp(state: dict, argument: str):
    if not argument:
        return state
    state["cursor"] += int(argument)
    return state

def nop(state: dict, argument: str):
    return state

OPERATIONS_MAP = {
    "acc": acc,
    "jmp": jmp,
    "nop": nop
}

def is_end_state(state: dict):
    end_status = ["ENDED"]
    return state["status"] == "ENDED"

def update_state(state: dict)->dict:
    if state["cursor"] in state["already_executed"]:
        state["status"] = "ENDED"
        state["error"] = "INSTRUCTION_ALREADY_EXECUTED"
    if state["cursor"] == len(state["instructions_list"]):
        state["status"] = "ENDED"
    return state

def program_runner(instructions_list: List[str]):
    state = {
        "acc": 0,
        "cursor": 0,
        "already_executed": [],
        "instructions_list": instructions_list,
        "status": "RUNNING"
    }
    while not is_end_state(state):
        current_cursor = state["cursor"]
        split_instruction = instructions_list[current_cursor].split()
        operation = split_instruction[0]
        argument = split_instruction[1]
        state = OPERATIONS_MAP[operation](state, argument)
        if current_cursor == state["cursor"]:
            # force incrementation of cursor if operation did not move it
            state["cursor"] += 1
        state["already_executed"].append(current_cursor)
        state = update_state(state)
    return state

def test_replace_one_instruction(instructions_list: List[str]):
    # returns state of program after a successful execution(or None if there's none)
    for idx in range(len(instructions_list)):
        instruction = instructions_list[idx]
        new_instruction_list = [ins for ins in instructions_list]
        if "nop" in instruction:
            instruction = instruction.replace("nop", "jmp")
        if "jmp" in instruction:
            instruction = instruction.replace("jmp", "nop")
        new_instruction_list[idx] = instruction
        state = program_runner(new_instruction_list)
        if "error" not in state:
            return state
    return None


ins_list = get_multiline_input("y2020/input/day8")

state_after_run = program_runner(ins_list)

acc_value_after_run = state_after_run["acc"]

print(f"Part 1: value of acc after run = {acc_value_after_run}")

part_2_state = test_replace_one_instruction(ins_list)
part_2_acc = part_2_state["acc"]
print(f"Part 2: value of acc after run = {part_2_acc}")