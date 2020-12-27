# Day 7, Part 1: Hand Haversacks


def parse_line(line):
    line = line.split(" bags contain ")

    color = line[0]

    sub_bags = [sub_bag.split(" ") for sub_bag in line[1].split(", ")]
    sub_bags = {} if sub_bags[0][0] == "no" else {
        " ".join(sub_bag[1:3]): int(sub_bag[0])
        for sub_bag in sub_bags
    }

    return (color, sub_bags)


def check_sub_bags(bag):
    if "shiny gold" in BAGS[bag]:
        return True
    else:
        return any(check_sub_bags(sub) for sub in BAGS[bag])


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = INP.split("\n")

    BAGS = dict(parse_line(line) for line in LINES)

    count = sum(1 for bag in BAGS if check_sub_bags(bag))
    print(count)
