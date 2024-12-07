ORDERING_SEPARATOR = "|"
UPDATE_SEPARATOR = ","

def get_ordering_rules(ordering_rules_lines)
    return ordering_rules_lines.join(",")
end

def get_middle(update_series)
    middle_index = (update_series.length / 2).floor
    return update_series[middle_index]
end

def order_valid?(update1, update2, ordering_rules)
    return ordering_rules.include?(update1 + ORDERING_SEPARATOR + update2)
end

def sort_update_series(update_series, ordering_rules)
    return update_series.sort {|a,b| order_valid?(a,b,ordering_rules) ? -1 : 1}
end

def update_series_valid?(update_series, ordering_rules)
    i = 0
    while i < update_series.length - 1 do
        if not order_valid?(update_series[i], update_series[i+1], ordering_rules) then return false end
        i += 1
    end
    return true
end

def input_to_update_series(input)
    update_series = []
    for line in input do
        update_series.push(line.split(UPDATE_SEPARATOR))
    end
    return update_series
end

# PART 1
def part1(input)
    result = 0
    ordering_rules = get_ordering_rules(input[0])
    update_series = input_to_update_series(input[1])
    for up_s in update_series do
        if update_series_valid?(up_s, ordering_rules) then result += Integer(get_middle(up_s)) end
    end
    return result
end

# PART 2
def part2(input)
    result = 0
    ordering_rules = get_ordering_rules(input[0])
    update_series = input_to_update_series(input[1])
    for up_s in update_series do
        if not update_series_valid?(up_s, ordering_rules) then
            sorted_update_series = sort_update_series(up_s, ordering_rules)
            result += Integer(get_middle(sorted_update_series))
        end
    end
    return result
end
