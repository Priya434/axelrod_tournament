from typing import Literal
from action import Action

C, D = Action.C, Action.D


class Player:
    """
    A class used to represent a Player

    ...

    Attributes:
        name: str
            The name of the player
        history: list[tuple[Literal['C', 'D'], Literal['C', 'D']]]
            a list of mutual plays made by self and opponent
        action: Action
            play made by the player
        total_score: int
            total score of the player
        score: int
            score gained in the current play

    Methods:
        strategy(self, opponent: Player) -> Action
            Returns the action of the player based on its strategy

        update_total_score(self, score: int) -> None
            Updates players total score made across all plays

        update_history(self, play: Action, coplay: Action) -> None
            Updates the mutual history of self and opponent

        @property
            score(self) -> int
                Returns the current play score
            total_score(self) -> int
                Return player total score
            history(self) -> list[tuple[Literal['C', 'D'], Literal['C', 'D']]]
                Return mutual play history of self and opponent 

        @property.setter
            score(self, value: int) -> None
                Set the current play score
    """

    name = "Player"
    """Name of the player"""

    def __init__(self):
        """Initializes all attributes"""
        self._history: list[tuple[Literal['C', 'D'], Literal['C', 'D']]] = []
        self._action: Action
        self._total_score = 0
        self._score = 0

    @property
    def total_score(self):
        return self._total_score

    def update_total_score(self, score: int):
        self._total_score += score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value: int):
        self._score = value

    @property
    def history(self):
        return self._history

    def update_history(self, play: Action, coplay: Action):
        self._history.append((play, coplay))

    def strategy(self, opponent) -> Action:
        """ opponent: Player,
            Placeholder for strategy"""
        raise NotImplementedError()
