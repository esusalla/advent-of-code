# Day 25, Part 1: Combo Breaker


def crack(pubkey_1, pubkey_2):
    pubkeys = set([pubkey_1, pubkey_2])

    value = 1
    subject = 7

    loop_size = 0
    while True:
        if value in pubkeys:
            pubkeys.remove(value)
            break

        value *= subject
        value %= 20201227
        loop_size += 1

    return transform(next(iter(pubkeys)), loop_size)


def transform(subject, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= subject
        value %= 20201227

    return value


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        PUBKEY_1, PUBKEY_2 = (int(line) for line in INP.split("\n"))

    privkey = crack(PUBKEY_1, PUBKEY_2)
    print(privkey)
