require './lib/input_utils.rb'

DAY_PREFIX = "day"
INPUT_PATH = './input/'

def run_day(day, is_test)
    input = nil
    day_str = DAY_PREFIX + day.to_s
    if is_test then
        puts "Running with TEST input"
        input = get_test_input(day_str, INPUT_PATH)
    else
        input = get_input(day_str, INPUT_PATH)
    end
    load("./" + day_str + "/" + day_str + ".rb")

    # PART 1
    result_1 = part1(input)
    puts("PART 1:", result_1)

    # PART 2
    result_2 = part2(input)
    puts("PART 2:", result_2)

end

if ARGV.length > 0 then
    input_day = Integer(ARGV[0])
    if 1 <= input_day and input_day <= 25 then
        is_test = ARGV.length > 1 and ARGV[1] == "test"
        run_day(input_day, is_test)
    else
        puts "Invalid first argument: Needs to be a number between 1 and 25"
    end
else
    puts "Missing argument. First argument should be day number, like '2'"
end