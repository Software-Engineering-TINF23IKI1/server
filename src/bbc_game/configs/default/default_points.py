from bbc_game.point_distribution import PointDistributerFactory
from datetime import timedelta

default_point_distributer_factory = PointDistributerFactory(
    point_distribution={
        1: lambda x: x + 5,
        2: lambda x: x + 3,
        3: lambda x: x + 1,
        -1: lambda x: x
    },
    point_interval=timedelta(seconds=5)
)
