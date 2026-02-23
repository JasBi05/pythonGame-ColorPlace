import pygame
import random
from Color_Space.Player.player import Player

#item script

#ideas:
    #1. A bomb that destroys some colors. Also, yours!
    #2. An Energy drink that makes you fast
    #3. A carrot that makes you bigger than the other player (You can color more space)
    #4. An item that makes you slow

class Item:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board


    def bomb_item(self, player):
        bomb = pygame.Rect(random.randint(0,700), random.randint(0,800), 25, 25)
        pygame.draw.rect(player.screen, (0, 0, 0), bomb)

    def make_player_fast(self, player):
        energy = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (0, 255, 0), energy)

        if energy.colliderect(player.rect):
            player.speed = 20

    def make_player_bigger(self, player):
        carrot = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (255, 165, 0), carrot)

        if carrot.colliderect(player.rect):
            player.width = 75
            player.height = 75

    def make_player_slow(self, player):
        snail = pygame.Rect(random.randint(0, 700), random.randint(0, 800), 25, 25)
        pygame.draw.rect(player.screen, (0, 0, 255), snail)

        if snail.colliderect(player.rect):
            player.speed = 3


    def random_item(self, player):
        methods = [self.bomb_item, self.make_player_fast,self.make_player_bigger, self.make_player_slow]

        random_method = random.choice(methods)
        random_method(player)

