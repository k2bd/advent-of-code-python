from advent_of_code.y2020.d3 import scan_slopes, trees_hit

TEST_INPUT = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def test_d3_p1():
    assert trees_hit(TEST_INPUT, 3, 1) == 7


def test_d3_p2():
    assert scan_slopes(TEST_INPUT) == 336
