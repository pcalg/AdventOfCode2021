from general.general import read_day
from general.puzzle import PuzzleInterface
import heapq

test = True

puzzle_input = read_day(15, test)


def create_grid(puzzle_input):
    grid = {}

    for y, line in enumerate(puzzle_input):
        for x, ch in enumerate(line):
            grid[(y, x)] = int(ch)

    return grid


def goal(grid):
    max_y = max([y for y, _ in grid.keys()])
    max_x = max([x for _, x in grid.keys()])
    return max_y, max_x


def neighbours(grid, visited, position):
    y, x = position

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            neighbour = y + dy, x + dx
            if neighbour != position and neighbour in grid and neighbour not in visited:
                yield neighbour


class PuzzleDay15(PuzzleInterface):

    def solve_part_1(self):
        pass

    def solve_part_2(self):
        pass


puzzle = PuzzleDay15(puzzle_input)

g = create_grid(puzzle_input)

y_goal, x_goal = goal(g)

# find shortest route
h = []
heapq.heappush(h, (0, (0, 0)))
visited = set()


print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
