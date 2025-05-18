from bbc_game._typing import ShopType, PointEarning
from typing import Optional

class BaseGame:
    def __init__(self, shop: Optional[ShopType] = None, base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1, point_earning: Optional[PointEarning] = None):
        self._shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier
        self.point_earning = point_earning
