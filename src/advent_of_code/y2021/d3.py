from dataclasses import dataclass
from typing import Callable, List

from advent_of_code.util import format_solution, puzzle_input


@dataclass
class Diagnostics:
    gamma_string: str

    @property
    def gamma(self):
        return int(self.gamma_string, 2)

    @property
    def epsilon_string(self):
        return "".join(str(int(not int(letter))) for letter in self.gamma_string)

    @property
    def epsilon(self):
        return int(self.epsilon_string, 2)


def get_most_common_bits(report: List[str]) -> List[int]:
    report_t = [[int(line[i]) for line in report] for i in range(len(report[0]))]
    return [int(len([i for i in line if i]) >= len(line) / 2) for line in report_t]


def get_least_common_bits(report: List[str]) -> List[int]:
    most_common = get_most_common_bits(report)
    return [int(not b) for b in most_common]


def get_rating(report: List[str], bit_criteria: Callable[[List[str]], List[int]]):
    """
    Get the oxygen generator or CO2 scrubber rating
    """
    for i in range(len(report[0])):
        bits = bit_criteria(report)
        report = [line for line in report if int(line[i]) == bits[i]]
        if len(report) == 1:
            (line,) = report
            return int(line, 2)


def get_rate(report: List[str], bit_criteria: Callable[[List[str]], List[int]]):
    """
    Get the gamma or epsilon rate
    """
    bits = bit_criteria(report)
    return int("".join(str(i) for i in bits), 2)


def solve_p1(report: List[str]) -> int:
    return get_rate(report, get_most_common_bits) * get_rate(
        report, get_least_common_bits
    )


def solve_p2(report: List[str]) -> int:
    return (get_rating(report, get_most_common_bits) or 0) * (
        get_rating(report, get_least_common_bits) or 0
    )


if __name__ == "__main__":
    report = puzzle_input(2021, 3)

    print(
        format_solution(
            solver_p1=lambda: solve_p1(report),
            solver_p2=lambda: solve_p2(report),
        )
    )
