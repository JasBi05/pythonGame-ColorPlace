import pygame
from Color_Space.Player.color import Color
from Color_Space.Player.player import Player


class GameLogic:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 700)) #width, height

        pygame.display.set_caption("Color Space")
        self.running = True

        self.red_player = Player(self.screen, Color.RED)
        self.blue_player = Player(self.screen, Color.BLUE)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.red_player.draw()
                self.blue_player.draw()
                pygame.display.flip()

    #add timer method