from advent_of_code.y2023.d7 import part_1, part_2

TEST_INPUT = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_part_1():
    assert part_1(TEST_INPUT) == 6440


def test_part_2():
    assert part_2(TEST_INPUT) == 0
