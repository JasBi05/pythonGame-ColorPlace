import pygame
import random


class ItemEffect:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board


    def _bomb_effect(self, player):
        pass

    def _make_player_fast(self, player):
        player.speed = 10
        player.countdown_fast = pygame.time.get_ticks() + 5000


    def _make_player_bigger(self, player):
        player.width = 65
        player.height = 65
        player.countdown_size = pygame.time.get_ticks() + 5000


    def _make_player_slow(self, player):
        player.speed = 1
        player.countdown_slow = pygame.time.get_ticks() + 5000


    def apply(self, player, item_type):

        if item_type == "bomb":
            self._bomb_effect(player)

        elif item_type == "energy":
            self._make_player_fast(player)

        elif item_type == "carrot":
            self._make_player_bigger(player)

        elif item_type == "snail":
            self._make_player_slow(player)