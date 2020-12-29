# Day 4, Part 1: Passport Processing


def is_valid(passport):
    fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False
    }

    for field in passport:
        fields[field] = True

    return all(fields.values())


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRPS = [grp.replace("\n", " ").split(" ")
                for grp in INP.split("\n\n")]

    PASSPORTS = [dict(field.split(":") for field in grp)
                 for grp in GRPS]

    valid = sum(1 for passport in PASSPORTS if is_valid(passport))
    print(valid)
