import sys
import requests
import subprocess
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
sessionToken = os.getenv("AOC_SESSION_TOKEN")


def _make_request(method, endpoint, day, **kwargs):
    url = "https://adventofcode.com/2023/day/" + str(day) + f"/{endpoint}"
    headers = {"Cookie": f"session={sessionToken}"}
    response = getattr(requests, method)(url, headers=headers, **kwargs)
    response.raise_for_status()
    return response


def get_input(day):
    response = _make_request(method="get", endpoint="input", day=day)
    return response.text


def submit(day, part, answer):
    data = {
        "level": part,
        "answer": answer,
    }
    response = _make_request(method="post", endpoint="answer", day=day, data=data)
    return response


def ensure_solution_module(day):
    root = Path(__file__).parent

    day_folder = root / f"day{day}"
    day_folder.mkdir(parents=True, exist_ok=True)
    (day_folder / "__init__.py").touch()
    return day_folder


def create_solution_script(day):
    day_folder = ensure_solution_module(day)
    for part in range(1, 3):
        script_path = day_folder / f"day{day}_part{part}.py"
        script_path.touch()
        if not script_path.read_text():
            starting_template = """from pathlib import Path


def main():
    input = (Path(__file__).parent / "input.txt").read_text()
    lines = input.strip().split()

    # Write the logic


if __name__ == "__main__":
    main()
"""
            script_path.write_text(starting_template)


def run(day, part):
    root_module = __name__.split(".")[0]
    day_folder = ensure_solution_module(day)
    script_module_name = f"day{day}_part{part}"
    script_module_full_name = f"{root_module}.{day_folder.stem}.{script_module_name}"
    stdout = subprocess.check_output([sys.executable, "-m", script_module_full_name])
    print(stdout.decode().strip())


def create_input_file(day):
    day_folder = ensure_solution_module(day)
    input = get_input(day)
    input_file = day_folder / "input.txt"
    input_file.write_text(input)
