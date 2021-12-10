from general.general import read_day
from general.puzzle import PuzzleInterface

test = True

puzzle_input = read_day(8, test)
#puzzle_input_int = [int(val) for val in puzzle_input[0].split(',')]


class PuzzleDay8(PuzzleInterface):

    def solve_part_1(self):
        pass

    def solve_part_2(self):
        pass

puzzle = PuzzleDay8(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
