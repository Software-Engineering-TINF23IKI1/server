from abc import ABC, abstractmethod
from bbc_server import Player
import datetime

class EndCondition(ABC):

    @abstractmethod
    def is_game_end(self) -> bool:
        pass

class TimeBasedEndCondition(EndCondition):
    
    def __init__(self, start_time: datetime.datetime, duration: datetime.timedelta):
        self._start_time = start_time
        self._duration = duration

    def is_game_end(self):
        return datetime.datetime.now() >= self._start_time + self._duration


class ScoreBasedEndCondition(EndCondition):

    def __init__(self, players: list[Player], score_goal:float):
        self._players = players
        self._score_goal = score_goal

    def is_game_end(self):
        return any([player.score >= self._score_goal for player in self._players])
