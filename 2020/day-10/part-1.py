# Day 10, Part 1: Adapter Array

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        PLUGS = [int(line) for line in INP.split("\n")]

    array = [0] + sorted(PLUGS) + [max(PLUGS) + 3]
    diffs = [b - a for a, b in zip(array, array[1:])]
    prod = diffs.count(1) * diffs.count(3)
    print(prod)
