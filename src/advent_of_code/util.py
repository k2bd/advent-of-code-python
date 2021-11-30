from contextlib import contextmanager
from typing import Any, Callable
from time import perf_counter

from pkg_resources import resource_filename


def puzzle_input(year: int, day: int):
    """
    Open a puzzle's input file, which should be saved under
    ``advent_of_code/y{year}/data/day{day}``
    """
    location = resource_filename("advent_of_code", f"y{year}/data/day{day}")
    with open(location, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


class Timer:
    def __enter__(self):
        self._start_time = perf_counter()
        return self
    
    def __exit__(self, type, value, traceback):
        self.result_seconds = perf_counter() - self._start_time

def print_solution(part: int, solver: Callable[[], Any]) -> None:
    """
    Print the solution to a puzzle in a standardized way, with timing info
    """
    with Timer() as t:
        solution = solver()
    print(f"Part {part!r}: {solution} ({t.result_seconds:.6f} sec)")
