from typing import Callable, Dict, Generator, List

from advent_of_code.util import format_part, puzzle_input

BIRTH_YEAR = "byr"
ISSUE_YEAR = "iyr"
EXPIRATION_YEAR = "eyr"
HEIGHT = "hgt"
HAIR_COLOR = "hcl"
EYE_COLOR = "ecl"
PASSPORT_ID = "pid"
COUNTRY_ID = "cid"

REQUIRED_FIELDS = {
    BIRTH_YEAR,
    ISSUE_YEAR,
    EXPIRATION_YEAR,
    HEIGHT,
    HAIR_COLOR,
    EYE_COLOR,
    PASSPORT_ID,
}


def parse_passports(lines: List[str]) -> Generator[Dict[str, str], None, None]:
    """
    Parse out individual passports according to the rules:

    Each passport is represented as a sequence of key:value pairs separated by
    spaces or newlines. Passports are separated by blank lines.
    """
    current_passport: Dict[str, str] = {}
    for line in [raw.strip() for raw in lines]:
        if line == "":
            yield current_passport
            current_passport = {}

        fields = line.split()
        current_passport.update(
            {key: value for key, value in [field.split(":") for field in fields]}
        )

    if current_passport != {}:
        yield current_passport


def validate_passport_p1(passport: Dict[str, str]) -> bool:
    return REQUIRED_FIELDS <= passport.keys()


def _validate_birth_year(byr: str) -> bool:
    return 1920 <= int(byr) <= 2002


def _validate_issue_year(iyr: str) -> bool:
    return 2010 <= int(iyr) <= 2020


def _validate_expiration_year(exp: str) -> bool:
    return 2020 <= int(exp) <= 2030


def _validate_height(height: str) -> bool:
    try:
        height_val = int(height[:-2])
    except ValueError:
        return False
    if height.endswith("cm"):
        return 150 <= height_val <= 193
    if height.endswith("in"):
        return 59 <= height_val <= 76
    return False


def _validate_hair_color(color: str) -> bool:
    return (
        color[0] == "#"
        and len(color) == 7
        and all(letter in "0123456789abcdef" for letter in color[1:].lower())
    )


def _validate_eye_color(color: str) -> bool:
    return color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def _validate_passport_id(pid: str) -> bool:
    return len(pid) == 9 and all(letter in "0123456789" for letter in pid)


def validate_passport_p2(passport: Dict[str, str]) -> bool:
    conditions = [
        lambda p: REQUIRED_FIELDS <= p.keys(),
        lambda p: _validate_birth_year(p[BIRTH_YEAR]),
        lambda p: _validate_issue_year(p[ISSUE_YEAR]),
        lambda p: _validate_expiration_year(p[EXPIRATION_YEAR]),
        lambda p: _validate_height(p[HEIGHT]),
        lambda p: _validate_hair_color(p[HAIR_COLOR]),
        lambda p: _validate_eye_color(p[EYE_COLOR]),
        lambda p: _validate_passport_id(p[PASSPORT_ID]),
    ]

    return all(condition(passport) for condition in conditions)


def count_valid_passports(
    lines: List[str],
    validator: Callable[[Dict[str, str]], int],
) -> int:
    return sum(validator(passport) for passport in parse_passports(lines))


if __name__ == "__main__":
    lines = puzzle_input(2020, 4)

    solve_p1 = lambda: count_valid_passports(lines, validate_passport_p1)  # noqa: E731
    print(format_part(1, solve_p1))

    solve_p2 = lambda: count_valid_passports(lines, validate_passport_p2)  # noqa: E731
    print(format_part(2, solve_p2))
