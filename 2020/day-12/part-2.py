# Day 12, Part 2: Rain Risk

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        ACTIONS = [(line[0], int(line[1:])) for line in INP.split("\n")]

    pos = (0, 0)
    way = (10, -1)

    for action, value in ACTIONS:
        if action == "N":
            way = (way[0], way[1] - value)

        elif action == "S":
            way = (way[0], way[1] + value)

        elif action == "E":
            way = (way[0] + value, way[1])

        elif action == "W":
            way = (way[0] - value, way[1])

        elif action == "L":
            for _ in range(value // 90):
                way = (way[1], -way[0])

        elif action == "R":
            for _ in range(value // 90):
                way = (-way[1], way[0])

        elif action == "F":
            pos = (pos[0] + way[0] * value, pos[1] + way[1] * value)

    md = abs(pos[0]) + abs(pos[1])
    print(md)
