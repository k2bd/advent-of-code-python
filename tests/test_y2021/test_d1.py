from advent_of_code.y2021.d1 import count_increases, count_sliding_increases

TEST_INPUT = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]


def test_d1_p1():
    assert count_increases(TEST_INPUT) == 7


def test_d1_p2():
    assert count_sliding_increases(TEST_INPUT) == 5
