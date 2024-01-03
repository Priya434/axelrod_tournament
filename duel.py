from matchstatistics import MatchStatistics
from player import Player
from match import Match


class Duel:

    def single_game(self):
        self.duel.game()

    def multi_game(self, rounds: int = 5):
        for _ in range(rounds):
            self.duel.game()

    def print_stats(self):
        print()

        print(
            f'{self.stats.players[self.player]} vs {self.stats.players[self.coplayer]}')

        print()

        print(f'{self.stats.history[self.player]}')
        print(f'{self.stats.history[self.coplayer]}')

        print()

        print(f'{self.stats.mutual_history[self.player]}')
        print(f'{self.stats.mutual_history[self.coplayer]}')

        print()

        print(
            f'{self.stats.total_score[self.player.name]} | {self.stats.total_score[self.coplayer.name]}')

        print()

    def __init__(self, player: Player, coplayer: Player, rounds: int = 5, multigame: bool = False, multirounds: int = 5):

        self.player = player
        self.coplayer = coplayer

        self.duel = Match(self.player, self.coplayer, rounds)

        if (multigame):
            self.multi_game(multirounds)
        else:
            self.single_game()

        self.stats: MatchStatistics = self.duel.match_statistics()
