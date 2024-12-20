def rec(design, patterns, attempt=0):
    print(f"Length: {len(design)}")
    if design[0] not in patterns.keys():
        return False
    for p in patterns[design[0]]:
        attempt += 1
        if design == p:
            return True
        if design.startswith(p):
            if rec(design[len(p):], patterns, attempt):
                return True
    return False


if __name__ == "__main__":
    with open("../input1.txt", "r") as f:
        data = f.readlines()
        tmp = [q.strip() for q in data[0].split(",")]
        patterns = dict()
        for p in tmp:
            if p[0] not in patterns.keys():
                patterns[p[0]] = [p]
            else:
                patterns[p[0]].append(p)
    with open("../input2.txt", "r") as f:
        data = f.readlines()
        designs = [q.strip() for q in data]

    # Part 1
    s = 0
    for idx, d in enumerate(designs):
        print(f"Design {idx}/{len(designs)} ({int(idx/len(designs)**100)}%)", end="\r")
        if rec(d, patterns):
            s += 1
    print(f"\nPart 1: {s}")