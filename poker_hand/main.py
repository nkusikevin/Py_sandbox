from poker import Hand, Card

def pick_best_hand(hands):
    best_hand = None
    best_rank = None

    for hand_str in hands:
        hand = Hand()
        for card_str in hand_str:
            rank, suit = card_str[:-1], card_str[-1]
            card = Card(rank, suit)
            hand.add_card(card)

        hand_rank = hand.rank()
        if best_hand is None or hand_rank > best_rank:
            best_hand = hand
            best_rank = hand_rank

    return best_hand

# Example usage
hands = [
    ['8H', '9H', 'TH', 'JH', 'QH'],  # Straight Flush
    ['2D', '2H', '2S', '2C', 'AH'],  # Four of a Kind
    ['KD', 'KH', 'KS', 'KC', 'AH'],  # Four Kings
    ['4S', '4D', '4H', '4C', '7S'],  # Four of a Kind
    ['AH', 'KH', 'QH', 'JH', 'TH']   # Flush
]

best_hand = pick_best_hand(hands)
print("Best hand:", best_hand)
