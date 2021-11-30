from contextlib import contextmanager

from pkg_resources import resource_filename


@contextmanager
def puzzle_input(year: int, day: int):
    """
    Open a puzzle's input file, which should be saved under
    ``advent_of_code/y{year}/data/day{day}``
    """
    location = resource_filename("advent_of_code", f"y{year}/data/day{day}")
    with open(location, "r", encoding="utf-8") as f:
        yield f
