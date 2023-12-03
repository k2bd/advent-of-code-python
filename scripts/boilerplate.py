import os

import typer
from aocd import get_data
from typer import confirm

from advent_of_code import __file__ as aoc_dir

PACKAGE_DIR = os.path.dirname(aoc_dir)
TESTS_DIR = os.path.join(os.path.dirname(PACKAGE_DIR), "tests")


PACKAGE_BOILERPLATE = """from advent_of_code.util import format_solution, puzzle_input


def part_1(input: list[str]) -> int:
    pass
    

def part_2(input: list[str]) -> int:
    pass
    

if __name__ == "__main__":
    puzzle = puzzle_input({year}, {day})

    print(
        format_solution(
            solver_p1=lambda: part_1(puzzle),
            solver_p2=lambda: part_2(puzzle),
        )
    )

"""


TEST_BOILERPLATE = """from advent_of_code.y{year}.d{day} import part_1, part_2

TEST_INPUT = []

def test_part_1():
    assert part_1(TEST_INPUT) == 0


def test_part_2():
    assert part_2(TEST_INPUT) == 0
"""


def package_boilerplate(year: int, day: int) -> str:
    return PACKAGE_BOILERPLATE.format(year=year, day=day)


def test_boilerplate(year: int, day: int) -> str:
    return TEST_BOILERPLATE.format(year=year, day=day)


def main(year: int, day: int):

    package_file = os.path.join(PACKAGE_DIR, f"y{year}", f"d{day}.py")
    os.makedirs(os.path.dirname(package_file), exist_ok=True)
    test_file = os.path.join(TESTS_DIR, f"test_y{year}", f"test_d{day}.py")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)

    if os.path.exists(package_file):
        confirm(
            f"File {package_file} already exists. Overwrite?",
            abort=True,
        )
    with open(package_file, "w") as f:
        f.write(package_boilerplate(year, day))

    if os.path.exists(test_file):
        confirm(
            f"File {test_file} already exists. Overwrite?",
            abort=True,
        )
    with open(test_file, "w") as f:
        f.write(test_boilerplate(year, day))


if __name__ == "__main__":
    typer.run(main)
