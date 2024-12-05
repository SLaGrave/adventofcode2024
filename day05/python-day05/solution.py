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


def create_ordering(rules):
    ordering = {}
    for rule in rules:
        tmp = rule.split("|")
        tmp = [int(q) for q in tmp]
        if tmp[0] not in ordering.keys():
            ordering[tmp[0]] = [tmp[1]]
        else:
            ordering[tmp[0]].append(tmp[1])
        if tmp[1] not in ordering.keys(): ordering[tmp[1]] = []
    return ordering



def part1(data: list):
    s = 0
    ordering = create_ordering(data[0])
    updates = data[1]
    bad_items = []
    for line in updates:
        line = line.split(",")
        line = [int(q) for q in line]
        good = True
        for idx, item in enumerate(line):
            if idx == 0: continue
            for i in range(idx):
                if line[i] in ordering[item]:
                    good = False
        if good:
            idx = int(len(line)/2)
            s += line[idx]
        else:
            # Save this for part 2
            bad_items.append(line)
    return s, bad_items


def cmp(x, y, ordering):
    x_before_y = y in ordering[x]
    y_before_x = x in ordering[y]
    if x_before_y and y_before_x:
        raise Exception("DEAR GOD!")
    elif x_before_y:
        return -1
    elif y_before_x:
        return 1
    else:
        return 0


def part2(data, ordering):
    s = 0
    for line in data:
        line = sorted(line, key=cmp_to_key(lambda x, y: cmp(x, y, ordering)))
        idx = int(len(line)/2)
        s += line[idx]
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1, bad_items = part1(data)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(bad_items, create_ordering(data[0]))
    print(f"Part 2 solution:\n{p2}")
