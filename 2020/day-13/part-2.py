# Day 13, Part 2: Shuttle Search

import math


# Extended GCD
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b//a) * x, x


# Inverse mod
def invmod(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError()
    else:
        return x % m


# Chinese remainder theorem solver
def crt(pairs):
    result = 0

    N = math.prod(n for _, n in pairs)
    for a, n in pairs:
        b = N // n
        result += a * b * invmod(b, n)

    return result % N


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    LINES = INP.split("\n")
    BUSES = [(i, int(bus))
             for i, bus in enumerate(LINES[1].split(","))
             if bus != "x"]

    pairs = [((bus-i) % bus, bus) for i, bus in BUSES]
    timestamp = crt(pairs)
    print(timestamp)
