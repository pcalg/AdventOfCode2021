from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(7, test)
puzzle_input_int = [int(val) for val in puzzle_input[0].split(',')]


class PuzzleDay7(PuzzleInterface):

    def solve_part_1(self):
        pass

    def solve_part_2(self):
        pass

puzzle = PuzzleDay7(puzzle_input_int)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
