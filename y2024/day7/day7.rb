def concat_operator(a, b)
    return Integer(a.to_s + b.to_s)
end

def add_operator(a, b)
    return a + b
end

def mul_operator(a, b)
    return a * b
end

BASIC_OPERATORS = ["add_operator", "mul_operator"]
ALL_OPERATORS = BASIC_OPERATORS + ["concat_operator"]

def get_equations(input)
    equations = []
    for line in input do
        split_line = line.split(": ")
        equation = {:expected_result => Integer(split_line[0]), :operands => split_line[1].split(" ").map {|num| Integer(num)}}
        equations.push(equation)
    end
    return equations
end

def solvable?(equation, operators)
    if equation[:operands].length == 1 then return equation[:operands][0] == equation[:expected_result] end
    first_operand = equation[:operands].first
    second_operand = equation[:operands][1]
    operators.each {
        |op|
        if solvable?({:expected_result => equation[:expected_result], :operands => [send(op, first_operand, second_operand)] + equation[:operands][2, equation[:operands].length - 1]}, operators) then
            return true
        end
    }
    return false
end

# PART 1
def part1(input)
    result = 0
    equations = get_equations(input)
    for equation in equations do
        if solvable?(equation, BASIC_OPERATORS) then
            result += equation[:expected_result]
        end
    end
    return result
end

# PART 2
def part2(input)
    result = 0
    equations = get_equations(input)
    for equation in equations do
        if solvable?(equation, ALL_OPERATORS) then
            result += equation[:expected_result]
        end
    end
    return result
end
