from typing import List

def get_first_by_sum(number_list: List[int], target_sum: int, numbers_required: int):
    if numbers_required <= 0:
        if target_sum == 0:
            return []
        return None
    if target_sum <= 0:
        return None
    to_check = [number for number in number_list]
    for number in number_list:
        to_check.remove(number)
        check_result = get_first_by_sum(to_check, target_sum - number, numbers_required - 1)
        if check_result is not None:
            check_result.append(number)
            return check_result
    return None