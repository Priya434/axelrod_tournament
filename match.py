from matchstatistics import MatchStatistics
from game import Game


class Match:

    def __init__(self, player, coplayer, rounds: int = 5):

        self.player = player
        self.coplayer = coplayer
        self.rounds = rounds

    def game(self):
        for _ in range(self.rounds):
            Game(self.player, self.coplayer)

    def match_statistics(self):

        stats = MatchStatistics(self.player, self.coplayer)

        return stats
