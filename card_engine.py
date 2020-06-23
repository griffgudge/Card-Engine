import random
from cards import *

class CardEngine:
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
        set, value = card
        graphic = self.sets[set].get(value)
        return graphic

    def print_card(self, auto_print=False, values=None):
        if values is None:
            values = self.card_reader()
        if auto_print == True:
            print(values[0])
            print("You drew a {} of {}!".format(values[1], values[2]))
            value, set = values[-2:]
            return value, set
        else:
            print("Out of Cards!")
