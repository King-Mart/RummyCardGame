# initialize the deck of cards
# here cards are tuples with the index 0 being the rank (converted to a digit) and the symbol (represented as a letter)
# To display the cards, I will use a dictionary with the symbols as key pointing towards a dictionary containing all possible card values
def card_to_txt(card : tuple[str, int]):
    return cards[card[0]][card[1]]
cards = {
    'C': { 1: 'A♣', 2: '2♣', 3: '3♣', 4: '4♣', 5: '5♣', 6: '6♣', 7: '7♣', 8: '8♣', 9: '9♣', 10: '10♣', 11: 'J♣', 12: 'Q♣', 13: 'K♣'},
    'D': { 1: 'A♦', 2: '2♦', 3: '3♦', 4: '4♦', 5: '5♦', 6: '6♦', 7: '7♦', 8: '8♦', 9: '9♦', 10: '10♦', 11: 'J♦', 12: 'Q♦', 13: 'K♦'},
    'H': { 1: 'A♥', 2: '2♥', 3: '3♥', 4: '4♥', 5: '5♥', 6: '6♥', 7: '7♥', 8: '8♥', 9: '9♥', 10: '10♥', 11: 'J♥', 12: 'Q♥', 13: 'K♥'},
    'S': { 1: 'A♠', 2: '2♠', 3: '3♠', 4: '4♠', 5: '5♠', 6: '6♠', 7: '7♠', 8: '8♠', 9: '9♠', 10: '10♠', 11: 'J♠', 12: 'Q♠', 13: 'K♠'}
}

# print the deck
deck = [(symbol, rank) for symbol in cards for rank in cards[symbol]]
print(" ".join(card_to_txt(card) for card in deck))
