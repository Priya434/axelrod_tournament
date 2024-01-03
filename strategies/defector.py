from action import Action
from player import Player

C, D = Action.C, Action.D


class Defector(Player):

    name = "Defector"

    def strategy(self, opponent: Player) -> Action:
        return D
