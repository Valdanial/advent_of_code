require "matrix"
require "./lib/grid_utils.rb"

XMAS = "XMAS"

DIAGONAL_VECTORS = [Vector[-1, -1], Vector[-1, 1], Vector[1, -1], Vector[1, 1]]
ORTHOGONAL_VECTORS = [Vector[-1, 0], Vector[1, 0], Vector[0, -1], Vector[0, 1]]
NEIGHBOUR_VECTORS = DIAGONAL_VECTORS + ORTHOGONAL_VECTORS

def find_words_from(grid, word, neighbour_vectors, position)
    count = 0
    if word[0] == get_grid_element(grid, position) then
        if word.length == 1 then return 1 end
        for neighbour_vector in neighbour_vectors do
            count += find_words_from(grid, word[1, word.length], [neighbour_vector], neighbour_vector + position)
        end
    end
    return count
end

def find_word_occurences(grid, word, neighbour_vectors)
    occurences = 0
    grid.each_index {
        |y|
        grid[y].each_index {
            |x|
            occurences += find_words_from(grid, word, neighbour_vectors, Vector[y, x])
        }
    }
    return occurences
end

def x_mas?(grid, position, neighbour_vectors)
    ms_count = 0
    for neighbour_vector in neighbour_vectors do
        char_to_check = get_grid_element(grid, position + neighbour_vector)
        if char_to_check == "M" then
            if get_grid_element(grid, position + neighbour_vector * -1) == "S" then ms_count += 1 end
        end
    end
    return ms_count == 2
end

def find_x_mas(grid, neighbour_vectors)
    count = 0
    grid.each_index {
        |y|
        grid[y].each_index {
            |x|
            if get_grid_element(grid, Vector[y, x]) == "A" and x_mas?(grid, Vector[y, x], neighbour_vectors) then count += 1 end
        }
    }
    return count
end

def get_word_grid(input)
    grid = []
    i = 0
    while i < input.length do
        grid[i] = []
        for char in input[i].split('') do
            grid[i].push(char)
        end
        i += 1
    end
    return grid
end


# PART 1
def part1(input)
    grid = get_word_grid(input)
    count = find_word_occurences(grid, XMAS, NEIGHBOUR_VECTORS)
    return count
end

# PART 2
def part2(input)
    grid = get_word_grid(input)
    return find_x_mas(grid, DIAGONAL_VECTORS)
end
