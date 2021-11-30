from typing import List


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


def scan_slopes(lines: List[str]):
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
    import os

    data_file = os.path.join(os.path.dirname(__file__), "data", "day3.dat")

    with open(data_file, "r") as f:
        trees_map = [line.strip() for line in f.readlines()]

    print(f"Part 1: {trees_hit(lines=trees_map, right=3, down=1)!r}")
    print(f"Part 2: {scan_slopes(lines=trees_map)!r}")
