import random
from cards import *

class CardEngine:
    """Allows the creation of a deck. Able to customize whether cards are removed from the deck, the cards in the deck, the sets in the deck and the names of the sets."""
    def make_deck():
        deck = []
        for i in range(0, 4):
            for o in range(1, 14):
                deck.append((i, o))
        return deck

    def __init__(self, auto_shuffle=True,deck=make_deck(), sets=sets, set_names=["Hearts", "Spades", "Diamonds", "Clubs"]):
        self.auto_shuffle = auto_shuffle
        self.deck = deck
        self.sets = sets
        self.set_names = set_names

    def card_picker(self):
        """Picks a card out of the deck in a (set, number) format."""
        length = len(self.deck)
        if length == 0:
            return True
        else:
            index = random.randint(0, length) - 1
            card = self.deck[index]
            if self.auto_shuffle == False:
                del self.deck[index]
            return card

    def card_reader(self, card=None):
        """Reads the card and returns its name (e.g (0, 1) returns an Ace), graphic, set name, value and set number.
        You can insert you own card for it to read but the default will draw a card for you."""
        if card is None:
            card = self.card_picker()
        if card != True:
            set, value = card
            graphic = self.sets[set].get(value)
            if value > 1 and value < 11:
                    card_name = str(value)
            elif value == 1:
                card_name = "Ace"
            elif value == 11:
                card_name = "Jack"
            elif value == 12:
                card_name = "Queen"
            elif value == 13:
                card_name = "King"
            set_name = self.set_names[set]
            return graphic, card_name, set_name, value, set
        else:
            return False

    def graphic(self, card):
        """Takes the card in the (set, number) format and returns its graphic only."""
        set, value = card
        graphic = self.sets[set].get(value)
        return graphic

    def hand_printer(self, hand):
        """Takes a group of cards (e.g hand = [(0, 1), (1, 5)]) and prints them out side by side."""
        cards = []
        for card in hand:
            cards.append((self.graphic(card).split("\n")))        
        length = len(cards)
        for rows in range(9):
            row = []
            for card in cards:
                row.append(card[rows])
                row.append("    ")
            print(*row)    

    def print_card(self, auto_print=False, values=None):
        """Prints the cards graphic, describes its set and name and returns its value and set number."""
        if values is None:
            values = self.card_reader()
        if auto_print == True and values != False:
            print(values[0])
            if values[1] == "8" or values[1] == "Ace":
                n = "n "
            else:
                n = " "
            print("You drew a{}{} of {}!".format(n, values[1], values[2]))
            value, set = values[-2:]
            return value, set
        else:
            print("Out of Cards!")
            return False