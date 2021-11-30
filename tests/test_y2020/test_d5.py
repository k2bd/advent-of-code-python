import pytest

from advent_of_code.y2020.d5 import get_seat


@pytest.mark.parametrize(
    "instructions, row, col, seat_id",
    [
        ("BFFFBBFRRR", 70, 7, 567),
        ("FFFBBBFRRR", 14, 7, 119),
        ("BBFFBBFRLL", 102, 4, 820),
    ],
)
def test_get_seat(instructions, row, col, seat_id):
    seat = get_seat(instructions)
    assert seat.row == row
    assert seat.col == col
    assert seat.seat_id == seat_id
