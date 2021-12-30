from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(18, test)


def parse(sn_number):
    level = 0
    result = []

    for ch in sn_number:
        if ch.isdecimal():
            result.append((int(ch), level))
        elif ch == '[':
            level += 1
        elif ch == ']':
            # save pair if any
            level -= 1
    return result


def explode_numbers(sn_numbers):
    # check for pairs to explode
    numbers = [number for number, _ in sn_numbers] + [0]
    levels = [level for _, level in sn_numbers] + [-1]

    for idx in range(len(numbers)):
        if levels[idx] == 5 and levels[idx + 1] == 5:
            # found the first pair
            idx_left = idx
            idx_right = idx + 1
            new_level = levels[idx] - 1

            result = []
            for idx in range(len(numbers) - 1):
                if idx == idx_left - 1:
                    result.append((numbers[idx] + numbers[idx_left], levels[idx]))
                elif idx == idx_right + 1:
                    result.append((numbers[idx] + numbers[idx_right], levels[idx]))
                elif idx == idx_left:
                    result.append((0, new_level))
                elif idx != idx_right:
                    result.append((numbers[idx], levels[idx]))
            return result, True

    # nothing to explode
    return [number for number in sn_numbers], False


def add(sn_numbers_1, sn_numbers_2):
    result = []
    for number, level in sn_numbers_1 + sn_numbers_2:
        # because of the addition every item gains one level
        result.append((number, level + 1))
    return result


def split_numbers(sn_numbers):
    result = []
    split = False
    for number, level in sn_numbers:
        if number >= 10 and not split:
            result.append((number // 2, level + 1))
            result.append(((number + 1) // 2, level + 1))
            split = True
        else:
            result.append((number, level))
    return result, split


def magnitude_numbers(sn_numbers):
    had_pair = True
    while had_pair:
        sn_numbers, had_pair = magnitude_run(sn_numbers)

    total = 0
    for number, level in sn_numbers:
        total += number
    return total


def magnitude_run(sn_numbers):
    result = []

    numbers = [number for number, _ in sn_numbers] + [0]
    levels = [level for _, level in sn_numbers] + [-1]

    pair = False
    had_pair = False
    for idx in range(len(numbers) - 1):
        if levels[idx] == levels[idx + 1] and not pair:
            result.append((numbers[idx] * 3 + numbers[idx + 1] * 2, levels[idx] - 1))
            pair = True
            had_pair = True
        elif pair:
            # already have this one
            pair = False
        else:
            result.append((numbers[idx], levels[idx]))

    return result, had_pair


def reduce(sn_numbers):
    explode = True
    split = True

    while explode or split:
        sn_numbers, explode = explode_numbers(sn_numbers)
        if not explode:
            sn_numbers, split = split_numbers(sn_numbers)

    return sn_numbers


def combinations(n):
    # 0, 1, 1, 0 etc
    for a in range(n):
        for b in range(n):
            if a != b:
                yield (a, b)


class PuzzleDay18(PuzzleInterface):

    def solve_part_1(self):
        numbers = parse(self.puzzle_contents[0])
        for idx in range(1, len(self.puzzle_contents)):
            numbers = add(numbers, parse(self.puzzle_contents[idx]))
            numbers = reduce(numbers)

        return magnitude_numbers(numbers)

    def solve_part_2(self):
        max_magnitude = 0

        parsed_numbers = [parse(content) for content in self.puzzle_contents]

        for idx_a, idx_b in combinations(len(parsed_numbers)):
            numbers_a = parsed_numbers[idx_a]
            numbers_b = parsed_numbers[idx_b]

            added_numbers = add(numbers_a, numbers_b)
            reduced_numbers = reduce(added_numbers)

            magnitude = magnitude_numbers(reduced_numbers)
            max_magnitude = max(max_magnitude, magnitude)
        return max_magnitude


puzzle = PuzzleDay18(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
