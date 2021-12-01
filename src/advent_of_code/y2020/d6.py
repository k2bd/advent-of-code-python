from typing import Callable, Generator, List, Set, Union

from advent_of_code.util import format_solution, puzzle_input

SetCombiner = Callable[[Set[str], Set[str]], Set[str]]


def parse_groups(
    lines: List[str], combiner: SetCombiner
) -> Generator[Set[str], None, None]:
    """
    Yield distinct groups from the list of inputs according to the combination
    rule given
    """
    current_group: Union[Set[str], None] = None
    for line in lines:
        if line == "" and current_group is not None:
            yield current_group
            current_group = None
            continue

        current_group = (
            combiner(current_group, set(line))
            if current_group is not None
            else set(line)
        )

    if current_group:
        yield current_group


def group_sum(lines: List[str], combiner: SetCombiner) -> int:
    return sum(len(group) for group in parse_groups(lines, combiner))


if __name__ == "__main__":
    lines = puzzle_input(2020, 6)

    print(
        format_solution(
            solver_p1=lambda: group_sum(lines, set.union),
            solver_p2=lambda: group_sum(lines, set.intersection),
        )
    )
