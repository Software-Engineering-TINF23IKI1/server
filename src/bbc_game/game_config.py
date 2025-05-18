from bbc_game._typing import ShopType, PointEarning
from typing import Optional

class GameConfig:
    def __init__(self, shop: Optional[ShopType] = None, base_currency: float = 0, base_earn_rate: float = 0,
                 base_modifier: float = 1, point_earning: Optional[PointEarning] = None):
        self.shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier
        self.point_earning = point_earning

class GameConfigFactory:
    def __init__(self, shop: Optional[ShopType] = None, base_currency: float = 0, base_earn_rate: float = 0,
                 base_modifier: float = 1, point_earning: Optional[PointEarning] = None):
        self.shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier
        self.point_earning = point_earning

    def create_game_config(self) -> GameConfig:
        """Creates a new GameConfig object using the config provided to the factory

        Returns:
            GameConfig: A new GameConfig object
        """
        return GameConfig(shop=self.shop, base_currency=self.base_currency, base_earn_rate=self.base_earn_rate,
                          base_modifier=self.base_modifier, point_earning=self.point_earning)
