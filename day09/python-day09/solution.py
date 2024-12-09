def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data[0]


def part1(data: list):
    s = 0
    idx = 0
    left_side = True
    left_slot = 0
    right_slot = int(len(data)/2)
    what = 0
    if len(data) % 2 == 0:
        data = data[0:len(data)-1]
    while len(data) > 0:
        if left_side:
            i = int(data[0])
            for _ in range(i):
                s += idx * left_slot
                idx += 1
            left_slot += 1
            left_side = False
            try:
                what = int(data[1])
                data = data[2:]
            except: return s
        else:
            for _ in range(what):
                i = int(data[len(data)-1])
                while i == 0:
                    data = data[:len(data)-2]
                    right_slot -= 1
                    try:
                        i = int(data[len(data)-1])
                    except: return s
                s += idx * right_slot
                idx += 1
                data = f"{data[:len(data)-1]}{int(i-1)}"
            left_side = True
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
    p1 = part1(data)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data)
    print(f"Part 2 solution:\n{p2}")
