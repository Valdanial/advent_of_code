import re

NUM_REGEX = r"\d+"

def get_score(line: str)->int:
    winning_cards_count = 0
    winning_numbers_line, hand_line = line.split(": ")[1].split(' | ')
    winning_numbers = winning_numbers_line.split(' ')
    hand = re.findall(NUM_REGEX, hand_line)
    for winning_number in winning_numbers:
        if winning_number in hand:
            winning_cards_count += 1
    return pow(2, winning_cards_count - 1) if winning_cards_count else 0

def get_scratchcards(input_str: list[str])->list[int]:
    scratchcards = [1] * len(input_str) # Start with one of each scratchcard
    for r, line in enumerate(input_str):
        winning_numbers_line, hand_line = line.split(": ")[1].split(' | ')
        winning_numbers = winning_numbers_line.split(' ')
        hand = re.findall(NUM_REGEX, hand_line)
        winning_cards_count = 0
        for winning_number in winning_numbers:
            if winning_number in hand:
                winning_cards_count += 1
        for i in range(r + 1, winning_cards_count + r + 1):
            if i < len(scratchcards):
                scratchcards[i] += scratchcards[r]
    return scratchcards

def get_score_sum(input_str: list[str])->int:
    score_sum = 0
    for line in input_str:
        score_sum += get_score(line)
    return score_sum

# Part 1
def part1(input_str: list[str])->str:
    return get_score_sum(input_str)

# Part 2
def part2(input_str: list[str])->str:
    return sum(get_scratchcards(input_str))
