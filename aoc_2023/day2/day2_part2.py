from functools import reduce
from operator import mul
from pathlib import Path
from collections import Counter
from aoc_2023.day2.common import (
    # make_cubeset_namedtuple,
    make_cubeset_counter,
)


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split("\n")

    # Write the logic
    power_of_max_cubes = []

    for line in lines:
        max_counter = Counter(red=0, blue=0, green=0)
        # max_red, max_green, max_blue = 0, 0, 0
        _, cube_sets = line.split(":")
        for cube_set in cube_sets.split(";"):
            # current_cubset = make_cubeset_namedtuple(cube_set)
            # max_red = max(max_red, current_cubset.red)
            # max_green = max(max_green, current_cubset.green)
            # max_blue = max(max_blue, current_cubset.blue)
            current_cubset = make_cubeset_counter(cube_set)
            max_counter = current_cubset | max_counter
        # power_of_max_cubes.append(max_red * max_blue * max_green)
        power_of_max_cubes.append(reduce(mul, max_counter.values()))

    print(sum(power_of_max_cubes))


if __name__ == "__main__":
    main()
