from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import deque
from collections import Counter

test = False

puzzle_input = read_day(14, test)


def parse_input(puzzle_input):
    pattern = puzzle_input[0]

    rules_split = (line.split(' -> ') for line in puzzle_input[2:])
    rules = {rule: element for rule, element in rules_split}
    return pattern, rules


def apply_rules(rules, pattern_list):
    idx = 0
    while idx < len(pattern_list) - 1:
        # get first two
        code = pattern_list[idx] + pattern_list[idx + 1]
        # lookup replacement
        element = rules[code]

        # pattern list insert
        pattern_list.insert(idx + 1, element)

        idx += 2


def statistics(pattern_list):
    c = Counter(pattern_list)
    stats = c.most_common()
    return stats[0][1] - stats[-1][1]


def get_next_pattern(rules, current_pattern):
    """
    Get the next two patterns based on the rule
    :param rules: dictionary with the rules {'CH': 'B',  }
    :param current_pattern: two letter code, for example 'CH'
    :return: CB, BH
    """
    ch = rules[current_pattern]

    return ch, (current_pattern[0] + ch, ch + current_pattern[1])


def process_rules(rules, patterns, stats):
    patterns_result = {}

    # return next rules
    for pattern, cnt in patterns.items():

        ch, next_patterns = get_next_pattern(rules, pattern)
        stats[ch] += cnt

        for next_pattern in next_patterns:
            patterns_result[next_pattern] = patterns_result.get(next_pattern, 0) + cnt

    return patterns_result, stats


class PuzzleDay14(PuzzleInterface):

    def solve_part_1(self):
        pattern, rules = parse_input(self.puzzle_contents)

        pattern_list = deque(pattern)

        for _ in range(10):
            apply_rules(rules, pattern_list)

        return statistics(pattern_list)

    def solve_part_2(self):
        start_pattern, rules = parse_input(self.puzzle_contents)

        # init
        current_patterns = {}

        for idx, ch in enumerate(start_pattern[:-1]):
            tmp_pattern = start_pattern[idx:idx + 2]
            current_patterns[tmp_pattern] = current_patterns.get(tmp_pattern, 0) + 1


        stats = Counter(start_pattern)

        for _ in range(40):
            current_patterns, stats = process_rules(rules, current_patterns, stats)

        return statistics(stats)

puzzle = PuzzleDay14(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
