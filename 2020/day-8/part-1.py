# Day 8, Part 1: Handheld Halting

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        OPS = [line.split(" ") for line in INP.split("\n")]

    pc = 0
    acc = 0
    seen = set()

    while pc not in seen:
        seen.add(pc)
        op = OPS[pc]

        if op[0] == "acc":
            acc += int(op[1])
            pc += 1
        elif op[0] == "jmp":
            pc += int(op[1])
        elif op[0] == "nop":
            pc += 1

    print(acc)
