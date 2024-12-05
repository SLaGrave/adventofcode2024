import itertools
from functools import cmp_to_key


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    rules = []
    updates = []
    rule = True
    for line in data:
        if line == "":
            rule = not rule
        elif rule:
            rules.append(line)
        else:
            updates.append(line)
    return [rules, updates]


BAD_ITEMS = []
BEFORE = {}


def part1(data: list):
    global BEFORE
    global BAD_ITEMS
    s = 0
    rules = data[0]
    updates = data[1]
    before = {}
    for rule in rules:
        tmp = rule.split("|")
        tmp = [int(q) for q in tmp]
        if tmp[0] not in before.keys():
            before[tmp[0]] = [tmp[1]]
        else:
            before[tmp[0]].append(tmp[1])
        if tmp[1] not in before.keys(): before[tmp[1]] = []
    for line in updates:
        line = line.split(",")
        line = [int(q) for q in line]
        good = True
        for idx, item in enumerate(line):
            if idx == 0: continue
            for i in range(idx):
                if line[i] in before[item]:
                    good = False
        if good:
            idx = int(len(line)/2)
            s += line[idx]
        else:
            # Save this for part 2
            BAD_ITEMS.append(line)
    # Save my befores dict for part 2
    BEFORE = before
    return s


def cmp(x, y):
    x_before = y in BEFORE[x]
    y_before = x in BEFORE[y]
    if x_before and y_before:
        raise Exception("DEAR GOD!")
    elif x_before:
        return -1
    elif y_before:
        return 1
    else:
        return 0


def part2():
    s = 0
    for line in BAD_ITEMS:
        line = sorted(line, key=cmp_to_key(cmp))
        idx = int(len(line)/2)
        s += line[idx]
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2()
    print(f"Part 2 solution:\n{p2}")
