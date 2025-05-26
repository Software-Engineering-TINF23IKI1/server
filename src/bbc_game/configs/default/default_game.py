from bbc_game.configs.game_config import GameConfigFactory
from bbc_game.configs.default.default_shop import DefaultShop
from bbc_game.configs.default.default_points import default_point_distributer_factory
from bbc_game.end_condition import PointBasedEndConditionFactory


default_game_config_factory = GameConfigFactory(
    end_condition_factory=PointBasedEndConditionFactory(250),
    point_earning_factory=default_point_distributer_factory,
    shop=DefaultShop,
    base_currency=0,
    base_earn_rate=0,
    base_modifier=1,
)
