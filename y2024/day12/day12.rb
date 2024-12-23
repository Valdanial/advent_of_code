require "matrix"
require "./lib/grid_utils.rb"

def get_garden(input)
    garden = input.map {
        |line|
        line.chars
    }
    return garden
end

def get_corner_count(empty_sides, empty_diagonals)
    result = 0
    if empty_sides.length == 4 then
        return 4
    elsif empty_sides.length == 3 then
        return 2
    elsif empty_sides.length == 2 then
        result += 1 if !empty_sides.sum(Vector.zero 2).zero?
    end
    (CARDINAL_VECTORS - empty_sides).combination(2).each {
        |pair|
        result += 1 if empty_diagonals.include?(pair[0] + pair[1])
    }
    return result
end

def compute_perimeters_and_groups(garden)
    groups = []
    tile_infos = Array.new(garden.length) {Array.new(garden.length)}
    garden.each_index {
        |y|
        garden[y].each_index {
            |x|
            if !tile_infos[y][x] then
                to_process = [Vector[y, x]]
                while to_process.length > 0 do
                    position = to_process.pop
                    type = get_grid_element(garden, position)
                    tile_info = {:group => nil, :perimeter => 0}
                    empty_sides = []
                    empty_diagonals = []
                    CARDINAL_VECTORS.each {
                        |direction|
                        neighbour = direction + position
                        if get_grid_element(garden, neighbour) == type then
                            if get_grid_element(tile_infos, neighbour) then
                                if !tile_info[:group] then
                                    tile_info[:group] = get_grid_element(tile_infos, neighbour)[:group]
                                    tile_info[:group][:tiles].push(position)
                                end
                            else
                                to_process.push(neighbour) if !to_process.include?(neighbour)
                            end
                        else
                            tile_info[:perimeter] += 1
                            empty_sides.push(direction)
                        end
                    }
                    DIAGONAL_VECTORS.each {
                        |direction|
                        neighbour = direction + position
                        empty_diagonals.push(direction) if get_grid_element(garden, neighbour) != type
                    }
                    if not tile_info[:group] then
                        # Initialize group if not present
                        tile_info[:group] = {:type => type, :perimeter => 0, :tiles => [position], :corner_count => 0} 
                        groups.push(tile_info[:group])
                    end
                    corner_count = get_corner_count(empty_sides, empty_diagonals)
                    tile_info[:group][:corner_count] += get_corner_count(empty_sides, empty_diagonals)
                    tile_info[:group][:perimeter] += tile_info[:perimeter]
                    tile_infos[position[0]][position[1]] = tile_info
                end
            end
        }
    }
    return groups, tile_infos
end

def get_total_prices(groups)
    total_price_perimeter = 0
    total_price_side = 0
    groups.each {
        |group|
        total_price_perimeter += group[:tiles].length * group[:perimeter]
        total_price_side += group[:tiles].length * group[:corner_count]
    }
    return total_price_perimeter, total_price_side
end

# PART 1
def part1(input)
    garden = get_garden(input)
    groups, tile_infos = compute_perimeters_and_groups(garden)
    total_price_perimeter, _ = get_total_prices(groups)
    return total_price_perimeter
end

# PART 2
def part2(input)
    garden = get_garden(input)
    groups, tile_infos = compute_perimeters_and_groups(garden)
    _, total_price_side = get_total_prices(groups)
    return total_price_side
end
