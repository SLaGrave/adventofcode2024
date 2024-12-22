def clean_data(data: list) -> list:
    data = [(line.strip(), int(line.replace("A", ""))) for line in data]
    return data


def part1(data: list):
    s = 0
    print(data)
    return s


def part2(data: list):
    s = 0
    for line in data:
        # do something
        ...
    
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
