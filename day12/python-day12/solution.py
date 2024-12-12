def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [[[k, None, None] for k in q] for q in data]
    return data


DIRS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

def get(x, y, data):
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        return [None, None, None]
    return data[y][x]


def part1(data: list):
    s = 0
    idx = 0
    sames = list()
    for y in range(len(data)):
        for x in range(len(data[y])):
            item = data[y][x]
            empty_edges = 0
            possible_group = list()
            for dir in DIRS:
                neighbor = get(x+dir[0], y+dir[1], data)
                if item[0] == neighbor[0]:
                    if neighbor[2] is not None:
                        possible_group.append(neighbor[2])
                else:
                    empty_edges += 1
            if len(set(possible_group)) > 1:
                found = False
                tmp = set()
                for i in range(len(sames)):
                    for g in possible_group:
                        if g in sames[i]:
                            found=True
                            tmp.add(i)
                if not found:
                    sames.append(possible_group)
                else:
                    tmp = sorted(list(tmp))
                    for i in range(len(tmp)):
                        if i == 0: continue
                        sames[tmp[0]].extend(sames[tmp[i]])
                        sames.pop(tmp[i])
                    sames[tmp[0]].extend(possible_group)
                    sames[tmp[0]] = list(set(sames[tmp[0]]))
            if len(possible_group) == 0:
                item[2] = idx
                idx += 1
            else:
                item[2] = possible_group[0]
            item[1] = empty_edges
    costs = list()
    sames = [sorted(q) for q in sames]
    for _ in range(idx):
        costs.append([0, 0])
    for y in range(len(data)):
        for x in range(len(data[y])):
            item = data[y][x]
            for same in sames:
                if item[2] in same:
                    item[2] = same[0]
            costs[item[2]][0] += 1
            costs[item[2]][1] += item[1]
    for item in costs:
        s += item[0] * item[1]
    return s


def part2(data: list):
    s = 0
    idx = 0
    sames = list()
    for y in range(len(data)):
        for x in range(len(data[y])):
            item = data[y][x]
            empty_edges = list()
            possible_group = list()
            for dir in DIRS:
                neighbor = get(x+dir[0], y+dir[1], data)
                if item[0] == neighbor[0]:
                    if neighbor[2] is not None:
                        possible_group.append(neighbor[2])
                else:
                    empty_edges.append((x+(dir[0]/2), y+(dir[1]/2)))
            if len(set(possible_group)) > 1:
                found = False
                tmp = set()
                for i in range(len(sames)):
                    for g in possible_group:
                        if g in sames[i]:
                            found=True
                            tmp.add(i)
                if not found:
                    sames.append(possible_group)
                else:
                    tmp = sorted(list(tmp))
                    for i in range(len(tmp)):
                        if i == 0: continue
                        sames[tmp[0]].extend(sames[tmp[i]])
                        sames.pop(tmp[i])
                    sames[tmp[0]].extend(possible_group)
                    sames[tmp[0]] = list(set(sames[tmp[0]]))
            if len(possible_group) == 0:
                item[2] = idx
                idx += 1
            else:
                item[2] = possible_group[0]
            item[1] = empty_edges
    sames = [sorted(q) for q in sames]
    costs = list()
    for _ in range(idx):
        costs.append([0, set()])
    for y in range(len(data)):
        for x in range(len(data[y])):
            item = data[y][x]
            for same in sames:
                if item[2] in same:
                    item[2] = same[0]
            costs[item[2]][0] += 1
            for tmp in item[1]:
                costs[item[2]][1].add(tmp)
    for item in costs:
        print(item, item[0] * len(item[1]))
        s += item[0] * len(item[1])
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
