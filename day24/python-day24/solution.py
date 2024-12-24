WIRES = dict()


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    # Get starting wires
    while data:
        item = data.pop(0)
        if item == "":
            break
        item = item.split(": ")
        WIRES[item[0]] = item[1]=="1"
    # Get gates
    gates = list()
    for item in data:
        item = item.replace(" -> ", " ")
        item = item.split(" ")
        if item[1] == "XOR":
            item[1] = lambda x, y: x ^ y
        elif item[1] == "AND":
            item[1] = lambda x, y: x & y
        elif item[1] == "OR":
            item[1] = lambda x, y: x | y
        else:
            raise Exception("OH NO")
        gates.append(item)
    return gates


def part1(data: list):
    # Run all gates
    while data:
        gate = data.pop(0)
        in1, func, in2, out = gate
        try:
            WIRES[out] = func(WIRES[in1], WIRES[in2])
        except:
            data.append(gate)
    # Get z wires
    zs = list()
    for wire in WIRES.keys():
        if wire.startswith("z"):
            zs.append(wire)
    zs = reversed(sorted(zs))
    # Construct s
    s = ""
    for z in zs:
        s += "1" if WIRES[z] else "0"
    return int(s, 2)


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
