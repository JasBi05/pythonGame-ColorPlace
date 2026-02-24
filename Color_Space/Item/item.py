import pygame
import random
from threading import Timer

class Item:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board

    def random_item(self, player):

        items = [
            self._bomb_effect,
            self._make_player_fast,
            self._make_player_bigger,
            self._make_player_slow
        ]

        effect = random.choice(items)

        delay = random.randint(5, 10)
        Timer(delay, effect, args=(player,)).start()


    def _bomb_effect(self, player):
        bomb = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (0, 0, 0), bomb)
        if bomb.colliderect(player.rect):
            print(f"Bomb trifft {player.player_color}")

    def _make_player_fast(self, player):
        energy = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (0, 255, 0), energy)
        if energy.colliderect(player.rect):
            player.speed = 20
            print(f"Player speed {player.speed}")
            def reset_speed():
                player.speed = 5
                print(f"Player speed {player.speed}")
            Timer(5, reset_speed).start()

    def _make_player_bigger(self, player):
        carrot = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (255, 165, 0), carrot)
        if carrot.colliderect(player.rect):
            print(f"Player speed {player.width}")
            player.width = 75
            player.height = 75
            def reset_size():
                self.width = 50
                self.height = 50
                print(f"Player width {player.speed}")
            Timer(5, reset_size).start()

            print(f"Player speed {player.width}")

    def _make_player_slow(self, player):
        snail = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (0, 0, 255), snail)
        if snail.colliderect(player.rect):
            player.speed = 3
            print(f"Player speed {player.speed}")
            def reset_speed():
                player.speed = 5
                print(f"Player speed {player.speed}")

            Timer(5, reset_speed).start()