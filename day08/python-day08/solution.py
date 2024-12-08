def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data


def legal_point(x, y, data):
    return x >= 0 and x < len(data[0]) and y >= 0 and y < len(data)


def part1(data: list):
    antipoints = set()
    antennas = dict()
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            if c != ".":
                if c not in antennas.keys():
                    antennas[c] = list()
                antennas[c].append([x, y])
    for _freq, ants in antennas.items():
        for i in range(len(ants)):
            for j in range(len(ants)):
                if i==j: continue
                xdiff = ants[i][0] - ants[j][0]
                ydiff = ants[i][1] - ants[j][1]
                if legal_point(ants[i][0] + xdiff, ants[i][1] + ydiff, data):
                    antipoints.add((ants[i][0] + xdiff, ants[i][1] + ydiff))
    return len(antipoints)



def part2(data: list):
    """Basically exactly the same as part one, excepts I
    continually apply the x/ydiff 0, 1, 2, 3... times until
    the point would be off the grid."""
    antipoints = set()
    antennas = dict()
    for y in range(len(data)):
        for x in range(len(data[y])):
            c = data[y][x]
            if c != ".":
                if c not in antennas.keys():
                    antennas[c] = list()
                antennas[c].append([x, y])
    for _freq, ants in antennas.items():
        for i in range(len(ants)):
            for j in range(len(ants)):
                if i==j: continue
                xdiff = ants[i][0] - ants[j][0]
                ydiff = ants[i][1] - ants[j][1]
                idx = 0
                while legal_point(ants[i][0] + (xdiff*idx), ants[i][1] + (ydiff*idx), data):
                    antipoints.add((ants[i][0] + (xdiff*idx), ants[i][1] + (ydiff*idx)))
                    idx += 1
    return len(antipoints)


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
