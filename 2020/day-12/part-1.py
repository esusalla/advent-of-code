# Day 12, Part 1: Rain Risk

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        ACTIONS = [(line[0], int(line[1:])) for line in INP.split("\n")]

    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # east, south, west, north

    pos = (0, 0)
    facing = (1, 0)

    for action, value in ACTIONS:
        if action == "N":
            pos = (pos[0], pos[1] - value)

        elif action == "S":
            pos = (pos[0], pos[1] + value)

        elif action == "E":
            pos = (pos[0] + value, pos[1])

        elif action == "W":
            pos = (pos[0] - value, pos[1])

        elif action == "L":
            idx = (DIRECTIONS.index(facing) - value//90) % len(DIRECTIONS)
            facing = DIRECTIONS[idx]

        elif action == "R":
            idx = (DIRECTIONS.index(facing) + value//90) % len(DIRECTIONS)
            facing = DIRECTIONS[idx]

        elif action == "F":
            pos = (pos[0] + facing[0] * value, pos[1] + facing[1] * value)

    md = abs(pos[0]) + abs(pos[1])
    print(md)
