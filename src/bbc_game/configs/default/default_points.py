from bbc_game import BasePointEarning
from datetime import timedelta

class DefaultPointEarning(BasePointEarning):
    point_distribution = {
        1: lambda x: x + 5,
        2: lambda x: x + 3,
        3: lambda x: x + 1,
        -1: lambda x: x
    }
    point_interval = timedelta(seconds=5)
