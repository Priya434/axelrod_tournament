from action import Action
from player import Player

C, D = Action.C, Action.D


class TitForTat(Player):

    name = "Tit for Tat"

    def strategy(self, opponent: Player) -> Action:

        if not self._history:
            return C

        if (opponent._history[-1][0] == D):
            return D

        return C
