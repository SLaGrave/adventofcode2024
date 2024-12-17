import math


def clean_data(data: list) -> list:
    data = [int(q) for q in data.strip().split(",")]
    return data


class Program:
    def __init__(self, a=44348299):
        self.a = a
        self.b = 0
        self.c = 0
        self.ic = 0
        self.output = []

    def literal(self, operand):
        return operand
    
    def combo(self, operand):
        return [0, 1, 2, 3, self.a, self.b, self.c, None][operand]
    
    def adv(self, operand):
        self.a = int((self.a)/(math.pow(2, self.combo(operand))))
        return True
    
    def bxl(self, operand):
        self.b = self.b ^ self.literal(operand)
        return True

    def bst(self, operand):
        self.b = self.combo(operand) % 8
        return True

    def jnz(self, operand):
        if self.a == 0:
            return True
        tmp = self.ic
        self.ic = self.literal(operand)
        return False
    
    def bxc(self, operand):
        self.b = self.b ^ self.c
        return True

    def out(self, operand):
        self.output.append(self.combo(operand)%8)
        return True
    
    def bdv(self, operand):
        self.b = int((self.a)/(math.pow(2, self.combo(operand))))
        return True
    
    def cdv(self, operand):
        self.c = int((self.a)/(math.pow(2, self.combo(operand))))
        return True

    def perform(self, opcode, operand):
        cmds = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]
        return cmds[opcode](operand)
    
    def run(self, program):
        while self.ic >= 0 and self.ic < len(program):
            inc = self.perform(program[self.ic], program[self.ic+1])
            if inc:
                self.ic += 2
        return self.output


def part1(data: list):
    p = Program()
    return p.run(data)


def part2(data: list):
    a = 0
    # while True:
    #     p = Program(a)
    #     x = p.run(data)
    #     if x == data:
    #         break
    #     a += 1
    return a


if __name__ == "__main__":
    with open("../input.txt", "r") as f:
        data = f.read()
    data = clean_data(data)
    p1 = part1(data.copy())
    print(f"Part 1 solution:\n{p1}")
    print("====================================")
    p2 = part2(data.copy())
    print(f"Part 2 solution:\n{p2}")
