# Day 2, Part 2: Password Philosophy

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    LINES = [line.split(" ") for line in INP.split("\n")]

    valid = 0
    for line in LINES:
        low, high = (int(n) - 1 for n in line[0].split("-"))
        char = line[1][:-1]
        pwd = line[2]

        if (pwd[low] == char) ^ (pwd[high] == char):
            valid += 1

    print(valid)
