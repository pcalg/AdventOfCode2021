from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = [int(value) for value in read_day(1, test)]

class PuzzleDay1(PuzzleInterface):

    def solve_part_1(self):
        prev_value = max(self.puzzle_contents)

        increased = 0

        for n in self.puzzle_contents:
            if n > prev_value:
                increased += 1
            prev_value = n

        print(increased)


    def solve_part_2(self):
        increased = 0
        prev_value = 0

        for idx, n in enumerate(self.puzzle_contents[:-2]):
            three_measurement = sum(self.puzzle_contents[idx: idx + 3])

            if three_measurement > prev_value:
                increased += 1

            prev_value = three_measurement

        print(increased - 1)


puzzle = PuzzleDay1(puzzle_input)

puzzle.solve_part_1()
puzzle.solve_part_2()
