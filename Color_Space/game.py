import pygame
from Color_Space.Player.color import Player_Color
from Color_Space.Player.player import Player
from Color_Space.Item.item_effect import ItemEffect
from Color_Space.Item.item_manager import ItemManager


class GameLogic:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700)) #width, height
        pygame.display.set_caption("Color Space")

        self.board = pygame.Surface((800, 700))
        self.board.fill((255, 255, 255))

        self.red_player = Player(self.screen, Player_Color.RED, self.board)
        self.blue_player = Player(self.screen, Player_Color.BLUE, self.board)

        self.running = True

        self.counter = 10
        self.font = pygame.font.SysFont('Franklin Gothic', 100)

        self.item_effect = ItemEffect(self.screen, self.board)
        self.item_manager = ItemManager(
            self.screen,
            self.board.get_rect(),
            self.item_effect
        )
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

            self.blue_player.move()
            self.red_player.move()

            self.screen.blit(self.board, (0, 0))
            self.red_player.draw()
            self.blue_player.draw()
            self.item_manager.update(self.red_player)
            self.item_manager.update(self.blue_player)
            self.draw_timer()

            pygame.display.flip()

    def update_timer(self, event):
        if event.type == self.timer_event:
            self.counter -= 1

    def draw_timer(self):
        if self.counter > 0:
            text = self.font.render(str(self.counter), True, (0, 0, 0))
        else:
            text = self.font.render('Game Over', True, (0, 0, 0))

        text_rect = text.get_rect(center=(400, 50))
        self.screen.blit(text, text_rect)
