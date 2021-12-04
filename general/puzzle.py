import abc


class PuzzleInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'solve_part_1') and
                callable(subclass.solve_part_1) and
                hasattr(subclass, 'solve_part_2') and
                callable(subclass.solve_part_2))

    def __init__(self, puzzle_contents):
        self.puzzle_contents = puzzle_contents

    @abc.abstractmethod
    def solve_part_1(self):
        """Solve part 1 of the puzzle"""
        raise NotImplementedError

    @abc.abstractmethod
    def solve_part_2(self):
        """Solve part 2 of the puzzle"""
        raise NotImplementedError
