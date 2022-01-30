from general.general import read_day
from general.puzzle import PuzzleInterface
from itertools import islice
from itertools import product

test = False

puzzle_input = read_day(21, test)


def parse(puzzle_input):
    result = {}
    values = []
    for line in puzzle_input:
        parts = line.split(' ')
        result[int(parts[1])] = int(parts[4])
        values.append(int(parts[4]))

    return result, values


def die():
    while True:
        for value in range(1, 101):
            yield value


def play_game(player_locations):
    die_rolls = die()

    points = {1: 0, 2: 0}

    dice_roll_count = 0

    for n in range(1000):
        current_player = n % 2 + 1
        other_player = (n + 1) % 2 + 1

        player_location = player_locations[current_player]

        current_rolls = list(islice(die_rolls, 3))
        roll_total = sum(current_rolls)

        dice_roll_count += 3

        # calculate where the player ends up
        new_location = (player_location + roll_total - 1) % 10 + 1

        points[current_player] += new_location
        player_locations[current_player] = new_location

        print(
            f"player: {current_player} rolls {'+'.join([str(r) for r in current_rolls])} moves to {new_location} for a total score of {points[current_player]}")

        if points[current_player] >= 1000:
            return points[other_player] * dice_roll_count

    return 0


def next_location(player_location, dice_value):
    return (player_location + dice_value - 1) % 10 + 1


def all_roll_totals(max_value=3):
    rolls = product([n for n in range(1, max_value + 1)], repeat=max_value)

    # totals
    for roll in rolls:
        yield sum(roll)


def calc_wins_player(lookup, current_player, positions, scores):
    pos0, pos1 = positions
    score0, score1 = scores

    next_player = 1 if current_player == 0 else 0

    if (current_player, pos0, pos1, score0, score1) in lookup:
        return lookup[(current_player, pos0, pos1, score0, score1)]

    # roll dice
    total = [0, 0]
    for roll in all_roll_totals(3):
        current_scores = scores.copy()
        current_positions = positions.copy()

        pos_next = next_location(current_positions[current_player], roll)

        current_positions[current_player] = pos_next
        current_scores[current_player] += pos_next

        if current_scores[current_player] >= 21:
            wins = [0, 0]
            wins[current_player] = 1
        else:
            wins = calc_wins_player(lookup, next_player, current_positions, current_scores)

        total[current_player] += wins[current_player]
        total[next_player] += wins[next_player]

    lookup[(current_player, pos0, pos1, score0, score1)] = total[0], total[1]
    return total[0], total[1]


class PuzzleDay21(PuzzleInterface):

    def solve_part_1(self):
        player_locations, _ = parse(self.puzzle_contents)
        return play_game(player_locations)

    def solve_part_2(self):
        #
        _, positions = parse(self.puzzle_contents)

        lookup = {}
        wins = calc_wins_player(lookup, 0, positions, [0, 0])
        return max(wins)


puzzle = PuzzleDay21(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
