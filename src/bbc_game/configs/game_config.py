from bbc_game._typing import ShopType
from typing import Optional
from bbc_game.point_distribution import PointDistributer, PointDistributerFactory

class GameConfig:
    def __init__(self, point_earning: PointDistributer, shop: Optional[ShopType] = None, base_currency: float = 0,
                 base_earn_rate: float = 0, base_modifier: float = 1):
        self.point_earning = point_earning
        self.shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier

class GameConfigFactory:
    def __init__(self, point_earning_factory: PointDistributerFactory, shop: Optional[ShopType] = None,
                 base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1):
        self.shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier
        self.point_earning_factory = point_earning_factory

    def create_game_config(self) -> GameConfig:
        """Creates a new GameConfig object using the config provided to the factory

        Returns:
            GameConfig: A new GameConfig object
        """
        return GameConfig(point_earning=self.point_earning_factory.create_point_earner(), shop=self.shop,
                          base_currency=self.base_currency, base_earn_rate=self.base_earn_rate,
                          base_modifier=self.base_modifier)
