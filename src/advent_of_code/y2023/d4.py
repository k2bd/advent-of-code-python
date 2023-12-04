import math
from dataclasses import dataclass

from advent_of_code.util import format_solution, puzzle_input


@dataclass
class ScratchCard:
    #: Card number
    number: int

    winning_numbers: set[int]

    your_numbers: set[int]

    def points_value(self):
        matches = len(self.winning_numbers & self.your_numbers)
        return int(math.pow(2, matches - 1)) if matches > 0 else 0

    def card_winnings(self) -> list[int]:
        matches = len(self.winning_numbers & self.your_numbers)
        return [self.number + i + 1 for i in range(matches)]


def parse_card(card: str) -> ScratchCard:
    card_info, nums_part = card.split(":")
    card_num = int(card_info.split("Card")[1].strip())

    winning_nums_part, your_nums_part = nums_part.split("|")

    winning_nums = {int(n.strip()) for n in winning_nums_part.split(" ") if len(n) > 0}
    your_nums = {int(n.strip()) for n in your_nums_part.split(" ") if len(n) > 0}

    return ScratchCard(
        number=card_num,
        winning_numbers=winning_nums,
        your_numbers=your_nums,
    )


def part_1(cards_input: list[str]) -> int:
    cards = [parse_card(line) for line in cards_input]

    return sum(card.points_value() for card in cards)


def part_2(cards_input: list[str]) -> int:
    cards = sorted([parse_card(line) for line in cards_input], key=lambda c: c.number)

    card_counts = {card.number: 1 for card in cards}

    for card in cards:
        for new_card_num in card.card_winnings():
            card_counts[new_card_num] += card_counts[card.number]

    return sum(card_counts.values())


if __name__ == "__main__":
    puzzle = puzzle_input(2023, 4)

    print(
        format_solution(
            solver_p1=lambda: part_1(puzzle),
            solver_p2=lambda: part_2(puzzle),
        )
    )
