# Day 8, Part 2: Handheld Halting

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    OPS = [line.split(" ") for line in INP.split("\n")]
    OPS_COUNT = len(OPS)

    # Get all JMP and NOP instructions in order to check output when switched
    for i in (i for i, op in enumerate(OPS) if op[0] == "jmp" or op[0] == "nop"):
        pc = 0
        acc = 0
        seen = set()

        while pc not in seen and pc < OPS_COUNT:
            seen.add(pc)
            op = OPS[pc]

            # Replace JMP with NOP and vice versa
            if pc == i:
                if op[0] == "jmp":
                    pc += 1
                elif op[0] == "nop":
                    pc += int(op[1])

            else:
                if op[0] == "acc":
                    acc += int(op[1])
                    pc += 1
                elif op[0] == "jmp":
                    pc += int(op[1])
                elif op[0] == "nop":
                    pc += 1

        if pc == OPS_COUNT:
            print(acc)
            break
