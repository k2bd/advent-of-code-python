import pytest
from pytest_subtests import SubTests

from advent_of_code.y2023.d6 import Race, part_1, part_2

TEST_INPUT = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


@pytest.mark.parametrize(
    "time, record, expected_min, expected_max",
    [(7, 9, 2, 5), (15, 40, 4, 11), (30, 200, 11, 19)],
)
def test_windup_times(
    time: int,
    record: int,
    expected_min: int,
    expected_max: int,
    subtests: SubTests,
):
    race = Race(time=time, record=record)
    with subtests.test("Min"):
        assert race.min_windup_time() == expected_min
    with subtests.test("Max"):
        assert race.max_windup_time() == expected_max


def test_part_1():
    assert part_1(TEST_INPUT) == 288


def test_part_2():
    assert part_2(TEST_INPUT) == 71503
