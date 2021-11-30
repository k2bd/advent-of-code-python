import os
from unittest import mock

from advent_of_code.util import __name__ as UTIL_NAME
from advent_of_code.util import format_solution, puzzle_input
from advent_of_code.y2020 import __file__ as Y2020_FILE


def test_puzzle_input():
    """
    Test that the ``puzzle_input`` context manager works
    """
    target = os.path.join(os.path.dirname(Y2020_FILE), "data", "day1")
    with open(target, "r", encoding="utf-8") as g:
        assert puzzle_input(2020, 1) == [line.strip() for line in g.readlines()]


def test_format_solution():
    initial_time = 10.345678
    fake_times = [initial_time, initial_time + 2.345678]

    def fake_perf_counter():
        return fake_times.pop(0)

    with mock.patch(UTIL_NAME + ".perf_counter", side_effect=fake_perf_counter):
        formatted = format_solution(5, lambda: 987654)

    assert formatted == "Part 5: 987654 (2.345678 sec)"
