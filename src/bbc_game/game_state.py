from enum import Enum

class GameState(Enum):
    Preperation = 0,
    Running = 1,
    Ended = 2,
    Kill = -1
