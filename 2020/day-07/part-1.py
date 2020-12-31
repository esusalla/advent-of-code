# Day 7, Part 1: Hand Haversacks


def parse_line(line):
    color = line[0]

    sub_bags_list = [sub_bag.split(" ") for sub_bag in line[1].split(", ")]
    if sub_bags_list[0][0] == "no":
        sub_bags = {}
    else:
        sub_bags = {" ".join(bag[1:3]): int(bag[0]) for bag in sub_bags_list}

    return (color, sub_bags)


def check_sub_bags(bag):
    if "shiny gold" in BAGS[bag]:
        return True
    else:
        return any(check_sub_bags(sub) for sub in BAGS[bag])


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = [line.split(" bags contain ") for line in INP.split("\n")]

    BAGS = dict(parse_line(line) for line in LINES)

    count = sum(1 for bag in BAGS if check_sub_bags(bag))
    print(count)
