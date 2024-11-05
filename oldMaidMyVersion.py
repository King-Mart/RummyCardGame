import random

# initialize the deck of cards
# here cards are tuples with the index 0 being the rank (converted to a digit) and the symbol (represented as a letter)
# To display the cards, I will use a dictionary with the symbols as key pointing towards a dictionary containing all possible card values
def card_to_txt(card : tuple[str, int]):
    return cards[card[0]][card[1]]
#The deck misses a queen as per the old maid's rules
cards = {
    'C': { 1: 'A♣', 2: '2♣', 3: '3♣', 4: '4♣', 5: '5♣', 6: '6♣', 7: '7♣', 8: '8♣', 9: '9♣', 10: '10♣', 11: 'J♣', 12: 'Q♣', 13: 'K♣'},
    'D': { 1: 'A♦', 2: '2♦', 3: '3♦', 4: '4♦', 5: '5♦', 6: '6♦', 7: '7♦', 8: '8♦', 9: '9♦', 10: '10♦', 11: 'J♦', 12: 'Q♦', 13: 'K♦'},
    'H': { 1: 'A♥', 2: '2♥', 3: '3♥', 4: '4♥', 5: '5♥', 6: '6♥', 7: '7♥', 8: '8♥', 9: '9♥', 10: '10♥', 11: 'J♥', 12: 'Q♥', 13: 'K♥'},
    'S': { 1: 'A♠', 2: '2♠', 3: '3♠', 4: '4♠', 5: '5♠', 6: '6♠', 7: '7♠', 8: '8♠', 9: '9♠', 10: '10♠', 11: 'J♠', 12: 'Q♠', 13: 'K♠'}
}

# print the deck
sorted_deck = []
for i in range(13):
    for symbol in cards:
        sorted_deck.append((symbol, i+1))
#Pop a random queen 
missing_queen = sorted_deck.pop(random.randrange(44,48))



#Now split the cards equally between both players
def split_deck(deck):

    player1_hand = deck[len(deck)//2:]
    player2_hand = deck[:len(deck)//2]

    return player1_hand, player2_hand

#removing pairs
def remove_pairs(hand, key=lambda x : x):
    encountered_once = set()
    encountered_twice = set()

    for card in hand:
        if key(card) in encountered_once:
            encountered_twice.add(key(card))
        else:
            encountered_once.add(key(card))

def shuffle_distribution(deck):
    players = [[],[]]
    decision_maker = [0] * (len(deck)//2) + [1] * round(len(deck)/2 +0.4999)

    random.shuffle(decision_maker)

    for i in range(len(decision_maker)):
        players[decision_maker[i]].append(deck[i])

    print(decision_maker, len(decision_maker), len(deck), sep='\n')

    return players[1], players[0]
shuffle_distribution(sorted_deck)
player1_hand, player2_hand = shuffle_distribution(sorted_deck)
print(player1_hand, player2_hand, sep='\n')