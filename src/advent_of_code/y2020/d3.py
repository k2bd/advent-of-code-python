from typing import List

from advent_of_code.util import format_part, puzzle_input


def trees_hit(lines: List[str], right: int, down: int) -> int:
    pos_x = 0
    pos_y = 0

    width = len(lines[0])

    hit = 0

    while True:
        pos_x = (pos_x + right) % width
        pos_y += down

        if pos_y >= len(lines):
            break

        if lines[pos_y][pos_x] == "#":
            hit += 1

    return hit


def scan_slopes(lines: List[str]) -> int:
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    prod = 1
    for right, down in slopes:
        prod *= trees_hit(lines, right, down)

    return prod


if __name__ == "__main__":
    trees_map = puzzle_input(2020, 3)

    print(format_part(1, lambda: trees_hit(lines=trees_map, right=3, down=1)))
    print(format_part(2, lambda: scan_slopes(lines=trees_map)))
