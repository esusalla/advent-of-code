# Day 24, Part 2: Lobby Layout


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


def count_adjs(pos):
    count = 0
    for vec in OFFSETS:
        if add(pos, vec) in black:
            count += 1

    return count


# All newly encountered tiles start as white
def expand(black, white):
    to_add = set()

    for pos in black:
        for vec in OFFSETS:
            adj = add(pos, vec)
            if adj not in black and adj not in white:
                to_add.add(adj)

    for pos in white:
        for vec in OFFSETS:
            adj = add(pos, vec)
            if adj not in black and adj not in white:
                to_add.add(adj)

    white.update(to_add)


def generate_lobby(black, white):
    for line in LINES:
        tokens = parse_line(line)
        pos = (0, 0)

        for token in tokens:
            pos = add(pos, OFFSETS[DIRECTIONS.index(token)])

        if pos in black:
            black.remove(pos)
            white.add(pos)
        else:
            white.discard(pos)
            black.add(pos)


def advance(black, white):
    expand(black, white)

    to_add_black = set()
    to_add_white = set()

    for pos in black:
        count = count_adjs(pos)
        if count == 0 or count > 2:
            to_add_white.add(pos)

    for pos in white:
        count = count_adjs(pos)
        if count == 2:
            to_add_black.add(pos)

    black.difference_update(to_add_white)
    black.update(to_add_black)

    white.difference_update(to_add_black)
    white.update(to_add_white)


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = [parse_line(line) for line in INP.split("\n")]

    DIRECTIONS = ["e", "w", "ne", "se", "nw", "sw"]
    OFFSETS = [(1, 0), (-1, 0), (1, -1), (0, 1), (0, -1), (-1, 1)]

    black = set()
    white = set()

    generate_lobby(black, white)

    for _ in range(100):
        advance(black, white)

    print(len(black))
