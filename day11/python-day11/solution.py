import functools
from collections import defaultdict


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = data[0]
    data = [int(q.strip()) for q in data.split(" ")]
    return data


@functools.cache
def logic(item) -> list:
    if item == 0:
        return [1]
    elif len(str(item))%2==0:
        halfway = len(str(item))/2
        halfway = int(halfway)
        first_half = str(item)[:halfway]
        second_half = str(item)[halfway:]
        return [int(first_half), int(second_half)]
    else:
        return [item*2024]


def part1(data: list):
    for _ in range(25):
        new = list()
        for item in data:
            new.extend(logic(item))
        data = new
    return len(data)


def part2(data: list):
    dd = defaultdict(int)
    for item in data:
        dd[item] += 1

    for _ in range(2024):
        new = defaultdict(int)
        for key, value in dd.items():
            answers = logic(key)
            for a in answers:
                new[a] += value
        dd = new
    
    return sum([value for _, value in dd.items()])


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
