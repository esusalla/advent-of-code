# Day 15, Part 2: Rambunctious Recitation

if __name__ == "__main__":
    last = {int(n): i for i, n in enumerate("0,3,1,6,7,5".split(","))}  # input

    TARGET = 30000000

    n = 0
    for i in range(len(last), TARGET - 1):
        if n in last:
            tmp = i - last[n]
            last[n] = i
            n = tmp
        else:
            last[n] = i
            n = 0

    print(n)
