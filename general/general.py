from pathlib import Path
from functools import wraps
from time import time


def read_day(day, test=False):
    file_name = f"input_{'test_' if test else ''}2021_{day:02d}.txt"

    with open(Path("puzzles") / file_name) as f:
        content = f.read().splitlines()

    return content


def save_output(file_location, file_name, lines):
    fn = file_location / file_name
    with open(fn, 'w') as f:
        f.write('\n'.join(lines) + '\n')


def save_grid(fn: Path, ascii_output: str):
    with open(fn, 'w') as f:
        for ch in ascii_output:
            f.write(ch)


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")

    return _time_it
