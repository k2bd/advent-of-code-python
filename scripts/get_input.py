import os

import typer
from aocd import get_data

from advent_of_code import __file__ as aoc_dir


def main(year: int, day: int):
    if "AOC_SESSION" not in os.environ and "AOCD_DIR" not in os.environ:
        raise Exception("No AOC_SESSION or AOCD_DIR found in environment")

    test_input = get_data(day=day, year=year)

    target_file = os.path.join(
        os.path.dirname(aoc_dir), f"y{year}", "data", f"day{day}"
    )

    with open(target_file, "w") as f:
        f.write(test_input)


if __name__ == "__main__":
    typer.run(main)
