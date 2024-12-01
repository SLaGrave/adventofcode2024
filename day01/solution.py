def clean_data(data: list) -> list:
    # Out is the two vertical lists
    out = [[], []]
    data = [line.strip() for line in data]
    for line in data:
        x = line.split("   ")
        out[0].append(int(x[0]))
        out[1].append(int(x[1]))
    return out


def part1(data: list):
    # S is the running total
    s = 0
    # X is the left list, Y is the right list - both are sorted
    x = sorted(data[0])
    y = sorted(data[1])
    # For each index, add the distance to the running total
    for i in range(len(x)):
        s += abs(x[i] - y[i])
    return s


def part2(data: list):
    # S is the running total
    s = 0
    # X is the left list, Y is the right list - both are sorted
    x = sorted(data[0])
    y = sorted(data[1])
    # Scores is a dictionary of how many times each number (up to the highest value in the left list)
    # appears in the right list.
    # This is done naively
    scores = {}
    for i in range(max(x) + 1):
        scores[i] = 0
        for item in y:
            if item == i:
                scores[i] += 1
    # For each number in the left list, add to the running
    # total that value * it's "score"
    for item in x:
        s += item * scores[item]
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
