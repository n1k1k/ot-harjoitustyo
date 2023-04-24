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

        if player.score > 21:
            for card in player.hand:
                if card.rank == 'A':
                    player.score -= 10
                    break


    def first_round(self):
        self.deck.cards = []
        self.deck.add_cards()
        random.shuffle(self.deck.cards)
    
    def deal_new_game(self):
        self.player.hand = []
        self.dealer.hand = []
        self.player.score = 0
        self.dealer.score = 0
        self.player.status = None
        self.dealer.status = None

        for _ in range(2):
            self.deal_card(self.player)
            self.deal_card(self.dealer)
        
        if self.player.score == 21:
            self.player.status = 'Blackjack'
        if self.dealer.score == 21:
            self.dealer.status = 'Blackjack'
        
    def stand(self):
        if self.dealer.score < 21:
            if len(self.dealer.hand) == 5:
                self.dealer.status = 'Win'
        if self.dealer.score > 21:
            self.player.status = 'Win'
        elif self.dealer.score == self.player.score:
            self.dealer.status = 'Tie'
            self.player.status = 'Tie'
        elif self.dealer.score > self.player.score:
            self.dealer.status = 'Win'
    
    def check_for_bust(self):
        if self.player.score > 21:
            self.player.status = 'Bust'
