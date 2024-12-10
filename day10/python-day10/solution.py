def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [[int(r) for r in q] for q in data]
    return data


DIRS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]


def part1(data: list):
    s = 0
    points = []
    for _ in range(10):
        points.append(dict())
    for y in range(len(data)):
        for x in range(len(data[y])):
            p = data[y][x]
            points[p][(x,y)] = set()
            if p == 9:
                points[p][(x,y)].add((x,y))
    for i in reversed(list(range(9))):
        for key, value in points[i].items():
            for dir in DIRS:
                try:
                    for item in points[i+1][(key[0]+dir[0], key[1]+dir[1])]:
                        value.add(item)
                except:
                    pass
    for _, value in points[0].items():
        s += len(value)
    return s


def part2(data: list):
    s = 0
    points = []
    for _ in range(10):
        points.append(dict())
    for y in range(len(data)):
        for x in range(len(data[y])):
            p = data[y][x]
            points[p][(x,y)] = 0
            if p == 9:
                points[p][(x,y)] += 1
    for i in reversed(list(range(9))):
        for key, value in points[i].items():
            for dir in DIRS:
                if (key[0]+dir[0], key[1]+dir[1]) in points[i+1].keys():
                    points[i][key] += points[i+1][(key[0]+dir[0], key[1]+dir[1])]
    for _, value in points[0].items():
        s += value
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
