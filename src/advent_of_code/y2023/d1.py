from advent_of_code.util import format_solution, puzzle_input


def is_digit(val: str) -> bool:
    try:
        int(val)
        return True
    except ValueError:
        return False


def get_line_value(line: str) -> int:
    digits = [int(d) for d in line if is_digit(d)]

    return int(f"{digits[0]}{digits[-1]}")


def part_1(calibration: list[str]) -> int:
    return sum(get_line_value(line) for line in calibration)


def restore_digits(line: str) -> str:
    digit_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    scanned_line = line
    result = ""
    while len(scanned_line):
        if is_digit(scanned_line[0]):
            result += scanned_line[0]
        else:
            for spelled, num in digit_map.items():
                if scanned_line.startswith(spelled):
                    result += str(num)
                    break

        scanned_line = scanned_line[1:]

    return result


def part_2(calibration: list[str]):
    return part_1([restore_digits(line) for line in calibration])


if __name__ == "__main__":
    calibration = puzzle_input(2023, 1)

    print(
        format_solution(
            solver_p1=lambda: part_1(calibration),
            solver_p2=lambda: part_2(calibration),
        )
    )
