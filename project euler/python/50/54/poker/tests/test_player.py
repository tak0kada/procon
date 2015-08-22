from __future__ import absolute_import, print_function
import unittest
import poker
from poker.player import *

class PlayerTest(unittest.TestCase):
    def test_Player(self):
        player0, player1 = Player(), Player()
        player0.set_hand("5H 5C 6S 7S KD")
        player1.set_hand("2C 3S 8S 8D TD")

        #test set_hand
        self.assertEqual(player0.hand, "5H 5C 6S 7S KD")
        self.assertEqual(player0.rank, [False, False, False, False, False, False, False, False, 4, 12])
        self.assertEqual(player0.values, [4, 4, 5, 6, 12])
        self.assertEqual(player0.suits, ['H', 'C', 'S', 'S', 'D'])
        #test __gt__
        self.assertEqual(player0 > player1, False)
        #test __lt__
        self.assertEqual(player0 < player1, True)
        #test __eq__
        self.assertEqual(player0 == player1, False)
        #test __str__
        self.assertEqual(player0.__str__(), "5H 5C 6S 7S KD")
        #test __repr__
        self.assertEqual(player0.__repr__(), "5H 5C 6S 7S KD")

class FunctionsTest(unittest.TestCase):
    def test_hand_to_vs(self):
        self.assertEqual(hand_to_vs("5H 5C 6S 7S KD"), ([4, 4, 5, 6, 12], ['H', 'C', 'S', 'S', 'D']))

    def test_vs_to_hand(self):
        self.assertEqual(vs_to_hand([4, 4, 5, 6, 12], ['H', 'C', 'S', 'S', 'D']), "5H 5C 6S 7S KD")

    def test_rank(self):
        pass

    def test_high_card(self):
        self.assertEqual(high_card([4, 4, 5, 6, 12]), 12)
        self.assertEqual(high_card([1, 1, 1, 1, 2]), 2)

    def test_pair(self):
        pass

    def test_one_pair(self):
        self.assertEqual(one_pair([4, 4, 5, 6, 12]), 4)
        self.assertEqual(one_pair([1, 1, 2, 2, 3]), 2)

    def test_two_pairs(self):
        self.assertEqual(two_pairs([4, 4, 5, 6, 12]), False)
        self.assertEqual(two_pairs([1, 1, 2, 2, 3]), [2, 1])

    def test_three_of_a_kind(self):
        self.assertEqual(three_of_a_kind([4, 4, 5, 6, 12]), False)
        self.assertEqual(three_of_a_kind([1, 1, 1, 2, 3]), 1)

    def test_straight(self):
        self.assertEqual(straight([4, 4, 5, 6, 12]), False)
        self.assertEqual(straight([1, 2, 3, 4, 5]), 1)

    def test_flush(self):
        self.assertEqual(flush(['H', 'C', 'S', 'S', 'D']), False)
        self.assertEqual(flush(['H', 'H', 'H', 'H', 'H']), True)

    def test_full_house(self):
        self.assertEqual(full_house([4, 4, 5, 6, 12]), False)
        self.assertEqual(full_house([2, 2, 2, 3, 3]), (2, 3))

    def test_four_of_a_kind(self):
        self.assertEqual(four_of_a_kind([4, 4, 5, 6, 12]), False)
        self.assertEqual(four_of_a_kind([1, 1, 1, 1, 3]), 1)

    def test_straight_flush(self):
        self.assertEqual(straight_flush([4, 4, 5, 6, 12], ['H', 'C', 'S', 'S', 'D']), False)
        self.assertEqual(straight_flush([1, 2, 3, 4, 5], ['H', 'H', 'H', 'H', 'H']), 1)

    def test_royal_flush(self):
        self.assertEqual(royal_flush([4, 4, 5, 6, 12], ['H', 'C', 'S', 'S', 'D']), False)
        self.assertEqual(royal_flush([9, 10, 11, 12, 13], ['H', 'H', 'H', 'H', 'H']), True)

if __name__ == "__main__":
    unittest.main()
