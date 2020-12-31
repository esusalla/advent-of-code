# Day 17, Part 1: Conway Cubes

import collections

Cube = collections.namedtuple("Cube", "x y z")


def build_offsets():
    offsets = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                offsets.append(Cube(x, y, z))

    offsets.remove(Cube(0, 0, 0))
    return offsets


def add(fst, snd):
    return Cube(fst.x + snd.x, fst.y + snd.y, fst.z + snd.z)


def count_active(cube):
    return sum(1 for offset in OFFSETS if add(cube, offset) in active)


def expand(cubes):
    return {add(cube, offset) for cube in cubes for offset in OFFSETS}


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRID = INP.split("\n")

    OFFSETS = build_offsets()

    active = set()
    inactive = set()
    for y in range(len(GRID)):
        for x in range(len(GRID[0])):
            if GRID[y][x] == "#":
                active.add(Cube(x, y, 0))
            else:
                inactive.add(Cube(x, y, 0))

    for _ in range(6):
        expanded = expand(active)
        next_active = set()

        for cube in expanded:
            count = count_active(cube)

            if cube in active:
                if not (count == 2 or count == 3):
                    continue
                else:
                    next_active.add(cube)

            elif cube not in active and count == 3:
                next_active.add(cube)

        active = next_active

    print(len(active))
