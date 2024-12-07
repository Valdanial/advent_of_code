def get_location_lists(input)
    left_location_list = []
    right_location_list = []
    for line in input do
        split_line = line.split('   ')
        left_location_list.push(Integer(split_line[0]))
        right_location_list.push(Integer(split_line[1]))
    end
    return [left_location_list, right_location_list]
end

def get_distance_list(left_location_list, right_location_list)
    sorted_left_location_list = left_location_list.sort
    sorted_right_location_list = right_location_list.sort
    distance_list = []
    i = 0
    while i < sorted_left_location_list.length do
        distance_list.push((sorted_left_location_list[i] - sorted_right_location_list[i]).abs)
        i += 1
    end
    return distance_list
end

def get_similarity_score(left_location_list, right_location_list)
    similarity_score = 0
    for location_id in left_location_list do
        similarity_score += right_location_list.count(location_id) * location_id
    end
    return similarity_score
end

# PART 1
def part1(input)
    location_lists = get_location_lists(input)
    return get_distance_list(location_lists[0], location_lists[1]).sum
end

# PART 2
def part2(input)
    location_lists = get_location_lists(input)
    return get_similarity_score(location_lists[0], location_lists[1])
end
