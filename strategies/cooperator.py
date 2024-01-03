from action import Action
from player import Player

C, D = Action.C, Action.D


class Cooperator(Player):

    name = "Cooperator"

    def strategy(self, opponent: Player) -> Action:
        return C
