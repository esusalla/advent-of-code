# Day 9, Part 2: Encoding Error


def is_valid(i, n):
    for j, x in enumerate(NUMS[i - 25:i]):
        for y in NUMS[i - 25 + j:i]:
            if x + y == n:
                return True

    return False


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    NUMS = [int(line) for line in INP.split("\n")]
    NUMS_COUNT = len(NUMS)

    for i, n in enumerate(NUMS):
        if i < 25:
            continue

        if not is_valid(i, n):
            INVALID = n
            break

    for i, n in enumerate(NUMS):
        j = i
        total = 0
        ns = []

        while total < INVALID and j < NUMS_COUNT:
            total += NUMS[j]
            ns.append(NUMS[j])
            j += 1

        if total == INVALID:
            ns = sorted(ns)
            print(ns[0] + ns[-1])
            break
