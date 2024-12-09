# There most likely exists a better implementation, especially as this is a bit slow

require "matrix"
require "./lib/grid_utils.rb"

DIRECTION_ARRAY = [Vector[-1, 0], Vector[0, 1], Vector[1, 0], Vector[0, -1]] # Cardinal direction, top first, order is in a clockwise rotation
GUARD_CHAR = "^"
EMPTY_SPACE_CHAR = "."
OBSTACLE_CHAR = "#"

DIRECTION_CHARS = ["^", ">", "v", "<"]

def print_state(state)
    # Just a test function to print the grid :)
    puts
    print_grid = Marshal.load(Marshal.dump(state[:grid]))
    print_grid[state[:guard_position][0]][state[:guard_position][1]] = DIRECTION_CHARS[state[:direction_index]]
    print_grid(print_grid)
end

def print_end_state(state, path)
    # Just a test function to print the grid at the end state :)
    puts
    print_grid = Marshal.load(Marshal.dump(state[:grid]))
    for position in path do
        print_grid[position[0]][position[1]] = "X"
    end
    print_grid(print_grid)
end

def get_initial_state(input)
    grid = []
    guard_position = nil
    input.each_index {
        |y|
        grid.push([])
        line = input[y].split("")
        line.each_index {
            |x|
            char = line[x]
            if char == GUARD_CHAR then
                guard_position = Vector[y, x]
                char = EMPTY_SPACE_CHAR
            end
            grid[y].push(char)
        }
    }

    return {:grid => grid, :initial_direction => 0, :initial_guard_position => guard_position}
end

def compute_guard_path(initial_state)
    grid_size = initial_state[:grid].length * initial_state[:grid][0].length
    state = {:grid => Marshal.load(Marshal.dump(initial_state[:grid])),:direction_index => initial_state[:initial_direction], :guard_position => initial_state[:initial_guard_position], :path => {:pos => [], :direction => []}, :stuck_in_loop => false}
    while in_bounds?(state[:grid], state[:guard_position]) do
        next_position = state[:guard_position] + DIRECTION_ARRAY[state[:direction_index]]
        if get_grid_element(state[:grid], next_position) == OBSTACLE_CHAR then
            state[:direction_index] = (state[:direction_index] + 1) % 4 # Rotation is handled via array order
        else
            # Loop detection
            if state[:path][:pos].length > grid_size then
                # We're in a loop
                state[:stuck_in_loop] = true
                return state
            end
            # No loop detected, path computing can resume
            # Firstly, modify grid to account for the path
            state[:path][:pos].push(state[:guard_position])
            state[:path][:direction].push(state[:direction_index])
            state[:guard_position] = next_position
        end
    end
    return state
end

def simulate_obstacle(grid, path, position)

end

# PART 1
def part1(input)
    initial_state = get_initial_state(input)
    state = compute_guard_path(initial_state)
    return Set.new(state[:path][:pos]).length
end

# PART 2
def part2(input)
    result_count = 0
    initial_state = get_initial_state(input)
    path_state = compute_guard_path(initial_state)
    pos_checked = []
    path_set = path_state[:path][:pos]
    path_set.each_index {|i|
        path_position = path_set[i]
        path_direction = path_state[:path][:direction]
        if path_position != initial_state[:initial_guard_position] and not pos_checked.include?(path_position) then
            pos_checked.push(path_position)
            initial_state[:grid][path_position[0]][path_position[1]] = OBSTACLE_CHAR
            test_state = compute_guard_path(initial_state)
            if test_state[:stuck_in_loop] then result_count += 1 
            end
            initial_state[:grid][path_position[0]][path_position[1]] = EMPTY_SPACE_CHAR
        end
    }
    return result_count
end
