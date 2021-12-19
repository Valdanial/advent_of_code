from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day16"
TEST_FILE_1 = "y2021/input/day16_test1"

LITERAL_VALUE_TYPE = 4

OPERATION_TYPES = {
    0: sum,
    1: lambda args: reduce(lambda a,b: a * b, args),
    2: min,
    3: max,
    5: lambda args: reduce(lambda a,b: a > b, args),
    6: lambda args: reduce(lambda a,b: a < b, args),
    7: lambda args: reduce(lambda a,b: a == b, args),
}

def decode_literal_value(binary_packet):
    remaining_packet = binary_packet
    binary_value = ''
    not_last_packet = 1
    while not_last_packet and len(remaining_packet) > 4:
        not_last_packet = int(remaining_packet[0])
        binary_value += remaining_packet[1:5]
        remaining_packet = remaining_packet[5:]
    return int(binary_value, 2), remaining_packet

def decode(binary_packet):
    # Decodes a single packets and its subpackets
    if not binary_packet or len(binary_packet) < 6:
        return None, binary_packet
    decoded_object = {}
    decoded_object['version_number'] = int(binary_packet[:3], 2)
    decoded_object['type'] = int(binary_packet[3:6], 2)
    remaining_packet = binary_packet
    if decoded_object['type'] == LITERAL_VALUE_TYPE:
        # literal value packet
        decoded_object['value'], remaining_packet = decode_literal_value(binary_packet[6:])
    else:
        # operator packet
        decoded_object['subpackets'] = []
        decoded_object['length_type'] = int(binary_packet[6:7], 2)
        to_decode = binary_packet
        if decoded_object['length_type']:
            decoded_object['length_type_value'] = int(binary_packet[7:18], 2)
            to_decode = binary_packet[18:]
            counter = 0
            while counter != decoded_object['length_type_value']:
                subdecoded, to_decode = decode(to_decode)
                decoded_object['subpackets'].append(subdecoded)
                counter += 1
            remaining_packet = to_decode
        else:
            decoded_object['length_type_value'] = int(binary_packet[7:22], 2)
            to_decode = binary_packet[22:22 + decoded_object['length_type_value']]
            while len(to_decode):
                subdecoded, to_decode = decode(to_decode)
                decoded_object['subpackets'].append(subdecoded)
            remaining_packet = binary_packet[22 + decoded_object['length_type_value']:]
    return decoded_object, remaining_packet

def get_version_sum(decoded_object):
    version_sum = 0
    version_sum += decoded_object["version_number"]
    for subpacket in decoded_object.get("subpackets", []):
        version_sum += get_version_sum(subpacket)
    return version_sum

def get_decoded_value(decoded_object):
    if decoded_object['type'] == LITERAL_VALUE_TYPE:
        return decoded_object['value']
    else:
        return OPERATION_TYPES[decoded_object['type']]([get_decoded_value(subpacket) for subpacket in decoded_object["subpackets"]])

def to_bits(packet):
    result = ''
    for hex in packet:
        result += str(bin(int(hex, 16)))[2:]
    return result

def get_part_1_result(input):
    decoded_object, _ = decode(to_bits(input))
    return get_version_sum(decoded_object)

def get_part_2_result(input):
    decoded_object, _ = decode(to_bits(input))
    return get_decoded_value(decoded_object)

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1)
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 16)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()