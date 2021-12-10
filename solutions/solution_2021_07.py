from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(7, test)
puzzle_input_int = [int(val) for val in puzzle_input[0].split(',')]


def determine_distance(goal_location, locations):
    total = 0
    for location in locations:
        total += abs(location - goal_location)
    return total


def fuel_cost(goal_location, locations):
    total = 0
    for location in locations:
        distance = abs(location - goal_location)
        if distance % 2 == 0:
            cost = (1 + distance) * (distance // 2)
        else:
            cost = (distance // 2 + 1) * distance
        total += cost

    return total


class PuzzleDay7(PuzzleInterface):

    def solve_part_1(self):
        min_fuel = -1

        for goal_location in self.puzzle_contents:
            fuel = determine_distance(goal_location, self.puzzle_contents)
            if min_fuel == -1:
                min_fuel = fuel
            else:
                min_fuel = min(fuel, min_fuel)

        return min_fuel

    def solve_part_2(self):

        # just try all locations
        max_location = max(self.puzzle_contents)
        min_location = min(self.puzzle_contents)

        min_fuel = fuel_cost(min_location, puzzle_input_int)

        for goal_location in range(min_location + 1, max_location + 1):
            fuel = fuel_cost(goal_location, self.puzzle_contents)
            min_fuel = min(fuel, min_fuel)

        return min_fuel


puzzle = PuzzleDay7(puzzle_input_int)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
