require 'Matrix'

NUM_PATTERN = /[-\d]+/

def get_pos_after(initial_pos, velocity, max_y, max_x, time)
    end_pos = initial_pos + time * velocity
    actual_end_pos = Vector[end_pos[0] % max_y, end_pos[1] % max_x]
    return actual_end_pos
end

def get_safety_factor(input, time, y_size, x_size)
    end_positions = Matrix.zero(y_size, x_size)
    top_left_count = 0
    top_right_count = 0
    bottom_right_count = 0
    bottom_left_count = 0
    input.each {
        |line|
        line_values = line.scan(NUM_PATTERN).map {|num| Integer(num)}
        initial_pos = Vector[*line_values.slice(0, 2).reverse]
        velocity = Vector[*line_values.slice(2, 2).reverse]
        end_pos = get_pos_after(initial_pos, velocity, y_size, x_size, time)
        end_positions[*end_pos] += 1
        if end_pos[0] > (y_size - 1) / 2 then
            if end_pos[1] > (x_size - 1) / 2 then
                bottom_right_count += 1
            elsif end_pos[1] < (x_size - 1) / 2
                bottom_left_count += 1
            end
        elsif end_pos[0] < (y_size - 1) / 2
            if end_pos[1] > (x_size - 1) / 2 then
                top_right_count += 1
            elsif end_pos[1] < (x_size - 1) / 2
                top_left_count += 1
            end
        end
    }
    return top_left_count * top_right_count * bottom_right_count * bottom_left_count, end_positions
end

def print_matrix(m)
    lines = []
    m.row_vectors.each {
        |row|
        line = ""
        row.each {
            |el|
            if el > 0 then
                line += "#"
            else
                line += "."
            end
        }
        lines.push(line)
    }
    puts lines.join("\n")
end

def get_christmas_tree(input, y_size, x_size)
    i = 0
    while i < 10000 do
        go_next = false
        _, m = get_safety_factor(input, i, y_size, x_size)
        m.row_vectors.each {
            |row|
            if !go_next then
                robot_line_size = 0
                row.each {
                    |el|
                    if !go_next then
                        if el > 0 then
                            robot_line_size += 1
                        else
                            robot_line_size = 0
                        end
                        if robot_line_size > 10 then
                            puts "i = #{i}"
                            print_matrix(m)
                            go_next = true
                        end
                    end
                }
            end
        }
        i += 1
    end
end


# PART 1
def part1(input)
    res, _ = get_safety_factor(input, 100, 103, 101)
    return res
end

# PART 2
def part2(input)
    get_christmas_tree(input, 103, 101)
    return "Implemented but in a pretty unclean way, because laziness"
end
