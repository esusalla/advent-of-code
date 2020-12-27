# Day 21, Part 1: Allergen Assessment

import functools

if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()
        LINES = [line.split(" (contains ") for line in INP.split("\n")]

    ingreds_set = set()
    ingreds_list = []
    allergen_map = {}

    for ingreds, allergens in LINES:
        ingreds = ingreds.split(" ")
        ingreds_list += ingreds

        ingreds = set(ingreds)
        ingreds_set.update(ingreds)

        allergens = allergens[:-1].split(", ")

        for allergen in allergens:
            if allergen in allergen_map:
                allergen_map[allergen] = allergen_map[allergen] & ingreds
            else:
                allergen_map[allergen] = ingreds

    possible = functools.reduce(set.__or__, allergen_map.values())
    diff = ingreds_set - possible

    count = sum(ingreds_list.count(ingred) for ingred in diff)
    print(count)
