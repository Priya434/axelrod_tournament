from strategies.cooperator import Cooperator
from strategies.defector import Defector
from strategies.randomplayer import RandomPlayer
from strategies.titfortat import TitForTat
from tournament import Tournament


players = [Cooperator, Defector, TitForTat, RandomPlayer]
rounds: int = 5
multigame: bool = False
multirounds: int = 5

tournament = Tournament(players)

print()
tournament.display_results()
print()
tournament.display_winners()
print()
tournament.display_scores()
print()
tournament.display_average()
print()
