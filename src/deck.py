from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def add_cards(self):
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit,rank))

    @property
    def cards_left(self):
        return len(self.cards)
