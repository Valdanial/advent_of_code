
LEFT =  Vector[0, -1]
RIGHT = Vector[0, 1]
UP = Vector[-1, 0]
DOWN = Vector[1, 0]
UP_LEFT = UP + LEFT
UP_RIGHT = UP + RIGHT
DOWN_LEFT = DOWN + LEFT
DOWN_RIGHT = DOWN + RIGHT

CARDINAL_VECTORS = [LEFT, RIGHT, UP, DOWN]
DIAGONAL_VECTORS = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

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

def get_grid_from_input(input)
    return input.map {
        |line|
        line.split('')
    }
end