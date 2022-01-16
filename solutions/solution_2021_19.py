from general.general import read_day
from general.puzzle import PuzzleInterface
from itertools import permutations
from itertools import product

test = False

puzzle_input = read_day(19, test)


def calc_distance(pos_from, pos_to):
    return sum([abs(a - b) for a, b in zip(pos_from, pos_to)])


def apply_delta(positions, delta):
    """
    Add the delta to the positions to align them in the same position as the base scanner

    :param positions: The positions to update
    :param delta: The delta to apply
    :return: The transformed list of positions
    """
    result_positions = set()

    dx, dy, dz = delta
    for x, y, z in positions:
        result_positions.add((x + dx, y + dy, z + dz))

    return list(result_positions)


def compare_scanners(base_positions, compare_positions):
    """
    Create the vectors for the base position between each node and
    also create vectors for each rotation in compare_positions.
     This enables to match them with the vectors we have from base_positions.

    :param base_positions:
    :param compare_positions:
    :return: if a match: True, rotated positions and also the delta location, which is the scanner location if not a match
    False and the compare_positions and a delta of (0, 0, 0)
    """

    base_vector, base_vector_lookup = create_vectors(base_positions)

    for current_positions in create_configurations(compare_positions):
        nodes = set()
        deltas = set()
        delta = (0, 0, 0)


        compare_vector, compare_vector_lookup = create_vectors(current_positions)
        for vector in base_vector:

            if vector in compare_vector:
                base_a, base_b = base_vector_lookup[vector]
                compare_a, compare_b = compare_vector_lookup[vector]

                nodes.add(base_a)
                nodes.add(base_b)

                pos_base_a = base_positions[base_a]

                pos_compare_a = current_positions[compare_a]

                delta = delta_vector(pos_compare_a, pos_base_a)
                deltas.add(delta)


        if len(nodes) >= 11 and len(deltas) == 1:
            return True, apply_delta(current_positions, delta), delta  # update to new positions

    return False, compare_positions, (0, 0)  # these two do not overlap so return the original

def create_configurations(positions):
    """
    Do all the rotations

    :param positions:
    :return:
    """

    for idx_x, idx_y, idx_z in list(permutations((0, 1, 2))):
        for sx, sy, sz in [sign for sign in product([-1, 1], repeat=3)]:
            result_positions = []
            for pos in positions:
                x = pos[idx_x]
                y = pos[idx_y]
                z = pos[idx_z]
                result_positions.append((x * sx, y * sy, z * sz))
            yield result_positions


def delta_vector(position_from, position_to):
    x1, y1, z1 = position_from
    x2, y2, z2 = position_to
    return x2 - x1, y2 - y1, z2 - z1

def create_vectors(positions):
    """ Calculate a vector between each node in positions """
    vectors = set()
    vector_lookup = {}


    for idx_from in range(len(positions)):
        for idx_to in range(idx_from + 1, len(positions)):
            d_v = delta_vector(positions[idx_from], positions[idx_to])
            vectors.add(d_v)
            if d_v in vector_lookup:
                raise Exception("same vector found, not expected")
            vector_lookup[d_v] = (idx_from, idx_to)

    return vectors, vector_lookup


def calc_unique_locations(scanners):
    unique_locations = set()
    for positions in scanners.values():
        for pos in positions:
            unique_locations.add(pos)

    return len(unique_locations)

def parse_input(puzzle_input):
    scanners = {}
    scanner_name = "invalid scanner"

    for line in puzzle_input:
        if "---" in line:
            scanner_name = line.replace("---", "").strip()
            scanners[scanner_name] = []
        elif line != "":
            position = tuple([int(val) for val in line.split(',')])
            scanners[scanner_name].append(position)

    return scanners



class PuzzleDay19(PuzzleInterface):

    def solve_part_1(self):
        scanners = parse_input(self.puzzle_contents)

        base_scanners = ['scanner 0']
        to_compare_scanners = set(list(scanners)[1:])

        #completed_scanners = []
        linked_scanners = set()

        while len(base_scanners) > 0:
            base_scanner_name = base_scanners.pop()
            base_scanner = scanners[base_scanner_name]

            for compare_scanner in to_compare_scanners:
                res, scanner_res, delta = compare_scanners(base_scanner, scanners[compare_scanner])
                if res:
                    scanners[compare_scanner] = scanner_res
                    base_scanners.append(compare_scanner)
                    linked_scanners.add(compare_scanner)

            to_compare_scanners -= linked_scanners
            #completed_scanners.append(base_scanner_name)

        return calc_unique_locations(scanners)

    def solve_part_2(self):
        scanners = parse_input(self.puzzle_contents)

        base_scanners = ['scanner 0']
        to_compare_scanners = set(list(scanners)[1:])

        linked_scanners = set()
        sensor_positions = [(0, 0)]

        while len(base_scanners) > 0:
            base_scanner_name = base_scanners.pop()
            base_scanner = scanners[base_scanner_name]

            for compare_scanner in to_compare_scanners:
                res, scanner_res, delta = compare_scanners(base_scanner, scanners[compare_scanner])
                if res:
                    scanners[compare_scanner] = scanner_res
                    base_scanners.append(compare_scanner)
                    linked_scanners.add(compare_scanner)
                    sensor_positions.append(delta)

            to_compare_scanners -= linked_scanners

        # calc the max distance between the sensors
        max_distance = 0
        for idx_a in range(len(sensor_positions)):
            for idx_b in range(idx_a + 1, len(sensor_positions)):
                pos_a = sensor_positions[idx_a]
                pos_b = sensor_positions[idx_b]
                dist = calc_distance(pos_a, pos_b)
                max_distance = max(dist, max_distance)

        return max_distance

puzzle = PuzzleDay19(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
