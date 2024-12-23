from collections import defaultdict


START_WITH = "t"


def clean_data(data: list) -> list:
    data = [line.strip().split("-") for line in data]
    return data


def part1(data: list):
    # Build connections map
    connections = defaultdict(list)
    for pair in data:
        connections[pair[0]].append(pair[1])
        connections[pair[1]].append(pair[0])
    # Build (t-based) trios
    trios = list()
    while data:
        pair = data.pop()
        for key, value in connections.items():
            if not key.startswith(START_WITH):
                continue
            if pair[0] in value and pair[1] in value:
                trio = set([key, *pair])
                if trio not in trios:
                    trios.append(trio)
    return len(trios)


def part2(data: list):
    # Build connections map
    connections = defaultdict(list)
    for pair in data:
        connections[pair[0]].append(pair[1])
        connections[pair[1]].append(pair[0])


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
