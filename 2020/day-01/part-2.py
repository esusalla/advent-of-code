# Day 1, Part 2: Report Repair

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    ENTRIES = {int(line) for line in INP.split("\n")}
    ENTRIES_LIST = list(ENTRIES)

    TARGET = 2020

    for i, entry_1 in enumerate(ENTRIES_LIST):
        for entry_2 in ENTRIES_LIST[i + 1:]:
            if TARGET - (entry_1+entry_2) in ENTRIES:
                print(entry_1 * entry_2 * (TARGET - (entry_1+entry_2)))
                exit()
