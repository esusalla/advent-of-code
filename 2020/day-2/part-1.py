# Day 2, Part 1: Password Philosophy

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = [line.split(" ") for line in INP.split("\n")]

    valid = 0
    for line in LINES:
        low, high = (int(n) for n in line[0].split("-"))
        char = line[1][:-1]
        pwd = line[2]

        if low <= pwd.count(char) <= high:
            valid += 1

    print(valid)
