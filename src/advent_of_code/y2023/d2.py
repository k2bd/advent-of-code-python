from dataclasses import dataclass

from advent_of_code.util import format_solution, puzzle_input


@dataclass
class GameObservation:
    blue: int = 0

    red: int = 0

    green: int = 0


@dataclass
class Game:
    game_id: int

    observations: list[GameObservation]


def parse_observation(obs_info: str) -> GameObservation:
    cube_counts = {}
    for cube_info in obs_info.strip().split(","):
        cube_info = cube_info.strip()
        split_info = cube_info.split(" ")
        if len(split_info) == 1:
            (color,) = split_info
            cube_counts[color] = 1
        else:
            count, color = split_info
            cube_counts[color] = int(count)

    return GameObservation(**cube_counts)


def parse_game(game_line: str) -> Game:
    game_info, observations_str = game_line.split(":")

    game_id = int(game_info.strip("Game "))

    observations = [parse_observation(obs) for obs in observations_str.split(";")]

    return Game(
        game_id=game_id,
        observations=observations,
    )


def part_1(games_input: list[str]) -> int:
    games = [parse_game(game) for game in games_input]

    return sum(
        game.game_id
        for game in games
        if max(obs.red for obs in game.observations) <= 12
        and max(obs.green for obs in game.observations) <= 13
        and max(obs.blue for obs in game.observations) <= 14
    )


def part_2(games_input: list[str]) -> int:
    games = [parse_game(game) for game in games_input]

    return sum(
        max(obs.red for obs in game.observations)
        * max(obs.blue for obs in game.observations)
        * max(obs.green for obs in game.observations)
        for game in games
    )


if __name__ == "__main__":
    games = puzzle_input(2023, 2)

    print(
        format_solution(
            solver_p1=lambda: part_1(games),
            solver_p2=lambda: part_2(games),
        )
    )
