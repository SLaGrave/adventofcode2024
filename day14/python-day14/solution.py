def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    new = list()
    for line in data:
        line = line.replace("p=", "")
        line = line.replace("v=", "")
        line = line.replace(",", " ")
        line = line.split()
        new.append([int(q) for q in line])
    return new


class Robot:
    def __init__(self, x, y, vx, vy, width, height):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height

    def move(self, times = 1):
        self.x += self.vx * times
        self.y += self.vy * times
        # Fix x
        if self.x < 0 or self.x > self.width:
            self.x = self.x % self.width
        # Fix y
        if self.y < 0 or self.y > self.height:
            self.y = self.y % self.height

    def in_quadrant(self):
        if self.x < int(self.width/2) and self.y < int(self.height/2):
            return 1
        elif self.x >= int(self.width/2)+1 and self.y < int(self.height/2):
            return 2
        elif self.x < int(self.width/2) and self.y >= int(self.height/2) + 1:
            return 3
        elif self.x >= int(self.width/2)+1 and self.y >= int(self.height/2)+1:
            return 4
        else:
            return 0


def part1(data: list):
    # Setup
    width = 101
    height = 103
    # width = 11
    # height = 7
    robots = list()
    for item in data:
        robots.append(Robot(*item, width, height))
    for robot in robots:
        robot.move(100)
    q = [0, 0, 0, 0, 0]
    for robot in robots:
        q[robot.in_quadrant()] += 1
    return q[1] * q[2] * q[3] * q[4]


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
