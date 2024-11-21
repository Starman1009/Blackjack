import random

suits = ["hearts", "diamonds", "clubs", "spades"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards = [[suit, rank] for suit in suits for rank in ranks]

def shuffle():
    random.shuffle(cards)
    
shuffle()
#This function will deal n-1 ammount of cards
def deal(n):
    dealed = [] #The turns variable is simply a loop counter n-1
    for turns in range(n): #This loop will have each iterable "turns" that returns what ever thing it
        picked = cards.pop()#.pop() will remove AND RETURN THE THING GETTING REMOVED 
        dealed.append(picked) #i am adding the cards picked into dealed
    return dealed #once the loop has made the dealed deck, the function will return dealed which is now changed
cards_dealt = deal(7) #cards is just the returned value of now many iterations the loop went through
card = cards_dealt[0]
ranks_of_cards = card[1]

print(card)
print(ranks_of_cards)

print("BRYAN IS A BAKA OWO")
