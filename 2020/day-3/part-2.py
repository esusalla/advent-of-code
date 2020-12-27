# Day 3, Part 2: Toboggan Trajectory

import math


def count_trees(u, v, grid):
    x, y = 0, 0
    trees = 0

    while y < HEIGHT:
        while x >= len(grid[y]):
            grid[y] *= 2

        if grid[y][x] == "#":
            trees += 1

        x += u
        y += v

    return trees


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        grid = INP.split("\n")

    HEIGHT = len(grid)
    SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    trees = math.prod(count_trees(u, v, grid) for u, v in SLOPES)
    print(trees)
