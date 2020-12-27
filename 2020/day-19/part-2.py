# Day 19, Part 2: Monster Messages

import re


def parse_rule(rule, parsed_rules):
    key = rule[0][:-1]

    if key not in parsed_rules:
        if rule[-1] == '"a"' or rule[-1] == '"b"':
            parsed_rules[key] = rule[-1][1]
        else:
            parsed = ""
            for other in rule[1:]:
                if other == "|":
                    parsed += other
                elif other not in parsed_rules:
                    parsed += parse_rule(RULES[other], parsed_rules)
                else:
                    parsed += parsed_rules[other]

            if key == "8":
                parsed_rules[key] = "(" + parsed + ")+"
            elif key == "11":
                fst = "(" + parsed_rules["42"] + "){n}"
                snd = "(" + parsed_rules["31"] + "){n}"
                parsed_rules[key] = fst + snd
            else:
                parsed_rules[key] = "(" + parsed + ")"

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

    exp = "".join(parsed_rules["0"]) + "$"
    regexs = [re.compile(exp.replace("n", str(n))) for n in range(1, 5)]
    count = sum(1 for msg in MSGS if any(regex.match(msg) for regex in regexs))
    print(count)
