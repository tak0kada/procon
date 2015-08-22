from __future__ import absolute_import
from .player import Player as __Player
from .game import Game as game

def player(hand):
    player = __Player()
    player.set_hand(hand)
    return player
