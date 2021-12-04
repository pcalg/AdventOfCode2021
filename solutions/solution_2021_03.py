from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(3, test)


def count_ones(ones, value: str):
    for idx, digit in enumerate(value):
        if digit == '1':
            ones[idx] += 1
    return ones


def get_value(digits, n):
    a, b = 0, 0

    for idx, val in enumerate(digits[::-1]):
        if val > (n / 2):
            a += 2 ** idx
        else:
            b += 2 ** idx
    return a, b


def bit_stats_dict(digits, idx):
    one_cnt = 0
    zero_cnt = 0

    for digit in digits:
        if digit[idx] == '1':
            one_cnt += 1
        else:
            zero_cnt += 1

    # equal then for oxygen 1 has precedence, for co2 0 has precedence
    if one_cnt >= zero_cnt:
        return {'oxygen': '1', 'co2': '0'}
    else:
        return {'oxygen': '0', 'co2': '1'}


def filter_rating(values, stat_type):
    for idx in range(len(values)):
        stats = bit_stats_dict(values, idx)

        values = [value for value in values if value[idx] == stats[stat_type]]
        if len(values) == 1:
            return values[0]
    return None


class PuzzleDay3(PuzzleInterface):

    def solve_part_1(self):
        ones = [0] * len(self.puzzle_contents[0])

        cnt_items = len(self.puzzle_contents)

        for value in self.puzzle_contents:
            ones = count_ones(ones, value)

        a, b = get_value(ones, cnt_items)

        return a * b

    def solve_part_2(self):
        oxygen = filter_rating([d for d in self.puzzle_contents], 'oxygen')
        co2 = filter_rating([d for d in self.puzzle_contents], 'co2')
        return int(oxygen, 2) * int(co2, 2)


puzzle = PuzzleDay3(puzzle_input)
print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
