from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(6, test)
puzzle_input_int = [int(val) for val in puzzle_input[0].split(',')]


def count_days(max_day, initial_day):
    days = defaultdict(int)

    days[initial_day + 1] = 1

    for day in range(max_day + 1):
        if days[day] > 0:
            n = days[day]
            days[day + 9] += n
            days[day + 7] += n

    # result is the total until the max day (can't use values directly as it also has days after max day)
    # this is because of the +9/+7.
    total = 1
    for day in range(max_day + 1):
        total += days[day]
    return total


class PuzzleDay6(PuzzleInterface):

    def solve_part_1(self):
        timers = self.puzzle_contents

        total = 0
        for timer in timers:
            total += count_days(80, timer)

        # initial (slow) solution:
        # for day in range(80):
        #     size_increase = 0
        #     new_timers = []
        #     for idx, timer_value in enumerate(timers):
        #         timer_value -= 1
        #         if timer_value < 0:
        #             timer_value = 6
        #             new_timers.append(8)
        #             size_increase += 1
        #         timers[idx] = timer_value
        #     timers.extend(new_timers)

        # return len(timers)
        return total

    def solve_part_2(self):
        timers = self.puzzle_contents

        total = 0
        for timer in timers:
            total += count_days(256, timer)
        return total


puzzle = PuzzleDay6(puzzle_input_int)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
