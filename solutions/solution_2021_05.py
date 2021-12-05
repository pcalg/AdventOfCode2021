import collections

from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(5, test)

# [pos.split(",") for pos in s.split(" -> ")]
def parse_input(puzzle_input):
    #lines = {}
    lines = []

    for line in puzzle_input:
        line_parts = [pos.split(",") for pos in line.split(" -> ")]
        #start_pos, end_pos = line_parts
        lines.append(line_parts)


        #lines[tuple(int(coord) for coord in start_pos)] = tuple(int(coord) for coord in end_pos)

    return lines

class PuzzleDay5(PuzzleInterface):


    def solve_part_1(self):
        lines = parse_input(self.puzzle_contents)
        # only straight lines
        straight_lines = [line for line in lines if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

        diagram = defaultdict(int)
        for line in straight_lines:
            x_vals = sorted([int(line[0][0]), int(line[1][0])])
            y_vals = sorted([int(line[0][1]), int(line[1][1])])

            for x in range(x_vals[0], x_vals[1] + 1):
                for y in range(y_vals[0], y_vals[1] + 1 ):
                    diagram[(x, y)] += 1

        # now check for values > 0 (overlap)
        return len([c for c in diagram.values() if c > 1])


    def solve_part_2(self):
        lines = parse_input(self.puzzle_contents)
        # only straight lines

        diagram = defaultdict(int)
        for line in lines:
            x_vals = sorted([int(line[0][0]), int(line[1][0])])
            y_vals = sorted([int(line[0][1]), int(line[1][1])])

            for x in range(x_vals[0], x_vals[1] + 1):
                for y in range(y_vals[0], y_vals[1] + 1 ):
                    diagram[(x, y)] += 1

        # now check for values > 0 (overlap)
        return len([c for c in diagram.values() if c > 1])



puzzle = PuzzleDay5(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
