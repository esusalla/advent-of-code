# Day 11, Part 2: Seating System


def count_occupied(x, y):
    count = 0

    for u, v in OFFSETS:
        a = u
        b = v

        while HEIGHT > y + b >= 0 and WIDTH > x + a >= 0 and seats[y + b][x + a] == ".":
            a += u
            b += v

        if HEIGHT > y + b >= 0 and WIDTH > x + a >= 0 and seats[y + b][x + a] == "#":
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
                elif seat == "#" and count >= 5:
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
