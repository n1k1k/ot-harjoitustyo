import unittest
from game import Game
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        card = Card('hearts', '7')
        self.game.deck.cards.append(card)
    
    def test_deal_card_deals_card_to_player_hand(self):
        self.game.deal_card(self.game.player)
        self.assertEqual(f"{self.game.player.hand[0]}","7 of hearts")
    
    def test_deal_card_changes_player_score_correctly(self):
        self.game.deal_card(self.game.player)
        self.assertEqual(self.game.player.score, 7)
    