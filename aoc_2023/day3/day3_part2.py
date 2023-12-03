from collections import defaultdict
from functools import reduce
from operator import mul
from pathlib import Path
import string
import re


def get_asterisk_cords(array, row, start_col, end_col):
    # 00 01 02 03
    # 10 11 12 13
    # 20 21 22 23

    # 11 12 -> 00 03 (for i = row - 1, check all col from col-1 to col + 1)
    #       -> 20 23 (for i = row + 1, check all col from col-1 to col + 1)
    #       -> 10 & 13 (check col - 1 and col + 1)

    cords = set()
    if start_col - 1 >= 0 and array[row][start_col - 1] == "*":
        cords.add((row, start_col - 1))
    if end_col + 1 < len(array[0]) and array[row][end_col + 1] == "*":
        cords.add((row, end_col + 1))
    for j in range(start_col - 1, end_col + 2):
        if j < 0 or j >= len(array[0]):
            continue
        if row - 1 > 0 and array[row - 1][j] == "*":
            cords.add((row - 1, j))
        if row + 1 < len(array[0]) and array[row + 1][j] == "*":
            cords.add((row + 1, j))

    return cords


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    #     input = """467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598.."""
    lines = input.strip().split()

    astrisk_cords_numbers = defaultdict(list)
    # Write the logic
    for index, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            if astrisk_cords := get_asterisk_cords(
                lines, index, match.start(), match.end() - 1
            ):
                for astrisk_cord in astrisk_cords:
                    astrisk_cords_numbers[astrisk_cord].append(int(match.group()))

    gear_ratios = []
    for _, part_numbers in astrisk_cords_numbers.items():
        if len(part_numbers) == 2:
            gear_ratios.append(reduce(mul, part_numbers))
    print(sum(gear_ratios))


if __name__ == "__main__":
    main()
