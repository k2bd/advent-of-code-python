from typing import Callable, List

from advent_of_code.util import puzzle_input, solution


def is_valid_p1(entry: str) -> bool:
    policy, password = entry.split(": ")
    count, letter = policy.split(" ")
    low, high = (int(i) for i in count.split("-"))

    if low <= password.count(letter) <= high:
        return True
    return False


def is_valid_p2(entry: str) -> bool:
    policy, password = entry.split(": ")
    pos, letter = policy.split(" ")
    pos_a, pos_b = (int(i) - 1 for i in pos.split("-"))

    return (password[pos_a] == letter) != (password[pos_b] == letter)


def solve(passwords: List[str], validator: Callable[[str], bool]) -> int:
    return len([password for password in passwords if validator(password)])


if __name__ == "__main__":
    passwords = puzzle_input(2020, 2)

    print(solution(1, lambda: solve(passwords=passwords, validator=is_valid_p1)))
    print(solution(2, lambda: solve(passwords=passwords, validator=is_valid_p2)))
