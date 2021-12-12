from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(10, test)


def calc_score(ch):
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    return score_table[ch]


def pairs(ch_start):
    table = {"{": "}", "[": "]", "(": ")", "<": ">"}
    return table[ch_start]


class PuzzleDay10(PuzzleInterface):

    def solve_part_1(self):
        score = 0
        for line in self.puzzle_contents:
            start_tags = list()
            for ch in line:
                # start tag?
                if ch in "<{[(":
                    start_tags.append(ch)
                else:
                    ch_start = start_tags.pop()
                    ch_expected = pairs(ch_start)
                    if ch_expected != ch:
                        score += calc_score(ch)
                        break

        return score

    def solve_part_2(self):
        pass


puzzle = PuzzleDay10(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
