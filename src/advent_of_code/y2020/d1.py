from itertools import combinations
from typing import Iterable, List

from advent_of_code.util import print_solution, puzzle_input


def mul(items: Iterable[int]) -> int:
    result = 1
    for item in items:
        result *= item
    return result


def solve(expense_report: List[int], count: int) -> int:
    for values in combinations(expense_report, count):
        if sum(values) == 2020:
            return mul(values)
    raise ValueError("No values adding up to 2020 found")


if __name__ == "__main__":
    expense_report = [int(line) for line in puzzle_input(2020, 1)]

    print_solution(1, lambda: solve(expense_report=expense_report, count=2))
    print_solution(2, lambda: solve(expense_report=expense_report, count=3))
