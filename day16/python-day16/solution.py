from enum import Enum
from heapq import heapify, heappop, heappush

class Direction(Enum):
    NORTH = (0, -1)
    EAST  = (1, 0)
    SOUTH = (0, 1)
    WEST  = (-1, 0)

    def __lt__(self, two):
        return True


class Graph:
    def __init__(self, graph = {}):
        self.graph = graph
        
    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def dijkstra(self, source):
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0

        pq = [(0, source)]
        heapify(pq)
        
        visited = set()
        
        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited: continue
            visited.add(current_node)
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        return distances


def get_char(x, y, data):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return "#"
    return data[y][x]


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data


def create_graph(data: list):
    g = Graph()
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = get_char(x, y, data)
            if c == "#": continue
            elif c == "S":
                starting_point = (x, y, Direction.EAST)
            elif c == "E":
                ending_points = [(x, y, d) for d in Direction]
            for d in Direction:
                node = (x, y, d)
                g.add_edge(node, node, 0)  # Add self
                if d in [Direction.NORTH, Direction.SOUTH]:
                    g.add_edge(node, (x, y, Direction.EAST), 1000)
                    g.add_edge(node, (x, y, Direction.WEST), 1000)
                elif d in [Direction.EAST, Direction.WEST]:
                    g.add_edge(node, (x, y, Direction.NORTH), 1000)
                    g.add_edge(node, (x, y, Direction.SOUTH), 1000)
                if get_char(x + d.value[0], y + d.value[1], data) in ["S", "E", "."]:
                    g.add_edge(node, (x + d.value[0], y + d.value[1], d), 1)
    return g, starting_point, ending_points


def part1(g, starting_point, ending_points) -> int:
    d = g.dijkstra(starting_point)
    return min([d[e] for e in ending_points])


def part2(g, starting_point, ending_points) -> int:
    return False


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    g, starting_point, ending_points = create_graph(data)
    p1 = part1(g, starting_point, ending_points)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(g, starting_point, ending_points)
    print(f"Part 2 solution:\n{p2}")
