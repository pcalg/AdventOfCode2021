from collections import defaultdict
from general.general import read_day
from general.puzzle import PuzzleInterface
import math

test = False

puzzle_input = read_day(9, test)


def read_grid(puzzle_input):
    grid = defaultdict(lambda: 9)
    y = 0
    for line in puzzle_input:
        x = 0
        for digit in line:
            grid[(y, x)] = int(digit)
            x += 1
        y += 1
    return grid


def is_low(grid, pos, value):
    y, x = pos
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in deltas:
        if grid[(y + dy, x + dx)] <= value:
            return False
    return True


def find_lows(grid):
    positions = list(grid.keys())

    lows = list()

    for y, x in positions:
        value = grid[(y, x)]
        if is_low(grid, (y, x), value):
            lows.append((y, x))
    return lows


def basin(grid, low):
    """
    find a basin startin at pos low.

    :param grid: input grid
    :param low: low position
    :return:
    """
    visited = set()

    basin_size = 0
    to_check = [low]
    while len(to_check) > 0:
        y, x = to_check.pop()
        basin_size += 1

        # add neighbours, if neighbour != 9 and not visited
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for yd, xd in deltas:
            y_neighbour = y + yd
            x_neighbour = x + xd
            value = grid[(y_neighbour, x_neighbour)]
            if value != 9 and (y_neighbour, x_neighbour) not in visited:
                to_check.append((y_neighbour, x_neighbour))
                visited.add((y_neighbour, x_neighbour))
    return basin_size - 1


class PuzzleDay9(PuzzleInterface):

    def solve_part_1(self):
        grid = read_grid(self.puzzle_contents)
        lows = find_lows(grid)

        total = 0
        for (y, x) in lows:
            total += grid[(y, x)] + 1
        return total

    def solve_part_2(self):
        grid = read_grid(self.puzzle_contents)
        lows = find_lows(grid)

        # find area of all basins start with each low (visit positions)
        basin_sizes = []
        for low in lows:
            basin_sizes.append(basin(grid, low))
        return math.prod((sorted(basin_sizes, reverse=True)[:3]))


puzzle = PuzzleDay9(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
