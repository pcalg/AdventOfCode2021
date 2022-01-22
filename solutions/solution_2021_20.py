from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import Counter

test = False

puzzle_input = read_day(20, test)


def parse_input(puzzle_input):
    image_enhancement = puzzle_input[0]

    current_image = {}

    for y, image_line in enumerate(puzzle_input[2:]):
        for x, ch in enumerate(image_line):
            current_image[(y, x)] = ch
    return image_enhancement, current_image, len(puzzle_input[2])


def calc_background_pixel(enhancement_code, n):
    if n <= 0:
        return '.'

    # if the first char is a '.' then it will stay a '.' outside the bounding box
    if enhancement_code[0] == '.':
        return '.'

    toggle_code = [enhancement_code[0], enhancement_code[9]]  # all 9 neighbours have the same value

    return toggle_code[(n - 1) % 2]


def calc_output_pixel(enhancement_code, grid, background_pixel, pos):
    y, x = pos
    pixel_neighbours = [(y + dy, x + dx) for dy in range(-1, 2) for dx in range(-1, 2)]

    code = ""
    for neighbour in pixel_neighbours:
        if neighbour not in grid:
            code += background_pixel
        else:
            code += grid[neighbour]

    value = code_to_number(code)

    return enhancement_code[value]


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


def simulate(enhancement_code, grid, base_grid_size, current_run):
    border_size = 2 * current_run
    new_grid = {}

    background_pixel = calc_background_pixel(enhancement_code, current_run)

    for y in range(-border_size - 1, base_grid_size + border_size + 1):
        for x in range(-border_size - 1, base_grid_size + border_size + 1):
            new_grid[(y, x)] = calc_output_pixel(enhancement_code, grid, background_pixel, (y, x))

    return new_grid


class PuzzleDay20(PuzzleInterface):

    def solve_part_1(self):
        enhancement_code, grid, base_grid_size = parse_input(self.puzzle_contents)

        for run in range(2):
            grid = simulate(enhancement_code, grid, base_grid_size, run)

        c = Counter(grid.values())
        return c['#']

    def solve_part_2(self):
        enhancement_code, grid, base_grid_size = parse_input(self.puzzle_contents)

        for run in range(50):
            grid = simulate(enhancement_code, grid, base_grid_size, run)

        c = Counter(grid.values())
        return c['#']


def show(grid):
    print("Printing grid")
    max_x = max([x for x, _ in grid])
    max_y = max([y for _, y in grid])

    min_x = min([x for x, _ in grid])
    min_y = min([y for y, _ in grid])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            val = grid[(y, x)]
            if val == '.':
                val = '-'
            print(val, end='')
        print("")


puzzle = PuzzleDay20(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
