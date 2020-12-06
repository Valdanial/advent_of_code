from typing import List

import re

from y2020.lib.multiline_input import get_multiline_input

HEIGHT_REGEX = re.compile(r"(?:^1(?:(?:[5-8][0-9])|(?:9[0-3]))cm$)|(?:^(?:(?:59)|(?:6[0-9])|(?:7[0-6]))in$)")
HEX_COLOR_REGEX = re.compile(r"^#[0-9a-f]{6}$")
PASSPORT_ID_REGEX = re.compile(r"^\d{9}$")

def validate_year(str_year: str, ymin: int, ymax: int):
    try:
        numeric_year = int(str_year)
        return ymin <= numeric_year <= ymax and len(str_year) == 4
    except Exception:
        return False

class Passport():
    def __init__(self):
        self.birth_year = None
        self.issue_year = None
        self.expiration_year = None
        self.height = None
        self.hair_color = None
        self.eye_color = None
        self.passport_id = None
        self.country_id = None

    def validate_birth_year(self):
        return validate_year(self.birth_year, 1920, 2002)

    def validate_issue_year(self):
        return validate_year(self.issue_year, 2010, 2020)

    def validate_expiration_year(self):
        return validate_year(self.expiration_year, 2020, 2030)

    def validate_height(self):
        if not self.height:
            return False
        return HEIGHT_REGEX.match(self.height)

    def validate_hair_color(self):
        if not self.hair_color:
            return False
        return HEX_COLOR_REGEX.match(self.hair_color)

    def validate_eye_color(self):
        whitelist = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.eye_color in whitelist

    def validate_passport_id(self):
        if not self.passport_id:
            return False
        return PASSPORT_ID_REGEX.match(self.passport_id)

    def might_be_valid(self):
        return self.birth_year and self.issue_year and self.expiration_year and self.height and self.hair_color and self.eye_color and self.passport_id

    def is_valid(self):
        return self.validate_birth_year() and self.validate_issue_year() and self.validate_expiration_year() and self.validate_height() and self.validate_hair_color() and self.validate_eye_color() and self.validate_passport_id()

passport_map = {
    "byr": "birth_year",
    "iyr": "issue_year",
    "eyr": "expiration_year",
    "hgt": "height",
    "hcl": "hair_color",
    "ecl": "eye_color",
    "pid": "passport_id",
    "cid": "country_id"
}

def create_passports_from_input_lines(input_lines: List[str])->List[Passport]:
    passports = []
    passport = Passport()
    for line in input_lines:
        if not line:
            passports.append(passport)
            passport = Passport()
        split_line = line.split()
        for item in split_line:
            split_item = item.split(":")
            key = split_item[0]
            value = split_item[1]
            if key in passport_map.keys():
                setattr(passport, passport_map[key], value)
    passports.append(passport)
    return passports


INPUT_FILE = "y2020/input/day4_input"

passport_list = create_passports_from_input_lines(get_multiline_input(INPUT_FILE))
maybe_valid_count = 0
valid_count = 0
for passport in passport_list:
    if passport.might_be_valid():
        maybe_valid_count += 1
    if passport.is_valid():
        valid_count += 1

print(f"Maybe valid passports: {maybe_valid_count}")
print(f"Valid passports: {valid_count}")
