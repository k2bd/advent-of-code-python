from dataclasses import dataclass
from typing import List

from advent_of_code.util import format_solution, puzzle_input


@dataclass(eq=True)
class Position:
    horizontal: int

    depth: int


def get_position(instructions: List[str]) -> Position:
    """
    Get the position of the sub, starting at 0, 0, after the following
    instructions
    """
    result = Position(horizontal=0, depth=0)

    for instruction in instructions:
        direction, amount = instruction.split()
        if direction == "forward":
            result.horizontal += int(amount)
        elif direction == "down":
            result.depth += int(amount)
        elif direction == "up":
            result.depth -= int(amount)

    return result


def p1_result(instructions: List[str]) -> int:
    position = get_position(instructions)
    return position.depth * position.horizontal


if __name__ == "__main__":
    instructions = puzzle_input(2021, 2)

    print(
        format_solution(
            solver_p1=lambda: p1_result(instructions), solver_p2=lambda: None
        )
    )
