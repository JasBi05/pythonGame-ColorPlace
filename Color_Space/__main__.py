from Color_Space import game
from Color_Space.game import GameLogic


# Initializing the Game Color Space
class Game:
    def __init__(self):
        self.logic = GameLogic()
        self.logic.run()
Game()