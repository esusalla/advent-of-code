# Day 16, Part 2: Ticket Translation

import math


def is_valid(ticket):
    for field in ticket:
        valid = False

        for range_1, range_2 in ranges:
            if field in range_1 or field in range_2:
                valid = True
                break

        if not valid:
            return False

    return True


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
    valid = [ticket for ticket in nearby if is_valid(ticket)]
    mine = [int(n) for n in GRPS[1][-1].split(",")]

    possible = {n: set() for n in range(20)}

    for field_idx in range(len(mine)):
        for i, (range_1, range_2) in enumerate(ranges):
            if all(ticket[field_idx] in range_1 or ticket[field_idx] in range_2 for ticket in valid):
                possible[field_idx].add(i)

    field_to_name = {n: "" for n in range(len(NAMES))}
    while any(len(v) == 1 for v in possible.values()):
        for k, v in possible.items():
            if len(v) == 1:
                i = next(iter(v))
                field_to_name[k] = NAMES[i]
                for v in possible.values():
                    if i in v:
                        v.remove(i)

    solution = math.prod(
        mine[k]
        for k, v in field_to_name.items()
        if v.startswith("departure")
    )
    print(solution)
