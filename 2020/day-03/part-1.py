# Day 3, Part 1: Toboggan Trajectory

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    grid = INP.split("\n")

    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    x, y = 0, 0
    trees = 0

    while y < HEIGHT:
        width = WIDTH
        while x >= width:
            grid[y] *= 2
            width *= 2

        if grid[y][x] == "#":
            trees += 1

        x += 3
        y += 1

    print(trees)
