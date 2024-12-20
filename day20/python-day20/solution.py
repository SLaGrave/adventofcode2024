from enum import Enum
from heapq import heapify, heappop, heappush
from collections import defaultdict


MIN_TIME_SAVE = 100


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
                # WHAT?!
                if neighbor not in distances:
                    continue
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
        return distances


def clean_data(data):
    return [q.strip() for q in data]


def get(x, y, data):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return None
    return data[y][x]


def part1(data):
    walls = list()
    g = Graph()
    # Setup graph
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = get(x, y, data)
            p = (x, y)
            if c == "S":
                starting_point = p
            elif c == "E":
                ending_point = p
            elif c == "#":
                walls.append(p)
                continue
            g.add_edge(p, p, 0)
            for d in Direction:
                new = (x+d.value[0], y+d.value[1])
                new_char = get(new[0], new[1], data)
                if new_char in [".", "S", "E"]:
                    g.add_edge(p, new, 1)
    print("Graph creation done")
    # Get base time
    base_time = g.dijkstra(starting_point)[ending_point]
    # Get cheats
    cheats = list()
    idx = -1
    for wall in walls:
        idx += 1
        print(f"Possbile cheat {idx}/{len(walls)} ({int(idx/len(walls) * 100)}%)", end="\r")
        new_g = Graph(g.graph.copy())
        new_g.add_edge(wall, wall, 0)
        for d in Direction:
            neighbor = (wall[0]+d.value[0], wall[1]+d.value[1])
            dc = get(neighbor[0], neighbor[1], data)
            if dc is None: continue
            if dc in [".", "S", "E"] and neighbor not in walls:
                new_g.add_edge(wall, neighbor, 1)
                new_g.add_edge(neighbor, wall, 1)
        new_time = new_g.dijkstra(starting_point)[ending_point]
        if base_time - new_time >= MIN_TIME_SAVE:
            cheats.append(wall)
    return len(cheats), cheats


def part2(data):
    return 0


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1, _ = part1(data)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data)
    print(f"Part 2 solution:\n{p2}")
