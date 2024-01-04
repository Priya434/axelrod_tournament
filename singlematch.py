from duel import Duel
from match import Match
from strategies.cooperator import Cooperator
from strategies.titfortat import TitForTat


g = Duel(TitForTat(), TitForTat(), rounds=200)
g.print_stats()
