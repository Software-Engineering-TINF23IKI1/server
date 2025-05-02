from abc import ABC, abstractmethod
from bbc_server import Player
from _typing import ShopType
from typing import Optional

class BaseGame(ABC):
    def __init__(self, shop: Optional[ShopType] = None, base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1):
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier

    @abstractmethod
    def update_Player_score(self, player: Player):
        """updates a Player score

        Args:
            player (Player): player object
        """
        pass
