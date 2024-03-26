from typing import List

def get_multiline_input(input_file_name: str, separator = "\n")->List[str]:
    file_content = open(input_file_name, "r").read()
    content_list = file_content.split(separator)
    if not content_list[-1]:
        content_list = content_list[:-1] # removing last line if empty
    return content_list

def get_multiline_integers(input_file_name: str, separator = "\n")->List[int]:
    str_list = get_multiline_input(input_file_name, separator)
    result_list = []
    for s in str_list:
        result_list.append(int(s))
    return result_list