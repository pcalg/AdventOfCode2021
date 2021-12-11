from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(8, test)
puzzle_input_split = [value.split(' | ') for value in puzzle_input]

unique_segments = {}

class PuzzleDay8(PuzzleInterface):

    def solve_part_1(self):
        contents = self.puzzle_contents
        # the unique lenght of these sections 1, 4, 7, 8:
        segment_lengths = {2, 4, 7, 3}
        unique_segments_cnt = 0

        for content in contents:
            output_value = content[1].split(' ')
            print(output_value)
            unique_segments_cnt += len([val for val in output_value if len(val) in segment_lengths])


        return unique_segments_cnt

    def solve_part_2(self):
        pass

puzzle = PuzzleDay8(puzzle_input_split)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
