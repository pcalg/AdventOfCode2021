from general.general import read_day
from general.puzzle import PuzzleInterface
import heapq

test = False

puzzle_input = read_day(15, test)


def create_grid(puzzle_input):
    grid = {}

    for y, line in enumerate(puzzle_input):
        for x, ch in enumerate(line):
            grid[(y, x)] = int(ch)

    return grid


def dist_goal(goal, pos):
    y_g, x_g = goal
    y, x = pos

    return abs(y_g - y) + abs(x_g - x)


def goal(grid, n=1):
    max_y = max([y for y, _ in grid.keys()])
    max_x = max([x for _, x in grid.keys()])
    return (max_y + 1) * n - 1, (max_x + 1) * n - 1


def get_value(grid, max_pos, pos):
    y, x = pos

    max_y, max_x = max_pos

    y_block = y // (max_y + 1)
    x_block = x // (max_x + 1)

    # get relative pos in the block
    y_base = y % (max_y + 1)
    x_base = x % (max_y + 1)

    # block numbers as follows:
    # 0 1 2 3
    # 1 2 3 4
    # 2 3 4 5
    value = (grid[(y_base, x_base)] + y_block + x_block)

    # only allow values between 1 and 9 inclusive
    value = (value - 1) % 9 + 1
    return value


def neighbours(goal, visited, position):
    y, x = position

    y_g, x_g = goal

    # only horizontal, vertical movements allowed
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dy, dx in deltas:
        y_n, x_n = y + dy, x + dx
        if y_n >= 0 and x_n >= 0 and y_n <= y_g and x_n <= x_g and (y_n, x_n) not in visited:
            yield y_n, x_n


class PuzzleDay15(PuzzleInterface):

    def solve_part_1(self):
        g = create_grid(puzzle_input)

        y_goal, x_goal = goal(g)

        # find shortest route
        h = []
        heapq.heappush(h, (0, (0, 0)))

        visited = {(0, 0)}

        while len(h) > 0:
            dist, pos = heapq.heappop(h)
            if pos == (y_goal, x_goal):
                return dist

            # for y_neighbour, x_neighbour in neighbours(g, visited, pos):
            for y_neighbour, x_neighbour in neighbours((y_goal, x_goal), visited, pos):
                dist_neighbour = dist + g[(y_neighbour, x_neighbour)]
                visited.add((y_neighbour, x_neighbour))

                heapq.heappush(h, (dist_neighbour, (y_neighbour, x_neighbour)))

    def solve_part_2(self):
        g = create_grid(puzzle_input)

        y_goal, x_goal = goal(g, n=5)

        # find shortest route
        h = []
        heapq.heappush(h, (0, (0, 0)))

        visited = {(0, 0)}

        max_y = max([y for y, _ in g.keys()])
        max_x = max([x for _, x in g.keys()])

        while len(h) > 0:
            dist, pos = heapq.heappop(h)
            if pos == (y_goal, x_goal):
                return dist

            for y_neighbour, x_neighbour in neighbours((y_goal, x_goal), visited, pos):
                dist_neighbour = dist + get_value(g, (max_y, max_x), (y_neighbour, x_neighbour))
                visited.add((y_neighbour, x_neighbour))

                heapq.heappush(h, (dist_neighbour, (y_neighbour, x_neighbour)))


puzzle = PuzzleDay15(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")

