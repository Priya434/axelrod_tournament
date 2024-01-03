from action import Action

C, D = Action.C, Action.D

r, p, s, t = 3, 1, 0, 5
"""
r = reward      for mutual cooperation
p = punishment  for mutual defection
s = sucker      to defect
t = temptation  to cooperate
"""


"""
self.action, opponent.action: self.score, opponent.score
(C, C) = mutual cooperation
(D, D) = mutual defection
(C, D), (D, C) = defection
"""

scores = {
    (C, C): (r, r),
    (D, D): (p, p),
    (D, C): (t, s),
    (C, D): (s, t)
}
"""
Player Usage example:
self.score = scores[(self.action, opponent.action)][0]
"""
