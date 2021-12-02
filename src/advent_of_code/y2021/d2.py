from dataclasses import dataclass
from typing import Callable, List

from advent_of_code.util import format_solution, puzzle_input


@dataclass(eq=True)
class Position:
    horizontal: int

    depth: int

    aim: int = 0


def get_position_p1(instructions: List[str]) -> Position:
    """
    Get the position of the sub, starting at 0, 0, after the following
    instructions according to the part 1 rules
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


def get_position_p2(instructions: List[str]) -> Position:
    """
    Get the position of the sub, starting at 0, 0, after the following
    instructions according to the part 2 rules
    """
    result = Position(horizontal=0, depth=0)

    for instruction in instructions:
        direction, amount = instruction.split()
        if direction == "forward":
            result.horizontal += int(amount)
            result.depth += result.aim * int(amount)
        elif direction == "down":
            result.aim += int(amount)
        elif direction == "up":
            result.aim -= int(amount)

    return result


def result(
    instructions: List[str],
    instruction_resolver: Callable[[List[str]], Position],
) -> int:
    position = instruction_resolver(instructions)
    return position.depth * position.horizontal


if __name__ == "__main__":
    instructions = puzzle_input(2021, 2)

    print(
        format_solution(
            solver_p1=lambda: result(
                instructions, instruction_resolver=get_position_p1
            ),
            solver_p2=lambda: result(
                instructions, instruction_resolver=get_position_p2
            ),
        )
    )
