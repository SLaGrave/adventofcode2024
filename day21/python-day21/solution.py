KEYPAD_TO_DIRS = {
    "A": {
        "A": "A",
        "0": "<A",
        "1": "^<<A",
        "2": "^<A",
        "3": "^A",
        "4": "^^<<A",
        "5": "^^<A",
        "6": "^^A",
        "7": "^^^<<A",
        "8": "^^^<A",
        "9": "^^^A",
    },
    "0": {
        "A": ">A",
        "0": "A",
        "1": "^<A",
        "2": "^A",
        "3": "^>A",
        "4": "^^<A",
        "5": "^^A",
        "6": "^^>A",
        "7": "^^^<A",
        "8": "^^^A",
        "9": "^^^>A",
    },
    "1": {
        "A": "v>>A",
        "0": "v>A",
        "1": "A",
        "2": ">A",
        "3": ">>A",
        "4": "^A",
        "5": "^>A",
        "6": "^>>A",
        "7": "^^A",
        "8": "^^>A",
        "9": "^^>>A",
    },
    "2": {
        "A": ">vA",
        "0": "vA",
        "1": "<A",
        "2": "A",
        "3": ">A",
        "4": "^<A",
        "5": "^A",
        "6": "^>A",
        "7": "^^<A",
        "8": "^^A",
        "9": "^^>A",
    },
    "3": {
        "A": "vA",
        "0": "<vA",
        "1": "<<A",
        "2": "<A",
        "3": "A",
        "4": "^<<A",
        "5": "^<A",
        "6": "^A",
        "7": "^^<<A",
        "8": "^^<A",
        "9": "^^A",
    },
    "4": {
        "A": "vv>>A",
        "0": "vv>A",
        "1": "vA",
        "2": "v>A",
        "3": "v>>A",
        "4": "A",
        "5": ">A",
        "6": ">>A",
        "7": "^A",
        "8": "^>A",
        "9": "^>>A",
    },
    "5": {
        "A": "vv>A",
        "0": "vvA",
        "1": "v<A",
        "2": "vA",
        "3": "v>A",
        "4": "<A",
        "5": "A",
        "6": ">A",
        "7": "^<A",
        "8": "^A",
        "9": "^>A",
    },
    "6": {
        "A": "vvA",
        "0": "vv<A",
        "1": "<<vA",
        "2": "<vA",
        "3": "vA",
        "4": "<<A",
        "5": "<A",
        "6": "A",
        "7": "^<<A",
        "8": "^<A",
        "9": "^A",
    },
    "7": {
        "A": "vvv>>A",
        "0": "vvv>A",
        "1": "vvA",
        "2": "vv>A",
        "3": "vv>>A",
        "4": "vA",
        "5": "v>A",
        "6": "v>>A",
        "7": "A",
        "8": ">A",
        "9": ">>A",
    },
    "8": {
        "A": "vvv>A",
        "0": "vvvA",
        "1": "<vvA",
        "2": "vvA",
        "3": "vv>A",
        "4": "v<A",
        "5": "vA",
        "6": "v>A",
        "7": "<A",
        "8": "A",
        "9": ">A",
    },
    "9": {
        "A": "vvvA",
        "0": "vvv<A",
        "1": "vv<<A",
        "2": "vv<A",
        "3": "vvA",
        "4": "v<<A",
        "5": "v<A",
        "6": "vA",
        "7": "<<A",
        "8": "<A",
        "9": "A",
    },
}

DIRS_TO_DIRS = {
    "A": {
        "A": "A",
        "^": "<A",
        "<": "v<<A",
        "v": "v<A",
        ">": "vA",
    },
    "^": {
        "A": ">A",
        "^": "A",
        "<": "v<A",
        "v": "vA",
        ">": ">vA",
    },
    "<": {
        "A": ">^>A",
        "^": ">^A",
        "<": "A",
        "v": ">A",
        ">": ">>A",
    },
    "v": {
        "A": ">^A",
        "^": "^A",
        "<": "<A",
        "v": "A",
        ">": ">A",
    },
    ">": {
        "A": "^A",
        "^": "^<A",
        "<": "<<A",
        "v": "<A",
        ">": "A",
    },
}


def clean_data(data: list) -> list:
    data = [[line.strip(), int(line.replace("A", ""))] for line in data]
    return data


def part1(data: list):
    # Apply first robot
    for idx in range(len(data)):
        code = data[idx][0]
        new_code = ""
        pointer = "A"
        for c in code:
            new_code += KEYPAD_TO_DIRS[pointer][c]
            pointer = c
        data[idx][0] = new_code
    # Apply second robot
    for idx in range(len(data)):
        code = data[idx][0]
        new_code = ""
        pointer = "A"
        for c in code:
            new_code += DIRS_TO_DIRS[pointer][c]
            pointer = c
        data[idx][0] = new_code
    # Apply third robot
    for idx in range(len(data)):
        code = data[idx][0]
        new_code = ""
        pointer = "A"
        for c in code:
            new_code += DIRS_TO_DIRS[pointer][c]
            pointer = c
        data[idx][0] = new_code
    s = 0
    for datum in data:
        print(len(datum[0]) , datum[1])
        s += len(datum[0]) * datum[1]
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
