from bbc_game._typing import ShopType
from typing import Optional
from bbc_game.point_distribution import PointDistributer, PointDistributerFactory
from bbc_game.end_condition import EndConditionFactory

class GameConfig:
    def __init__(self, point_earning: PointDistributer, end_condition_factory: EndConditionFactory, shop: Optional[ShopType] = None, base_currency: float = 0,
                 base_earn_rate: float = 0, base_modifier: float = 1, base_scoreboard_top_players = 5):
        self.point_earning = point_earning
        self.endcondition_factory = end_condition_factory
        self.shop = shop
        self.base_currency = base_currency
        self.base_earn_rate = base_earn_rate
        self.base_modifier = base_modifier
        self.base_scoreboard_top_players = base_scoreboard_top_players

class GameConfigFactory:
    def __init__(self, end_condition_factory: EndConditionFactory, point_earning_factory: PointDistributerFactory, shop: Optional[ShopType] = None,
                 base_currency: float = 0, base_earn_rate: float = 0, base_modifier: float = 1, base_scoreboard_top_players = 5):
        self.__shop = shop
        self.__base_currency = base_currency
        self.__base_earn_rate = base_earn_rate
        self.__base_modifier = base_modifier
        self.__point_earning_factory = point_earning_factory
        self.__base_scoreboard_top_players = base_scoreboard_top_players
        self.__base_endcondition = end_condition_factory

    def create_game_config(self) -> GameConfig:
        """Creates a new GameConfig object using the config provided to the factory

        Returns:
            GameConfig: A new GameConfig object
        """
        return GameConfig(end_condition_factory = self.__base_endcondition, point_earning=self.__point_earning_factory.create_point_earner(), shop=self.__shop,
                          base_currency=self.__base_currency, base_earn_rate=self.__base_earn_rate,
                          base_modifier=self.__base_modifier, base_scoreboard_top_players=self.__base_scoreboard_top_players)
