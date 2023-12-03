from pathlib import Path
import re


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split()
    digits = [re.findall(r"\d", line) for line in lines]
    numbers = [int(num[0] + num[-1]) for num in digits]
    print(sum(numbers))


if __name__ == "__main__":
    main()
