def clean_data(data: list) -> list:
    data = [list(line.strip()) for line in data]
    return data


DIRS = {
    "^": [0, -1],
    "v": [0, 1],
    "<": [-1, 0],
    ">": [1, 0],
}


def can_move(x, y, d, map):
    goal_x, goal_y = x+d[0], y+d[1]
    if map[goal_y][goal_x] == ".":
        return True, None
    if map[goal_y][goal_x] == "#":
        return False, None
    swap_x, swap_y = goal_x, goal_y
    while map[swap_y][swap_x] == "O":
        swap_x += d[0]
        swap_y += d[1]
    if map[swap_y][swap_x] == ".":
        return True, [swap_x, swap_y]
    elif map[swap_y][swap_x] == "#":
        return False, None


def move(x, y, d, map, swap):
    goal_x, goal_y = x+d[0], y+d[1]
    if swap is not None:
        tmp = map[goal_y][goal_x]
        map[goal_y][goal_x] = map[swap[1]][swap[0]]
        map[swap[1]][swap[0]] = tmp
    map[y][x] = "."
    map[goal_y][goal_x] = "@"


def get_pos(map):
    # Get position of robot
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "@":
                pos = [x, y]
    return pos


def part1(map, dirs):
    s = 0
    x, y = get_pos(map)
    for c in dirs:
        d = DIRS[c]
        can, swap = can_move(x, y, d, map)
        if not can:
            continue
        move(x, y, d, map, swap)
        x, y = get_pos(map)
    # Get GPS Scores
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "O":
                s += 100*y + x
    return s


def part2(data, dirs):
    s = 0
    for line in data:
        # do something
        ...
    
    return s


if __name__ == "__main__":
    with open("../input1.txt", "r") as f:
        data = f.readlines()
    with open("../input2.txt", "r") as f:
        dirs = f.read()
        dirs = dirs.strip()
        dirs = dirs.replace("\n", "")
    map = clean_data(data)
    p1 = part1(map.copy(), dirs)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(map.copy(), dirs)
    print(f"Part 2 solution:\n{p2}")

