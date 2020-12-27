# Day 16, Part 1: Ticket Translation

def invalid_values(ticket):
    total = 0

    for field in ticket:
        valid = False

        for range_1, range_2 in ranges:
            if field in range_1 or field in range_2:
                valid = True
                break

        if not valid:
            total += field

    return total


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRPS = [grp.split("\n") for grp in INP.split("\n\n")]

    NAMES, RULES = list(zip(*(line.split(": ") for line in GRPS[0])))

    ranges = []
    for rule in RULES:
        rule_1, rule_2 = rule.split(" or ")
        rule_1 = [int(n) for n in rule_1.split("-")]
        rule_2 = [int(n) for n in rule_2.split("-")]

        ranges.append((range(rule_1[0], rule_1[1]+1),
                       range(rule_2[0], rule_2[1]+1)))

    nearby = [[int(n) for n in grp.split(",")] for grp in GRPS[2][1:]]
    total = sum(invalid_values(ticket) for ticket in nearby)
    print(total)
