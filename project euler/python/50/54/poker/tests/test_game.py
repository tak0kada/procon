from __future__ import absolute_import, print_function
import unittest
import poker
from poker.game import *

class GameTest(unittest.TestCase):
    def test_set_player(self):
        game = Game()
        game.set_player(*range(10))
        self.assertEqual(game.players, list(range(10)))

    def test_winner(self):
        game = Game()
        game.set_player(*range(10))
        self.assertEqual(game.winner(), 9)


if __name__ == "__main__":
    unittest.main()
