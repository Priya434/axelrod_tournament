from action import Action
from player import Player
import random

C, D = Action.C, Action.D


class RandomPlayer(Player):

    name = "Random Player"

    def strategy(self, opponent: Player) -> Action:
        return random.choice([C, D])
