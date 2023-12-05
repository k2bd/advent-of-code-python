from advent_of_code.y2023.d5 import AlmanacMap, part_1, part_2

TEST_INPUT = [
    "seeds: 79 14 55 13",
    "",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]


def test_part_1():
    assert part_1(TEST_INPUT) == 35


def test_transform_range():
    almanac = AlmanacMap()
    almanac.set_key_range(3, 13, 6)
    almanac.set_key_range(11, 31, 3)

    transformed = almanac.transform_range(7, 6)

    assert transformed == [(17, 2), (31, 2), (9, 2)]


def test_part_2():
    assert part_2(TEST_INPUT) == 46
