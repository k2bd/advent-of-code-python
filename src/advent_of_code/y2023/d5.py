from typing import Any
from advent_of_code.util import format_solution, puzzle_input
from collections import UserDict
from dataclasses import dataclass, field


@dataclass
class AlmanacMap(UserDict):
    """
    A dict whose values are their own key by default, but key:value sets
    can be overwritten in ranges
    """

    key_ranges: list[tuple[int, int, int]] = field(default_factory=list)

    def set_key_range(self, key_start: int, value_start: int, map_range: int):
        self.key_ranges.append((key_start, value_start, map_range))

    def __getitem__(self, key: int) -> int:
        for key_start, value_start, map_range in self.key_ranges:
            if key_start <= key <= key_start + map_range:
                return value_start + (key - key_start)
        else:
            return key


@dataclass
class Almanac:
    seed_to_soil: AlmanacMap
    soil_to_fertilizer: AlmanacMap
    fertilizer_to_water: AlmanacMap
    water_to_light: AlmanacMap
    light_to_temperature: AlmanacMap
    temperature_to_humidity: AlmanacMap
    humidity_to_location: AlmanacMap

    @classmethod
    def from_input(cls, almanac_input: list[str]) -> "Almanac":
        def _get_section(section_header: str) -> AlmanacMap:
            """Lazy helper to get sections by name"""
            result_lines: list[str] = []
            found_start = False
            for line in almanac_input:
                if found_start:
                    if line.strip() != "":
                        result_lines.append(line)
                    else:
                        break
                elif line.startswith(section_header):
                    found_start = True
                    continue

            result = AlmanacMap()
            for line in result_lines:
                dest_start, source_start, map_range = [int(p) for p in line.split()]
                result.set_key_range(
                    key_start=source_start,
                    value_start=dest_start,
                    map_range=map_range,
                )

            return result

        return cls(
            seed_to_soil=_get_section("seed-to-soil"),
            soil_to_fertilizer=_get_section("soil-to-fertilizer"),
            fertilizer_to_water=_get_section("fertilizer-to-water"),
            water_to_light=_get_section("water-to-light"),
            light_to_temperature=_get_section("light-to-temperature"),
            temperature_to_humidity=_get_section("temperature-to-humidity"),
            humidity_to_location=_get_section("humidity-to-location"),
        )

    def get_seed_location(self, seed: int):
        return self.humidity_to_location[
            self.temperature_to_humidity[
                self.light_to_temperature[
                    self.water_to_light[
                        self.fertilizer_to_water[
                            self.soil_to_fertilizer[self.seed_to_soil[seed]]
                        ]
                    ]
                ]
            ]
        ]


def part_1(almanac_input: list[str]) -> int:
    almanac = Almanac.from_input(almanac_input)
    seeds = [int(s) for s in almanac_input[0].split("seeds:")[1].strip().split()]

    return min(almanac.get_seed_location(s) for s in seeds)


def part_2(almanac_input: list[str]) -> int:
    almanac = Almanac.from_input(almanac_input)


if __name__ == "__main__":
    puzzle = puzzle_input(2023, 5)

    print(
        format_solution(
            solver_p1=lambda: part_1(puzzle),
            solver_p2=lambda: part_2(puzzle),
        )
    )
