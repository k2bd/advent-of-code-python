from dataclasses import dataclass
from functools import cached_property, total_ordering

from advent_of_code.util import format_solution, puzzle_input

HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7


@total_ordering
@dataclass(frozen=True)
class CamelCardsHand:
    """
    Represent a hand with a bid in a game of Camel Cards
    """

    bid: int

    cards: tuple[int, int, int, int, int]

    @cached_property
    def hand_type_strength(self) -> int:
        card_value_counts = {
            v: sum(1 for c in self.cards if c == v)
            for v in {card for card in self.cards if card != 0}
        }
        card_counts = card_value_counts.values()

        num_jokers = sum(1 for c in self.cards if c == 0)

        if max(card_counts or [0]) + num_jokers == 5:
            return FIVE_OF_A_KIND
        elif max(card_counts or [0]) + num_jokers == 4:
            return FOUR_OF_A_KIND
        elif set(card_counts) == {3, 2} or (
            sorted(card_counts) == [2, 2] and num_jokers == 1
        ):
            return FULL_HOUSE
        elif max(card_counts or [0]) + num_jokers == 3:
            return THREE_OF_A_KIND
        elif sorted(card_counts) == [1, 2, 2]:
            return TWO_PAIR
        elif 2 in card_counts or num_jokers == 1:
            return ONE_PAIR
        else:
            return HIGH_CARD

    def __eq__(self, other) -> bool:
        if not isinstance(other, CamelCardsHand):
            return NotImplemented

        return self.cards == other.cards

    def __lt__(self, other) -> bool:
        if not isinstance(other, CamelCardsHand):
            return NotImplemented

        if self.hand_type_strength < other.hand_type_strength:
            return True
        if self.hand_type_strength == other.hand_type_strength:
            for self_num, other_num in zip(self.cards, other.cards):
                if self_num < other_num:
                    return True
                elif self_num == other_num:
                    continue
                else:
                    return False
        return False

    @classmethod
    def from_input(cls, input_line: str, joker_rule: bool = False) -> "CamelCardsHand":
        cards_part, bid_part = input_line.split()

        values_map = {
            "T": 10,
            "J": 0 if joker_rule else 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }

        card_values = tuple(
            values_map[v] if v in values_map else int(v) for v in cards_part
        )

        return cls(
            bid=int(bid_part),
            cards=card_values,  # type: ignore
        )


def part_1(cards_input: list[str]) -> int:
    hands = [CamelCardsHand.from_input(line) for line in cards_input]

    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), start=1))


def part_2(cards_input: list[str]) -> int:
    hands = [CamelCardsHand.from_input(line, joker_rule=True) for line in cards_input]

    return sum(i * hand.bid for i, hand in enumerate(sorted(hands), start=1))


if __name__ == "__main__":
    puzzle = puzzle_input(2023, 7)

    print(
        format_solution(
            solver_p1=lambda: part_1(puzzle),
            solver_p2=lambda: part_2(puzzle),
        )
    )
