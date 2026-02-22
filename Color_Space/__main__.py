from Color_Space import game
from Color_Space.game import GameSplatoon


# Initializing the Game Color Space
class Game:
    def __init__(self):
        self.logic = GameSplatoon()
        self.logic.run()

Game()