#player script
import pygame
from Color_Space.Player.color import Color


#Player needs:
    #speed, size and color

class Player:
    def __init__(self, screen, color):
        self.screen = screen
        self.color = color

        if self.color == Color.RED:
            self.color = "red"
            self.x = 10
            self.y = 10

        elif self.color == Color.BLUE:
            self.color = "blue"
            self.x = 685
            self.y = 590

        self.speed = 0.3
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])


