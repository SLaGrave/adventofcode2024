from functools import cache


PATTERNS = dict()


@cache
def rec(design):
    global PATTERNS
    if design[0] not in PATTERNS.keys():
        return False
    for p in PATTERNS[design[0]]:
        if design == p:
            return True
        if design.startswith(p):
            if rec(design[len(p):]):
                return True
    return False


if __name__ == "__main__":
    with open("../input1.txt", "r") as f:
        data = f.readlines()
        tmp = [q.strip() for q in data[0].split(",")]
        for p in tmp:
            if p[0] not in PATTERNS.keys():
                PATTERNS[p[0]] = [p]
            else:
                PATTERNS[p[0]].append(p)
    with open("../input2.txt", "r") as f:
        data = f.readlines()
        designs = [q.strip() for q in data]

    # Part 1
    s = 0
    for idx, d in enumerate(designs):
        print(f"Design {idx}/{len(designs)} ({int(idx/len(designs)**100)}%)", end="\r")
        if rec(d):
            s += 1
    print(f"Part 1: {s}{' '*20}")