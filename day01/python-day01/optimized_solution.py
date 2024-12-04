from collections import Counter


def clean_data(data: list) -> list[list]:
    data = [line.strip() for line in data]
    left = list()
    right = list()
    for line in data:
        x = line.split("   ")
        left.append(int(x[0]))
        right.append(int(x[1]))
    return left, right


def part1(left, right) -> int:
    # S is the running total
    s = 0
    # Sort both lists
    left = sorted(left)
    right = sorted(right)
    # For each index, add the distance to the running total
    for i in range(len(left)):
        s += abs(left[i] - right[i])
    return s


def part2(left, right) -> int:
    # S is the running total
    s = 0
    # This counts how many time each values appears in the right
    # list. It will return 0 for keys which don't appear.
    c = Counter(right)
    # For each number in the left list, add to the running
    # total that value * it's appearances in the right.
    for item in left:
        s += item * c[item]
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    left, right = clean_data(data)
    p1 = part1(left.copy(), right.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(left.copy(), right.copy())
    print(f"Part 2 solution:\n{p2}")
