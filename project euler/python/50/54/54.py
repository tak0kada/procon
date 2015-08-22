from __future__ import absolute_import, print_function
import poker

if __name__ == "__main__":
    with open("poker.txt", "r") as f:
        data = f.read()
        data = data.splitlines()

    games = []
    for line in data:
        hand0, hand1 = line[:14], line[15:]
        player0 = poker.player(hand0)
        player1 = poker.player(hand1)
        game = poker.game()
        game.set_player(player0, player1)
        games.append(game)

    result = [game.winner() for game in games]
    print("player0 win: " + str(result.count(0)) + "times")
    print("player1 win: " + str(result.count(1)) + "times")
