import pygame

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

    def bomb_item(self):
        bomb = pygame.Rect(20, 50, 25, 25)
        pygame.draw.rect(self.screen, (0, 0, 0), bomb)

    def make_player_fast(self):
        energy = pygame.Rect(20, 50, 25, 25)

    def make_player_bigger(self):
        carrot = pygame.Rect(20, 50, 25, 25)

    def make_player_slow(self):
        snail = pygame.Rect(20, 50, 25, 25)

