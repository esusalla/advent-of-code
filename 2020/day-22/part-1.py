# Day 22, Part 1: Crab Combat

import collections


def play_game(deck_1, deck_2):
    while deck_1 and deck_2:
        card_1 = deck_1.popleft()
        card_2 = deck_2.popleft()

        if card_1 < card_2:
            deck_2 += [card_2, card_1]
        else:
            deck_1 += [card_1, card_2]


if __name__ == "__main__":
    with open("inp.txt") as infile:
        INP = infile.read().strip()

    DECKS = [collections.deque(int(line) for line in grp.split("\n")[1:])
             for grp in INP.split("\n\n")]

    player_1, player_2 = DECKS
    play_game(player_1, player_2)

    winner = player_1 if player_1 else player_2
    total = sum(i * card for i, card in enumerate(reversed(winner), 1))
    print(total)
