from advent_of_code.util import format_solution, puzzle_input
from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Coord:
    x: int
    y: int

    def neighbors(self) -> set["Coord"]:
        return {
            Coord(self.x - 1, self.y - 1),
            Coord(self.x - 1, self.y),
            Coord(self.x - 1, self.y + 1),
            Coord(self.x, self.y - 1),
            Coord(self.x, self.y + 1),
            Coord(self.x + 1, self.y - 1),
            Coord(self.x + 1, self.y),
            Coord(self.x + 1, self.y + 1),
        }


@dataclass
class Engine:
    symbols: list[tuple[str, Coord]]

    numbers: list[tuple[int, set[Coord]]]

    def part_numbers(self) -> list[int]:
        all_neighbors = set()
        result = []
        for _, coord in self.symbols:
            all_neighbors |= coord.neighbors()

        for num, coords in self.numbers:
            if coords & all_neighbors:
                result.append(num)

        return result


def _is_numerical(item: str) -> bool:
    #if "+" in item or "-" in item:
    #    return False
    try:
        int(item)
        return True
    except ValueError:
        return False


def _parse_item(
    item: str,
    y: int,
    start_x: int,
) -> tuple[list[tuple[int, set[Coord]], list[tuple[str, Coord]]]]:
    """
    Process an item in the engine schematic, separating numbers and parts that
    appear together, e.g "617*"
    """
    numbers = []
    symbols = []

    current_number_str = ""

    def _add_number():
        nonlocal start_x
        nonlocal current_number_str

        if len(current_number_str) > 0:
            numbers.append(
                (
                    int(current_number_str),
                    {
                        Coord(x, y)
                        for x in range(start_x, start_x + len(current_number_str))
                    },
                )
            )
            start_x += len(current_number_str)
            current_number_str = ""

    while len(item) > 0:
        if _is_numerical(item[0]):
            current_number_str += item[0]
        else:
            _add_number()
            symbols.append((item[0], Coord(start_x, y)))
            start_x += 1
        item = item[1:]

    _add_number()

    return numbers, symbols


def _parse_line(
    line: str, y: int
) -> tuple[list[tuple[int, set[Coord]], list[tuple[str, Coord]]]]:
    numbers = []
    symbols = []

    start_x = 0
    while len(line) > 0:
        dot_pos = line.find(".")
        if dot_pos == 0:
            line = line[1:]
            start_x += 1
            continue

        if dot_pos == -1:
            dot_pos = len(line)

        item = line[0:dot_pos]

        number_parts, symbol_parts = _parse_item(item, y=y, start_x=start_x)

        numbers.extend(number_parts)
        symbols.extend(symbol_parts)

        line = line[dot_pos:]
        start_x += dot_pos

    return numbers, symbols


def parse_engine_schematic(schematic: list[str]):
    numbers = []
    symbols = []

    for y, line in enumerate(schematic):
        line_numbers, line_symbols = _parse_line(line, y=y)
        numbers.extend(line_numbers)
        symbols.extend(line_symbols)

    return Engine(symbols=symbols, numbers=numbers)


def part_1(schematic: list[str]) -> int:
    engine = parse_engine_schematic(schematic)

    return sum(engine.part_numbers())


def part_2(schematic: list[str]) -> int:
    pass


if __name__ == "__main__":
    games = puzzle_input(2023, 3)

    print(
        format_solution(
            solver_p1=lambda: part_1(games),
            solver_p2=lambda: part_2(games),
        )
    )
