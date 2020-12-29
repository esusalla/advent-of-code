# Day 4, Part 2: Passport Processing

import string


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

    for field, value in passport.items():
        if field == "byr" and not (1920 <= int(value) <= 2002):
            return False

        elif field == "iyr" and not (2010 <= int(value) <= 2020):
            return False

        elif field == "eyr" and not (2020 <= int(value) <= 2030):
            return False

        elif field == "hgt" and not ((value.endswith("cm") and 150 <= int(value[:-2]) <= 193)
                                     or (value.endswith("in") and 59 <= int(value[:-2]) <= 76)):
            return False

        elif field == "hcl" and not (len(value) == 7 and value[0] == "#"
                                     and all(c in string.hexdigits for c in value[1:])):
            return False

        elif field == "ecl" and value not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
            return False

        elif field == "pid" and not (len(value) == 9 and value.isnumeric()):
            return False

        fields[field] = True

    return all(fields.values())


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        GRPS = [grp.replace("\n", " ").split(" ") for grp in INP.split("\n\n")]

    PASSPORTS = [dict(field.split(":") for field in grp) for grp in GRPS]

    valid = sum(1 for passport in PASSPORTS if is_valid(passport))
    print(valid)
