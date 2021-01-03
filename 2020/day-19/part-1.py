# Day 19, Part 1: Monster Messages

import re


def parse_rule(rule, parsed_rules):
    key = rule[0][:-1]

    if key not in parsed_rules:
        if rule[-1] == '"a"' or rule[-1] == '"b"':
            parsed_rules[key] = rule[-1][1]
        else:
            parsed = []
            for other in rule[1:]:
                if other == "|":
                    parsed.append(other)
                elif other not in parsed_rules:
                    parsed.append(parse_rule(RULES[other], parsed_rules))
                else:
                    parsed.append(parsed_rules[other])
            parsed_rules[key] = "(" + "".join(parsed) + ")"

    return parsed_rules[key]


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    GRPS = [grp.split("\n") for grp in INP.split("\n\n")]
    RULES = {rule[0][:-1]: rule for rule in (grp.split(" ") for grp in GRPS[0])}
    MSGS = GRPS[1]

    parsed_rules = {}
    for rule in RULES.values():
        parse_rule(rule, parsed_rules)

    regex = re.compile("".join(parsed_rules["0"]) + "$")
    count = sum(1 for msg in MSGS if regex.match(msg))
    print(count)
