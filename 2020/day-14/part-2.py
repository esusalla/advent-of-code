# Day 14, Part 2: Docking Data


def apply(mask, base):
    base = bin(base)[2:].zfill(36)
    base = "".join(
        a if b == "0"
        else "1" if b == "1"
        else "X" for a, b in zip(base, mask))
    return base


def get_addrs(base):
    if "X" in base:
        yield from get_addrs(base.replace("X", "0", 1))
        yield from get_addrs(base.replace("X", "1", 1))
    else:
        yield base


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    OPS = [line.split(" = ") for line in INP.split("\n")]

    mem = {}
    for left, right in OPS:
        if left == "mask":
            mask = right
        else:
            base = int(left[4:-1])
            base = apply(mask, base)

            for addr in get_addrs(base):
                mem[addr] = int(right)

    total = sum(mem.values())
    print(total)
