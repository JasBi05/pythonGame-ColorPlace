#player script
import pygame
from Color_Space.Player.color import Player_Color

#Player needs:
    #speed, size and color
class Player:
    def __init__(self, screen, player_color, board):
        self.board = board
        self.screen = screen
        self.score = 0
        self.player_color = player_color

        if self.player_color == Player_Color.RED:
            self.color = (255, 0, 0)
            self.x = 10
            self.y = 10

        elif self.player_color == Player_Color.BLUE:
            self.color = (0, 0, 255)
            self.x = 685
            self.y = 590

        self.speed = 5
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self):
        if self.player_color == Player_Color.BLUE:
            pygame.draw.rect(self.screen, (0,0,130), (self.x, self.y, self.width, self.height), 5)

        if self.player_color == Player_Color.RED:
            pygame.draw.rect(self.screen, (130,0,0), (self.x, self.y, self.width, self.height), 5)

    def move(self):
        keys = pygame.key.get_pressed()
        self.rect.topleft = (self.x, self.y)

        moved = False

        if self.player_color == Player_Color.BLUE:
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
                moved = True
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
                moved = True
            if keys[pygame.K_UP]:
                self.y -= self.speed
                moved = True
            if keys[pygame.K_DOWN]:
                self.y += self.speed
                moved = True

        elif self.player_color == Player_Color.RED:
            if keys[pygame.K_a]:
                self.x -= self.speed
                moved = True
            if keys[pygame.K_d]:
                self.x += self.speed
                moved = True
            if keys[pygame.K_w]:
                self.y -= self.speed
                moved = True
            if keys[pygame.K_s]:
                self.y += self.speed
                moved = True

        if self.x + self.width > 800:
            self.x = 800 - self.width
        if self.x < 0:
            self.x = 0

        if self.y + self.height > 700:
            self.y = 700 - self.height
        if self.y < 0:
            self.y = 0

        if moved:
            pygame.draw.rect(self.board, self.color,
                             (self.x, self.y, self.width, self.height))

