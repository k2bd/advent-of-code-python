from advent_of_code.y2023.d3 import parse_engine_schematic, part_1, part_2, Engine


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


def test_part_1():
    assert part_1(EXAMPLE_INPUT) == 4361
