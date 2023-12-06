from dataclasses import dataclass
from math import ceil, floor, prod, sqrt

from advent_of_code.util import format_solution, puzzle_input


@dataclass
class Race:
    time: int
    record: int

    def max_windup_time(self):
        return floor((self.time + sqrt(self.time**2 - 4 * (self.record + 1))) / 2)

    def min_windup_time(self):
        return ceil((self.time - sqrt(self.time**2 - 4 * (self.record + 1))) / 2)


def parse_input_multi(races_input: list[str]) -> list[Race]:
    times = [int(t) for t in races_input[0].split("Time: ")[1].split()]
    records = [int(d) for d in races_input[1].split("Distance: ")[1].split()]

    result = []
    for time, record in zip(times, records):
        result.append(Race(time=time, record=record))

    return result


def parse_input_single(races_input: list[str]) -> Race:
    time = int("".join(t for t in races_input[0].split("Time: ")[1].split()))
    record = int("".join(d for d in races_input[1].split("Distance: ")[1].split()))

    return Race(time=time, record=record)


def part_1(races_input: list[str]) -> int:
    races = parse_input_multi(races_input)

    return prod(1 + race.max_windup_time() - race.min_windup_time() for race in races)


def part_2(races_input: list[str]) -> int:
    race = parse_input_single(races_input)

    return 1 + race.max_windup_time() - race.min_windup_time()


if __name__ == "__main__":
    puzzle = puzzle_input(2023, 6)

    print(
        format_solution(
            solver_p1=lambda: part_1(puzzle),
            solver_p2=lambda: part_2(puzzle),
        )
    )
