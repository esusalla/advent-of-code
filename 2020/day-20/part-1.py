# Day 20, Part 1: Jurassic Jigsaw

import collections
import math

Pos = collections.namedtuple("Pos", "x y")
Tile = collections.namedtuple("Tile", "nid rows")
PlacedTile = collections.namedtuple("Tile", "rows pos")


def add(fst, snd):
    return Pos(fst.x + snd.x, fst.y + snd.y)


def flip(rows):
    return list(reversed(rows))


def rotate(rows):
    return list(zip(*reversed(rows)))


def left(rows):
    return [row[0] for row in rows]


def right(rows):
    return [row[-1] for row in rows]


def top(rows):
    return rows[0]


def bottom(rows):
    return rows[-1]


# Compare one tile's edges to another's including each possible flip and rotation
def find_match(tile, placed_tile, placed):
    rows = tile.rows

    for _ in range(2):  # flips
        for _ in range(4):  # rotations
            for (edge_1, edge_2), offset in MATCHES:
                if (edge_1(rows) == edge_2(placed_tile.rows)):
                    placed[tile.nid] = PlacedTile(
                        rows, add(placed_tile.pos, offset))
                    return True
            rows = rotate(rows)
        rows = flip(rows)

    return False


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRPS = [grp.split("\n") for grp in INP.split("\n\n")]
        TILES = [Tile(int(grp[0].split(" ")[-1][:-1]), grp[1:])
                 for grp in GRPS]

    # Possible ways for two tiles to match and the appropriate offset for placement
    MATCHES = [((left, right), Pos(1, 0)), ((right, left), Pos(-1, 0)),
               ((top, bottom), Pos(0, 1)), ((bottom, top), Pos(0, -1))]

    # Place the first tile in the list and use it as a starting point to place others
    placed = {TILES[0].nid: PlacedTile(TILES[0].rows, Pos(0, 0))}

    # Continually iterate through tiles until all are placed
    while not all(tile.nid in placed for tile in TILES):
        for tile in TILES:
            if tile.nid in placed:
                continue

            for placed_tile in placed.values():
                if find_match(tile, placed_tile, placed):
                    break

    # Find the corners of the placed tiles and multiply their numeric IDs together
    min_x = min(x for _, (x, _) in placed.values())
    max_x = max(x for _, (x, _) in placed.values())
    min_y = min(y for _, (_, y) in placed.values())
    max_y = max(y for _, (_, y) in placed.values())
    corners = [Pos(min_x, min_y), Pos(max_x, min_y),
               Pos(max_x, max_y), Pos(min_x, max_y)]

    prod = math.prod(nid for nid, placed_tile in placed.items()
                     if placed_tile.pos in corners)
    print(prod)
