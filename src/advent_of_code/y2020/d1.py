from typing import Iterable, List
from itertools import combinations


def mul(items: Iterable[int]) -> int:
    result = 1
    for item in items:
        result *= item
    return result


def solve(expense_report: List[int], count: int) -> int:
    for values in combinations(expense_report, count):
        if sum(values) == 2020:
            return mul(values)


if __name__ == "__main__":
    import os

    data_file = os.path.join(os.path.dirname(__file__), "data", "day1.dat")

    with open(data_file, "r") as f:
        expense_report = [int(line) for line in f.readlines()]

    print(f"Part 1: {solve(expense_report=expense_report, count=2)}")
    print(f"Part 2: {solve(expense_report=expense_report, count=3)}")
