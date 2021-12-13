from general.general import read_day
from general.puzzle import PuzzleInterface
from collections import defaultdict

test = False

puzzle_input = read_day(12, test)


def parse_graph(puzzle_input):
    g = defaultdict(set)

    for edge in puzzle_input:
        node_from, node_to = edge.split('-')
        g[node_from].add(node_to)
        g[node_to].add(node_from)
    return g


class PuzzleDay12(PuzzleInterface):

    def solve_part_1(self):
        g = parse_graph(self.puzzle_contents)

        # node, visite, route
        to_process = [('start', {'start'}, ['start'])]
        routes = []

        while len(to_process) > 0:
            current, visited, route = to_process.pop()

            # check neighbours
            for neighbour_node in g[current]:
                if neighbour_node not in visited:
                    # if neighbour_node != 'start':
                    route_next = [r for r in route] + [neighbour_node]
                    if neighbour_node == 'end':
                        routes.append(route_next)
                    else:
                        visited_next = visited.copy()
                        if neighbour_node.islower():
                            visited_next.add(neighbour_node)
                        to_process.append((neighbour_node, visited_next, route_next))

        return len(routes)

    def solve_part_2(self):
        g = parse_graph(self.puzzle_contents)

        # node, visite, route
        to_process = [('start', {'start'}, ['start'], '')]
        routes = []

        while len(to_process) > 0:
            current, visited, route, lower_ch = to_process.pop()

            # check neighbours
            for neighbour_node in g[current]:
                if neighbour_node not in visited or lower_ch == '':
                    if neighbour_node != 'start':
                        route_next = [r for r in route] + [neighbour_node]
                        if neighbour_node == 'end':
                            routes.append(route_next)
                        else:
                            visited_next = visited.copy()
                            if neighbour_node.islower and neighbour_node in visited_next:
                                lower_ch_next = neighbour_node
                            else:
                                lower_ch_next = lower_ch

                            if neighbour_node.islower():
                                visited_next.add(neighbour_node)

                            to_process.append((neighbour_node, visited_next, route_next, lower_ch_next))

        return len(routes)


puzzle = PuzzleDay12(puzzle_input)

print(f"Solution: {puzzle.solve_part_1()}")
print(f"Solution: {puzzle.solve_part_2()}")
