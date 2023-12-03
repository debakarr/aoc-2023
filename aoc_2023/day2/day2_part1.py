from pathlib import Path
from aoc_2023.day2.common import (
    make_cubeset_counter,
    # make_cubeset_namedtuple,
    # contraints_namedtuple,
    contraints_counter,
)


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split("\n")

    # Write the logic
    valid_games = []

    for index, line in enumerate(lines, start=1):
        # print(line)
        _, cube_sets = line.split(":")
        for cube_set in cube_sets.split(";"):
            # current_cubset = make_cubeset_namedtuple(cube_set)
            # if not current_cubset.met_constraint(contraints):
            #     break
            current_cubset = make_cubeset_counter(cube_set)
            # print(
            #     f"{current_cubset = } <= {contraints_counter = } -> {current_cubset <= contraints_counter}"
            # )
            if not (current_cubset <= contraints_counter):
                break
        else:
            valid_games.append(index)

    print(sum(valid_games))


if __name__ == "__main__":
    main()
