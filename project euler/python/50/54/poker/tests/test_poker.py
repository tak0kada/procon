from __future__ import absolute_import, print_function
import unittest
import poker

testdata = ["5H 5C 6S 7S KD 2C 3S 8S 8D TD",
            "5D 8C 9S JS AC 2C 5C 7D 8S QH",
            "2D 9C AS AH AC 3D 6D 7D TD QD",
            "4D 6S 9H QH QC 3D 6D 7H QD QS",
            "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D"]

testwinner = [1, 0, 1, 0, 0]

class TestPoker(unittest.TestCase):
    def testpoker(self):
        games = []
        for line in testdata:
            hand0, hand1 = line[:14], line[15:]
            player0 = poker.player(hand0)
            player1 = poker.player(hand1)
            game = poker.game()
            game.set_player(player0, player1)
            games.append(game)
        for i in range(5):
            game = games[i]
            winner = testwinner[i]
            self.assertEqual(game.winner(), winner)

if __name__ == "__main__":
    unittest.main()
