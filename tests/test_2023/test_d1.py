import pytest

from advent_of_code.y2023.d1 import part_1, part_2, restore_digits

TEST_INPUT_1 = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]

TEST_INPUT_2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def test_d1_p1():
    assert part_1(TEST_INPUT_1) == 142


@pytest.mark.parametrize(
    "string, expected",
    [
        ("eighthree", "83"),
        ("sevenine", "79"),
        ("two1nine", "219"),
        ("abcone2threexyz", "123"),
    ],
)
def test_restore_digits(string: str, expected: int):
    assert restore_digits(string) == expected


def test_d1_p2():
    assert part_2(TEST_INPUT_2) == 281
