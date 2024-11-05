# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

from random import randrange, shuffle, choice as randomChoice

def wait_for_player() -> None:
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck() -> list[str]:
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck : list[str]) -> None:
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    shuffle(deck)

#####################################

def deal_cards(deck : list[str]) -> tuple[list[str]]:
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     dealer, other = deck[:len(deck)//2], deck[len(deck)//2:]

     return (dealer, other)
 

def card_to_num(card : str) -> int:
    """Converts a card to its number counterpart to ensure type safety

    Args:
        card (str): The card in question
    Returns:
        int: The number counterpart of the card
    """
    match card[0]:
        case  'A':
            return 1
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case _:
            return int(card[0]) * (9*(card[1] == '0')) + int(card[0])

def remove_pairs(l : list[str]) -> None:
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND ||| Shouldn't the list be ordered like all card games, that is how people play cards usually.
       edit, I understand we have to shuffle so the opponent cant strategize his picks. I think shuffling can be handled in a separate function as it is not necessary here
     We should use an ordered list in all of the code and return a shuffled copy whenever truly necessary (which is when picking a card from the opponent)

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    l.sort(key=lambda x: card_to_num(x))

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    index = 0
    while index < len(l)-1:
        if card_to_num(l[index]) == card_to_num(l[index+1]):
            l.pop(index)
            l.pop(index)
        else:
            index += 1

    shuffle(l)

def print_deck(deck : list[str]) -> None:
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    print(' '.join(deck), end='\n\n')

    
def get_valid_input(n : int) -> int:
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     uinput = n+1
     while uinput < 1 or uinput > n:
        try:
            uinput = int(input())
        except ValueError as e:
            print(e)
            uinput = n + 1
     return uinput-1

def human_turn(hand : list[str], opponent_hand : list[str]) -> None:
    print("***********************************************************\nYour turn.\n")
    print("Your current hand is:\n")
    print_deck(hand)
    print(f"I, Robot, have {len(opponent_hand)} cards. If 1 stands for my first card and if\n{len(opponent_hand)} stands for my last card, which of my cards would you like?")
    print(f'Give me an integer between 1 and {len(opponent_hand)}: ', end='')
    chosen_card = get_valid_input(len(opponent_hand))
    print(f"You asked for my {str(chosen_card) + {1 : "st", 2 : "nd", 3: "rd"}.get(chosen_card, "th")} card.")
    if card_to_num(opponent_hand[chosen_card]) == 12:
        input("Are you sure you wanna pick this card, it's the old maid.")
        print("As if I'd let you change your mind! prepare to lose HAHA.")
    else:
        print(f"Here is your new card: {opponent_hand[chosen_card]}")
    remove_subseqent_pairs(hand, opponent_hand.pop(chosen_card))
    print("Your new hand after discard and shuffle is:\n")
    print_deck(hand)

    wait_for_player()

    if len(opponent_hand) == 0:
        return victory("Robot")
    return False

def computer_turn(hand : list[str], opponent_hand : list[str]) -> bool:
    print("***********************************************************\nMy turn.\n")
    chosen_card = randrange(0,len(opponent_hand))
    print(f"I chose {opponent_hand[chosen_card]}, your{' ' + {1 : "st", 2 : "nd", 3: "rd"}.get(chosen_card, "th")} card.")
    match card_to_num(opponent_hand[chosen_card]):
        case 12:
            print(randomChoice(["Looks like I have miscalculated, there must've been a bit shift in my code", "Fly like a penguin sting like a mosquito. I don't think that's the phrase but it stings to pick the wrong card...", "I knew it was the queen but I picked it strategically", "I gathered all the info I need to beat you next turn.\nThat turn might be next game."]))
        case 1:
            print("I think I have a pair of Aces, I'll have to remove them")
        case 2:
            print("I think I have a pair of Twos, two steps closer to victory!")
        case 3:
            print("Thre like the amount of leaves on a lucky clover. I must be lucky!")
        case 4:
            print("According to my calculations, I'll beat you in 2 moves")
        case 13:
            print("I picked a king like the king I am")
    remove_subseqent_pairs(hand, opponent_hand.pop(chosen_card), printtxt=False)

    wait_for_player()

    if len(opponent_hand) == 0:
        return victory("Human")
    return False


def remove_subseqent_pairs(hand : list[str], new_card : str, printtxt = True) -> None:
     '''(list of str, str)->None
     Removes the pair formed in the given hand after a new card is added
     '''
     if printtxt:
        print(f"with {new_card} added your current hand is : ")
        print_deck(hand)
     new_card = card_to_num(new_card)
     i = 0
     while i < len(hand):
         if card_to_num(hand[i]) == new_card:
             hand.pop(i)
             i = 99999999999999999
         i += 1
     shuffle(hand)

def victory(winner : str):
    print(f"Congratulations to the winner... It is {winner}!")
    return True

def play_game() -> None:
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer. I definetly don't cheat.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards. I don't need to see them to win!")

     #Since the player isn't discarding the cards himself, it is incoherent to tell him to discard them
     print("Now I will discard all the pairs from your deck (without looking). I will do the same for me.")

     wait_for_player()
     
     remove_pairs(dealer)
     remove_pairs(human)
     print_deck(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     victory = False
     while not victory:
         victory = human_turn(human, dealer)
         if not victory:
             victory = computer_turn(dealer, human)
	
	 

# main

play_game()
