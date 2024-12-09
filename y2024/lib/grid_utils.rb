def in_bounds?(grid, vector)
    result = (vector[0] >= 0) && (vector[1] >= 0) && (vector[0] < grid.length) && (vector[1] < grid[vector[0]].length)
    return result
end

def get_grid_element(grid, vector)
    if in_bounds?(grid, vector) then
        return grid[vector[0]][vector[1]]
    end
    return nil
end

def print_grid(grid)
    for line in grid do
        puts line.join("")
    end
end