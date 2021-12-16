from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(13, test)


def fold_y(grid, y_fold):
    grid_new = set()

    # all positions lower than y_fold stay, others move down distance y - y_fold
    for x, y in grid:
        if y > y_fold:
            dist_fold = y - y_fold
            y = y_fold - dist_fold
        grid_new.add((x, y))
    return grid_new


def fold_x(grid, x_fold):
    grid_new = set()

    # all positions lower than x_fold stay, others move down distance x - x_fold
    for x, y in grid:
        if x > x_fold:
            dist_fold = x - x_fold
            x = x_fold - dist_fold
        grid_new.add((x, y))
    return grid_new


def process_fold(grid, fold):
    fold_dimension, fold_position = fold
    fold_funcs = {'x': fold_x, 'y': fold_y}

    return fold_funcs[fold_dimension](grid, fold_position)


def parse_input(puzzle_input):
    grid = set()
    folds = []

    for value in puzzle_input:
        if value == '':
            continue
        elif 'fold along ' in value:
            dimension, val = value.replace('fold along ', '').split('=')
            folds.append((dimension, int(val)))
        else:
            x, y = [int(val) for val in value.split(',')]
            grid.add((x, y))

    return grid, folds


def show(grid):
    print("Printing grid")
    max_x = max([x for x, _ in grid])
    max_y = max([y for _, y in grid])

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in grid:
                print("#", end='')
            else:
                print("-", end='')
        print("")


class PuzzleDay13(PuzzleInterface):

    def solve_part_1(self):
        grid, folds = parse_input(self.puzzle_contents)
        grid = process_fold(grid, folds[0])
        return len(grid)

    def solve_part_2(self):
        grid, folds = parse_input(self.puzzle_contents)
        for fold in folds:
            grid = process_fold(grid, fold)

        # PZEHRAER
        show(grid)
        return len(grid)


puzzle = PuzzleDay13(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
