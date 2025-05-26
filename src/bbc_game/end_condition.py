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
    
    def __init__(self, start_time: datetime.datetime, duration: datetime.timedelta):
        self._start_time = start_time
        self._duration = duration

    def is_game_end(self):
        return datetime.datetime.now() >= self._start_time + self._duration


class TimeBasedEndConditionFactory(EndConditionFactory):

    def __init__(self, start_time: datetime.datetime, duration: datetime.timedelta):
        self.__start_time = start_time
        self.__duration = duration

    def create_TimeBasedEndCondition(self) -> TimeBasedEndCondition:
        return TimeBasedEndCondition(start_time=self.__start_time, duration=self.__duration)


class PointBasedEndCondition(EndCondition):

    def __init__(self, players: list[Player], point_goal:float):
        self._players = players
        self._point_goal = point_goal

    def is_game_end(self):
        return any([player.points >= self._point_goal for player in self._players])


class PointBasedEndConditionFactory(EndConditionFactory):

    def __init__(self, players: list[Player], point_goal:float):
        self.__players = players
        self.__point_goal = point_goal

    def create_PointBasedEndCondition(self) -> PointBasedEndCondition:
        return PointBasedEndCondition(players=self.__players, point_goal=self.__point_goal)
