# Day 13, Part 1: Shuttle Search

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = INP.split("\n")

    TIMESTAMP = int(LINES[0])
    BUSES = [int(bus) for bus in LINES[1].split(",") if bus != "x"]

    pairs = [(bus, bus - (TIMESTAMP % bus)) for bus in BUSES]
    best = min(pairs, key=lambda pair: pair[1])

    print(best[0] * best[1])
