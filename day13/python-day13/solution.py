import sympy as sp
import math


def clean_data(data: list) -> list:
    data = [line.strip() for line in data]
    data = [[int(q) for q in k.split(" ")] for k in data]
    return data


def part1(data: list):
    s = 0
    for line in data:
        dxa, dya, dxb, dyb, tx, ty = line
        a_click = sp.Symbol('a_click')
        b_click = sp.Symbol('b_click')
        eq1 = sp.Eq((dxa*a_click)+(dxb*b_click), tx)
        eq2 = sp.Eq((dya*a_click)+(dyb*b_click), ty)
        ans = sp.solve([eq1, eq2], a_click, b_click)
        if ans[a_click] == int(ans[a_click]) and ans[b_click] == int(ans[b_click]):
            s += 3*int(ans[a_click]) + int(ans[b_click])
    return s


def part2(data: list):
    s = 0
    for line in data:
        dxa, dya, dxb, dyb, tx, ty = line
        tx += 10000000000000
        ty += 10000000000000
        a_click = sp.Symbol('a_click')
        b_click = sp.Symbol('b_click')
        eq1 = sp.Eq((dxa*a_click)+(dxb*b_click), tx)
        eq2 = sp.Eq((dya*a_click)+(dyb*b_click), ty)
        ans = sp.solve([eq1, eq2], a_click, b_click)
        if ans[a_click] == int(ans[a_click]) and ans[b_click] == int(ans[b_click]):
            s += 3*int(ans[a_click]) + int(ans[b_click])
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
