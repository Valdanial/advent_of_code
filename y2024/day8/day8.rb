require "matrix"
require "./lib/grid_utils.rb"

def get_grid(input)
    grid = []
    input.each {
        |line|
        grid.push line.split("")
    }
    return grid
end

def get_occurences_positions(grid)
    occurences_positions = {}
    # Collect all antennas
    grid.each_index {
        |y|
        grid[y].each_index {
            |x|
            char = grid[y][x]
            if char != "." then
                if not occurences_positions[char] then occurences_positions[char] = [] end
                occurences_positions[char].push(Vector[y,x])
            end
        }
    }
    return occurences_positions
end

def get_unique_antinode_locations(grid, occurences_positions)
    unique_antinode_locations = Set.new()
    
    # Compute antinodes
    occurences_positions.each {
        |antenna, positions|
        combinations = positions.combination(2)
        combinations.each {
            |pair|
            antinode_pos = [2 * pair[0] - pair[1], 2 * pair[1] - pair[0]]
            antinode_pos.each {
                |pos| if in_bounds?(grid, pos) then unique_antinode_locations.add(pos) end
            }
        }
    }
    return unique_antinode_locations
end

def get_unique_antinode_locations_v2(grid, occurences_positions)
    unique_antinode_locations = Set.new()
    
    # Compute antinodes
    occurences_positions.each {
        |antenna, positions|
        combinations = positions.combination(2)
        combinations.each {
            |pair|
            antinode_pos = Set.new()
            continue1, continue2 = true, true
            for i in (0..grid.length - 1) do
                if not (continue1 || continue2) then break end
                pos1 = (pair[0] - pair[1]) * i + pair[0]
                pos2 = (pair[1] - pair[0]) * i + pair[1]
                if continue1 && in_bounds?(grid, pos1) then
                    unique_antinode_locations.add(pos1)
                else
                    continue1 = false
                end
                if continue2 && in_bounds?(grid, pos2) then
                    unique_antinode_locations.add(pos2)
                else
                    continue2 = false
                end
            end
        }
    }
    return unique_antinode_locations
end


# PART 1
def part1(input)
    grid = get_grid(input)
    occurences_positions = get_occurences_positions(grid)
    return get_unique_antinode_locations(grid, occurences_positions).length
end

# PART 2
def part2(input)
    grid = get_grid(input)
    occurences_positions = get_occurences_positions(grid)
    return get_unique_antinode_locations_v2(grid, occurences_positions).length
end
