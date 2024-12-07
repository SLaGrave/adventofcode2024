def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    out = list()
    for line in data:
        item = []
        line = line.split(":")
        item.append(int(line[0].strip()))
        item.append([int(q) for q in line[1].strip().split(" ")])
        out.append(item)
    return out


def part1(data: list):
    s = 0
    for line in data:
        target = line[0]
        nums = line[1]
        for idx, value in enumerate(nums):
            if idx == 0:
                answers = [value]
                continue
            multed = [(q * value) for q in answers.copy()]
            added = [(q + value) for q in answers.copy()]
            answers = multed + added
        if target in answers:
            s += target
    return s


def part2(data: list):
    s = 0
    for line in data:
        target = line[0]
        nums = line[1]
        for idx, value in enumerate(nums):
            if idx == 0:
                answers = [value]
                continue
            multed = [(q * value) for q in answers.copy()]
            added = [(q + value) for q in answers.copy()]
            cated = [(int(f"{q}{value}")) for q in answers.copy()]
            answers = multed + added + cated
        if target in answers:
            s += target
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
