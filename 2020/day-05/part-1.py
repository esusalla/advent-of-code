# Day 5, Part 1: Binary Boarding


def calc_seat_id(bp):
    low = 0
    high = 127
    for c in bp[:7]:
        if c == "F":
            high -= ((high-low) // 2) + 1
        elif c == "B":
            low += ((high-low) // 2) + 1

    row = low

    low = 0
    high = 7
    for c in bp[7:]:
        if c == "L":
            high -= ((high-low) // 2) + 1
        elif c == "R":
            low += ((high-low) // 2) + 1

    col = low

    return row*8 + col


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    seat_id = max(calc_seat_id(bp) for bp in INP.split("\n"))
    print(seat_id)
