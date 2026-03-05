import pygame
import random

class ItemEffect:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

    def _bomb_effect(self, player):
        pass

    def _make_player_fast(self, player):
        pass


    def _make_player_bigger(self, player):
        pass


    def _make_player_slow(self, player):
        pass

    def apply(self, player, item_type):

        if item_type == "bomb":
            self._bomb_effect(player)

        elif item_type == "energy":
            self._make_player_fast(player)

        elif item_type == "carrot":
            self._make_player_bigger(player)

        elif item_type == "snail":
            self._make_player_slow(player)