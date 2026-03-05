import pygame
import random


class ItemManager:

    def __init__(self, screen, board_rect, item_logic):
        self.screen = screen
        self.board_rect = board_rect
        self.item_logic = item_logic

        self.active_item_rect = None
        self.active_item_type = None
        self.next_spawn_time = 0
        self.item_expires_at = 0


    def _schedule_next_spawn(self):
        self.next_spawn_time = pygame.time.get_ticks() + random.randint(5000, 7000)

    def _spawn_item(self):
        now = pygame.time.get_ticks()
        self.item_expires_at = now + 5000

        item_size = 25
        x = random.randint(self.board_rect.left, self.board_rect.right - item_size)
        y = random.randint(self.board_rect.top, self.board_rect.bottom - item_size)

        self.active_item_rect = pygame.Rect(x, y, item_size, item_size)

        item = [ 'bomb', 'energy', 'carrot', 'snail']

        self.active_item_type = random.choice(item)

    def _draw_item(self):
        if self.active_item_rect is None:
            return

        COLORS = \
        {
            'bomb': (0,0,0),
            'energy': (0,255,0),
            'carrot': (255, 165, 0),
            'snail': (0, 180, 255),
        }

        pygame.draw.rect(self.screen, COLORS[self.active_item_type], self.active_item_rect)




    def _check_collision(self, player):
        if self.active_item_rect is not None and player.rect.colliderect(self.active_item_rect):
            self.item_logic.apply(player, self.active_item_type)
            self.active_item_rect = None
            self.active_item_type = None
            self._schedule_next_spawn()

    def update(self, player):
        now = pygame.time.get_ticks()

        if self.active_item_rect is None:
            if now > self.next_spawn_time:
                self._spawn_item()
            return
        if now >= self.item_expires_at:
            self.active_item_rect = None
            self.active_item_type = None
            self._schedule_next_spawn()
            return

        self._draw_item()
        self._check_collision(player)