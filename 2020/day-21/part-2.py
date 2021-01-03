# Day 21, Part 2: Allergen Assessment

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

    # Process of elimination
    pairs = []
    while any(len(v) == 1 for v in allergen_map.values()):
        for k, v in allergen_map.items():
            if len(v) == 1:
                ingred = next(iter(v))
                pairs.append((k, ingred))

                for k, v in allergen_map.items():
                    v.discard(ingred)

    cdil = ",".join(b for _, b in sorted(pairs))
    print(cdil)
