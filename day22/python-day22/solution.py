from functools import cache


def clean_data(data: list) -> list:
    data = [int(line.strip()) for line in data]
    return data


@cache
def mix(secret, result):
    return secret ^ result


@cache
def prune(secret):
    return secret % 16777216


@cache
def evolve(secret):
    # Step 1
    result = secret * 64
    secret = mix(secret, result)
    secret = prune(secret)
    # Step 2
    result = int(secret / 32)
    secret = prune(mix(secret, result))
    # Step 3
    result = secret * 2048
    secret = prune(mix(secret, result))
    return secret


def part1(data: list):
    secrets = data.copy()
    for idx in range(len(data)):
        for _ in range(2000):
            secrets[idx] = evolve(secrets[idx])
    return sum(secrets)


def part2(data: list):
    s = 0
    for line in data:
        # do something
        ...
    
    return s


if __name__ == "__main__":
    # Tests
    assert mix(42, 15) == 37
    assert prune(100000000) == 16113920
    assert evolve(123) == 15887950
    assert evolve(evolve(123)) == 16495136

    # Logic
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
