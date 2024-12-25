def clean_data(data: list) -> list:
    locks = list()
    keys = list()
    data = [line.strip() for line in data]
    idx = 0
    while idx <= len(data):
        grid = data[idx:idx+7]
        key = grid[0][0] == "."
        layout = [0, 0, 0, 0, 0]
        for y in range(1, len(grid)-1):
            for x in range(len(grid[y])):
                if grid[y][x] == "#":
                    layout[x] += 1
        if key:
            keys.append(layout)
        else:
            locks.append(layout)    
        idx += 8
    return locks, keys


def invert_locks(locks):
    new_locks = list()
    for lock in locks:
        new = list()
        for col in lock:
            new.append(5-col)
        new_locks.append(new)
    return new_locks


def part1(locks, keys):
    s = 0
    locks = invert_locks(locks.copy())
    for lock in locks:
        for key in keys:
            fail = False
            for c in range(len(lock)):
                if key[c] > lock[c]:
                    fail = True
                    break
            if not fail:
                s += 1
    return s


def part2(locks, keys):
    s = 0
    for line in data:
        # do something
        ...
    
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    locks, keys = clean_data(data)
    print("Done parsing layouts")
    p1 = part1(locks, keys)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(locks, keys)
    print(f"Part 2 solution:\n{p2}")
