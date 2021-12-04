from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(4, test)


class Board:
    def __init__(self):
        self.rows = defaultdict(list)
        self.columns = defaultdict(list)
        self.current_row = 0

    def add_row(self, row_numbers):
        self.rows[self.current_row].extend(row_numbers)

        for col, number in enumerate(row_numbers):
            self.columns[col].append(number)

        self.current_row += 1

    def complete(self, found_numbers):
        bingo_sets = [set(row) for row in self.rows.values()] + [set(col) for col in self.columns.values()]
        found_numbers_set = set(found_numbers)

        for bingo_item in bingo_sets:
            if bingo_item.issubset(found_numbers_set):
                return True
        return False

    def unmarked(self, found_numbers):
        found_numbers_set = set(found_numbers)

        total = 0
        for bingo_row in self.rows.values():
            total += sum(set(bingo_row).difference(found_numbers_set))

        return total


class PuzzleDay4(PuzzleInterface):

    def load_boards(self):
        boards = []

        current_board = Board()
        boards.append(current_board)

        for row in self.puzzle_contents[2:]:
            if row == "":
                current_board = Board()
                boards.append(current_board)
            else:
                row_values = [int(val) for val in row.split(" ") if val != ""]
                current_board.add_row(row_values)
        return boards

    def solve_part_1(self):
        numbers = [int(n) for n in self.puzzle_contents[0].split(",")]
        boards = self.load_boards()

        for idx, _ in enumerate(numbers):
            current_numbers = numbers[:idx]
            for board in boards:
                if board.complete(current_numbers):
                    return board.unmarked(current_numbers) * current_numbers[-1]

        return -1

    def solve_part_2(self):
        numbers = [int(n) for n in self.puzzle_contents[0].split(",")]
        current_boards = self.load_boards()

        last_complete_board = None

        for idx, _ in enumerate(numbers):
            current_numbers = numbers[:idx]
            new_boards = []
            for board in current_boards:
                if not board.complete(current_numbers):
                    new_boards.append(board)
                else:
                    last_complete_board = board

            current_boards = new_boards

            if len(current_boards) == 0:
                return last_complete_board.unmarked(current_numbers) * current_numbers[-1]

        return -1


puzzle = PuzzleDay4(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
