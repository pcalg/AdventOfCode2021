from general.general import read_day
from general.puzzle import PuzzleInterface

test = True

puzzle_input = read_day(21, test)


class PuzzleDay21(PuzzleInterface):

    def solve_part_1(self):
        pass

    def solve_part_2(self):
        pass


puzzle = PuzzleDay21(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
