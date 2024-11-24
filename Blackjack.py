import random
suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = [[suit, rank] for suit in suits for rank in ranks]

def shuffle():
    random.shuffle(cards)
    
shuffle()

def deal(n):
    dealed = []
    for turns in range(n):
        card_picked = cards.pop()
        dealed.append(card_picked)
    return dealed
card = deal(1)[0]
rank_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
rank_dict = {"rank": card[1], "value": rank_values[card[1]]}
print(card)