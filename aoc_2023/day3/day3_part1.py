from pathlib import Path
import string
import re


def check_symbol(array, row, start_col, end_col):
    # 00 01 02 03
    # 10 11 12 13
    # 20 21 22 23

    # 11 12 -> 00 03 (for i = row - 1, check all col from col-1 to col + 1)
    #       -> 20 23 (for i = row + 1, check all col from col-1 to col + 1)
    #       -> 10 & 13 (check col - 1 and col + 1)

    symbols = set(string.punctuation)
    symbols.remove(".")

    if start_col - 1 >= 0 and array[row][start_col - 1] in symbols:
        return True
    if end_col + 1 < len(array[0]) and array[row][end_col + 1] in symbols:
        return True
    for j in range(start_col - 1, end_col + 2):
        if j < 0 or j >= len(array[0]):
            continue
        if row - 1 > 0 and array[row - 1][j] in symbols:
            return True
        if row + 1 < len(array[0]) and array[row + 1][j] in symbols:
            return True

    return False


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

    part_numbers = []
    # Write the logic
    for index, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            if check_symbol(lines, index, match.start(), match.end() - 1):
                part_numbers.append(int(match.group()))

    print(sum(part_numbers))


if __name__ == "__main__":
    main()
