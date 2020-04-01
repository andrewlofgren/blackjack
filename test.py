import unittest
from card import Card

class CardTest(unittest.TestCase):

    def test_visibility(self):
        c = Card('3', 'h')
        self.assertTrue(c.visible())

