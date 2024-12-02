def clean_data(data: list) -> list:
    data = [line.strip() for line in data]

    return data


def part1(data: list):
    s = 0
    for line in data:
        report = line.split(" ")
        report = [int(q) for q in report]
        good = True
        if not (
            sorted(report) == report
            or list(reversed(sorted(report))) == report
        ):
            good = False
        if not (len(set(report)) == len(report)):
            good = False
        for i in range(len(report)-1):
            x = int(report[i])
            y = int(report[i+1])
            if not (abs(x-y) <= 3):
                good = False
                break
        if good: s += 1
    return s


def part2(data: list):
    s = 0
    for line in data:
        # do something
        ...
    
    return s


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
