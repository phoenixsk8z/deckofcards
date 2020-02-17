from gameclass import Game
from deckclass import Deck
import random 

class GoFish(Game, Deck):
    def __init__(self, players, isPond):
        self.isPond = isPond
        Deck.__init__(self)
        Deck.shuffle(self)
        Game.__init__(self, self.deck, 7, players)

    def draw(self, player):
        if self.isPond:
            self.hands[player].append(
                self.deck.pop(
                    random.randrange(
                        len(self.deck)
                    )
                )
            )
        else:
            self.hands[player].append(self.deck.pop())

    def ask(self, me, player, cardvalue):
        count = 0 
        for card in self.hands[player]:
            if card[0] == cardvalue:
                count += 1
                self.hands[player].remove(card)
                self.hands[me].append(card)
        return count 


if __name__ == "__main__":
    game = GoFish(2, True)
    game.shuffle()
    game.deal()
    print("Deck {}, lengh {}".format(game.deck, len(game.deck)))
    print("player0 {}".format(game.hands[0]))
    if game.ask(0, 1, 4) == 0:
        game.draw(0)
    print(game.hands[0])