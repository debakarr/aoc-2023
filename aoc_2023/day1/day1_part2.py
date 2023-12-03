from pathlib import Path
import re


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split()

    # Write the logic
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    patterns = list(number_map.keys())
    patterns.append(r"\d")

    matches = [re.findall(r"(?=(" + "|".join(patterns) + r"))", line) for line in lines]
    translate_digits = [
        [number_map.get(key, key) for key in digit] for digit in matches
    ]
    numbers = [int(num[0] + num[-1]) for num in translate_digits]
    print(sum(numbers))


if __name__ == "__main__":
    main()
