MUL_PATTERN = /mul\(([\d]+),([\d]+)\)/

FUNC_PATTERN = /((?:mul)|(?:do)|(?:don't))\(([\d\w,]*?)\)/

FUNC_DICTIONARY = {
    "mul" => "mul_func",
    "do" => "do_func",
    "don't" => "dont_func"
}

def get_mul_couples(line)
    return line.scan(MUL_PATTERN)
end

def execute_mul(input)
    result = 0
    for line in input do
        mul_couples = get_mul_couples(line)
        for mul_couple in mul_couples do
            result += Integer(mul_couple[0]) * Integer(mul_couple[1])
        end
    end
    return result
end

def get_funcs(line)
    return line.scan(FUNC_PATTERN)
end

def mul_func(args, state)
    if args.length == 2 and not state[:mul_pause] then
        state[:acc] += Integer(args[0]) * Integer(args[1])
    end
end

def do_func(args, state)
    if args.length == 0 then
        state[:mul_pause] = false
    end
end

def dont_func(args, state)
    if args.length == 0 then
        state[:mul_pause] = true
    end
end

def execute_code(input)
    state = {:acc => 0,
    :mul_pause => false
    }
    for line in input do
        funcs = get_funcs(line)
        for func_and_args in funcs do
            send(FUNC_DICTIONARY[func_and_args[0]], func_and_args[1].split(","), state)
        end
    end
    return state
end

# PART 1
def part1(input)
    mul_result = execute_mul(input)
    return mul_result
end

# PART 2
def part2(input)
    state = execute_code(input)
    return state[:acc]
end
