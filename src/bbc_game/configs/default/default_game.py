from bbc_game.configs.game_config import GameConfigFactory
from bbc_game.configs.default.default_shop import DefaultShop
from bbc_game.configs.default.default_points import default_point_distributer_factory

default_game_config_factory = GameConfigFactory(shop=DefaultShop, base_currency=0, base_earn_rate=0, base_modifier=1,
                                                point_earning=default_point_distributer_factory)
