from match import Match
from strategies.cooperator import Cooperator
from strategies.titfortat import TitForTat


g = Match(Cooperator(), TitForTat())
g.game()
