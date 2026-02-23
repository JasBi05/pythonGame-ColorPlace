import pygame
from Color_Space.Player.color import Player_Color
from Color_Space.Player.player import Player


class GameLogic:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700)) #width, height
        pygame.display.set_caption("Color Space")

        self.red_player = Player(self.screen, Player_Color.RED)
        self.blue_player = Player(self.screen, Player_Color.BLUE)

        self.running = True

        self.counter = 10
        self.font = pygame.font.SysFont(None, 60)

        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.update_timer(event)

            self.screen.fill((0, 0, 0))

            self.blue_player.move()
            self.red_player.move()

            self.red_player.draw()
            self.blue_player.draw()

            self.draw_timer()  # ← Timer zeichnen

            pygame.display.flip()

    def update_timer(self, event):
        if event.type == self.timer_event:
            self.counter -= 1

    def draw_timer(self):
        if self.counter > 0:
            text = self.font.render(str(self.counter), True, (0, 200, 0))
        else:
            text = self.font.render('Zeit abgelaufen', True, (255, 0, 0))

        text_rect = text.get_rect(center=(400, 50))
        self.screen.blit(text, text_rect)
