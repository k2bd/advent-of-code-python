from advent_of_code.y2021.d3 import (
    get_least_common_bits,
    get_most_common_bits,
    get_rate,
    get_rating,
)

TEST_INPUT = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_get_gamma():
    assert get_rate(TEST_INPUT, get_most_common_bits) == 22


def test_get_epsilon():
    assert get_rate(TEST_INPUT, get_least_common_bits) == 9


def test_get_oxygen_rating():
    assert get_rating(TEST_INPUT, get_most_common_bits) == 23


def test_get_co2_rating():
    assert get_rating(TEST_INPUT, get_least_common_bits) == 10
