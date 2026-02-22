import pygame

class GameLogic:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((800, 700)) #width, height

        pygame.display.set_caption("Color Space")
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    #add timer method