from advent_of_code.y2020.d6 import parse_groups

TEST_INPUT = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


def test_parse_groups_union():
    assert list(parse_groups(TEST_INPUT, set.union)) == [
        {"a", "b", "c"},
        {"a", "b", "c"},
        {"a", "b", "c"},
        {"a"},
        {"b"},
    ]


def test_parse_groups_intersection():
    assert list(parse_groups(TEST_INPUT, set.intersection)) == [
        {"a", "b", "c"},
        set(),
        {"a"},
        {"a"},
        {"b"},
    ]
