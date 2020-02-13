'''deal some # of cards to some # of players'''

class Game:
    def __init__(self, deck, hand, players):
        self.deck = deck
        self.hand = hand
        self.players = players
        self.hands = [list() for player in range(players)]

    def deal(self):
        for count in range(self.hand):
            for player in range(self.players):
                self.hands[player].append(self.deck.pop())

if __name__ == "__main__":
    deck = {
        (6, "diamonds"),
        (8,"spades"),
        (9,"diamonds"),
        (2,"clubs"),
        (4,"diamonds"),
        (1,"spades"),
        (7,"hearts"),
        (9,"hearts")}
    mygame = Game(deck, 2, 4)

    mygame.deal()

    print(mygame.hands)
                
        
        
