# Day 6, Part 1: Custom Customs

import functools

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRPS = [[set(grp) for grp in lines.split("\n")]
                for lines in INP.split("\n\n")]

    total = sum(len(functools.reduce(set.__or__, grp)) for grp in GRPS)
    print(total)
