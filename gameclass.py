'''deal some # of cards to some # of players'''

class Game:
    def __init__(self, deck, hand, players):
        self.deck = deck
        self.hand = hand
        self.players = players
        self.hands = [list() for player in range(players)]
        self.discardpile = list()

    def deal(self):
        for _ in range(self.hand):
            for player in range(self.players):
                self.hands[player].append(self.deck.pop())
                
    def discard(self, player, card):
        hand = self.hands[player]
        dropcard = hand.pop(card)
        self.discardpile.append(dropcard)

    def draw(self, pile, player):
        self.hands[player].append(pile.pop())


if __name__ == "__main__":
    deck = {
        (6, "diamonds"),
        (8,"spades"),
        (9,"diamonds"),
        (2,"clubs"),
        (4,"diamonds"),
        (1,"spades"),
        (7,"hearts"),
        (9,"hearts"),
        (5,"clubs"),
        (6,"clubs"),
        (9,"clubs"),
    }
    mygame = Game(deck, 2, 4)

    mygame.deal()

    print(mygame.hands)
    mygame.draw(mygame.deck, 0)
    print(mygame.hands[0])
    mygame.discard(0,1)
    print("discard {}, hand {}".format(mygame.discardpile, mygame.hands[0]))
    mygame.draw(mygame.discardpile, 1)
    print("\nplayer1 hand {}".format(mygame.hands[1]))
        
        
