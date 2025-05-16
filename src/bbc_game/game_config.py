from abc import ABC, abstractmethod
from bbc_server import Player
from bbc_game._typing import ShopType
from typing import Optional

class BaseGame:
    def __init__(self, shop: Optional[ShopType] = None, base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1):
        self._shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier


