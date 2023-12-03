import pytest
from advent_of_code.y2023.d3 import (
    Coord,
    parse_engine_schematic,
    part_1,
    _parse_line,
    part_2,
    Engine,
    _parse_item,
)


EXAMPLE_INPUT = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


@pytest.mark.parametrize(
    "item, y, start_x, expected_result",
    [
        (
            "617*",
            4,
            0,
            (
                [
                    (617, {Coord(y=4, x=0), Coord(y=4, x=1), Coord(y=4, x=2)}),
                ],
                [
                    ("*", Coord(y=4, x=3)),
                ],
            ),
        ),
        (
            "-617",
            4,
            0,
            (
                [
                    (617, {Coord(y=4, x=1), Coord(y=4, x=2), Coord(y=4, x=3)}),
                ],
                [
                    ("-", Coord(y=4, x=0)),
                ],
            ),
        ),
        (
            "617*444",
            4,
            0,
            (
                [
                    (617, {Coord(y=4, x=0), Coord(y=4, x=1), Coord(y=4, x=2)}),
                    (444, {Coord(y=4, x=4), Coord(y=4, x=5), Coord(y=4, x=6)}),
                ],
                [
                    ("*", Coord(y=4, x=3)),
                ],
            ),
        ),
        (
            "*617*444&",
            4,
            10,
            (
                [
                    (617, {Coord(y=4, x=11), Coord(y=4, x=12), Coord(y=4, x=13)}),
                    (444, {Coord(y=4, x=15), Coord(y=4, x=16), Coord(y=4, x=17)}),
                ],
                [
                    ("*", Coord(y=4, x=10)),
                    ("*", Coord(y=4, x=14)),
                    ("&", Coord(y=4, x=18)),
                ],
            ),
        ),
        ("*", 4, 3, ([], [("*", Coord(y=4, x=3))])),
        (
            "456",
            4,
            3,
            ([(456, {Coord(y=4, x=3), Coord(y=4, x=4), Coord(y=4, x=5)})], []),
        ),
        ("**", 4, 3, ([], [("*", Coord(y=4, x=3)), ("*", Coord(y=4, x=4))])),
        ("*1", 4, 3, ([(1, {Coord(y=4, x=4)})], [("*", Coord(y=4, x=3))])),
    ],
)
def test_parse_item(
    item: str,
    y: int,
    start_x: int,
    expected_result: tuple[list[tuple[int, set[Coord]], list[tuple[str, Coord]]]],
):
    assert _parse_item(item, y=y, start_x=start_x) == expected_result


@pytest.mark.parametrize(
    "line, y, expected",
    [
        (
            "467..114..",
            6,
            (
                [
                    (467, {Coord(y=6, x=0), Coord(y=6, x=1), Coord(y=6, x=2)}),
                    (114, {Coord(y=6, x=5), Coord(y=6, x=6), Coord(y=6, x=7)}),
                ],
                [],
            ),
        ),
        (
            "..467..114",
            6,
            (
                [
                    (467, {Coord(y=6, x=2), Coord(y=6, x=3), Coord(y=6, x=4)}),
                    (114, {Coord(y=6, x=7), Coord(y=6, x=8), Coord(y=6, x=9)}),
                ],
                [],
            ),
        ),
        (
            "#.467..114",
            6,
            (
                [
                    (467, {Coord(y=6, x=2), Coord(y=6, x=3), Coord(y=6, x=4)}),
                    (114, {Coord(y=6, x=7), Coord(y=6, x=8), Coord(y=6, x=9)}),
                ],
                [
                    ("#", Coord(y=6, x=0)),
                ],
            ),
        ),
        (
            "467..114.&",
            6,
            (
                [
                    (467, {Coord(y=6, x=0), Coord(y=6, x=1), Coord(y=6, x=2)}),
                    (114, {Coord(y=6, x=5), Coord(y=6, x=6), Coord(y=6, x=7)}),
                ],
                [
                    ("&", Coord(y=6, x=9)),
                ],
            ),
        ),
    ],
)
def test_parse_line(
    line: str,
    y: int,
    expected: tuple[list[tuple[int, set[Coord]], list[tuple[str, Coord]]]],
):
    assert _parse_line(line, y=y) == expected


def test_part_1():
    assert part_1(EXAMPLE_INPUT) == 4361


def test_part_2():
    assert part_2(EXAMPLE_INPUT) == 467835
