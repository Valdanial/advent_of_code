from functools import reduce
from y2021.lib.multiline_input import get_multiline_input

INPUT_FILE = "y2021/input/day18"
TEST_FILE_1 = "y2021/input/day18_test1"

class NodeFactory():
    def __init__(self) -> None:
        self.uid_counter = 0

    def create_node(self, value=None):
        node = Node(self.uid_counter)
        if value is not None:
            node.is_end = True
            node.left_value = value
        self.uid_counter += 1
        return node

NODE_FACTORY = NodeFactory()

class Node():
    def __init__(self, uid) -> None:
        self.uid = uid
        self.left_value = None
        self.right_value = None
        self.parent_node = None
        self.is_end = False

    def get_right_innermost(self):
        if self.is_end:
            return self
        return self.right_value.get_right_innermost()

    def get_left_innermost(self):
        if self.is_end:
            return self
        return self.left_value.get_left_innermost()

    def split(self):
        left_value = NODE_FACTORY.create_node(int(self.left_value / 2))
        left_value.parent_node = self
        right_value = NODE_FACTORY.create_node(self.left_value - left_value.left_value)
        right_value.parent_node = self
        self.left_value = left_value
        self.right_value = right_value
        self.is_end = False

    def explode(self):
        parent_node = self.parent_node
        if parent_node.left_value == self:
            if not parent_node.right_value.is_end:
                pri = parent_node.right_value.get_left_innermost()
                pri.left_value += self.right_value.left_value
            else:
                parent_node.right_value.left_value += self.right_value.left_value
            # Check parents
            current_node = parent_node
            while current_node and current_node.parent_node and current_node.parent_node.left_value == current_node:
                current_node = current_node.parent_node
            if current_node and current_node.parent_node:
                cri = current_node.parent_node.left_value.get_right_innermost()
                if cri:
                    cri.left_value += self.left_value.left_value
            parent_node.left_value = NODE_FACTORY.create_node(0)
            parent_node.left_value.parent_node = parent_node
        else:
            if not parent_node.left_value.is_end:
                pli = parent_node.left_value.get_right_innermost()
                pli.right_value += self.left_value.left_value
            else:
                parent_node.left_value.left_value += self.left_value.left_value
            # Check parents
            current_node = parent_node
            while current_node and current_node.parent_node and current_node.parent_node.right_value == current_node:
                current_node = current_node.parent_node
            if current_node and current_node.parent_node:
                cli = current_node.parent_node.right_value.get_left_innermost()
                if cli:
                    cli.left_value += self.right_value.left_value
            parent_node.right_value = NODE_FACTORY.create_node(0)
            parent_node.right_value.parent_node = parent_node

    def __eq__(self, other):
        return isinstance(other, Node) and self.uid == other.uid

    def check_splittable(self):
        if self.is_end:
            return self.left_value >= 10 and self
        return self.left_value.check_splittable() or self.right_value.check_splittable()

    def check_explodable(self, depth=0):
        if self.is_end:
            return False
        if depth >= 4 and self.left_value.is_end and self.right_value.is_end:
            return self
        return (self.left_value.check_explodable(depth + 1)) or (self.right_value.check_explodable(depth + 1))

    def reduce(self):
        node_reduced = True
        while node_reduced:
            node_reduced = False
            explodable = self.check_explodable()
            if explodable:
                explodable.explode()
                node_reduced = True
            else:
                splittable = self.check_splittable()
                if splittable:
                    splittable.split()
                    node_reduced = True

    def __add__(self, other):
        if self.is_end:
            self.left_value += other.left_value
            result = self
        else:
            result = NODE_FACTORY.create_node()
            result.left_value = self
            result.right_value = other
            self.parent_node = result
            other.parent_node = result
            result.reduce()
        return result

    def get_magnitude(self):
        if self.is_end:
            return self.left_value
        return 3 * self.left_value.get_magnitude() + 2 * self.right_value.get_magnitude()

    def __str__(self):
        if self.is_end:
            return str(self.left_value)
        left_str = str(self.left_value)
        right_str = str(self.right_value)
        return f'[{left_str},{right_str}]'


def get_snail_number(input_number):
    node_to_return = NODE_FACTORY.create_node()
    current_node = node_to_return
    for c in input_number[1:]:
        if c == '[':
            # Create new Node, with current_node as parent
            new_node = NODE_FACTORY.create_node()
            new_node.parent_node = current_node
            if current_node.left_value is None:
                current_node.left_value = new_node
            else:
                current_node.right_value = new_node
            current_node = new_node
        elif c == ']':
            # End of node, new current is parent
            current_node = current_node.parent_node
        elif c != ',':
            if not current_node.left_value:
                current_node.left_value = NODE_FACTORY.create_node(int(c))
                current_node.left_value.parent_node = current_node
            else:
                current_node.right_value = NODE_FACTORY.create_node(int(c))
                current_node.right_value.parent_node = current_node
    return node_to_return

def get_part_1_result(input):
    snail_numbers = []
    for line in input:
        snail_numbers.append(get_snail_number(line))
    result_node = reduce(lambda x, y: x + y, snail_numbers)
    return result_node.get_magnitude()

def get_part_2_result(input):
    m = 0
    for line_1 in input:
        for line_2 in [line for line in input if line != line_1]:
            result_1 = get_snail_number(line_1) + get_snail_number(line_2)
            result_2 = get_snail_number(line_2) + get_snail_number(line_1)
            m = max(m, result_1.get_magnitude(), result_2.get_magnitude())
    return m

def test_and_execute():
    # Part 1 tests
    test_list_1 = get_multiline_input(TEST_FILE_1)
    test_1_1_result = get_part_1_result(test_list_1)
    assert(test_1_1_result == 4140)

    test_2_1_result = get_part_2_result(test_list_1)
    assert(test_2_1_result == 3993)

    # Part 1

    input_list = get_multiline_input(INPUT_FILE)
    part_1_result = get_part_1_result(input_list)
    print(f"Part 1: result = {part_1_result}")

    # Part 2

    input_list = get_multiline_input(INPUT_FILE)
    part_2_result = get_part_2_result(input_list)
    print(f"Part 2: result = {part_2_result}")

test_and_execute()