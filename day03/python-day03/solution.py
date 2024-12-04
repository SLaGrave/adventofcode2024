import re


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]

    return data


def part1(data: list):
    s = 0
    pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)", re.IGNORECASE)
    for line in data:
        for mul in pattern.findall(line):
            mul = mul.replace("mul(", "")
            mul = mul.replace(")", "")
            mul = [int(q) for q in mul.split(',')]
            s += mul[0] * mul[1]
    return s


def part2(data: list):
    s = 0
    enabled = True
    for line in data:
        for cmd in re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line):
            if cmd == "do()":
                enabled = True
            elif cmd == "don't()":
                enabled = False
            else:
                if not enabled: continue
                mul = cmd.replace("mul(", "")
                mul = mul.replace(")", "")
                mul = [int(q) for q in mul.split(',')]
                s += mul[0] * mul[1]
    
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
