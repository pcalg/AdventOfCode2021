from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(2, test)


def go_down(horizontal, depth, distance):
    return horizontal, depth + distance

def go_up(horizontal, depth, distance):
    return horizontal, depth - distance

def go_forward(horizontal, depth, distance):
    return horizontal + distance, depth


def go_down_aim(horizontal, depth, aim, distance):
    return horizontal, depth, aim + distance

def go_up_aim(horizontal, depth, aim, distance):
    return horizontal, depth, aim - distance

def go_forward_aim(horizontal, depth, aim, distance):
    return horizontal + distance, depth + aim * distance, aim


class PuzzleDay2(PuzzleInterface):

    def solve_part_1(self):
        horizontal = 0
        depth = 0

        actions = {"down": go_down, "up": go_up, "forward": go_forward}

        for reading in self.puzzle_contents:
            action, distance = reading.split(" ")

            horizontal, depth = actions[action](horizontal, depth, int(distance))

        print(horizontal * depth)


    def solve_part_2(self):
        horizontal = 0
        depth = 0
        aim = 0

        actions = {"down": go_down_aim, "up": go_up_aim, "forward": go_forward_aim}

        for reading in self.puzzle_contents:
            action, distance = reading.split(" ")

            horizontal, depth, aim = actions[action](horizontal, depth, aim, int(distance))

        print(horizontal * depth)



puzzle = PuzzleDay2(puzzle_input)

puzzle.solve_part_1()
puzzle.solve_part_2()
