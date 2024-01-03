from more_itertools import distinct_combinations
from duel import Duel
from player import Player


class Tournament:

    winners: list[dict[str, str | int]] = []
    results: list[dict[str, int]] = []
    scores: list[tuple[str, int]] = []

    def display_average(self):
        rounds = len(self.round_robin)
        print('\033[4m', "Average Scores", '\033[0m')
        for score in self.scores:
            print(f'{score[0]}: {round((score[1] * 2)/rounds)}')

    def display_scores(self):
        print('\033[4m', "Total Scores", '\033[0m')
        for score in self.scores:
            print(score)

    def display_results(self):
        print('\033[4m', "Match Results", '\033[0m')
        for result in self.results:
            print(result)

    def display_winners(self):
        print('\033[4m', "Match Winners", '\033[0m')
        for winner in self.winners:
            print(f'{winner["name"]}: {winner["score"]}')

    def __init__(self, players: list[Player], rounds=5, multigame=False, multirounds=5):

        self.players = players
        self.round_robin = list(distinct_combinations(self.players, r=2))

        # conduct round robin tournament
        for duel in self.round_robin:

            game = Duel(player=duel[0](), coplayer=duel[1](
            ), rounds=rounds, multigame=multigame, multirounds=multirounds)

            self.winners.append(game.stats.winner)
            self.results.append(game.stats.total_score)

        # set individual player scores
        for player in self.players:
            score = 0
            for result in self.results:
                if result.get(player.name):
                    score += result.get(player.name)
            self.scores.append((player.name, score))

        self.scores = sorted(
            self.scores, key=lambda t: t[1], reverse=True)
