def get_reports(input)
    reports = []
    for line in input do
        report = line.split.map{ |level| Integer(level)}
        reports.push(report)
    end
    return reports
end

# Could most likely be cleaner ans smarter
def safe?(report, tolerance_left = 0)
    tolerance = tolerance_left
    asc = nil
    i = 0
    while i < report.length - 1 do
        flagged_unsafe = false
        level_diff = (report[i] - report[i+1]).abs
        if level_diff < 1 or level_diff > 3 then
            flagged_unsafe = true
        end
        if report[i] > report[i+1] and [nil, false].include?(asc) and not flagged_unsafe then
            asc = false
        elsif report[i] < report[i+1] and [nil, true].include?(asc) and not flagged_unsafe then
            asc = true
        else
            flagged_unsafe = true
        end
        if flagged_unsafe then
            if tolerance == 0 then
                return false
            end
            without_first = report.clone
            without_first.delete_at(i)
            without_second = report.clone
            without_second.delete_at(i + 1)
            
            if safe?(without_first, tolerance - 1) or safe?(without_second, tolerance - 1) then
                return true
            end
            if i > 0 then
                without_previous = report.clone
                without_previous.delete_at(i - 1)
                return safe?(without_previous, tolerance - 1)
            end
            return false
        end
        i += 1
    end
    return true
end

def get_safe_sum(reports, fault_tolerance = 0)
    safe_sum = 0
    for report in reports do
        if safe?(report, fault_tolerance) then
            safe_sum += 1
        end
    end
    return safe_sum
end


# PART 1
def part1(input)
    reports = get_reports(input)
    return get_safe_sum(reports)
end

# PART 2
def part2(input)
    reports = get_reports(input)
    return get_safe_sum(reports, 1)
end
