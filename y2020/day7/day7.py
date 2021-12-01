import re

from typing import List

from y2020.lib.multiline_input import get_multiline_input

STATEMENTS_REGEX = re.compile(r"^([\w ]+) bags? contain ((?:\d+ [\w ]+ bags?,? ?)+|(?:no other bags))\.$")
CONTAINED_REGEX = re.compile(r" ?(\d+) ([\w+ ]+) bags?\.?,?")

def get_bag_map(bags_spec: List[str])->dict:
    bag_map = {}
    for bag_spec in bags_spec:
        container_bag, contained_bags_spec = STATEMENTS_REGEX.match(bag_spec).groups()
        if contained_bags_spec != "no other bags":
            bag_map[container_bag] = []
            split_contained_bags_spec = contained_bags_spec.split(",")
            for contained_bag_spec in split_contained_bags_spec:
                quantity, color = CONTAINED_REGEX.match(contained_bag_spec).groups()
                bag_map[container_bag].append({
                    "quantity": int(quantity),
                    "color": color
                })
    return bag_map

def get_bags_that_can_contain(bag_color: str, bag_map: dict, ignore_list: List[str] = None)->List[str]:
    directly_contains = []
    blacklist = ignore_list or []
    for container_color, content_list in bag_map.items():
        for content in content_list:
            if content["color"] == bag_color and not(blacklist and container_color in blacklist):
                directly_contains.append(container_color)
                blacklist.append(container_color)
    other_containers = []
    for container in directly_contains:
        other_containers += get_bags_that_can_contain(container, bag_map, blacklist)
    return directly_contains + other_containers

def get_number_of_contained_bags(bag_color: str, bag_map: dict):
    # There could be an issue of recursion between contained bags, but that would mean the input bag contains an infinity of bags, so let's ignore that...
    count = 0
    content_list = bag_map[bag_color]
    for content in content_list:
        subcount = get_number_of_contained_bags(content["color"], bag_map) if content["color"] in bag_map else 0
        count += content["quantity"] * (subcount + 1)
    return count

spec = get_multiline_input("y2020/input/day7")

bag_map = get_bag_map(spec)

part_1_number = len(get_bags_that_can_contain("shiny gold", bag_map))
print(f"Part 1: Nubmer of bags that contain shiny gold bag = {part_1_number}")

part_2_count = get_number_of_contained_bags("shiny gold", bag_map)
print(f"Part 2: Number of contained bags = {part_2_count}")