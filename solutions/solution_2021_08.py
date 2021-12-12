import collections

from general.general import read_day
from general.puzzle import PuzzleInterface
from itertools import permutations
from typing import List

test = False

puzzle_input = read_day(8, test)
puzzle_input_split = [value.split(' | ') for value in puzzle_input]

unique_segments = {}


def segment_to_number(segments: List[str]):
    segment_tuple = tuple(segment_code for segment_code in sorted(segments))

    lookup = {("s_a", "s_b", "s_c", "s_e", "s_f", "s_g"): 0,
              ("s_c", "s_f"): 1,
              ("s_a", "s_c", "s_d", "s_e", "s_g"): 2,
              ("s_a", "s_c", "s_d", "s_f", "s_g"): 3,
              ("s_b", "s_c", "s_d", "s_f"): 4,
              ("s_a", "s_b", "s_d", "s_f", "s_g"): 5,
              ("s_a", "s_b", "s_d", "s_e", "s_f", "s_g"): 6,
              ("s_a", "s_c", "s_f"): 7,
              ("s_a", "s_b", "s_c", "s_d", "s_e", "s_f", "s_g"): 8,
              ("s_a", "s_b", "s_c", "s_d", "s_f", "s_g"): 9,
              }

    if segment_tuple in lookup:
        return lookup[segment_tuple]
    else:
        return -1


class Display:
    def __init__(self):
        self.code_segment = {}

    def set(self, mapping):
        segment_codes = [f's_{ch}' for ch in 'abcdefg']
        self.code_segment = {}
        for idx, segment_code in enumerate(segment_codes):
            self.code_segment[mapping[idx]] = segment_code

    def digit(self, codes):
        segment_codes = [self.code_segment[code] for code in codes]
        return segment_to_number(segment_codes)

    def total(self, code_list):
        total = 0
        base = 1
        for codes in code_list[::-1]:
            total += base * self.digit(codes)
            base *= 10
        return total


def get_total_line(train_part, solution_part):
    d = Display()

    trains_parts_split = train_part.split(' ')

    # use brute force algorithm
    for segment_permutation in permutations("abcdefg"):
        d.set(segment_permutation)
        is_valid = True
        for code in trains_parts_split:
            if d.digit(code) == -1:
                is_valid = False
                break
        if is_valid:
            return d.total(solution_part.split(' '))
    raise Exception("no solution found")


class PuzzleDay8(PuzzleInterface):

    def solve_part_1(self):
        contents = self.puzzle_contents
        # the unique length of these sections 1, 4, 7, 8:
        segment_lengths = {2, 4, 7, 3}
        unique_segments_cnt = 0

        for content in contents:
            output_value = content[1].split(' ')
            unique_segments_cnt += len([val for val in output_value if len(val) in segment_lengths])

        return unique_segments_cnt

    def solve_part_2(self):
        total = 0
        for line in self.puzzle_contents:
            value = get_total_line(line[0], line[1])
            total += value

        return total


puzzle = PuzzleDay8(puzzle_input_split)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
