def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data


def get_at(x, y, data):
    if y >= len(data) or x >= len(data[y]) or y < 0 or x < 0:
        return ""
    return data[y][x]


directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
]

dir2 = [
    [-1, -1],
    [1, -1],
    [1, 1],
    [-1, 1],
]


def part1(data: list):
    s = 0
    testing = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if get_at(x, y, data) == "X":
                for dir in directions:
                    my = [[x, y]]
                    tmp = "X"
                    for i in range(3):
                        i += 1
                        tmp += get_at(x+(dir[0]*i), y+(dir[1]*i), data)
                        my.append([x+(dir[0]*i), y+(dir[1]*i)])
                    if tmp == "XMAS":
                        testing += my
                        s += 1
    # for y in range(len(data)):
    #     line = ""
    #     for x in range(len(data[y])):
    #         if [x, y] in testing:
    #             line += get_at(x, y, data)
    #         else:
    #             line += "."
    #     print(line)
    return s


def part2(data: list):
    s = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if get_at(x, y, data) == "A":
                tmp = ""
                for dir in dir2:
                    tmp += get_at(x+dir[0], y+dir[1], data)
                if tmp in ["MMSS", "SMMS", "SSMM", "MSSM"]:
                    s += 1
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
