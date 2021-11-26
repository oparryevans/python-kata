import itertools


def hand(hole_cards, community_cards):
    suit_map = {'♥': 1, '♦': 2, '♠': 3, '♣': 4}
    rank_map = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
                '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

    rank_map_inv = dict((v, k) for k, v in rank_map.items())

    possible_hands = [i for i in itertools.combinations(hole_cards + community_cards, 5)]
    best_score = 0
    for proposed_hand in possible_hands:
        suit_hand = list(map(lambda x: suit_map[x[-1:]], proposed_hand))
        rank_hand = sorted(list(map(lambda x: rank_map[x[:-1]], proposed_hand)), reverse=True)

        if (len(set(suit_hand)) == 1) & (set([j-i for i, j in zip(rank_hand[:-1], rank_hand[1:])]) == {-1}):
            if 1000 + sum(rank_hand) > best_score:
                best_hand = "straight-flush", rank_hand
                best_score = 1000 + sum(rank_hand)

        elif max([rank_hand.count(i) for i in rank_hand]) == 4:
            if 900 + sum(rank_hand) > best_score:
                best_hand = 'four-of-a-kind', rank_hand
                best_score = 900 + sum(rank_hand)

        elif len(set(rank_hand)) == 2:
            if 800 + sum(rank_hand) > best_score:
                best_hand = 'full house', rank_hand
                best_score = 800 + sum(rank_hand)

        elif len(set(suit_hand)) == 1:
            if 700 + sum(rank_hand) > best_score:
                best_hand = 'flush', rank_hand
                best_score = 700 + sum(rank_hand)

        elif set([j-i for i, j in zip(rank_hand[:-1], rank_hand[1:])]) == {-1}:
            if 600 + sum(rank_hand) > best_score:
                best_hand = 'straight', rank_hand
                best_score = 600 + sum(rank_hand)

        elif max([rank_hand.count(i) for i in rank_hand]) == 3:
            if 500 + sum(rank_hand) > best_score:
                best_hand = 'three-of-a-kind', rank_hand
                best_score = 500 + sum(rank_hand)

        elif (max([rank_hand.count(i) for i in rank_hand]) == 2) & (len(set(rank_hand)) == 3):
            if 400 + sum(rank_hand) > best_score:
                best_hand = 'two pair', rank_hand
                best_score = 400 + sum(rank_hand)

        elif max([rank_hand.count(i) for i in rank_hand]) == 2:
            if 300 + sum(rank_hand) > best_score:
                best_hand = 'pair', rank_hand
                best_score = 300 + sum(rank_hand)

        else:
            if 200 + sum(rank_hand) > best_score:
                best_hand = 'nothing', rank_hand
                best_score = 200 + sum(rank_hand)

    ranked_hand = sorted(best_hand[1], key=best_hand[1].count, reverse=True)
    return best_hand[0], list(map(lambda x: rank_map_inv[x], list(dict.fromkeys(ranked_hand))))
