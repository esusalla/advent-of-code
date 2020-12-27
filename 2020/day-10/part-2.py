# Day 10, Part 2: Adapter Array

import itertools
import math

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        PLUGS = [int(line) for line in INP.split("\n")]

    # Generate plug array
    arr = [0] + sorted(PLUGS) + [max(PLUGS) + 3]

    # Determine indexes of removable plugs
    rmv = [i for i, n in enumerate(arr[1:-1]) if arr[i + 2] - arr[i] <= 3]

    # Get length of consecutive indexes (e.g., 4,5,6,8 -> 3, 8,9,10,11,13 -> 4)
    lens = [len(list(g)) for _, g in
            itertools.groupby(enumerate(rmv), lambda p: p[0] - p[1])]

    # Rather than normal increase by factor of 2 for every removable plug,
    # groups of 3 only increase total factor by 7 rather than 8 (2**3)
    # because one combination of plugs in each triplet is invalid due to
    # the fact that a plug can only connect to another one within 3 levels
    count = math.prod(7**(n // 3) * 2**(n % 3) for n in lens)
    print(count)
