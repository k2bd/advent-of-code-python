from dataclasses import dataclass
from typing import List

from advent_of_code.util import format_solution, puzzle_input

KEEP_LOWER_HALF = ["F", "L"]
KEEP_UPPER_HALF = ["B", "R"]


def get_location(instructions: str, lower: int, upper: int):
    """
    Get a location by binary space partitioning given some instructions (either
    a string of F/B or a string of L/R) and upper and lower bounds.
    """
    step_size = (upper + 1 - lower) // 2

    if len(instructions) == 1:
        return lower if instructions[0] in KEEP_LOWER_HALF else upper

    if instructions[0] in KEEP_LOWER_HALF:
        return get_location(instructions[1:], lower, upper - step_size)
    return get_location(instructions[1:], lower + step_size, upper)


@dataclass
class Seat:
    row: int
    col: int

    @property
    def seat_id(self) -> int:
        return self.row * 8 + self.col


def get_seat(instructions: str) -> Seat:
    return Seat(
        row=get_location(instructions[:7], 0, 127),
        col=get_location(instructions[7:], 0, 7),
    )


def get_largest_seat_id(instruction_sets: List[str]) -> int:
    return max(get_seat(instruction).seat_id for instruction in instruction_sets)


def find_my_seat_id(instruction_sets: List[str]) -> int:
    seats = (get_seat(instruction) for instruction in instruction_sets)
    taken_seats = {(seat.row, seat.col) for seat in seats}

    for row in range(0, 128):
        for col in range(0, 8):
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            if (row, col) not in taken_seats and all(
                neighbor in taken_seats for neighbor in neighbors
            ):
                return Seat(row, col).seat_id
    raise ValueError("There is no free seat")


if __name__ == "__main__":
    instruction_sets = puzzle_input(2020, 5)

    print(format_solution(1, lambda: get_largest_seat_id(instruction_sets)))
    print(format_solution(2, lambda: find_my_seat_id(instruction_sets)))
