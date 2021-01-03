# Day 24, Part 1: Lobby Layout


def parse_line(line):
    tokens = []

    i = 0
    length = len(line)
    while i < length:
        if line[i] == "n" or line[i] == "s":
            tokens.append(line[i:i + 2])
            i += 2
        else:
            tokens.append(line[i])
            i += 1

    return tokens


def add(fst, snd):
    return (fst[0] + snd[0], fst[1] + snd[1])


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    LINES = [parse_line(line) for line in INP.split("\n")]
    DIRECTIONS = ["e", "w", "ne", "se", "nw", "sw"]
    OFFSETS = [(1, 0), (-1, 0), (1, -1), (0, 1), (0, -1), (-1, 1)]

    black = set()
    for line in LINES:
        tokens = parse_line(line)
        pos = (0, 0)

        for token in tokens:
            pos = add(pos, OFFSETS[DIRECTIONS.index(token)])

        if pos in black:
            black.remove(pos)
        else:
            black.add(pos)

    print(len(black))
