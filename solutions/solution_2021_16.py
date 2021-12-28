from general.general import read_day
from general.puzzle import PuzzleInterface
from enum import IntEnum
from math import prod
from operator import eq, gt, lt

test = False

puzzle_input = read_day(16, test)

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


class PackageTypes(IntEnum):
    SUM = 0
    PROD = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GT = 5
    LT = 6
    EQ = 7


calculation_funcs = {
    PackageTypes.SUM: sum,
    PackageTypes.PROD: prod,
    PackageTypes.MIN: min,
    PackageTypes.MAX: max,
    PackageTypes.EQ: eq,
    PackageTypes.GT: gt,
    PackageTypes.LT: lt
}


def calculate(package_type, values):
    fn = calculation_funcs[package_type]

    if package_type in (PackageTypes.EQ, PackageTypes.GT, PackageTypes.LT):
        return int(fn(*values))
    else:
        return fn(values)


def to_binary(packet_hex):
    result = ""

    for ch in packet_hex:
        result += hex_to_bin[ch]
    return result


def get_packet_meta(packet_binary):
    version = int(packet_binary[:3], 2)

    packet_type = int(packet_binary[3:6], 2)

    return version, packet_type


def read_literal_value(packet_binary):
    # packets of 5 bits each, stops when the first bit of a group is 0
    start_groups_idx = 6
    total = ''

    while True:
        packet_group = packet_binary[start_groups_idx:start_groups_idx + 5]
        total += packet_group[1:]
        if packet_group[0] == '0':
            value = int(total, 2)
            remaining_package = packet_binary[start_groups_idx + 5:]
            return value, remaining_package

        start_groups_idx += 5


def get_value_range(packet_binary, start_idx, size):
    total = packet_binary[start_idx: start_idx + size]
    return int(total, 2)


def all_zero(packet_binary):
    for ch in packet_binary:
        if ch != '0':
            return False
    return True


def process_package(packet_binary):
    if all_zero(packet_binary):
        return 0, 0, ""

    version_total, packet_type = get_packet_meta(packet_binary)

    if packet_type == PackageTypes.LITERAL:
        value, remaining_package = read_literal_value(packet_binary)
        return version_total, value, remaining_package

    # operators
    length_type_id = int(packet_binary[6])

    sub_values = []
    remaining_package = ""

    if length_type_id == 0:
        # get 15 bits to see what the length is of the subpackets to read
        sub_packet_length = get_value_range(packet_binary, 7, 15)

        # get sub package of length n
        remaining_package = packet_binary[7 + 15: 7 + 15 + sub_packet_length]

        # value from the sub, this doesn't have a remaining
        while len(remaining_package) > 0:
            sub_version_total, sub_value, remaining_package = process_package(remaining_package)
            sub_values.append(sub_value)
            version_total += sub_version_total

        # now keep the rest of the packages if any
        remaining_package = packet_binary[7 + 15 + sub_packet_length:]

    if length_type_id == 1:
        # get 11 bits to see what the length is of the sub packets to read
        n_packages = get_value_range(packet_binary, 7, 11)

        remaining_package = packet_binary[7 + 11:]

        for _ in range(n_packages):
            sub_version_total, sub_value, remaining_package = process_package(remaining_package)
            version_total += sub_version_total
            sub_values.append(sub_value)

    return version_total, calculate(packet_type, sub_values), remaining_package


class PuzzleDay16(PuzzleInterface):

    def solve_part_1(self):
        version_total, _, _ = process_package(to_binary(self.puzzle_contents[0]))
        return version_total

    def solve_part_2(self):
        _, value, _ = process_package(to_binary(self.puzzle_contents[0]))
        return value



puzzle = PuzzleDay16(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")

