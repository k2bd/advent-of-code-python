from advent_of_code.y2020.d1 import solve

EXAMPLE_LIST = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]


def test_d1_p1():
    assert solve(EXAMPLE_LIST, 2) == 514579


def test_d1_p2():
    assert solve(EXAMPLE_LIST, 3) == 241861950
