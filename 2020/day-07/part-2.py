# Day 7, Part 2: Handy Haversacks


def parse_line(line):
    line = line.split(" bags contain ")

    color = line[0]

    sub_bags = [sub_bag.split(" ") for sub_bag in line[1].split(", ")]
    sub_bags = {} if sub_bags[0][0] == "no" else {
        " ".join(sub_bag[1:3]): int(sub_bag[0])
        for sub_bag in sub_bags
    }

    return (color, sub_bags)


def count_sub_bags(bag, count):
    return sum(count_sub_bags(k, v * count) for k, v in BAGS[bag].items()) + count


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = INP.split("\n")

    BAGS = dict(parse_line(line) for line in LINES)

    count = count_sub_bags("shiny gold", 1) - 1
    print(count)
