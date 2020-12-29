# Day 9, Part 1: Encoding Error


def valid(i, n):
    for j, x in enumerate(NUMS[i - 25:i]):
        for y in NUMS[i - 25 + j:i]:
            if x + y == n:
                return True

    return False


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        NUMS = [int(line) for line in INP.split("\n")]

    for i, n in enumerate(NUMS):
        if i < 25:
            continue

        if not valid(i, n):
            print(n)
            break
