from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(11, test)


def calc_deltas():
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (dy, dx) != (0, 0):
                yield (dy, dx)


class Grid:
    def __init__(self, puzzle_input):
        self.step_cnt = 0
        self.flash_count = 0
        self.grid = {}
        self.deltas = list(calc_deltas())
        self.synced = -1

        y = 0
        for line in puzzle_input:
            x = 0
            for digit in line:
                self.grid[(y, x)] = int(digit)
                x += 1
            y += 1

        # grid is rectangular
        self.size = y

    def show(self):
        print(f"After step: {self.step_cnt} flash count: {self.flash_count}")
        for y in range(self.size):
            for x in range(self.size):
                print(self.grid[(y, x)], end='')
            print('')
        print('')

    def step(self):
        self.step_cnt += 1

        # first part increase every cell
        grid = self.grid
        for key in grid:
            grid[key] += 1

        visited = set()
        while True:
            cells_to_consider = {key for key, value in grid.items() if value > 9 and key not in visited}

            for y, x in cells_to_consider:
                visited.add((y, x))
                for (dy, dx) in self.deltas:
                    if (y + dy, x + dx) in self.grid:
                        self.grid[(y + dy, x + dx)] += 1

            if len(cells_to_consider) == 0:
                break

        # now update to 0 where is > 9
        current_flash_count = 0
        for key in grid:
            if grid[key] > 9:
                current_flash_count += 1

                grid[key] = 0
        self.flash_count += current_flash_count

        if current_flash_count == self.size * self.size:
            self.synced = self.step_cnt


class PuzzleDay11(PuzzleInterface):

    def solve_part_1(self):
        g = Grid(self.puzzle_contents)
        for _ in range(100):
            g.step()
        return g.flash_count

    def solve_part_2(self):
        g = Grid(self.puzzle_contents)
        while g.synced == -1:
            g.step()
        return g.step_cnt


puzzle = PuzzleDay11(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
