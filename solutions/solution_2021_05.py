import collections

from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(5, test)


def sign(value):
    if value == 0:
        return 0
    if value < 0:
        return -1
    else:
        return 1


def parse_input(puzzle_input):
    lines = []

    for line in puzzle_input:
        line_parts = [pos.split(",") for pos in line.split(" -> ")]
        lines.append(line_parts)

    return lines

def process_line(diagram, line):
    x1, y1 = int(line[0][0]), int(line[0][1])
    x2, y2 = int(line[1][0]), int(line[1][1])

    if y1 == y2:
        distance = abs(x2 - x1)
    else:
        # either x1 == x2 or 45 degrees, so only consider one (either x or y) for distance
        distance = abs(y2 - y1)

    dx = sign(x2 - x1)
    dy = sign(y2 - y1)

    for n in range(distance + 1):
        diagram[(x1 + n * dx, y1 + n * dy)] += 1

    return diagram

class PuzzleDay5(PuzzleInterface):

    def solve_part_1(self):
        lines = parse_input(self.puzzle_contents)

        # only straight lines
        straight_lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

        diagram = defaultdict(int)

        for line in straight_lines:
            diagram = process_line(diagram, line)

        # now check for values > 0 (overlap)
        return len([c for c in diagram.values() if c > 1])

    def solve_part_2(self):
        lines = parse_input(self.puzzle_contents)
        diagram = defaultdict(int)

        for line in lines:
            diagram = process_line(diagram, line)

        # now check for values > 0 (overlap)
        return len([c for c in diagram.values() if c > 1])


puzzle = PuzzleDay5(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
