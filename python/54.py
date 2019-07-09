#!/bin/env python3

# Problem at:
# https://projecteuler.net/problem=54

import enum
from collections import Counter

CARD_LITERALS = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K",
                 "A")
CARD_VALS = {val: index + 1 for index, val in enumerate(CARD_LITERALS)}


def extract_cards(hand_raw):
    hand = hand_raw.upper().strip().split(" ") if isinstance(hand_raw,
                                                             str) else hand_raw
    cards = list(
        sorted(hand, key=lambda elem: CARD_VALS[elem[0]], reverse=True))
    types = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    types_counter = Counter(types)

    return (cards, suits, types, types_counter)


def get_best_grouping(cards_data):
    _, suits, types, types_counter = cards_data

    types_groupings = list(zip(*types_counter.most_common()))[1]
    straight = any(types == CARD_LITERALS[i + 5:i:-1] for i in range(8))
    flush = len(set(suits)) == 1

    checks = [
        flush and types == ["A", "K", "Q", "J", "T"],
        flush and straight,
        types_counter.most_common(1)[0][1] == 4,
        types_groupings == (3, 2),
        flush,
        straight,
        types_groupings[0] == 3,
        types_groupings[:3] == (2, 2),
        types_groupings[0] == 2,
        True,
    ]
    return len(checks) - checks.index(True)


def get_score_array(cards_data):
    grouping = get_best_grouping(cards_data)
    cards, _, types, types_counter = cards_data

    to_return = [grouping]
    if grouping in (2, 4, 7, 8):
        to_return.append(CARD_VALS[types_counter.most_common(1)[0][0]])
    elif grouping == 3:
        pair_vals = list(zip(types_counter.most_common(2)))[0]
        to_return.append(CARD_VALS[max(pair_vals)])

    return to_return + [CARD_VALS[card[0]] for card in cards]


def p1_wins(data):
    def compare_scores(p1_score, p2_score):
        if p1_score[0] == p2_score[0]:
            return compare_scores(p1_score[1:], p2_score[1:])
        return p1_score[0] > p2_score[0]

    scores = list(map(get_score_array, data))
    return compare_scores(*scores)


# while True:
# player1_hand = extract_cards(input("1> "))
# player2_hand = extract_cards(input("2> "))
# print(p1_wins(player1_hand, player2_hand))

with open("54_poker.txt", "rt") as hands_file:
    rounds = [line.split(" ") for line in hands_file.read().split("\n")]
rounds = [(extract_cards(elem[:5]), extract_cards(elem[5:])) for elem in rounds
          if elem != [""]]
player1_rounds = [play for play in rounds if p1_wins(play)]
print(player1_rounds)
