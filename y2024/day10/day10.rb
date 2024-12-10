require "matrix"
require "./lib/grid_utils.rb"

CARDINAL_VECTORS = [Vector[-1, 0], Vector[1, 0], Vector[0, -1], Vector[0, 1]]
TRAIL_PROCESSING_ORDER = ((0..9).map {|el| el.to_s}).reverse

TRAIL_END = TRAIL_PROCESSING_ORDER[0]
TRAIL_START = TRAIL_PROCESSING_ORDER[-1]

def get_trail_infos(grid)
    destinations_map = Array.new(grid.length) {Array.new(grid[0].length) {Set.new()}}
    trail_possibility_map = Matrix.zero(grid.length)
    TRAIL_PROCESSING_ORDER.each_index {
        |current_trail_step_index|
        grid.each_index {
            |y|
            grid[y].each_index {
                |x|
                pos = Vector[y, x]
                if get_grid_element(grid, pos) != TRAIL_START && get_grid_element(grid, pos) == TRAIL_PROCESSING_ORDER[current_trail_step_index] then
                    CARDINAL_VECTORS.each {
                        |direction|
                        neighbour = pos + direction
                        if get_grid_element(grid, neighbour) == TRAIL_PROCESSING_ORDER[current_trail_step_index + 1] then
                            if get_grid_element(grid, pos) == TRAIL_END then
                                destinations_map[neighbour[0]][neighbour[1]].add(pos)
                                trail_possibility_map[*neighbour] += 1
                            else
                                destinations_map[neighbour[0]][neighbour[1]] += destinations_map[y][x]
                                trail_possibility_map[*neighbour] += trail_possibility_map[*pos]
                            end
                        end
                    }
                end
            }
        }
    }
    return destinations_map, trail_possibility_map
end

def get_trailhead_score_sum(grid, destinations_map)
    sum = 0
    grid.each_index {
        |y|
        grid[y].each_index {
            |x|
            if grid[y][x] == TRAIL_START then
                sum += destinations_map[y][x].length
            end
        }
    }
    return sum
end

def get_trailhead_rating_sum(grid, trail_possibility_map)
    sum = 0
    grid.each_index {
        |y|
        grid[y].each_index {
            |x|
            if grid[y][x] == TRAIL_START then
                sum += trail_possibility_map[y, x]
            end
        }
    }
    return sum
end

# PART 1
def part1(input)
    grid = get_grid_from_input(input)
    destinations_map, _ = get_trail_infos(grid)
    return get_trailhead_score_sum(grid, destinations_map)
end

# PART 2
def part2(input)
    grid = get_grid_from_input(input)
    _, trail_possibility_map = get_trail_infos(grid)
    return get_trailhead_rating_sum(grid, trail_possibility_map)
end
