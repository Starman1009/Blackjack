import random

suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = [[suit, rank] for suit in suits for rank in ranks]
print(len(cards))
def shuffle():
    random.shuffle(cards)
    
shuffle()
def deal(n):
    backlog = []
    for turns in range(n):
        picked = cards.pop()#.pop() will remove AND RETURN THE THING GETTING REMOVEDpicked
        backlog.append(picked)
    return backlog
card = deal(7)
print(card)