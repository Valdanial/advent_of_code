TEST_SUFFIX = "_test"

def get_input(day, input_path)
    raw_input = File.read(INPUT_PATH + day)
    return raw_input.lines(chomp: true)
end

def get_test_input(day, input_path)
    return get_input(day + TEST_SUFFIX, input_path)
end
