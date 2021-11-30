import pytest

from advent_of_code.y2020.d4 import (
    _validate_birth_year,
    _validate_eye_color,
    _validate_hair_color,
    _validate_height,
    _validate_passport_id,
    count_valid_passports,
    parse_passports,
    validate_passport_p1,
    validate_passport_p2,
)

TEST_INPUT = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in",
]

EXAMPLE_P2_INVALID = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007",
]

EXAMPLE_P2_VALID = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
]


def test_parse_passports():
    assert len(list(parse_passports(TEST_INPUT))) == 4


def test_d4_p1():
    assert count_valid_passports(TEST_INPUT, validate_passport_p1) == 2


def test_d4_validate_birth_year():
    assert _validate_birth_year("2002")
    assert not _validate_birth_year("2003")


def test_d4_validate_height():
    assert _validate_height("60in")
    assert _validate_height("190cm")
    assert not _validate_height("190in")
    assert not _validate_height("60")


def test_d4_validate_hair_color():
    assert _validate_hair_color("#123abc")
    assert not _validate_hair_color("#123abz")
    assert not _validate_hair_color("123abc")


def test_d4_validate_eye_color():
    assert _validate_eye_color("brn")
    assert not _validate_eye_color("wat")


def test_d4_validate_passport_id():
    assert _validate_passport_id("000000001")
    assert not _validate_passport_id("0123456789")


@pytest.mark.parametrize(
    "input, expected_valid",
    [(EXAMPLE_P2_VALID, 4), (EXAMPLE_P2_INVALID, 0)],
)
def test_d4_p2(input, expected_valid):
    assert count_valid_passports(input, validate_passport_p2) == expected_valid
