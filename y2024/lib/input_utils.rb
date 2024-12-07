TEST_SUFFIX = "_test"

def get_input(day, input_path)
    raw_input = File.read(INPUT_PATH + day)
    if raw_input.include? "\n\n" then
        split_parts = raw_input.split("\n\n")
        return split_parts.map { |part| part.split("\n")}
    end
    return raw_input.split("\n")
end

def get_test_input(day, input_path)
    return get_input(day + TEST_SUFFIX, input_path)
end
