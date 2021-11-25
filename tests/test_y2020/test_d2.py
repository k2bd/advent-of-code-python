from advent_of_code.y2020.d2 import is_valid_p1, solve, is_valid_p2

TEST_INPUT = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]


def test_d2_p1():
    assert solve(TEST_INPUT, is_valid_p1) == 2

def test_d2_p2():
    assert solve(TEST_INPUT, is_valid_p2) == 1
