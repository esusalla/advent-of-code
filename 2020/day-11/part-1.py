# Day 11, Part 1: Seating System


def count_occupied(x, y):
    count = 0

    for u, v in OFFSETS:
        if HEIGHT > y + v >= 0 and WIDTH > x + u >= 0:
            if seats[y + v][x + u] == "#":
                count += 1

    return count


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        seats = [list(line) for line in INP.split("\n")]

    OFFSETS = [(1, 0), (1, 1), (0, 1), (-1, 1),
               (-1, 0), (-1, -1), (0, -1), (1, -1)]
    HEIGHT = len(seats)
    WIDTH = len(seats[0])

    while True:
        occupied = set()
        empty = set()

        for y, row in enumerate(seats):
            for x, seat in enumerate(row):
                count = count_occupied(x, y)

                if seat == "L" and count == 0:
                    occupied.add((x, y))
                elif seat == "#" and count >= 4:
                    empty.add((x, y))

        # Seats have stopped changing
        if not occupied and not empty:
            break

        for x, y in occupied:
            seats[y][x] = "#"
        for x, y in empty:
            seats[y][x] = "L"

    count = sum(sum(1 for seat in row if seat == "#") for row in seats)
    print(count)
