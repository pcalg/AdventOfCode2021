from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(20, test)


def parse_input(puzzle_input):
    image_enhancement = puzzle_input[0]

    current_image = {}

    for y, image_line in enumerate(puzzle_input[2:]):
        for x, ch in enumerate(image_line):
            current_image[(y, x)] = ch
    return image_enhancement, current_image, (-2, len(puzzle_input[2:]) + 2)

def outside_values(enhancement_code, n):
    start_code = enhancement_code[0] # all 0
    # if the first char is a '.' then it will stay a '.'
    if start_code == '.':
        return '.'

    toggle_code = enhancement_code[9] # all 9 neighbours have the same value



# e, i, box = parse_input(puzzle_input)

def code_to_number(code: str):
    """
    Convert the code to a number.

    :param code: Code is for example "...##.." a '.' is a 0 and a '#' a 1.
    :return: The converted number.
    """
    total = 0
    for n, ch in enumerate(code[::-1]):
        if ch == '#':
            total += 2 ** n

    return total


class PuzzleDay20(PuzzleInterface):

    def solve_part_1(self):
        pass

    def solve_part_2(self):
        pass


puzzle = PuzzleDay20(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
