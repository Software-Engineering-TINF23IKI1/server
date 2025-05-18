from bbc_game._typing import PointEarningFunctionType
import datetime

class PointDistributer:
    def __init__(self, point_distribution: dict[int, PointEarningFunctionType], point_interval: datetime.timedelta):
        if -1 not in point_distribution:
            raise ValueError("point_distribution in Point Earning Systems must provide a default case with the key -1")

        self.point_distribution = point_distribution
        self.point_interval = point_interval

        self._tick_time: datetime.datetime = None  # Variable holding the last point update time
        self._tick_count: int = 0  # Variable holding the number of point updates to perform

    def tick(self) -> bool:
        """Function that updates the point earning timer and checks for the timer to be elapsed

        Returns:
            bool: Whether the point earning timer elapsed
        """
        if not self._tick_time:
            self._tick_time = datetime.datetime.now()
            self._tick_count = 0
            return False

        time_diff: datetime.timedelta = datetime.datetime.now() - self._tick_time
        if time_diff < self.point_interval:
            return False
        else:
            self._tick_count = (int)(time_diff / self.point_interval)
            return True

    def earn_points(self, player_rank: int, current_points: float) -> float:
        """Funciton that calculates the new points using the players rank

        Args:
            player_rank (int): current players rank
            current_points (float): current points

        Returns:
            float: the new points
        """
        if player_rank in self.point_distribution:
            for _ in range(self._tick_count):
                current_points = self.point_distribution[player_rank](current_points)
            return current_points
        else:
            for _ in range(self._tick_count):
                current_points = self.point_distribution[-1](current_points)
            return current_points

class PointDistributerFactory:
    def __init__(self, point_distribution: dict[int, PointEarningFunctionType], point_interval: datetime.timedelta):
        self.point_distribution = point_distribution
        self.point_interval = point_interval

    def create_point_earner(self) -> PointDistributer:
        """Creates a new PointDistributer object using the config provided to the factory

        Returns:
            PointDistributer: A new PointDistributer object
        """
        return PointDistributer(point_distribution=self.point_distribution, point_interval=self.point_interval)
