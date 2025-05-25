from bbc_game._typing import ShopType
from typing import Optional
from bbc_game.point_distribution import PointDistributer, PointDistributerFactory

class GameConfig:
    def __init__(self, point_earning: PointDistributer, shop: Optional[ShopType] = None, base_currency: float = 0,
                 base_earn_rate: float = 0, base_modifier: float = 1, base_top_players = 5, base_endcondition = 25):
        self.point_earning = point_earning
        self.shop = shop
        self.base_currency      = base_currency
        self.base_earn_rate     = base_earn_rate
        self.base_modifier      = base_modifier
        self.base_top_players   = base_top_players
        self.base_endcondition  = base_endcondition

class GameConfigFactory:
    def __init__(self, point_earning_factory: PointDistributerFactory, shop: Optional[ShopType] = None,
                 base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1, base_top_players = 5, base_endcondition = 25):
        self.__shop = shop
        self.__base_currency = base_currency
        self.__base_earn_rate = base_earn_rate
        self.__base_modifier = base_modifier
        self.__point_earning_factory = point_earning_factory
        self.__base_top_players   = base_top_players
        self.__base_endcondition  = base_endcondition

    def create_game_config(self) -> GameConfig:
        """Creates a new GameConfig object using the config provided to the factory

        Returns:
            GameConfig: A new GameConfig object
        """
        return GameConfig(point_earning=self.__point_earning_factory.create_point_earner(), shop=self.__shop,
                          base_currency=self.__base_currency, base_earn_rate=self.__base_earn_rate,
                          base_modifier=self.__base_modifier)
