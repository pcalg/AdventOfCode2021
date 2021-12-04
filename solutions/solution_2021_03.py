from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(3, test)

def count_ones(ones, value: str):
    for idx, digit in enumerate(value):
        if digit == '1':
            ones[idx] += 1
    return ones
    #return count_digits(ones, '1', value)

# def count_digits(digits, ch, value: str):
#     for idx, digit in enumerate(value):
#         if digit == ch:
#             digits[idx] += 1
#     return digits


def get_value(digits, n):

    a, b = 0, 0

    for idx, val in enumerate(digits[::-1]):
        if val > (n / 2):
            a += 2**idx
        else:
            b += 2**idx
    return a, b


# def get_max_value(digits, n):
#
#     result = 0
#
#     for idx, val in enumerate(digits[::-1]):
#         if val >= (n / 2):
#             result += 2**idx
#     return result


def bit_stats(digits, idx):
    one_cnt = 0
    zero_cnt = 0

    for digit in digits:
        if digit[idx] == '1':
            one_cnt += 1
        else:
            zero_cnt += 1

    #return one_cnt, zero_cnt

    # equal then for oxygen 1 has precedence, for co2 0 has precedence
    if one_cnt == zero_cnt:
        return '1', '0'

    # more ones than zeros
    if one_cnt > zero_cnt:
        return '1', '0'

    # more zeros than ones
    return '0', '1'


class PuzzleDay3(PuzzleInterface):

    def solve_part_1(self):
        #ones_counter = defaultdict(int)
        ones = [0] * len(self.puzzle_contents[0])

        cnt_items = len(self.puzzle_contents)

        for value in self.puzzle_contents:
            ones = count_ones(ones, value)


        a, b = get_value(ones, cnt_items)

        print(a * b)


    def solve_part_2(self):
        ones = [0] * len(self.puzzle_contents[0])

        # oxygen generator
        oxygen_values = [d for d in self.puzzle_contents]

        idx = 0
        while len(oxygen_values) > 1:
            keep_oxygen, _ = bit_stats(oxygen_values, idx)
            oxygen_values = [value for value in oxygen_values if value[idx] == keep_oxygen]
            idx += 1

        idx = 0
        co2_values = [d for d in self.puzzle_contents]
        while len(co2_values) > 1:
            _, keep_co2 = bit_stats(co2_values, idx)
            co2_values = [value for value in co2_values if value[idx] == keep_co2]

            idx += 1

        print(int(oxygen_values[0], 2) * int(co2_values[0], 2))


puzzle = PuzzleDay3(puzzle_input)

puzzle.solve_part_1()
puzzle.solve_part_2()
