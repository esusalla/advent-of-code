# Day 14, Part 1: Docking Data


def apply(mask, n):
    n = bin(n)[2:].zfill(36)
    n = "".join(b if a == "X" else a for a, b in zip(mask, n))
    return int(n, 2)


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        OPS = [line.split(" = ") for line in INP.split("\n")]

    mem = {}
    for left, right in OPS:
        if left == "mask":
            mask = right
        else:
            addr = int(left[4:-1])
            mem[addr] = apply(mask, int(right))

    total = sum(mem.values())
    print(total)
