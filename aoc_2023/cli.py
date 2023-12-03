import argparse
import pprint
from aoc_2023.helper import (
    create_input_file,
    create_solution_script,
    run,
    submit,
)


def main(argv=None):
    parser = argparse.ArgumentParser()

    # subcommand
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # fetch problem (will create script and input file)
    add_parser = subparsers.add_parser(
        "fetch",
        help="fetch a specific day problem",
    )
    add_parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="day to fetch",
    )

    # will run the solution script
    run_parser = subparsers.add_parser("run", help="run a day and part")
    run_parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="day to run",
    )
    run_parser.add_argument(
        "-p",
        "--part",
        type=int,
        choices=[1, 2],
        required=True,
        help="part to run",
    )

    # will submit the solution
    submit_parser = subparsers.add_parser(
        "submit", help="submit a specific day problem"
    )
    submit_parser.add_argument(
        "-d",
        "--day",
        type=int,
        required=True,
        help="day to submit",
    )
    submit_parser.add_argument(
        "-p",
        "--part",
        type=int,
        required=True,
        choices=[1, 2],
        help="part to submit",
    )
    submit_parser.add_argument(
        "-a",
        "--answer",
        required=True,
        help="answer for the puzzle",
    )
    args = parser.parse_args(argv)

    if args.cmd == "fetch":
        create_solution_script(day=args.day)
        create_input_file(day=args.day)
    elif args.cmd == "submit":
        submit(args.day, args.part, args.answer)
    elif args.cmd == "run":
        run(day=args.day, part=args.part)

    return 0


if __name__ == "__main__":
    exit(main())
