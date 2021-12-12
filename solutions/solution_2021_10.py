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


def invalid_line(line):
    start_tags = list()
    for ch in line:
        # start tag?
        if ch in "<{[(":
            start_tags.append(ch)
        else:
            ch_start = start_tags.pop()
            ch_expected = pairs(ch_start)
            if ch_expected != ch:
                return True
    return False


def missing_tags(line):
    start_tags = list()
    for ch in line:
        # start tag?
        if ch in "<{[(":
            start_tags.append(ch)
        else:
            start_tags.pop()

    # now we have a list of remaining tags we expect
    return start_tags[::-1]


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
        score_lookup = {"[": 2, "(": 1, "{": 3, "<": 4}

        all_scores = []
        for line in self.puzzle_contents:

            if not invalid_line(line):
                score = 0
                tags = missing_tags(line)
                for tag in tags:
                    score = score * 5 + score_lookup[tag]
                all_scores.append(score)
        return sorted(all_scores)[len(all_scores) // 2]


puzzle = PuzzleDay10(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
