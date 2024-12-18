from enum import Enum
from heapq import heapify, heappop, heappush


WIDTH = 71
HEIGHT = 71


class Direction(Enum):
    NORTH = (0, -1)
    EAST  = (1, 0)
    SOUTH = (0, 1)
    WEST  = (-1, 0)


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


def clean_data(data: list) -> list:
    data = [[int(q) for q in line.strip().split(",")] for line in data]
    return data


def get_point(x, y, grid):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return "#"
    return grid[y][x] 


def part1(data):
    # Create grid
    grid = list()
    for _ in range(HEIGHT):
        row = list()
        for _ in range(WIDTH):
            row.append(".")
        grid.append(row)
    # Place first 1024 points
    for i in range(1024):
        x, y = data[i]
        grid[y][x] = "#"
    # Create graph
    g = Graph()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            node = (x, y)
            g.add_edge(node, node, 0)
            for d in Direction:
                new = (x+d.value[0], y+d.value[1])
                if get_point(new[0], new[1], grid) == "#":
                    continue
                g.add_edge(node, new, 1)
    # Get shortest path
    starting_point = (0, 0)
    ending_point = (WIDTH-1, HEIGHT-1)
    dists = g.dijkstra(starting_point)
    return dists[ending_point]


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print(data[3042])
