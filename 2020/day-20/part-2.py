# Day 20, Part 2: Jurassic Jigsaw

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


def remove_edges(rows):
    return [row[1:-1] for row in rows[1:-1]]


def build_image(placed_tiles):
    width = math.isqrt(len(placed_tiles))

    # Sort all tiles and remove their edges
    # Invert x and y in position when sorting to account for grid[y][x] indexing
    tiles = sorted(placed_tiles, key=lambda tile: (tile.pos.y, tile.pos.x))
    tiles = [remove_edges(rows) for rows, _ in tiles]

    # Square consists of 12x12 grid of tiles
    square = [tiles[i:i + width] for i in range(0, len(tiles), width)]

    img = []
    height = len(square[0][0])
    # Iterate through each row in square and join together rows of each tile
    for row in square:
        for i in range(height):
            img_row = []
            for tile in row:
                img_row += tile[i]
            img.append("".join(img_row))

    return img


def in_bounds(pos):
    return pos.y < IMG_HEIGHT and pos.x < IMG_WIDTH


# Calculate offsets from any one node to determine if surrounding nodes contain sea monster
def calc_offsets(sea_monster):
    sea_monster_offsets = []

    for y, row in enumerate(sea_monster.split('\n')):
        for x, c in enumerate(row):
            if c == "#":
                sea_monster_offsets.append(Pos(x, y))

    return sea_monster_offsets


# Check if every offset postion is in bounds and a "#" and then add all to set if so
def check_sea_monster(img, offsets):
    in_sea_monster = set()

    for _ in range(2):  # flips
        for _ in range(4):  # rotations
            for y, row in enumerate(img):
                for x in range(len(row)):
                    pairs = [add(Pos(x, y), offset) for offset in offsets]
                    if all(in_bounds(pair) and img[pair.y][pair.x] == "#" for pair in pairs):
                        in_sea_monster.update(pairs)

            if in_sea_monster:
                return in_sea_monster

            img = rotate(img)
        img = flip(img)


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

    # Stitch together the tiles into an image
    img = build_image(placed.values())
    IMG_HEIGHT = len(img)
    IMG_WIDTH = len(img[0])

    # Identify offsets for sea monster checking
    SEA_MONSTER = "                  #\n#    ##    ##    ###\n #  #  #  #  #  #"
    offsets = calc_offsets(SEA_MONSTER)

    # Detect which "#" in the image are part of a sea monster and flip / rotate the image if needed
    in_sea_monster = check_sea_monster(img, offsets)

    # Get the difference between the total number of "#" and those that are part of a sea monster
    total = sum(sum(1 for c in row if c == "#") for row in img)
    diff = total - len(in_sea_monster)
    print(diff)
