import os

from advent_of_code.util import puzzle_input
from advent_of_code.y2020 import __file__ as Y2020_FILE


def test_puzzle_input():
    """
    Test that the ``puzzle_input`` context manager works
    """
    target = os.path.join(os.path.dirname(Y2020_FILE), "data", "day1")
    with puzzle_input(2020, 1) as f:
        with open(target, "r", encoding="utf-8") as g:
            assert f.read() == g.read()
