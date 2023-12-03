from pathlib import Path
from aoc_2023.day2.common import make_cubeset, contraints


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split("\n")

    # Write the logic
    valid_games = []

    for index, line in enumerate(lines, start=1):
        _, cube_sets = line.split(":")
        for cube_set in cube_sets.split(";"):
            current_cubset = make_cubeset(cube_set)
            if not current_cubset.met_constraint(contraints):
                break
        else:
            valid_games.append(index)

    print(sum(valid_games))


if __name__ == "__main__":
    main()
