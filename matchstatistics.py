

from player import Player


class MatchStatistics:

    def __init__(self, player: Player, coplayer: Player):

        self.players = {
            player: player.name,
            coplayer: coplayer.name
        }

        self.history = {
            player: list(map(lambda x: (x[0].name), player._history)),
            coplayer: list(map(lambda x: (x[0].name), coplayer._history))
        }

        self.mutual_history = {
            player: list(map(lambda x: (x[0].name, x[1].name), player._history)),
            coplayer: list(
                map(lambda x: (x[0].name, x[1].name), coplayer._history))
        }

        self.total_score = {
            player.name: player._total_score,
            coplayer.name: coplayer._total_score
        }

        self.winner = {
            "name": "Draw" if (self.total_score[player.name] == self.total_score[coplayer.name]) else max(self.total_score),
            # "name": self.total_score[player]
            "score": self.total_score[max(self.total_score)]
        }
