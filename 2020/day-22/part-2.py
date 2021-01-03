# Day 22, Part 2: Crab Combat


def play_game(deck_1, deck_2, seen):
    while deck_1 and deck_2:
        tup_1 = tuple(deck_1)
        tup_2 = tuple(deck_2)
        if (tup_1, tup_2) in seen:
            deck_2.clear()
            return
        seen.add((tup_1, tup_2))

        # popleft on deque is more efficient but would have to use
        # itertools.islice and reconstruct deques below
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if card_1 > len(deck_1) or card_2 > len(deck_2):
            if card_1 < card_2:
                deck_2 += [card_2, card_1]
            else:
                deck_1 += [card_1, card_2]
            continue

        subdeck_1 = deck_1[:card_1]
        subdeck_2 = deck_2[:card_2]

        play_game(subdeck_1, subdeck_2, set())
        if subdeck_1:
            deck_1 += [card_1, card_2]
        else:
            deck_2 += [card_2, card_1]


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    DECKS = [[int(line) for line in grp.split("\n")[1:]]
             for grp in INP.split("\n\n")]

    player_1, player_2 = DECKS

    play_game(player_1, player_2, set())

    winner = player_1 if player_1 else player_2
    total = sum(i * card for i, card in enumerate(reversed(winner), 1))
    print(total)
