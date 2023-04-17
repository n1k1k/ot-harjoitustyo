import unittest
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "7")
    
    def test_constructor_sets_suit_correctly(self):
        self.assertEqual(self.card.suit, "Hearts")
    
    def test_constructor_sets_rank_correctly(self):
        self.assertEqual(self.card.rank, "7")
    
    def test_value_correct_when_rank_Q(self):
        self.card = Card("Hearts", "Q")
        self.assertEqual(self.card.value, 10)
    
    def test_value_correct_when_rank_A(self):
        self.card = Card("Hearts", "A")
        self.assertEqual(self.card.value, 11)
