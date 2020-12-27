# Day 1, Part 1: Report Repair

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        ENTRIES = {int(line) for line in INP.split("\n")}

    TARGET = 2020

    for entry in ENTRIES:
        if TARGET - entry in ENTRIES:
            print(entry * (TARGET-entry))
            break
