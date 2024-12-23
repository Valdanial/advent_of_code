require 'Matrix'

NUM_PATTERN = /\d+/

def solve_equation_system(m, v)
    # Doing it only for matrix of size 2 because I'm lazy
    c = m[1, 1] * m[0, 0] - m[0, 1] * m[1, 0]
    d = v[1] * m[0, 0] - v[0] * m[1, 0]
    # Then we solve cb = d
    return nil if c == 0 || d % c !=0 || d / c < 0
    result_b = d / c
    e = v[0] - m[0, 1] * result_b
    return nil if e % m[0, 0] != 0 || e/m[0, 0] < 0
    result_a = e / m[0, 0]
    return [result_a, result_b]
end

def get_token_cost(input, a_cost, b_cost, offset = 0, max_press_count = nil)
    token_cost = 0
    machines = input.join('\n').split('\n\n')
    machines.each {
        |machine_str|
        machine = machine_str.split('\n')
        a_col = machine[0].scan(NUM_PATTERN).map {|n| Integer(n)}
        b_col = machine[1].scan(NUM_PATTERN).map {|n| Integer(n)}
        v = machine[2].scan(NUM_PATTERN).map {|n| Integer(n) + offset}
        m = Matrix.columns([a_col, b_col])
        eq_result = solve_equation_system(m, v)
        if eq_result then
            if !max_press_count || (eq_result[0] <= max_press_count && eq_result[1] <= max_press_count) then
                token_cost += a_cost * eq_result[0] + b_cost * eq_result[1]
            end
        end
    }
    return token_cost
end

# PART 1
def part1(input)
    return get_token_cost(input, 3, 1, 0, 100)
end

# PART 2
def part2(input)
    return get_token_cost(input, 3, 1, 10000000000000)
end
