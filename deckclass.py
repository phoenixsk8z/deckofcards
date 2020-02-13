'''A deck generates some # of cards it has methods
to shuffle and to deal the cards'''
import random

class Deck:
    def __init__(self, cardvalue = 13, suits = {"hearts","clubs","spades","diamonds"}):
        def makedeck():
            return {(i+1, j) for j in suits for i in range(cardvalue)}
        
        self.cardvalue = cardvalue
        self.suits = suits
        self.deck = makedeck()

    def shuffle(self):
        self.deck = random.sample(self.deck,len(self.deck))
        return self.deck

if __name__ == "__main__":
    mydeck = Deck()
    print("my deck is {}".format(mydeck.deck))
    mydeck.shuffle()
    print("my deck is now {}".format(mydeck.deck))

    phase10 = Deck(suits = {"red","blue","green","yellow"})
    print(phase10.deck)
