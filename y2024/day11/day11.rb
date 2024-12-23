require './day11/super_stone_solver.rb'

# PART 1
def part1(input)
    stones = input[0].split(" ")
    super_stone_solver = SuperStoneSolver.new()
    return super_stone_solver.process_stones(stones, 25)
end

# PART 2
def part2(input)
    stones = input[0].split(" ")
    super_stone_solver = SuperStoneSolver.new()
    return super_stone_solver.process_stones(stones, 75)
end
