import pygame
import random


class ItemEffect:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

    def _bomb_effect(self, player):

        w, h = 200, 200

        area = pygame.Rect(0, 0, w, h)
        area.center = player.rect.center

        area.clamp_ip(player.board.get_rect())
        pygame.draw.rect(player.board, (255, 255, 255), area)

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