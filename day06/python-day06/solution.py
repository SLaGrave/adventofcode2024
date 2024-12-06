from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


DIRECTION_MAP = {
    Direction.UP: [0, -1],
    Direction.DOWN: [0, 1],
    Direction.RIGHT: [1, 0],
    Direction.LEFT: [-1, 0],
}


def turn(dir):
    if dir == Direction.UP: return Direction.RIGHT
    elif dir == Direction.RIGHT: return Direction.DOWN
    elif dir == Direction.DOWN: return Direction.LEFT
    elif dir == Direction.LEFT: return Direction.UP


class AOCMap:
    def __init__(self, data):
        self.obstacles = list()
        self.position = None
        self.direction = None
        self.height = len(data)
        self.width = len(data[0])
        self.history = list()
        for y in range(self.height):
            for x in range(self.width):
                c = data[y][x]
                if c == "#":
                    self.obstacles.append([x, y])
                elif c == "^":
                    self.position = [x, y]
                    self.direction = Direction.UP
                elif c == "v":
                    self.position = [x, y]
                    self.direction = Direction.DOWN
                elif c == ">":
                    self.position = [x, y]
                    self.direction = Direction.RIGHT
                elif c == "<":
                    self.position = [x, y]
                    self.direction = Direction.LEFT

    def out_of_bounds(self, pos):
        x = pos[0]
        y = pos[1]
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def trace(self):
        self.history = list()
        while not self.out_of_bounds(self.position):
            if [*self.position, self.direction] in self.history:
                return None, None
            self.history.append([*self.position, self.direction])
            goal = [
                self.position[0] + DIRECTION_MAP[self.direction][0],
                self.position[1] + DIRECTION_MAP[self.direction][1]
            ]
            if goal in self.obstacles:
                self.direction = turn(self.direction)
            else:
                self.position = goal
        tmp = set()
        for item in self.history:
            tmp.add((item[0], item[1]))
        return len(tmp), tmp



def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    return data


def part1(data: AOCMap):
    return data.trace()[0]


def part2(data: list):
    s = 0
    base = AOCMap(data)
    route = base.trace()[1]
    for y in range(base.height):
        for x in range(base.width):
            print(" "*80, end="\r")
            print(f"Row {y}/{base.height}, Col {x}/{base.width}", end="\r")
            # If we've already got this space as an obstacle
            if [x, y] in base.obstacles: continue
            # If this space isn't in the route already
            if (x, y) not in route: continue
            new_map = AOCMap(data)
            new_map.obstacles.append([x, y])
            x = new_map.trace()[0]
            if x is None:
                s += 1
    return s


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.readlines()
    data = clean_data(data)
    p1_map = AOCMap(data)
    p1 = part1(p1_map)
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    print("NOTE: It's possible the following answer is one too large.")
    print("I didn't exclude the starting position from being a possible")
    print("obstacle location.")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
