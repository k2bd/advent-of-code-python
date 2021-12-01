from typing import List

from advent_of_code.util import format_solution, puzzle_input


def count_increases(depths: List[int]) -> int:
    """
    Count the number of times the depth increases between two measurements
    """
    increases = [1 for first, second in zip(depths, depths[1:]) if second > first]
    return len(increases)


def count_sliding_increases(depths: List[int]) -> int:
    """
    Count the number of 3-member sliding sum increases in a list of measurements
    """
    sliding_sums = [
        sum(measurements) for measurements in zip(depths, depths[1:], depths[2:])
    ]
    return count_increases(sliding_sums)


if __name__ == "__main__":
    depths = [int(line) for line in puzzle_input(2021, 1)]

    print(format_solution(1, lambda: count_increases(depths)))
    print(format_solution(1, lambda: count_sliding_increases(depths)))
