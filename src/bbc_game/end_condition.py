from abc import ABC, abstractmethod
from bbc_server import Player
import datetime

class EndCondition(ABC):

    @abstractmethod
    def is_game_end(self) -> bool:
        pass


class EndConditionFactory(ABC):

    @abstractmethod
    def create_EndCondition(self, **kwargs) -> EndCondition:
        """create the EndConditionObject"""
        pass


class TimeBasedEndCondition(EndCondition):
    
    def __init__(self, duration: datetime.timedelta):
        self._start_time = datetime.datetime.now()
        self._duration = duration

    def is_game_end(self):
        return datetime.datetime.now() >= self._start_time + self._duration


class TimeBasedEndConditionFactory(EndConditionFactory):

    def __init__(self, duration: datetime.timedelta):
        self.__duration = duration

    def create_EndCondition(self) -> TimeBasedEndCondition:
        return TimeBasedEndCondition(duration=self.__duration)


class PointBasedEndCondition(EndCondition):

    def __init__(self, point_goal:float):
        self._point_goal = point_goal
        self._players = None

    def add_players(self, players: list[Player]):
        self._players = players

    def is_game_end(self):
        if not self._players:
            raise ValueError("PointBasedEndCondition.players is not set but required for evaluate condition.")
        
        return any([player.points >= self._point_goal for player in self._players])


class PointBasedEndConditionFactory(EndConditionFactory):

    def __init__(self, point_goal:float):
        self.__point_goal = point_goal

    def create_EndCondition(self) -> PointBasedEndCondition:
        return PointBasedEndCondition(point_goal=self.__point_goal)
