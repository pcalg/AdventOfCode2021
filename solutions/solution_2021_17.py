from general.general import read_day
from general.puzzle import PuzzleInterface

test = False

puzzle_input = read_day(17, test)


def parse_input(puzzle_input):
    items = puzzle_input[0].replace('target area: ', '').split(',')

    x_range = sorted([int(x) for x in items[0].split('=')[1].split('..')])
    y_range = sorted([int(y) for y in items[1].split('=')[1].split('..')])

    return x_range, y_range


def min_velocity(x_min):
    vel = 0
    for n in range(1, x_min + 1):
        vel += n
        if vel >= x_min:
            return n
    return 0


def probe_steps(goal, velocity, max_steps=1200):
    x_min, x_max = goal[0]
    y_min, y_max = goal[1]

    x_current, y_current = (0, 0)
    x_velocity, y_velocity = velocity
    y_max = 0

    for _ in range(max_steps):
        x_current += x_velocity
        x_velocity -= 1

        if x_velocity < 0:
            x_velocity = 0

        y_current += y_velocity
        y_velocity -= 1

        # keep count of the highest y in this run
        y_max = max(y_max, y_current)

        if x_current > x_max or y_current < y_min:
            break

        yield ((x_current, y_current), y_max)


def simulate(goal):
    x_goal_min, x_goal_max = goal[0]
    y_goal_min, y_goal_max = goal[1]

    x_min_velocity = min_velocity(x_goal_min)
    x_max_velocity = x_goal_max + 1

    max_y_pos = 0
    velocities_at_target = set()

    for x_vel in range(x_min_velocity, x_max_velocity + 1):
        for y_vel in range(-300, 650):
            for (x_step, y_step), cur_max_y in probe_steps(goal, (x_vel, y_vel)):
                if x_step >= x_goal_min and x_step <= x_goal_max and y_step >= y_goal_min and y_step <= y_goal_max:
                    max_y_pos = max(cur_max_y, max_y_pos)
                    velocities_at_target.add((x_vel, y_vel))

    return max_y_pos, len(velocities_at_target)


class PuzzleDay17(PuzzleInterface):

    def solve_part_1(self):
        goal = parse_input(self.puzzle_contents)
        max_y, _ = simulate(goal)
        return max_y

    def solve_part_2(self):
        goal = parse_input(self.puzzle_contents)
        _, at_target = simulate(goal)
        return at_target


puzzle = PuzzleDay17(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
