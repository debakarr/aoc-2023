from pathlib import Path

from aoc_2023.day2.common import make_cubeset


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split("\n")

    # Write the logic
    power_of_max_cubes = []

    for line in lines:
        max_red, max_green, max_blue = 0, 0, 0
        _, cube_sets = line.split(":")
        for cube_set in cube_sets.split(";"):
            current_cubset = make_cubeset(cube_set)
            max_red = max(max_red, current_cubset.red)
            max_green = max(max_green, current_cubset.green)
            max_blue = max(max_blue, current_cubset.blue)
        power_of_max_cubes.append(max_red * max_blue * max_green)

    print(sum(power_of_max_cubes))


if __name__ == "__main__":
    main()
