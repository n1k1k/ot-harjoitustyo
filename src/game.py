import random
from deck import Deck
from player import Player

class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck()

    def deal_card(self, player: Player):
        card = self.deck.cards.pop(0)
        player.hand.append(card)
        player.score += card.value

    def first_round(self):
        self.deck.add_cards()
        random.shuffle(self.deck.cards)
        for _ in range(2):
            self.deal_card(self.player)
            self.deal_card(self.dealer)
